---
title: "Claude Code 102 for Academic Researchers (Bilal)"
tags: [summary, foundations-setup, claude-code, project-organization]
sources:
  - "[[raw/articles/Claude Code 102 for Academic Researchers.md]]"
date_updated: 2026-05-15
date_published: 2026-05-07
---

- **Author/Source**: Mushtaq Bilal, X thread (sequel to Claude Code 101)
- **Original**: [https://x.com/MushtaqBilalPhD/status/2053829787219595725](https://x.com/MushtaqBilalPhD/status/2053829787219595725)

- **Key Ideas**
  - Continuation of [[claude-code-101-bilal|Claude Code 101]] for academics: how to scale from a single-folder project to a multi-year dissertation or monograph.
  - Recommended project layout for a long project (e.g. a dissertation): subfolders for `Literature` (PDFs and notes), `Chapters` (drafts), `Data` (datasets), `Notes` (meeting notes, ideas), `Correspondence` (advisor emails, co-author exchanges, reviewer reports).
  - **Nested CLAUDE.md files**: a "global" CLAUDE.md at the project root describes the overall project; a "local" CLAUDE.md in each subfolder gives task-specific instructions (citation style for chapters, filename conventions for data, prioritization rules for correspondence).
  - Local files inherit global context — Claude Code reads both when working inside a subfolder — so local files stay short and topical without losing the project frame.
  - Worked examples for each subfolder: Chapters folder uses "argument, evidence, literature, counterargument" critique structure and MLA 9th; Data folder treats all CSV/Excel as raw, never overwritten, with `_clean` suffix on cleaned versions; Correspondence folder prioritizes points common between reviewer reports and co-author exchanges.

- **Summary**

A practical extension of the 101 tutorial to multi-year projects. Bilal's central insight is that a flat folder with one `CLAUDE.md` collapses task-specific judgment: chapter drafting, data cleaning, and correspondence triage need different conventions, and stuffing all of them into one instruction file either bloats it or makes it vague. The fix is the nested-CLAUDE.md pattern that Claude Code already supports natively but rarely gets explained in non-technical language.

The folder taxonomy (`Literature / Chapters / Data / Notes / Correspondence`) is opinionated but reasonable for humanities and qualitative work. For quantitative researchers, the same principle applies — separate `code/`, `data/`, `drafts/`, `referee-correspondence/` — with the same nested-instruction logic. Part 2 also begins to introduce Claude Code's understanding of project context: Claude knows where to look for a given data point because the folder layout tells it.

- **Relevance to Economics Research**

The nested-CLAUDE.md pattern is one of the highest-leverage scaling moves for any long-running empirical project (working paper plus replication code plus referee responses plus revisions). The explicit `_clean` filename convention in the Data subfolder example is the kind of small discipline that pays off across years of revisions — a directly transferable Iron Rule for any quantitative project. Bilal's framing of `Correspondence/` as a Claude-readable subfolder also gestures at a useful pattern: revise-and-resubmit responses become much easier when the agent can read both the reviewer reports and the co-author exchanges in one folder (see [[point-by-point|Point by Point]] for a dedicated R&R tool).

- **Related Concepts**
  - [[concepts/claude-md-files]]
  - [[concepts/claude-code]]
  - [[concepts/context-management]]

- **Related Summaries**
  - [[summaries/claude-code-101-bilal]]
  - [[summaries/codex-102-bilal]]
  - [[summaries/real-claude-md]]
  - [[summaries/starter-templates]]
