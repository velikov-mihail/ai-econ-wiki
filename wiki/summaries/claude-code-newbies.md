---
title: "Claude Code for Newbies - Setup Guide"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Claude Code for Newbies - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---
- **Original**: [https://claudeblattman.com/setup/](https://claudeblattman.com/setup/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/setup/)

## Key Ideas

- Claude Code can be run from a plain terminal or inside a code editor (VS Code or Cursor); no coding experience is required
- Installation requires Node.js and a single `npm install -g @anthropic-ai/claude-code` command, with walkthroughs for both Mac and Windows
- Three operating modes: Default (proposes edits, user confirms), Plan Mode (explores without touching files), and Auto-Accept (applies edits automatically); cycle with Shift+Tab
- The setup sequence is: install Claude Code, optionally set up VS Code, create a CLAUDE.md instruction file, then configure MCP integrations
- CLAUDE.md is described as the critical personalization file that tells Claude about the user's role, projects, and preferences
- A paid Anthropic account (Claude Pro minimum) and basic willingness to use a terminal are the only prerequisites
- The end result is an AI system with email/calendar/document integrations and a library of slash-command skills that improves over time

## Summary

This article is the primary onboarding guide for non-technical users who want to set up Claude Code. It frames the terminal as the biggest hurdle and systematically addresses that barrier by explaining two ways to run Claude Code (plain terminal or inside a code editor like VS Code), providing step-by-step installation instructions for both Mac and Windows, and introducing the three operating modes that control how much autonomy Claude has over file edits.

The guide structures setup as a five-step sequence: install Claude Code, optionally install VS Code with the Claude Code extension, create a CLAUDE.md personalization file, and configure MCP integrations for email and calendar access. It explains how Claude Code thinks in each mode (Default asks permission for every edit, Plan mode explores without changing anything, Auto-Accept runs autonomously) and provides guidance on when to use each. A troubleshooting table addresses the most common setup failures. The article positions this setup as a few-hour investment that pays for itself within the first week of regular use.

## Relevance to Economics Research

This guide is the entry point for economists who want to move beyond browser-based chatbot interactions to an AI system that can read and edit local files, search email, and run automated workflows. The CLAUDE.md concept is particularly relevant for researchers who want Claude to understand their specific research context (datasets, co-authors, methodological preferences). The Plan Mode is useful for exploring unfamiliar codebases or data files without risk, and the skill library concept maps onto automating recurring research tasks like literature search, data cleaning, and report generation.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/claude-md-files]]
- [[concepts/mcp-protocol]]
- [[concepts/ai-workflows]]

## Related Summaries

- [[summaries/mcp-setup]]
- [[summaries/chatbot-essentials]]
- [[summaries/chatbots-done-right]]
- [[summaries/my-claude-code-setup]]
