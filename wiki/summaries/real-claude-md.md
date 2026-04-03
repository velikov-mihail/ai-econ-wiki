---
title: "A Real CLAUDE.md -- Annotated Example"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/A Real CLAUDE.md - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/downloads/real-claude-md-example/)

## Key Ideas

- A production CLAUDE.md file is 150+ lines compared to the starter template's 20 lines -- that gap represents months of iteration
- The Confirmation Guidelines section is the most-iterated part: defining when Claude should act autonomously vs. ask for permission took weeks of refinement
- A Modular Rules pattern keeps the main file under 200 lines by splitting detailed instructions into topic-specific files (core-voice.md, email-voice.md, project-management.md, integration-notes.md, ra-management.md, tool-limitations.md)
- The Technology Stack table gives Claude a complete map of where files live and how to access each system (Dropbox, Box, GitHub, Overleaf, Google Docs, Gmail, Calendar, Granola)
- Inline Triggers are the most critical lines -- they override default behavior for high-stakes actions like sending emails (use send-email.py, not MCP) and writing to Overleaf (use `gh` CLI, not MCP)
- Global CLAUDE.md describes how you work; project-level CLAUDE.md files describe what you're working on

## Summary

This article presents a sanitized version of Chris Blattman's actual production CLAUDE.md file -- the global configuration file that governs how Claude Code operates across all his work. The file defines his identity and role (professor managing 10-20 active research projects), specifies Claude's role as project manager, research manager, and executive assistant, sets current priorities, and establishes detailed working style preferences. The article emphasizes that this is the end product of months of iteration, not something to build on day one.

The most instructive sections are the Confirmation Guidelines and the Modular Rules pattern. The Confirmation Guidelines define a clear boundary: Claude should ask before sending emails, writing to Google Docs, or performing destructive operations, but should not ask after receiving clear instructions, after plan approval, for routine file operations, or after errors (just retry). The author notes this section required weeks of tuning to get the balance right, and recommends starting permissive and tightening. The Modular Rules pattern addresses the scaling problem -- without it, the file would be 800+ lines. Instead, detailed instructions are split into topic-specific files (core voice, email voice, project management, integration notes, RA management, tool limitations) that load only when relevant.

The Technology Stack table and Key Directories section provide Claude with a spatial map of the user's digital environment, preventing guesswork about where files live. Inline Triggers serve as critical overrides for high-stakes actions -- specifying, for example, that email must be sent via a Python script rather than MCP (which can only draft), and that Overleaf/LaTeX operations must use the `gh` CLI. The article concludes by distinguishing between global instructions (how you work) and project-level instructions (what you're working on).

## Relevance to Economics Research

This annotated example is directly applicable to any economics researcher setting up Claude Code for their workflow. The professor persona -- managing multiple research projects, coordinating with RAs, writing in LaTeX/Overleaf, storing data across Dropbox and university Box systems -- mirrors a typical empirical economics researcher's setup. The Confirmation Guidelines provide a tested template for the autonomy-vs-oversight balance that researchers need when using AI for tasks ranging from low-stakes file operations to high-stakes email communications with coauthors or journal editors. The Modular Rules pattern is essential for researchers with complex workflows spanning data analysis, paper writing, grant management, and teaching. The Technology Stack table approach solves the practical problem of Claude not knowing where CRSP data lives vs. where paper drafts are stored.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/claude-md-configuration]]
- [[concepts/ai-workflow-automation]]
- [[concepts/prompt-engineering]]

## Related Summaries

- [[summaries/building-skills]]
- [[summaries/build-your-own]]
- [[summaries/skill-library]]
- [[summaries/continuous-improvement]]
