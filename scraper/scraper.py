"""
scraper.py — BFS orchestrator and CLI entrypoint.

Usage:
    python scraper.py [--dry-run] [--verbose]

Options:
    --dry-run    Discover and log URLs without saving files.
    --verbose    Enable DEBUG logging.
"""

import argparse
import logging
import sys
from collections import deque
from pathlib import Path

from config import HIG_MD_ROOT, HIG_PATH_PREFIX_LOWER, MAX_DEPTH, BASE_URL
from fetcher import BlockedURLError, fetch
from manifest import Manifest
from parser import ParsedPage, md_url, parse, slug_from_url
from writer import save

KB_ROOT = Path(__file__).resolve().parent.parent / "guidelines"


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(KB_ROOT / "scrape_run.log", mode="w", encoding="utf-8"),
        ],
    )


def is_hig_url(url: str) -> bool:
    """Return True if url is a HIG content page (not an anchor, not external)."""
    path = url.replace(BASE_URL, "")
    return path.lower().startswith(HIG_PATH_PREFIX_LOWER)


def canonical(url: str) -> str:
    """Strip .md suffix, trailing slash, and anchor fragments for dedup purposes."""
    url = url.split("#")[0]  # strip #fragment anchors
    return url.rstrip("/").removesuffix(".md")


def crawl(dry_run: bool, manifest: Manifest) -> None:
    logger = logging.getLogger("crawl")

    # Queue entries: (canonical_url, depth)
    queue: deque[tuple[str, int]] = deque()
    queue.append((canonical(HIG_MD_ROOT), 0))

    visited: set[str] = set()

    while queue:
        url, depth = queue.popleft()

        if url in visited:
            continue
        visited.add(url)

        if manifest.already_visited(url):
            logger.debug("Skip (already in manifest): %s", url)
            continue

        if depth > MAX_DEPTH:
            logger.warning("Max depth %d exceeded, skipping: %s", MAX_DEPTH, url)
            manifest.record_skip(url, f"max_depth_{MAX_DEPTH}")
            continue

        fetch_url = md_url(url)

        logger.info("[depth=%d] Fetching: %s", depth, fetch_url)

        # ── Fetch ────────────────────────────────────────────────────────────
        try:
            raw = fetch(fetch_url)
        except BlockedURLError as exc:
            logger.error("BLOCKED: %s", exc)
            manifest.record_skip(url, "blocked_url")
            continue
        except Exception as exc:
            logger.error("Failed to fetch %s: %s", fetch_url, exc)
            manifest.record_error(url, str(exc))
            continue

        # ── Parse ────────────────────────────────────────────────────────────
        page: ParsedPage = parse(url, raw)

        # ── Enqueue child links ──────────────────────────────────────────────
        for child_url in page.child_links:
            canon = canonical(child_url)
            if canon not in visited and is_hig_url(child_url):
                queue.append((canon, depth + 1))

        # ── Save or dry-run ──────────────────────────────────────────────────
        if dry_run:
            logger.info("[DRY-RUN] Would save: %s (role=%s, title=%s)",
                        url, page.meta.role, page.meta.title)
            manifest.record_skip(url, "dry_run")
            continue

        try:
            abs_path = save(page, KB_ROOT)
            rel_path = abs_path.relative_to(KB_ROOT)
            byte_count = abs_path.stat().st_size
            manifest.record_success(url, page.meta, rel_path, byte_count)
        except Exception as exc:
            logger.error("Failed to save %s: %s", url, exc)
            manifest.record_error(url, str(exc))


def main() -> None:
    parser = argparse.ArgumentParser(description="Apple HIG Knowledge Base Scraper")
    parser.add_argument("--dry-run", action="store_true", help="Discover URLs without saving files")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    KB_ROOT.mkdir(parents=True, exist_ok=True)
    setup_logging(args.verbose)
    logger = logging.getLogger("main")

    logger.info("=" * 60)
    logger.info("Apple HIG Knowledge Base Scraper")
    logger.info("Output: %s", KB_ROOT)
    logger.info("Dry-run: %s", args.dry_run)
    logger.info("=" * 60)

    manifest = Manifest(KB_ROOT)

    try:
        crawl(dry_run=args.dry_run, manifest=manifest)
    finally:
        manifest.save()
        logger.info(manifest.summary())
        logger.info("Done.")


if __name__ == "__main__":
    main()
