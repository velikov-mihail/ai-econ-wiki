---
title: "Guide to Codex for Economists"
tags: [summary, foundations-setup, claude-code-skills, coding-with-llms, agentic-workflows]
sources:
  - "[[raw/articles/Guide to Codex for Economists.md]]"
date_updated: 2026-06-20
date_published: 2026-06-20
---

- **Author/Source**: Aniket Panjwani, via aieconomist.io
- **Original**: [https://aieconomist.io/guides/codex-for-economists](https://aieconomist.io/guides/codex-for-economists)

## Key Ideas

- A timestamped guide to the Codex Desktop App Full Course (4-hour YouTube video) — not to be read as an app developer, but with the narrower economist's goal: learn the interface, permissions, skills, Git, and the review loop to make research folders safer and faster.
- Core workflow pattern: **plan the work → let Codex operate → inspect the diff → keep only what improves the project**.
- **Skills are the highest-leverage agentic coding concept** for economists. The guide explicitly flags this section ("pay close attention") above plugins, MCPs, and other advanced features.
- **Git is essential for agentic coding**: checkpoints, branches, private repos, reviewing diffs. You don't need to memorize Git commands, but you need to know how to get Codex to use Git.
- Project instructions / AGENTS.md should be kept short for research: commands to run, files never to edit, what counts as valid output, how results should be checked. Giant instruction files backfire.
- Practical exercises after watching: (1) turn a YouTube seminar transcript into a research memo, (2) create one LaTeX skill (for tables, Beamer decks, or paper-to-deck conversion), (3) connect one real knowledge surface (email, calendar, Drive, Notion) for seminar prep or coauthor follow-up, (4) ask Claude Code to evaluate an old project repo and implement its suggested cleanup.

## Summary

Panjwani's guide provides economists with a purposeful reading plan for a 4-hour YouTube course on the OpenAI Codex Desktop App. Rather than watching as an app developer, he recommends focusing on what matters for research: the conceptual framing of Codex as a file-reading, file-editing, command-running agent (not just a chatbot), context window management, the permissions model, and above all, skills. The guide is explicit that skills — pre-written instruction files that encode reusable workflows — are the single highest-leverage concept to learn in the agentic coding toolkit.

For economists, the guide's structure is particularly useful: it identifies which sections to watch closely (conceptual intro, desktop app basics, skills), which to skim (plugins, deciding what to build), and which to skip (cloud delegation). The four practical exercises ground the course in genuine research tasks, from literature processing to LaTeX automation to repo hygiene.

## Relevance to Economics Research

This is a concise, economist-specific on-ramp for the Codex Desktop App — a direct companion to the parallel Claude Code ecosystem. The emphasis on skills as the key differentiator aligns with the growing consensus in this wiki that reusable workflows (skills/commands) are where the sustained productivity gains come from, not ad hoc prompting. The exercises — transcript-to-memo, LaTeX skill, knowledge surface connection, repo cleanup — map directly to tasks economists face regularly. The guide complements the Panjwani VoxDev webinar and the Goldsmith-Pinkham Markus Academy series by providing an app-specific entry point.

## Related Concepts

- [[concepts/claude-code-skills]]
- [[concepts/coding-with-llms]]
- [[concepts/agentic-workflows]]
- [[concepts/claude-md-files]]
- [[concepts/ide-and-terminal]]

## Related Summaries

- [[summaries/ai-agents-econ-research|AI Agents for Economic Research (Panjwani VoxDev)]]
- [[summaries/panjwani-slides|AI Agents for Economics Research (Slides)]]
- [[summaries/panjwani-codex-course|OpenAI Codex Full Course]]
- [[summaries/skills-markus-162-6|Skills: Claude Code for Economists (Markus Academy 162-6)]]
- [[summaries/building-skills|Building Skills (Blattman)]]
