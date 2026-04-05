---
title: "Claude Code Skills for Academic Researchers: A Practical Introduction"
tags: [summary, claude-code-skills, skills, claude-code, workflow, presentation]
sources:
  - "[[raw/papers/Brownbag_Claude_Skills.pdf]]"
date_updated: 2026-04-05
date_published: 2026-04-01
---

- **Author/Source**: Alessandro Spina (UTS Finance Department)
- **Original**: Local file (no URL available)

- **Key Ideas**
  - Claude Code Skills are reusable folders containing a SKILL.md file (instructions, conventions, templates) that Claude loads on demand, solving the "RA who forgets everything" problem across sessions.
  - Skills differ from CLAUDE.md: CLAUDE.md is always loaded and holds short conventions (~100-150 lines); Skills are loaded on demand and encode full workflows with examples, templates, and helper scripts.
  - Skills use progressive disclosure: Level 1 (metadata, ~100 tokens, always in system prompt) triggers Level 2 (full SKILL.md body) only when relevant, which may reference Level 3 (bundled scripts and templates).
  - The description field is critical -- Claude tends to under-trigger, so descriptions should be explicit, name specific packages/methods, and include "even if the user doesn't mention X" language.
  - Five example skills for researchers: R empirical code standards (data.table, fixest, arrow), structured paper review, Beamer slide checker, dataset profiler, and a meta-skill for writing better skills.

- **Summary**

Spina's presentation introduces Claude Code Skills as a practical solution for academic researchers who repeatedly correct Claude on the same conventions across sessions. A Skill is a folder with a required SKILL.md file (YAML frontmatter for metadata plus Markdown body for instructions) and optional subfolders for scripts, references, and assets (e.g., Beamer preambles, style files). Skills can be installed globally (~/.claude/skills/ for cross-project conventions) or at the project level (.claude/skills/ for paper-specific workflows).

The presentation walks through five concrete skills. The R Empirical Code Standards skill enforces data.table over tidyverse, fixest for regressions, arrow for Parquet I/O, and clustered standard errors by default. The Structured Paper Review skill produces consistent summaries with a dedicated identification strategy section that forces Claude to report exogenous variation, instrument validity, and parallel trends rather than just "they ran a regression." The Beamer Slide Checker implements a five-phase audit loop (compile, render PNGs for visual inspection, fix, recompile, summarize). The Dataset Profiler runs a five-phase exploration protocol before analysis begins. The Skill Writing Guide is a meta-skill encoding best practices: start small, use concrete examples, include "what NOT to do" sections, and apply the "3-correction rule" (if you have corrected Claude 3+ times on something, it belongs in a skill).

Practical advice includes: skills are reactive (they fire when Claude decides they are relevant, not on a schedule), they cannot scrape websites or maintain state between sessions, and they should be iterated -- tested with natural prompts, updated when Claude gets corrections, and hosted in a GitHub repo.

- **Relevance to Economics Research**

This presentation provides a hands-on guide to structuring Claude Code workflows for empirical research. The example skills (R code standards with fixest and data.table, paper review with identification strategy focus, dataset profiling) are directly tailored to the empirical economics stack. The progressive disclosure architecture and description-writing tips are essential for anyone building Claude Code skills for research projects.

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/claude-code]]
  - [[concepts/ai-skills]]
  - [[concepts/claude-md-files]]
  - [[concepts/agentic-workflows]]

- **Related Summaries**
  - [[summaries/building-skills]]
  - [[summaries/agents-vs-skills]]
  - [[summaries/cc-series-33-continue-learning]]
