---
title: "Operations Log"
tags: [log, internal]
date_updated: 2026-04-05
---

# Operations Log

Chronological record of wiki maintenance operations (newest first).

## [2026-04-05] maintain --fix | Maintenance pass with auto-fix
- Pending sources: 26
- Errors: 5 → 0 (fixed 5 orphan summaries: added to category pages)
- Warnings: 0
- Indexes rebuilt: yes
- Auto-fixed: yes (baylor-ai-taskforce, blattman-x-post, korinek-2023, panjwani-slides, spina-paper)

## [2026-04-05] maintain | Maintenance pass
- Pending sources: 26
- Errors: 5 (orphan summaries not on category pages)
- Warnings: 0
- Info: 96 summaries, 64 concepts, 10 categories
- Indexes rebuilt: yes (no changes needed)

## [2026-04-05] maintain | Maintenance pass (post-fix)
- Pending sources: 0
- Errors: 0
- Warnings: 0 (duplicate pairs are expected same-series sources)
- Indexes rebuilt: yes (no changes needed)

## [2026-04-05] maintain | Maintenance pass
- Pending sources: 0
- Errors: 25 orphan summaries not in summaries/index.md
- Warnings: build_index.py --write drops entries (reverted); mkdocs nav has no individual page listings (by design)
- Info: frontmatter validation passed; duplicate pairs are expected (same-series sources)
- Indexes rebuilt: no (reverted — script is lossy)

## [2026-04-04] maintain | Maintenance pass
- Pending sources: 0
- Errors: 26 orphan summaries not in index
- Warnings: 8 high-similarity duplicate pairs; mkdocs.yml nav missing individual summaries
- Info: 106 summaries, 64 concepts, 10 categories
- Indexes rebuilt: yes
