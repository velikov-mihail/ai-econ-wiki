"""Unified wiki health-check: frontmatter, orphans, index drift, nav drift.

Aggregates results from existing tools and adds orphan/drift checks.
Classifies findings as error, warning, or info.

Usage:
    python tools/lint_wiki.py          # report only
    python tools/lint_wiki.py --fix    # auto-repair mechanical issues
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
TOOLS_DIR = ROOT / "tools"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")

# Known category landing-page stems (not individual summaries)
CATEGORY_SLUGS = {
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
}

# ── Helpers ────────────────────────────────────────────────────────────


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


def read_body(path: Path) -> str:
    """Return file body after frontmatter."""
    txt = path.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return txt
    end = txt.find("---", 3)
    return txt[end + 3:] if end != -1 else txt


def wikilinks_in(text: str) -> list[str]:
    """Extract all wikilink targets from text."""
    return [m.group(1) for m in WIKILINK_RE.finditer(text)]


def stems_linked_in(text: str) -> set[str]:
    """Return set of stems (no path, no .md) referenced by wikilinks."""
    stems = set()
    for link in wikilinks_in(text):
        # Handle paths like summaries/foo or just foo
        name = link.split("/")[-1]
        if name.endswith(".md"):
            name = name[:-3]
        stems.add(name)
    return stems


def collect_summary_stems() -> set[str]:
    """Return stems of all summary .md files (excluding index and categories)."""
    sdir = WIKI_DIR / "summaries"
    stems = set()
    for fp in sdir.glob("*.md"):
        if fp.stem == "index" or fp.stem in CATEGORY_SLUGS:
            continue
        stems.add(fp.stem)
    return stems


def collect_concept_stems() -> set[str]:
    """Return stems of all concept .md files (excluding index)."""
    cdir = WIKI_DIR / "concepts"
    return {fp.stem for fp in cdir.glob("*.md") if fp.stem != "index"}


def stems_listed_in_index(index_path: Path) -> set[str]:
    """Return stems referenced by wikilinks in an index file."""
    if not index_path.exists():
        return set()
    return stems_linked_in(index_path.read_text(encoding="utf-8"))


def stems_listed_in_category_pages() -> set[str]:
    """Return summary stems referenced from any category landing page."""
    sdir = WIKI_DIR / "summaries"
    linked = set()
    for slug in CATEGORY_SLUGS:
        fp = sdir / f"{slug}.md"
        if fp.exists():
            linked |= stems_linked_in(fp.read_text(encoding="utf-8"))
    return linked


def parse_mkdocs_nav(yml_path: Path) -> list[str]:
    """Return list of page paths from mkdocs.yml nav."""
    if not yml_path.exists():
        return []
    # mkdocs.yml may use !!python/name tags; strip them for safe parsing
    raw = yml_path.read_text(encoding="utf-8")
    raw = re.sub(r"!!python/name:\S+", "''", raw)
    data = yaml.safe_load(raw)
    nav = data.get("nav", [])
    pages = []

    def walk(node):
        if isinstance(node, str):
            pages.append(node)
        elif isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(nav)
    return pages


# ── Checks ─────────────────────────────────────────────────────────────


def check_frontmatter() -> list[tuple[str, str]]:
    """Run frontmatter validation; return list of (severity, message)."""
    findings = []
    # Import and run validate_frontmatter logic inline
    from validate_frontmatter import validate
    errors = validate()
    for rel, msg in errors:
        findings.append(("error", f"{rel}: {msg}"))
    return findings


def check_orphan_summaries() -> list[tuple[str, str]]:
    """Summaries not listed on any category landing page."""
    findings = []
    all_stems = collect_summary_stems()
    linked = stems_listed_in_category_pages()
    orphans = sorted(all_stems - linked)
    for stem in orphans:
        findings.append(("error", f"Orphan summary: wiki/summaries/{stem}.md — not on any category page"))
    return findings


def check_orphan_concepts() -> list[tuple[str, str]]:
    """Concepts not listed in concepts/index.md."""
    findings = []
    all_stems = collect_concept_stems()
    idx = WIKI_DIR / "concepts" / "index.md"
    linked = stems_listed_in_index(idx)
    orphans = sorted(all_stems - linked)
    for stem in orphans:
        findings.append(("error", f"Orphan concept: wiki/concepts/{stem}.md — not in concepts/index.md"))
    return findings


def check_zero_concept_links() -> list[tuple[str, str]]:
    """Summaries with no wikilinks to any concept page."""
    findings = []
    concept_stems = collect_concept_stems()
    sdir = WIKI_DIR / "summaries"
    for fp in sorted(sdir.glob("*.md")):
        if fp.stem == "index" or fp.stem in CATEGORY_SLUGS:
            continue
        body = read_body(fp)
        linked = stems_linked_in(body)
        if not linked & concept_stems:
            findings.append(("warning", f"Zero concept links: wiki/summaries/{fp.stem}.md"))
    return findings


def check_index_drift() -> list[tuple[str, str]]:
    """Files on disk not in index, or index entries pointing to missing files."""
    findings = []

    # Summaries index
    sidx = WIKI_DIR / "summaries" / "index.md"
    s_on_disk = collect_summary_stems()
    s_in_idx = stems_listed_in_index(sidx)
    for stem in sorted(s_on_disk - s_in_idx):
        findings.append(("warning", f"Index drift: wiki/summaries/{stem}.md on disk but not in summaries/index.md"))
    for stem in sorted(s_in_idx - s_on_disk - CATEGORY_SLUGS):
        if not (WIKI_DIR / "summaries" / f"{stem}.md").exists():
            findings.append(("warning", f"Index drift: summaries/index.md links to {stem}.md which doesn't exist"))

    # Concepts index
    cidx = WIKI_DIR / "concepts" / "index.md"
    c_on_disk = collect_concept_stems()
    c_in_idx = stems_listed_in_index(cidx)
    for stem in sorted(c_on_disk - c_in_idx):
        findings.append(("warning", f"Index drift: wiki/concepts/{stem}.md on disk but not in concepts/index.md"))
    for stem in sorted(c_in_idx - c_on_disk):
        if not (WIKI_DIR / "concepts" / f"{stem}.md").exists():
            findings.append(("warning", f"Index drift: concepts/index.md links to {stem}.md which doesn't exist"))

    return findings


def check_mkdocs_nav() -> list[tuple[str, str]]:
    """Pages in mkdocs.yml nav that don't exist, or wiki pages missing from nav."""
    findings = []
    yml = ROOT / "mkdocs.yml"
    if not yml.exists():
        return findings

    nav_pages = set(parse_mkdocs_nav(yml))

    # Nav entries pointing to missing files
    for pg in sorted(nav_pages):
        fp = WIKI_DIR / pg
        if not fp.exists():
            findings.append(("warning", f"mkdocs nav drift: {pg} in nav but file missing"))

    # Wiki pages not in nav (summaries + concepts only, skip index/categories)
    for fp in sorted(WIKI_DIR.rglob("*.md")):
        rel = fp.relative_to(WIKI_DIR).as_posix()
        # Only check summaries and concepts (individual pages)
        if rel.startswith("summaries/") and fp.stem not in CATEGORY_SLUGS and fp.stem != "index":
            if rel not in nav_pages:
                # Individual summaries are accessed through category pages, not nav directly
                pass
        elif rel.startswith("concepts/") and fp.stem != "index":
            if rel not in nav_pages:
                findings.append(("warning", f"mkdocs nav drift: {rel} not in mkdocs.yml nav"))

    return findings


def check_pending_sources() -> list[tuple[str, str]]:
    """Run find_new_sources and report count."""
    try:
        r = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "find_new_sources.py")],
            capture_output=True, text=True, cwd=str(ROOT)
        )
        output = (r.stdout + r.stderr).strip()
        # First line has the count
        m = re.match(r"(\d+) raw source", output)
        count = int(m.group(1)) if m else 0
        if count > 0:
            return [("info", f"Pending sources: {count} raw file(s) without summaries")]
        return [("info", "Pending sources: 0")]
    except Exception as e:
        return [("info", f"Pending sources: could not run find_new_sources.py ({e})")]


def check_duplicates() -> list[tuple[str, str]]:
    """Run find_duplicates and report flagged pairs."""
    try:
        r = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "find_duplicates.py")],
            capture_output=True, text=True, cwd=str(ROOT)
        )
        output = r.stdout.strip()
        m = re.search(r"Found (\d+) pair", output)
        count = int(m.group(1)) if m else 0
        if count > 0:
            return [("info", f"Duplicate detection: {count} near-duplicate pair(s) found")]
        return [("info", "Duplicate detection: none")]
    except Exception as e:
        return [("info", f"Duplicate detection: could not run ({e})")]


def check_counts() -> list[tuple[str, str]]:
    """Total summaries, concepts, categories."""
    ns = len(collect_summary_stems())
    nc = len(collect_concept_stems())
    ncat = sum(1 for s in CATEGORY_SLUGS if (WIKI_DIR / "summaries" / f"{s}.md").exists())
    return [("info", f"Totals: {ns} summaries, {nc} concepts, {ncat} categories")]


# ── Main ───────────────────────────────────────────────────────────────


def run_all_checks() -> list[tuple[str, str]]:
    """Run every check and return combined findings."""
    findings = []
    findings += check_frontmatter()
    findings += check_orphan_summaries()
    findings += check_orphan_concepts()
    findings += check_zero_concept_links()
    findings += check_index_drift()
    findings += check_mkdocs_nav()
    findings += check_pending_sources()
    findings += check_duplicates()
    findings += check_counts()
    return findings


def print_report(findings: list[tuple[str, str]]):
    """Print structured report grouped by severity."""
    severity_order = ["error", "warning", "info"]
    grouped = {s: [] for s in severity_order}
    for sev, msg in findings:
        grouped[sev].append(msg)

    for sev in severity_order:
        items = grouped[sev]
        label = sev.upper()
        print(f"\n=== {label} ({len(items)}) ===")
        if items:
            for msg in items:
                print(f"  {msg}")
        else:
            print("  (none)")

    ne = len(grouped["error"])
    nw = len(grouped["warning"])
    ni = len(grouped["info"])
    print(f"\nSummary: {ne} error(s), {nw} warning(s), {ni} info")
    return ne, nw, ni


def do_fix():
    """Auto-repair mechanical issues."""
    repairs = []

    # Rebuild indexes
    r = subprocess.run(
        [sys.executable, str(TOOLS_DIR / "build_index.py"), "--write"],
        capture_output=True, text=True, cwd=str(ROOT)
    )
    if r.returncode == 0:
        repairs.append("Rebuilt indexes")
    else:
        print(f"  build_index.py failed: {r.stderr.strip()}")

    # Add orphan concepts to concepts/index.md (handled by build_index)
    # Add orphan summaries to summaries/index.md (handled by build_index)
    # build_index already includes all on-disk files, so index drift is fixed.

    if repairs:
        print(f"\nAuto-fixed: {', '.join(repairs)}")
    return repairs


def main():
    # Ensure we can import sibling tools
    if str(TOOLS_DIR) not in sys.path:
        sys.path.insert(0, str(TOOLS_DIR))

    parser = argparse.ArgumentParser(description="Wiki health check")
    parser.add_argument("--fix", action="store_true",
                        help="Auto-repair mechanical issues (rebuild indexes, fix orphans)")
    args = parser.parse_args()

    print(f"Linting {WIKI_DIR} ...\n")

    findings = run_all_checks()
    ne, nw, ni = print_report(findings)

    if args.fix:
        print("\n--- Auto-fix mode ---")
        do_fix()
        # Re-run to show updated state
        print("\n--- Post-fix report ---")
        findings2 = run_all_checks()
        print_report(findings2)

    return 1 if ne > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
