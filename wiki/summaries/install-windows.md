---
title: "Install Claude Code (Windows)"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Install (Windows) - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---
- **Original**: [https://claudeblattman.com/toolkit/install-windows/](https://claudeblattman.com/toolkit/install-windows/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/toolkit/install-windows/)

## Key Ideas

- Claude Code on Windows runs in PowerShell rather than Terminal, but the workflow is otherwise identical to the Mac version
- Installation requires Node.js (LTS from nodejs.org) with the "Tools for Native Modules" checkbox enabled during install, plus `npm install -g @anthropic-ai/claude-code`
- Permission issues are resolved by running PowerShell as Administrator (right-click, "Run as administrator")
- Windows-specific troubleshooting includes execution policy errors (fix with `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`) and antivirus interference
- Claude Code can access cloud-synced folders (OneDrive, Dropbox, Google Drive) on the local filesystem
- Session management is the same as Mac: `claude -c` to continue, `claude --resume` to pick from past sessions
- The working directory when launching Claude Code determines its file access scope

## Summary

This article mirrors the Mac installation guide but is tailored for Windows users. It walks complete beginners through opening PowerShell, installing Node.js, installing Claude Code via npm, authenticating with an Anthropic account, and running a first conversation. The conceptual framing is the same: Claude Code gives Claude direct access to your local files and workflow, making it far more powerful than the browser-based chat interface.

The Windows-specific content focuses on PowerShell as the command-line interface, the importance of checking "Tools for Native Modules" during Node.js installation, and troubleshooting issues unique to Windows such as execution policy restrictions and antivirus software blocking npm packages. The guide also notes that closing and reopening PowerShell (or restarting the computer) is often necessary after installing Node.js for the PATH to update.

After setup, the guide covers the same daily usage patterns as the Mac version -- navigating to project folders, starting sessions, resuming conversations, and basic keyboard shortcuts. It concludes with the same recommended next steps: CLAUDE.md setup, understanding operating modes, MCP connections, and the skill library.

## Relevance to Economics Research

Most economists at universities use Windows machines, making this the more relevant installation guide for the typical researcher. The step-by-step instructions lower the barrier for social scientists who may have never opened PowerShell. Once installed, Claude Code provides the same direct file access and script execution capabilities that make it valuable for empirical research workflows -- data cleaning, code iteration, and project management.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/ide-and-terminal]]
- [[concepts/ai-tools-landscape]]

## Related Summaries

- [[summaries/install-mac]]
- [[summaries/setup-vs-code]]
- [[summaries/privacy-setup]]
- [[summaries/getting-started-researchers]]
