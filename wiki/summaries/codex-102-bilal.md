---
title: "Codex 102 for Academic Researchers (Bilal)"
tags: [summary, foundations-setup, codex, project-organization]
sources:
  - "[[raw/articles/Codex 102 for Academic Researchers.md]]"
date_updated: 2026-05-15
date_published: 2026-05-15
---

- **Author/Source**: Mushtaq Bilal, X thread
- **Original**: [https://x.com/MushtaqBilalPhD/status/2055223177001726349](https://x.com/MushtaqBilalPhD/status/2055223177001726349)

- **Key Ideas**
  - Sequel to [[codex-101-bilal|Codex 101]]. Covers five topics for scaling Codex from short projects to multi-year work: (1) structuring a long project; (2) Plan Mode and Skills; (3) custom agents for parallel research tasks; (4) connecting Codex to other apps; (5) hooks and automations.
  - Same folder taxonomy as the Claude Code 102 article (`Literature / Chapters / Data / Notes / Correspondence`), with **`AGENTS.md`** replacing `CLAUDE.md` as the per-folder instruction file.
  - Introduces Codex's **Plan Mode and Skills** (Codex equivalents of Claude Code's plan mode and skill bundles), **custom agents** for parallelizing different research tasks, **MCP connections** to external apps, and **hooks** for automation.
  - Maintains the deliberately non-technical voice: "if you can write sentences in English, you can use Codex."

- **Summary**

A direct Codex translation of the [[claude-code-102-bilal|Claude Code 102]] organization pattern, plus a survey of Codex-specific features (Plan Mode, Skills, custom agents, MCP, hooks). The organization advice is portable across both ecosystems — the same folder layout, the same nested-instruction-file principle — and the comparison is useful for researchers choosing between Codex and Claude Code: most of the workflow conventions transfer.

The introduction of hooks and automations in a beginner-friendly tutorial is notable; Codex's hook system enables time-based and event-based automation (e.g., periodic checks for new bugs, automatic responses to incoming files) that Claude Code currently exposes only to more advanced users. For long-running research projects, this could be the differentiating Codex feature for academics willing to set up scheduled tasks (literature alerts, citation re-verification, draft auto-review).

- **Relevance to Economics Research**

Useful for any economist running a multi-year empirical project on the Codex stack. The hooks/automations section in particular is worth a closer read — automating "every Friday, re-run the literature search and flag new papers citing X" or "after each data refresh, re-run integrity checks" is the kind of cadence-based maintenance most empirical projects skip because it would otherwise need a cron job and a Python wrapper. Codex hooks remove the wrapper.

- **Related Concepts**
  - [[concepts/agentic-workflows]]
  - [[concepts/context-management]]
  - [[concepts/mcp-protocol]]

- **Related Summaries**
  - [[summaries/codex-101-bilal]]
  - [[summaries/claude-code-102-bilal]]
  - [[summaries/panjwani-codex-course]]
