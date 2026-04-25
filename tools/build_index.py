"""Auto-generate index files from existing wiki pages.

Reads all summary and concept pages, then regenerates:
  - wiki/summaries/index.md  (all summaries grouped by category)
  - wiki/concepts/index.md   (all concept pages alphabetically)
  - wiki/recent.md           (last N pages added to the wiki, newest first)
  - wiki/index.md            (Recent section between RECENT-START/END markers)

Usage:
    python tools/build_index.py                       # preview to stdout
    python tools/build_index.py --write               # overwrite the index files
    python tools/build_index.py --recent-count 20     # change recent.md length
    python tools/build_index.py --home-recent-count 7 # change home embed length
"""

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
REPO_ROOT = WIKI_DIR.parent

# Category landing pages in canonical display order (also used to skip them
# as individual summaries).  Must be a list so iteration order is stable.
CATEGORY_ORDER = [
    "professional-productivity",
    "institutional-societal",
    "foundations-setup",
    "ai-tools",
    "claude-code-skills",
    "ai-agents",
    "data-analysis",
    "academic-research",
    "finance-econometrics",
    "prompt-engineering-workflow",
]
CATEGORY_SLUGS = set(CATEGORY_ORDER)


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


def classify_category(tags):
    """Return the first tag that matches a known category slug, or 'uncategorized'."""
    if not tags:
        return "uncategorized"
    for t in tags:
        if t in CATEGORY_SLUGS:
            return t
    return "uncategorized"


# ── Category display names ──────────────────────────────────────────────
CAT_DISPLAY = {
    "foundations-setup": "Foundations & Setup",
    "prompt-engineering-workflow": "Prompt Engineering & Workflow Architecture",
    "ai-agents": "AI Agents & Agentic AI",
    "claude-code-skills": "Claude Code Skills & Advanced Workflows",
    "data-analysis": "Data Analysis & Web Scraping",
    "academic-research": "AI for Academic Research & Publishing",
    "finance-econometrics": "Finance & Econometrics Applications",
    "ai-tools": "AI Tools & Comparisons",
    "institutional-societal": "Institutional & Societal Implications",
    "professional-productivity": "Professional Productivity",
    "uncategorized": "Uncategorized",
}


def build_summaries_index():
    """Return markdown string for wiki/summaries/index.md."""
    sdir = WIKI_DIR / "summaries"
    pages = {}  # category -> [(title, filename)]

    for fp in sorted(sdir.glob("*.md")):
        stem = fp.stem
        if stem == "index" or stem in CATEGORY_SLUGS:
            continue
        meta = read_meta(fp)
        if not meta:
            continue
        title = meta.get("title", stem)
        tags = meta.get("tags", [])
        cat = classify_category(tags)
        pages.setdefault(cat, []).append((title, stem))

    lines = [
        "---",
        'title: "All Summaries"',
        "tags: [index, summaries]",
        "date_updated: 2026-04-03",
        "---",
        "",
        "# All Summaries",
        "",
        f"This wiki contains **{sum(len(v) for v in pages.values())}** source summaries "
        "across the following categories.",
        "",
    ]

    # Emit in canonical category order
    order = list(CATEGORY_ORDER) + ["uncategorized"]
    for cat in order:
        if cat not in pages:
            continue
        display = CAT_DISPLAY.get(cat, cat)
        lines.append(f"## {display}")
        lines.append("")
        lines.append(f"See also: [[summaries/{cat}|{display} overview]]")
        lines.append("")
        for title, stem in sorted(pages[cat]):
            lines.append(f"- [[summaries/{stem}|{title}]]")
        lines.append("")

    return "\n".join(lines)


def build_concepts_index():
    """Return markdown string for wiki/concepts/index.md."""
    cdir = WIKI_DIR / "concepts"
    pages = []  # [(title, stem)]

    for fp in sorted(cdir.glob("*.md")):
        if fp.stem == "index":
            continue
        meta = read_meta(fp)
        if not meta:
            continue
        title = meta.get("title", fp.stem)
        pages.append((title, fp.stem))

    lines = [
        "---",
        'title: "Concept Pages"',
        "tags: [index, concepts]",
        "date_updated: 2026-04-03",
        "---",
        "",
        "# Concept Pages",
        "",
        f"**{len(pages)}** cross-cutting concept pages synthesizing ideas across multiple sources.",
        "",
    ]

    for title, stem in sorted(pages):
        lines.append(f"- [[concepts/{stem}|{title}]]")

    lines.append("")
    return "\n".join(lines)


def git_first_added_dates():
    """Return {repo_relpath: ISO date} for each tracked file's first-add commit.

    One git invocation. Renames (R entries) propagate the original add date
    forward to the new path, so renamed files keep their first-add date.
    """
    # -M enables rename detection; --name-status emits A/R lines we can parse.
    out = subprocess.check_output(
        ["git", "log", "-M", "--diff-filter=AR", "--reverse",
         "--name-status", "--format=COMMIT %aI"],
        cwd=str(REPO_ROOT), text=True, encoding="utf-8",
    )
    dates = {}
    cur = None
    for line in out.splitlines():
        if line.startswith("COMMIT "):
            cur = line[len("COMMIT "):]
            continue
        if not line.strip() or cur is None:
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("A") and len(parts) >= 2:
            # First time we see a path is its first-add commit (git log --reverse).
            dates.setdefault(parts[1], cur)
        elif status.startswith("R") and len(parts) >= 3:
            # Rename: new path inherits the original path's first-add date.
            old_path, new_path = parts[1], parts[2]
            dates.setdefault(new_path, dates.get(old_path, cur))
    return dates


def _parse_authors_md():
    """Return {summary_slug: "Author Name(s)"} parsed from wiki/authors.md.

    authors.md is hand-maintained as the canonical author index. Each
    `## Heading` is treated as the author label for the wikilinks that
    follow until the next heading. A "with X" parenthetical at the end
    of a line is stripped so each summary keeps the section's heading.
    """
    path = WIKI_DIR / "authors.md"
    mapping = {}
    if not path.exists():
        return mapping
    current = None
    link_re = re.compile(r"\[\[summaries/([^|\]]+)(?:\|[^\]]+)?\]\]")
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            current = line[3:].strip()
            continue
        if current is None:
            continue
        for slug in link_re.findall(line):
            mapping.setdefault(slug, current)
    return mapping


def _collect_recent_entries():
    """Return list of (iso, kind, title, stem, author) for all summaries+
    concepts, sorted newest-first by git first-add date. `author` is None
    for concepts and for any summary not listed in authors.md.
    """
    git_dates = git_first_added_dates()
    authors = _parse_authors_md()
    entries = []
    for kind, sub in [("summary", "summaries"), ("concept", "concepts")]:
        for fp in (WIKI_DIR / sub).glob("*.md"):
            stem = fp.stem
            if stem == "index":
                continue
            if kind == "summary" and stem in CATEGORY_SLUGS:
                continue
            meta = read_meta(fp)
            if not meta:
                continue
            iso = git_dates.get(f"wiki/{sub}/{fp.name}")
            if iso is None:
                continue
            author = authors.get(stem) if kind == "summary" else None
            entries.append((iso, kind, meta.get("title", stem), stem, author))
    entries.sort(key=lambda e: (e[0], e[3]), reverse=True)
    return entries


def _format_entry_line(entry):
    iso, kind, title, stem, author = entry
    sub = "summaries" if kind == "summary" else "concepts"
    suffix = f" — {author}" if author else f" ({kind})"
    return f"- **{iso.split('T')[0]}** — [[{sub}/{stem}|{title}]]{suffix}"


def build_recent_index(n=15):
    """Return markdown string for wiki/recent.md (full list of n entries)."""
    entries = _collect_recent_entries()

    lines = [
        "---",
        'title: "Recent"',
        "tags: [index, recent]",
        f"date_updated: {date.today().isoformat()}",
        "---",
        "",
        "# Recent",
        "",
        f"The last {n} pages added to the wiki, newest first. "
        "Generated from git history — see [[visualizations/source-timeline|"
        "Source Timeline]] for sources ordered by publication date.",
        "",
    ]
    for entry in entries[:n]:
        lines.append(_format_entry_line(entry))
    lines.append("")
    return "\n".join(lines)


# Markers used to identify the auto-updated Recent section on wiki/index.md.
HOME_RECENT_RE = re.compile(
    r"(<!-- RECENT-START -->\n).*?(\n<!-- RECENT-END -->)", re.DOTALL
)


def update_home_recent_section(home_text: str, top_n: int, total_n: int) -> str:
    """Return wiki/index.md text with the Recent block between markers refreshed.

    If markers are missing the text is returned unchanged and a warning printed.
    """
    if not HOME_RECENT_RE.search(home_text):
        print("WARN: <!-- RECENT-START --> markers not found in wiki/index.md; "
              "skipping home-page update.", file=sys.stderr)
        return home_text

    entries = _collect_recent_entries()[:top_n]
    lines = ["<!-- Auto-generated by tools/build_index.py — do not edit between markers -->"]
    lines.extend(_format_entry_line(e) for e in entries)
    lines.append("")
    lines.append(f"See [[recent|more recent summaries →]]")
    block = "\n".join(lines)
    return HOME_RECENT_RE.sub(lambda m: f"{m.group(1)}{block}{m.group(2)}", home_text)


def main():
    parser = argparse.ArgumentParser(description="Rebuild wiki index files")
    parser.add_argument("--write", action="store_true",
                        help="Overwrite index files (default: preview only)")
    parser.add_argument("--recent-count", type=int, default=15,
                        help="Number of entries on wiki/recent.md (default: 15)")
    parser.add_argument("--home-recent-count", type=int, default=5,
                        help="Number of entries embedded on wiki/index.md (default: 5)")
    args = parser.parse_args()

    summaries_md = build_summaries_index()
    concepts_md = build_concepts_index()
    recent_md = build_recent_index(n=args.recent_count)

    home_path = WIKI_DIR / "index.md"
    home_md = update_home_recent_section(
        home_path.read_text(encoding="utf-8"),
        top_n=args.home_recent_count,
        total_n=args.recent_count,
    )

    if args.write:
        (WIKI_DIR / "summaries" / "index.md").write_text(summaries_md, encoding="utf-8")
        (WIKI_DIR / "concepts" / "index.md").write_text(concepts_md, encoding="utf-8")
        (WIKI_DIR / "recent.md").write_text(recent_md, encoding="utf-8")
        home_path.write_text(home_md, encoding="utf-8")
        print("Wrote wiki/summaries/index.md, wiki/concepts/index.md, "
              "wiki/recent.md, wiki/index.md")
    else:
        print("=== wiki/summaries/index.md ===")
        print(summaries_md)
        print("\n=== wiki/concepts/index.md ===")
        print(concepts_md)
        print("\n=== wiki/recent.md ===")
        print(recent_md)
        print("\n=== wiki/index.md (Recent section refresh) ===")
        print(home_md)
        print("\nRun with --write to overwrite the files.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
