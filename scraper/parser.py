"""
parser.py — Extract links and metadata from Apple HIG Markdown pages.

Each HIG Markdown page starts with a JSON metadata block inside an HTML comment:

    <!--
    {
      "documentType" : "article",
      "framework"    : "Human Interface Guidelines",
      "identifier"   : "/design/Human-Interface-Guidelines/accessibility",
      "metadataVersion" : "0.1.0",
      "role"         : "article",
      "title"        : "Accessibility"
    }
    -->
"""

import json
import re
from dataclasses import dataclass, field
from typing import Optional

from config import BASE_URL, BLOCKED_URLS, HIG_PATH_PREFIX_LOWER

# Regex to capture the JSON metadata comment at the top of the page
_META_RE = re.compile(r"<!--\s*(\{.*?\})\s*-->", re.DOTALL)

# Regex to find all Markdown links: [text](/design/Human-Interface-Guidelines/...)
# Also catches bare links without brackets when present
_LINK_RE = re.compile(r"\[([^\]]+)\]\((/design/[^\)]+)\)")


@dataclass
class PageMeta:
    document_type: str = ""
    framework: str = ""
    identifier: str = ""
    metadata_version: str = ""
    role: str = ""          # "collection" | "collectionGroup" | "article"
    title: str = ""
    raw: dict = field(default_factory=dict)


@dataclass
class ParsedPage:
    url: str
    meta: PageMeta
    body: str                    # Markdown content without the metadata comment
    child_links: list[str]       # Absolute URLs to child HIG pages (no .md suffix)


def _is_blocked(url: str) -> bool:
    return any(url.startswith(b) for b in BLOCKED_URLS)


def _is_hig_link(path: str) -> bool:
    """Return True if path is under /design/Human-Interface-Guidelines/."""
    return path.lower().startswith(HIG_PATH_PREFIX_LOWER + "/")


def parse(url: str, raw_text: str) -> ParsedPage:
    """
    Parse raw Markdown text from a HIG page.

    Returns a ParsedPage with extracted metadata, cleaned body, and child links.
    """
    # ── 1. Extract metadata comment ─────────────────────────────────────────
    meta = PageMeta()
    body = raw_text

    m = _META_RE.search(raw_text)
    if m:
        try:
            data = json.loads(m.group(1))
            meta = PageMeta(
                document_type=data.get("documentType", ""),
                framework=data.get("framework", ""),
                identifier=data.get("identifier", ""),
                metadata_version=data.get("metadataVersion", ""),
                role=data.get("role", ""),
                title=data.get("title", ""),
                raw=data,
            )
        except json.JSONDecodeError:
            pass
        # Remove the metadata comment from the body
        body = raw_text[: m.start()] + raw_text[m.end() :]

    # Strip leading blank lines left by comment removal
    body = body.lstrip("\n")

    # ── 2. Extract child links ───────────────────────────────────────────────
    child_links: list[str] = []
    seen: set[str] = set()

    for _text, path in _LINK_RE.findall(raw_text):
        # Strip anchor fragments (#section) — anchors are not separate pages
        path = path.split("#")[0]
        # Normalise: strip trailing slash, strip .md if already there
        clean_path = path.rstrip("/").removesuffix(".md")

        if not clean_path:
            continue

        if not _is_hig_link(clean_path):
            continue

        abs_url = BASE_URL + clean_path

        if _is_blocked(abs_url):
            continue

        if abs_url not in seen:
            seen.add(abs_url)
            child_links.append(abs_url)

    return ParsedPage(url=url, meta=meta, body=body, child_links=child_links)


def md_url(page_url: str) -> str:
    """Convert a canonical HIG page URL to its .md equivalent."""
    url = page_url.rstrip("/").removesuffix(".md")
    return url + ".md"


def slug_from_url(page_url: str) -> str:
    """
    Return the last path segment of a HIG URL as the article slug.

    e.g. https://developer.apple.com/design/Human-Interface-Guidelines/accessibility
         → "accessibility"
    """
    return page_url.rstrip("/").split("/")[-1].lower()


def relative_link_rewrite(body: str, depth: int) -> str:
    """
    Rewrite absolute /design/Human-Interface-Guidelines/X links in Markdown body
    to relative paths, so the saved .md files are cross-linkable offline.

    depth=1 → section index   → "../X.md"   (one level below root)
    depth=2 → article         → "X.md"      (sibling)
    depth=3 → sub-group index → "../../X.md"
    depth=4 → sub article     → "../X.md"
    """

    def _replace(m: re.Match) -> str:
        text = m.group(1)
        path = m.group(2).rstrip("/").removesuffix(".md")

        if not _is_hig_link(path):
            return m.group(0)

        # Strip the HIG prefix to get just the slug(s)
        prefix = "/design/Human-Interface-Guidelines"
        relative = path[len(prefix):].lstrip("/")

        # Build relative path based on caller depth
        up = "../" * (depth - 1)  # go up to root, then descend
        rel_path = f"{up}{relative}.md" if relative else f"{up}index.md"
        return f"[{text}]({rel_path})"

    return _LINK_RE.sub(_replace, body)
