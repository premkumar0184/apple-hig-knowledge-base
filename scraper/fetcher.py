"""
fetcher.py — HTTP layer with rate-limiting, retry, and blocked URL enforcement.

The blocked URL check runs BEFORE every HTTP request. Any URL on the blocklist
raises BlockedURLError immediately — no network call is made.
"""

import logging
import time
from typing import Optional

import requests

from config import (
    BLOCKED_URLS,
    MAX_RETRIES,
    RATE_LIMIT_DELAY_S,
    REQUEST_TIMEOUT_S,
    RETRY_BACKOFF_BASE_S,
    USER_AGENT,
)

logger = logging.getLogger(__name__)

_session: Optional[requests.Session] = None
_last_request_time: float = 0.0


class BlockedURLError(Exception):
    """Raised when a fetch is attempted against a blocked URL."""


def _get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update({"User-Agent": USER_AGENT})
    return _session


def _enforce_blocklist(url: str) -> None:
    """Raise BlockedURLError if the URL matches any blocked pattern."""
    for blocked in BLOCKED_URLS:
        if url.startswith(blocked) or url == blocked.rstrip("/"):
            raise BlockedURLError(
                f"[BLOCKED] Refused to fetch '{url}' — matches blocked pattern '{blocked}'"
            )


def _rate_limit() -> None:
    """Sleep enough to honour RATE_LIMIT_DELAY_S between requests."""
    global _last_request_time
    elapsed = time.monotonic() - _last_request_time
    wait = RATE_LIMIT_DELAY_S - elapsed
    if wait > 0:
        time.sleep(wait)
    _last_request_time = time.monotonic()


def fetch(url: str) -> str:
    """
    Fetch *url* and return its text content.

    Raises:
        BlockedURLError   — URL is on the permanent blocklist.
        requests.HTTPError — Non-retriable HTTP error (4xx except 429).
        RuntimeError       — All retries exhausted.
    """
    # ── Blocklist gate (zero network calls for blocked URLs) ────────────────
    _enforce_blocklist(url)

    session = _get_session()
    last_exc: Exception = RuntimeError("unreachable")

    for attempt in range(1, MAX_RETRIES + 1):
        _rate_limit()
        try:
            logger.debug("GET %s (attempt %d/%d)", url, attempt, MAX_RETRIES)
            response = session.get(url, timeout=REQUEST_TIMEOUT_S)

            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", RETRY_BACKOFF_BASE_S * attempt))
                logger.warning("429 Too Many Requests for %s — waiting %ds", url, retry_after)
                time.sleep(retry_after)
                continue

            response.raise_for_status()
            return response.text

        except requests.HTTPError as exc:
            # 4xx (not 429) are not retried
            logger.error("HTTP error for %s: %s", url, exc)
            raise

        except (requests.ConnectionError, requests.Timeout) as exc:
            last_exc = exc
            backoff = RETRY_BACKOFF_BASE_S * (2 ** (attempt - 1))
            logger.warning(
                "Transient error for %s (attempt %d/%d): %s — retrying in %ds",
                url, attempt, MAX_RETRIES, exc, backoff,
            )
            time.sleep(backoff)

    raise RuntimeError(f"All {MAX_RETRIES} retries exhausted for {url}") from last_exc
