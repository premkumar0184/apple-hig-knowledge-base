"""
config.py — scraper constants and safety configuration
"""

BASE_URL = "https://developer.apple.com"
HIG_ROOT_PATH = "/design/human-interface-guidelines"
HIG_MD_ROOT = f"{BASE_URL}{HIG_ROOT_PATH}.md"

# URL prefix for all valid HIG pages (case-insensitive match applied in fetcher)
HIG_PATH_PREFIX = "/design/Human-Interface-Guidelines"
HIG_PATH_PREFIX_LOWER = HIG_PATH_PREFIX.lower()

# ── Blocked URLs ────────────────────────────────────────────────────────────
# Any URL matching these patterns will NEVER be fetched.
# Attempting to fetch a blocked URL raises BlockedURLError immediately.
BLOCKED_URLS: list[str] = [
    "https://www.apple.com/legal/internet-services/terms/site.html",
    "https://www.apple.com/legal/",
    "https://www.apple.com/privacy/",
]

# ── HTTP behaviour ──────────────────────────────────────────────────────────
REQUEST_TIMEOUT_S = 15
RATE_LIMIT_DELAY_S = 1.0          # seconds between requests
MAX_RETRIES = 3
RETRY_BACKOFF_BASE_S = 2          # exponential: 2s, 4s, 8s

USER_AGENT = "AppleHIG-KnowledgeBase-Builder/1.0 (personal research; not for redistribution)"

# ── Crawl limits ────────────────────────────────────────────────────────────
MAX_DEPTH = 4                      # prevent runaway recursion

# ── Output paths (relative to knowledge-base root) ─────────────────────────
METADATA_FILENAME = "metadata.json"
LOG_FILENAME = "scrape_log.jsonl"
