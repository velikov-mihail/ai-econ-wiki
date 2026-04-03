"""Validate YAML frontmatter and wikilink targets across the wiki.

Checks every .md file under wiki/ for:
  1. Valid YAML frontmatter with required fields (title, tags, date_updated)
  2. Wikilinks that resolve to existing files
  3. Sources array entries (concept pages) that point to real summaries

Usage:
    python tools/validate_frontmatter.py
"""

import re
import sys
from pathlib import Path

import yaml

# ── Config ──────────────────────────────────────────────────────────────
WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
REQUIRED_FIELDS = {"title", "tags", "date_updated"}
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def parse_frontmatter(path: Path):
    """Return (metadata_dict, body_str) or (None, body_str) if no frontmatter."""
    txt = path.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return None, txt
    end = txt.find("---", 3)
    if end == -1:
        return None, txt
    try:
        meta = yaml.safe_load(txt[3:end])
    except yaml.YAMLError:
        return None, txt
    return meta, txt[end + 3 :]


def resolve_wikilink(link: str, src: Path) -> bool:
    """Return True if a wikilink target exists as a file."""
    link = link.strip()

    # Full path from repo root (e.g. wiki/summaries/foo.md)
    candidate = WIKI_DIR.parent / link
    if candidate.exists():
        return True

    # Path relative to wiki/ (e.g. summaries/foo.md)
    candidate = WIKI_DIR / link
    if candidate.exists():
        return True

    # Bare name — search wiki/ recursively
    bare = link if link.endswith(".md") else link + ".md"
    matches = list(WIKI_DIR.rglob(bare))
    if matches:
        return True

    # Also try bare name without .md extension (roamlinks resolves both)
    if not link.endswith(".md"):
        matches = list(WIKI_DIR.rglob(link + ".md"))
        if matches:
            return True

    return False


def validate():
    errors = []
    md_files = sorted(WIKI_DIR.rglob("*.md"))

    for fp in md_files:
        rel = fp.relative_to(WIKI_DIR.parent)
        meta, body = parse_frontmatter(fp)

        # ── Frontmatter field checks ───────────────────────────────
        if meta is None:
            errors.append((rel, "missing YAML frontmatter"))
            continue

        for field in REQUIRED_FIELDS:
            if field not in meta:
                errors.append((rel, f"missing required field '{field}'"))

        if "tags" in meta and not isinstance(meta["tags"], list):
            errors.append((rel, "'tags' should be a list"))

        # ── Sources array (concept pages) ──────────────────────────
        if "sources" in meta:
            for src in meta["sources"]:
                # Extract link from wikilink syntax in sources
                m = WIKILINK_RE.search(src)
                target = m.group(1) if m else src
                if not resolve_wikilink(target, fp):
                    errors.append((rel, f"source link not found: {target}"))

        # ── Body wikilinks ─────────────────────────────────────────
        for m in WIKILINK_RE.finditer(body):
            target = m.group(1)
            if not resolve_wikilink(target, fp):
                errors.append((rel, f"broken wikilink: [[{target}]]"))

    return errors


def main():
    print(f"Scanning {WIKI_DIR} ...\n")
    errors = validate()

    if not errors:
        print("All clear — no issues found.")
        return 0

    # Group by file
    by_file = {}
    for rel, msg in errors:
        by_file.setdefault(rel, []).append(msg)

    for rel in sorted(by_file):
        print(f"{rel}")
        for msg in by_file[rel]:
            print(f"  - {msg}")
        print()

    print(f"Total: {len(errors)} issue(s) in {len(by_file)} file(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
