"""
writer.py — Save parsed HIG pages into a mirrored directory structure.

Output layout:
  <kb_root>/index.md                           ← root collection
  <kb_root>/foundations/index.md               ← section collection group
  <kb_root>/foundations/accessibility.md       ← leaf article
  <kb_root>/components/content/index.md        ← sub-group
  <kb_root>/components/content/charts.md       ← deep leaf
"""

import logging
from pathlib import Path

from config import BASE_URL, HIG_PATH_PREFIX_LOWER
from parser import ParsedPage, relative_link_rewrite

logger = logging.getLogger(__name__)

_HIG_PREFIX = "/design/Human-Interface-Guidelines"


def _url_to_rel_path(page_url: str) -> Path:
    """
    Convert a canonical HIG page URL to a relative filesystem path.

    Root page → index.md
    /foundations → foundations/index.md
    /foundations/accessibility → foundations/accessibility.md
    /components/content → components/content/index.md
    /components/content/charts → components/content/charts.md
    """
    url = page_url.rstrip("/").removesuffix(".md")
    path_part = url.replace(BASE_URL, "")  # strip scheme+host

    # Strip /design/Human-Interface-Guidelines prefix (case-insensitive)
    lower = path_part.lower()
    if lower == HIG_PATH_PREFIX_LOWER:
        return Path("index.md")

    suffix = path_part[len(_HIG_PREFIX):].lstrip("/")  # e.g. "foundations/accessibility"
    parts = suffix.split("/")

    if len(parts) == 1:
        # Top-level section → section/index.md  (it's a collectionGroup)
        return Path(parts[0].lower()) / "index.md"
    else:
        # article slug is the last part; parent parts form directories
        dirs = [p.lower() for p in parts[:-1]]
        slug = parts[-1].lower()
        return Path(*dirs) / f"{slug}.md"


def _page_depth(rel_path: Path) -> int:
    """Return depth (number of path components including filename)."""
    return len(rel_path.parts)


def save(page: ParsedPage, kb_root: Path) -> Path:
    """
    Write page content to disk under kb_root.

    Returns the absolute path of the file written.
    """
    rel_path = _url_to_rel_path(page.url)
    abs_path = kb_root / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    depth = _page_depth(rel_path)
    body = relative_link_rewrite(page.body, depth)

    # Prepend YAML-style front matter for interoperability with static-site
    # generators and graphify's document extractor.
    front_matter = _build_front_matter(page)
    content = front_matter + body

    abs_path.write_text(content, encoding="utf-8")
    logger.info("Saved %s → %s (%d bytes)", page.url, rel_path, len(content))
    return abs_path


def _build_front_matter(page: ParsedPage) -> str:
    if not page.meta.title:
        return ""
    lines = [
        "---",
        f"title: \"{page.meta.title}\"",
        f"role: \"{page.meta.role}\"",
        f"identifier: \"{page.meta.identifier}\"",
        f"source_url: \"{page.url}\"",
        "---",
        "",
    ]
    return "\n".join(lines) + "\n"
