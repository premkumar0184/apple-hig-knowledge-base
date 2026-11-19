"""
manifest.py — Track visited URLs and emit metadata.json + scrape_log.jsonl.
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from config import METADATA_FILENAME, LOG_FILENAME
from parser import PageMeta

logger = logging.getLogger(__name__)


class Manifest:
    """
    Tracks all pages encountered during the crawl.

    After the crawl completes, call .save(kb_root) to write:
      - metadata.json  — full URL→page-info map
      - scrape_log.jsonl — per-page status events (append-safe)
    """

    def __init__(self, kb_root: Path) -> None:
        self._kb_root = kb_root
        self._pages: dict[str, dict] = {}          # url → record
        self._log_path = kb_root / LOG_FILENAME
        self._log_path.parent.mkdir(parents=True, exist_ok=True)

    def record_success(
        self,
        url: str,
        meta: PageMeta,
        rel_path: Path,
        byte_count: int,
    ) -> None:
        ts = _now()
        record = {
            "url": url,
            "title": meta.title,
            "role": meta.role,
            "identifier": meta.identifier,
            "rel_path": str(rel_path),
            "scraped_at": ts,
            "status": "ok",
            "bytes": byte_count,
        }
        self._pages[url] = record
        self._append_log({"event": "page_ok", **record})

    def record_skip(self, url: str, reason: str) -> None:
        ts = _now()
        record = {"url": url, "status": "skipped", "reason": reason, "scraped_at": ts}
        self._pages[url] = record
        self._append_log({"event": "page_skip", **record})

    def record_error(self, url: str, error: str) -> None:
        ts = _now()
        record = {"url": url, "status": "error", "error": error, "scraped_at": ts}
        self._pages[url] = record
        self._append_log({"event": "page_error", **record})

    def already_visited(self, url: str) -> bool:
        return url in self._pages

    def save(self) -> None:
        meta_path = self._kb_root / METADATA_FILENAME
        payload = {
            "generated_at": _now(),
            "total_pages": len(self._pages),
            "ok": sum(1 for p in self._pages.values() if p.get("status") == "ok"),
            "skipped": sum(1 for p in self._pages.values() if p.get("status") == "skipped"),
            "errors": sum(1 for p in self._pages.values() if p.get("status") == "error"),
            "pages": self._pages,
        }
        meta_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        logger.info("Manifest saved → %s (%d pages)", meta_path, len(self._pages))

    def summary(self) -> str:
        ok = sum(1 for p in self._pages.values() if p.get("status") == "ok")
        skip = sum(1 for p in self._pages.values() if p.get("status") == "skipped")
        err = sum(1 for p in self._pages.values() if p.get("status") == "error")
        return f"Pages scraped: {ok} ok · {skip} skipped · {err} errors (total {len(self._pages)})"

    # ── private ──────────────────────────────────────────────────────────────

    def _append_log(self, record: dict) -> None:
        with self._log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()
