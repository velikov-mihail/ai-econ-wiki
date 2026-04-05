"""Find raw sources that don't yet have a wiki summary.

Scans wiki/summaries/*.md frontmatter for sources: entries, compares
against raw/articles/*.md and raw/papers/*, reports unmatched files.

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


def normalize_str(s: str) -> str:
    """Normalize unicode (curly quotes, etc.) for reliable comparison."""
    s = unicodedata.normalize("NFKC", s)
    # Map curly quotes to straight equivalents
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return s


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
            target = target.replace("\\", "/").strip()
            refs.add(normalize_str(target))
    return refs


def collect_raw_files():
    """Return list of raw-relative paths for all source files."""
    files = []
    for subdir in ["articles", "papers"]:
        d = RAW_DIR / subdir
        if not d.exists():
            continue
        for fp in sorted(d.iterdir()):
            if fp.is_file():
                rel = normalize_str(f"raw/{subdir}/{fp.name}")
                files.append(rel)
    return files


def main():
    refs = collect_referenced_sources()
    raw_files = collect_raw_files()

    pending = [f for f in raw_files if f not in refs]

    if not pending:
        print("All raw sources have summaries.")
        return 0

    print(f"{len(pending)} raw source(s) without summaries:\n")
    for f in pending:
        print(f"  {f}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
