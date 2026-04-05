---
title: Your CLAUDE.md
tags:
- summary
- claude-code-skills
- context-management
- claude-code
- configuration
sources:
- '[[raw/articles/Your CLAUDE.md - Claude Blattman · AI for Professionals Who Don''t
  Code.md]]'
date_updated: 2026-04-03
date_published: 2026-03
---
- **Original**: [https://claudeblattman.com/toolkit/claude-md/](https://claudeblattman.com/toolkit/claude-md/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/toolkit/claude-md/)

## Key Ideas

- A CLAUDE.md file is a personal instruction document that Claude Code reads automatically at the start of every session, providing persistent context about who you are, how you work, and what tools you use.
- Without it, every session starts fresh; with it, Claude tailors suggestions to your actual workflow and skill level from the first interaction.
- The file lives at `~/.claude/CLAUDE.md` for global context and can be supplemented with project-specific CLAUDE.md files in individual project directories. Claude loads the global file first, then project-specific overrides.
- A good CLAUDE.md is specific and actionable (file paths, skill levels, tool preferences) rather than vague ("I do data analysis"). The article contrasts underdeveloped vs. good examples.
- The investment is small (20-30 minutes initially) and compounds over time as you refine it.
- Cross-machine sync is handled via symlinks from `~/.claude/CLAUDE.md` to a cloud-synced folder (Dropbox, OneDrive, etc.).
- Voice and writing style preferences can be stored in `~/.claude/rules/core-voice.md` for auto-loading, with context-specific registers loaded on demand.

## Summary

This article explains how to create and maintain a CLAUDE.md file -- the configuration mechanism that gives Claude Code persistent knowledge about the user across sessions. The file captures professional identity, primary work, tools and software, file locations, skill levels, working preferences, and current projects. The article provides a fill-in-the-blank template and contrasts a vague three-line example ("I'm a researcher") with a detailed, actionable example for a predoctoral RA that includes specific tools, file paths, skill levels by language, and current project phases.

The article also covers the two-tier system: a global CLAUDE.md at `~/.claude/CLAUDE.md` for personal identity and preferences, and optional project-level CLAUDE.md files for project-specific conventions, team members, and tools. Claude loads both when starting a session in a project directory, with project instructions able to override or extend global ones. Practical tips include starting minimal and expanding, being specific about file locations, including honest skill level assessments, and updating when things change. The article notes that everything in CLAUDE.md is sent to the API, so passwords and API keys should be excluded.

The voice and writing style section introduces a mechanism for ensuring AI output matches the user's actual writing patterns rather than defaulting to generic AI prose. A core voice file auto-loads from `~/.claude/rules/`, while context-specific registers (proposal voice vs. email voice) can be loaded on demand through skills or imports.

## Relevance to Economics Research

For economics researchers, a well-crafted CLAUDE.md dramatically improves AI assistance by encoding domain-specific context: research field, preferred statistical packages, data locations (e.g., WRDS data on a specific drive), coding skill level, and current paper stages. The two-tier system is especially useful for researchers managing multiple projects -- a global file captures identity and general preferences, while project-level files capture each paper's specific conventions, co-author preferences, and data pipeline details. The honest skill-level specification prevents Claude from producing code that is too advanced or too basic for the user's capabilities.

## Related Concepts

- [[concepts/context-management]]
- [[concepts/claude-code]]
- [[concepts/ai-workflows]]
- [[concepts/claude-md-files]]

## Related Summaries

- [[summaries/prompt-plan-review-revise]]
- [[summaries/prompt-engineering]]
- [[summaries/ai-project-folders]]
