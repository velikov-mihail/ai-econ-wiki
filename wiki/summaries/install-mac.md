---
title: "Install Claude Code (Mac)"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Install (Mac) - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/toolkit/install-mac/)

## Key Ideas

- Claude Code runs Claude in the terminal instead of a browser, giving it direct access to your local files and workflows
- Installation requires only Node.js (from nodejs.org) and a single npm command: `npm install -g @anthropic-ai/claude-code`
- First-time authentication links Claude Code to your Anthropic account via a one-time browser-based login flow
- The folder you launch Claude Code from determines which files it can see -- navigate to a project folder before starting
- Session management commands (`claude -c` to continue, `claude --resume` to pick from history) let you pick up where you left off
- Claude Code can read any file on your machine, including cloud-synced folders; content read is sent to Anthropic's API but is not used for model training per their data policy
- The guide is aimed at complete terminal beginners and requires no prior command-line experience

## Summary

This article is a step-by-step beginner's guide to installing Claude Code on macOS. It starts by explaining the difference between using Claude in a browser (isolated, copy-paste workflow) versus Claude Code in the terminal (integrated, direct file access). The analogy offered is that the browser version is like texting a smart friend, while Claude Code is like having that friend sit at your computer with you.

The installation process is straightforward: open Terminal, install Node.js from nodejs.org (LTS version), run `npm install -g @anthropic-ai/claude-code`, then type `claude` to authenticate via your browser. The guide provides troubleshooting tips for common issues like permission errors (use `sudo`) and `node: command not found` (reopen Terminal).

After installation, the article covers daily usage patterns -- starting new sessions, navigating to project folders, continuing previous conversations, and basic Claude Code commands. It concludes with recommended next steps including setting up a CLAUDE.md file, understanding Claude Code's three operating modes, connecting external services via MCP, and exploring the skill library.

## Relevance to Economics Research

For economists and social scientists who are not regular terminal users, this guide removes the technical barrier to entry for Claude Code. The tool's ability to read project files directly, run scripts, and maintain conversation context makes it particularly valuable for research workflows involving data cleaning, code debugging, and iterative analysis -- tasks that previously required either command-line expertise or tedious copy-paste between a browser chat and a code editor.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/terminal-basics]]
- [[concepts/ai-tool-setup]]

## Related Summaries

- [[summaries/install-windows]]
- [[summaries/setup-vs-code]]
- [[summaries/privacy-setup]]
- [[summaries/getting-started-researchers]]
