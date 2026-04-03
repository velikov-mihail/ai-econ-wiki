---
title: "Building Skills"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/Building Skills - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/system/building-skills/)

## Key Ideas

- Skills are reusable markdown-based prompts saved as `.md` files in `~/.claude/commands/` that act as slash commands in Claude Code
- The development lifecycle follows five stages: notice a repeated pattern, do it manually 3-4 times, write the skill, test and iterate, then stabilize with versioning and documentation
- Skills accept `$ARGUMENTS` for user input and can reference external files with `@` syntax for shared rules and style guides
- Core design principles: one skill per job, match complexity to task, default to action with no arguments, fail gracefully with helpful error messages
- Common iteration problems include excessive verbosity, missing context, wrong output format, and poor edge-case handling
- Reusable patterns include flags parsing, phased execution with user checkpoints, depth calibration (light/standard/deep), critic stance, output templates, and iteration gates

## Summary

This article provides a comprehensive guide to building custom skills (slash commands) for Claude Code. Skills are the building blocks of a self-improving AI workflow system, and the article walks through the full development lifecycle from recognizing a repeated task pattern to stabilizing a production-ready skill. The key insight is that the best skills emerge from noticing what you do repeatedly -- prompts typed more than twice, multi-step workflows walked through manually, or tasks where the same context is always re-provided.

The article details the anatomy of a well-designed skill file, covering arguments handling (`$ARGUMENTS`), external file references via `@` syntax, error handling blocks, and explicit output format specifications. It emphasizes that skills are just structured markdown with no code or compilation required, making them accessible to non-programmers.

A particularly useful section catalogs reusable design patterns found in well-designed skills: flags parsing for named parameters, phased execution with user checkpoints between stages, depth calibration for adjusting thoroughness, critic stance for shifting Claude's role, output templates for consistent formatting, and iteration gates that pause for user feedback. These patterns provide a toolkit for building increasingly sophisticated workflows.

## Relevance to Economics Research

For economics researchers, the skill-building framework offers a systematic way to automate repetitive research workflows -- running robustness checks, formatting regression tables, reviewing paper drafts, or generating data summaries. The phased execution pattern (discover, plan, implement with checkpoints) maps naturally onto empirical research workflows where each stage requires human judgment. The ability to build skills without coding makes this accessible to researchers who work primarily in LaTeX and statistical software rather than general-purpose programming.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/skills-vs-agents]]
- [[concepts/prompt-engineering]]
- [[concepts/ai-workflow-automation]]

## Related Summaries

- [[summaries/skill-library]]
- [[summaries/build-your-own]]
- [[summaries/continuous-improvement]]
- [[summaries/patterns]]
- [[summaries/real-claude-md]]
