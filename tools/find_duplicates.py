"""Detect near-duplicate raw articles using trigram similarity.

Compares all .md files in raw/articles/ pairwise. Reports pairs whose
trigram Jaccard similarity exceeds a threshold (default 0.40).

Usage:
    python tools/find_duplicates.py                # default threshold 0.40
    python tools/find_duplicates.py --threshold 0.3
"""

import argparse
import re
import sys
from itertools import combinations
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parent.parent / "raw" / "articles"


def trigrams(text: str) -> set:
    """Return set of character trigrams from lowercased, whitespace-normalized text."""
    text = re.sub(r"\s+", " ", text.lower().strip())
    return {text[i : i + 3] for i in range(len(text) - 2)}


def jaccard(a: set, b: set) -> float:
    """Jaccard similarity between two sets."""
    if not a and not b:
        return 1.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def main():
    parser = argparse.ArgumentParser(description="Find near-duplicate raw articles")
    parser.add_argument("--threshold", type=float, default=0.40,
                        help="Jaccard similarity threshold (default: 0.40)")
    args = parser.parse_args()

    if not RAW_DIR.exists():
        print(f"Directory not found: {RAW_DIR}")
        print("(raw/ is gitignored — this tool only works locally)")
        return 0

    files = sorted(RAW_DIR.glob("*.md"))
    if len(files) < 2:
        print(f"Only {len(files)} file(s) found — nothing to compare.")
        return 0

    print(f"Comparing {len(files)} files (threshold={args.threshold:.2f}) ...\n")

    # Pre-compute trigram sets
    tsets = {}
    for fp in files:
        try:
            txt = fp.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        tsets[fp.name] = trigrams(txt)

    # Pairwise comparison
    dupes = []
    names = sorted(tsets.keys())
    for a, b in combinations(names, 2):
        sim = jaccard(tsets[a], tsets[b])
        if sim >= args.threshold:
            dupes.append((sim, a, b))

    dupes.sort(reverse=True)

    if not dupes:
        print("No near-duplicates found.")
        return 0

    for sim, a, b in dupes:
        print(f"  {sim:.2%}  {a}")
        print(f"         {b}")
        print()

    print(f"Found {len(dupes)} pair(s) above threshold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
