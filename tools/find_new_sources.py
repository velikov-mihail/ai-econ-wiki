"""Find raw sources that don't yet have a wiki summary.

Scans wiki/summaries/*.md frontmatter for sources: entries, compares
against every source file anywhere under raw/, reports unmatched files.

Matching is by normalized basename, not full path, so reorganizing raw/
(renaming or moving folders) does not make already-summarized files
reappear as pending.

Exit code 0 = nothing pending, 1 = sources pending.

Usage:
    python tools/find_new_sources.py
"""

import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
RAW_DIR = ROOT / "raw"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")

# Extensions that count as ingestable sources. Everything else under raw/
# (images, .DS_Store, Obsidian metadata) is ignored.
SOURCE_EXTS = {".md", ".pdf", ".tex", ".txt", ".docx"}

# Directories under raw/ that never hold ingestable sources.
SKIP_DIRS = {"images"}


def normalize_str(s: str) -> str:
    """Normalize unicode (curly quotes, etc.) for reliable comparison."""
    s = unicodedata.normalize("NFKC", s)
    # Map curly quotes to straight equivalents
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return s


def source_key(path_or_name: str) -> str:
    """Normalized basename used to match a raw file against a summary's
    sources: entry. Folder-independent, so moving a file within raw/ is a
    no-op for detection."""
    name = normalize_str(path_or_name).replace("\\", "/").strip().split("/")[-1]
    return re.sub(r"\s+", " ", name).strip().lower()


def read_meta(path: Path):
    """Return frontmatter dict or None."""
    txt = path.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return None
    end = txt.find("---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(txt[3:end])
    except yaml.YAMLError:
        return None


def collect_referenced_sources():
    """Return set of raw-relative paths already referenced by summaries."""
    refs = set()
    sdir = WIKI_DIR / "summaries"
    if not sdir.exists():
        return refs

    for fp in sdir.glob("*.md"):
        meta = read_meta(fp)
        if not meta or "sources" not in meta:
            continue
        for src in meta["sources"]:
            m = WIKILINK_RE.search(src)
            target = m.group(1) if m else src
            # Normalize to forward slashes and strip leading wiki/ if present
            refs.add(source_key(target))
    return refs


def collect_raw_files():
    """Return raw-relative paths for every source file anywhere under raw/."""
    files = []
    if not RAW_DIR.exists():
        return files
    for fp in sorted(RAW_DIR.rglob("*")):
        if not fp.is_file():
            continue
        rel = fp.relative_to(ROOT)
        parts = rel.parts[1:]  # drop the leading "raw"
        if any(part.startswith(".") for part in parts):
            continue
        if any(part in SKIP_DIRS for part in parts[:-1]):
            continue
        if fp.suffix.lower() not in SOURCE_EXTS:
            continue
        files.append(rel.as_posix())
    return files


def main():
    refs = collect_referenced_sources()
    raw_files = collect_raw_files()

    # Dedupe by source key so the same clipping filed in two folders is
    # reported once, not twice.
    pending = []
    seen = set()
    for f in raw_files:
        key = source_key(f)
        if key in refs or key in seen:
            continue
        seen.add(key)
        pending.append(f)

    if not pending:
        print("All raw sources have summaries.")
        return 0

    print(f"{len(pending)} raw source(s) without summaries:\n")
    for f in pending:
        print(f"  {f}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
