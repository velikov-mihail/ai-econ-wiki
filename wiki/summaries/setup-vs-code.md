---
title: "Set Up VS Code for Claude Code"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Set Up VS Code - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/setup/vscode-setup/)

## Key Ideas

- VS Code provides a visual file explorer, syntax-highlighted editor, and integrated terminal -- making Claude Code easier to use than a standalone terminal
- The recommended layout is: Explorer (left), Editor (center), Terminal with Claude Code (right) -- giving a three-panel research workspace
- The official Claude Code extension by Anthropic integrates into VS Code but requires the CLI to be installed first
- AI-focused alternatives include Cursor ($20/month) and Windsurf ($10/month), both VS Code forks with deeper AI integration, but VS Code is free and well-supported
- Opening a project folder (File > Open Folder) is essential -- Claude Code needs folder context to see and work with your files
- VS Code highlights Claude's file edits in green (added) and red (removed), a major advantage over plain terminal usage
- A mature research project example shows Claude Code managing proposals, literature, IRB documents, grants, and field materials alongside specialized skills like `/proposal-write` and `/review-plan`

## Summary

This article guides users through setting up VS Code as the primary interface for working with Claude Code. It positions VS Code not as a coding tool per se, but as a container that makes Claude Code more usable -- you do not need to write code to benefit from it. The setup involves downloading VS Code, installing the official Claude Code extension from Anthropic, opening a project folder, and rearranging the layout so that the terminal (where Claude Code runs) sits on the right side of the screen.

The guide walks through each step with screenshots, from the initial Welcome screen through to a fully configured workspace. It emphasizes closing the default Chat panel in favor of the terminal, which is described as "more powerful." The recommended workflow is to click files in the Explorer to view them in the editor while conversing with Claude in the terminal panel alongside.

The article also showcases what a mature research project looks like in VS Code, using a real example (the Medellin Mental Health Study) with dedicated folders for papers, presentations, grants, IRB documents, and field materials. This demonstrates how Claude Code scales from simple file queries to complex project management involving proposal writing, critical review simulation, and status reporting. The article briefly compares VS Code to paid alternatives (Cursor, Windsurf) but recommends VS Code for most users due to its zero cost and official extension support.

## Relevance to Economics Research

The three-panel layout (files, document, AI assistant) directly maps to how researchers work -- navigating project files, reading or editing manuscripts and code, and iterating with an AI assistant. The mature project example explicitly shows an academic research workflow with grant proposals, referee reports, and IRB materials, making the case that VS Code plus Claude Code can serve as a complete research project management environment rather than just a coding tool.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/ide-setup]]
- [[concepts/ai-tool-setup]]
- [[concepts/research-project-management]]

## Related Summaries

- [[summaries/install-mac]]
- [[summaries/install-windows]]
- [[summaries/getting-started-researchers]]
