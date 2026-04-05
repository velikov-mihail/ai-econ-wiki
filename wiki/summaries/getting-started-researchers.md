---
title: "Getting Started with Claude Code: A Researcher's Setup Guide"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Getting Started with Claude Code A Researcher's Setup Guide.md]]"
date_updated: 2026-04-03
date_published: 2026-03-29
---
- **Original**: [https://paulgp.substack.com/p/getting-started-with-claude-code](https://paulgp.substack.com/p/getting-started-with-claude-code)


**Author/Source**: Paul Goldsmith-Pinkham, [paulgp.substack.com](https://paulgp.substack.com/p/getting-started-with-claude-code) (companion to Markus Academy Video 1)

## Key Ideas

- Claude Code is a terminal-based AI assistant with direct access to your local filesystem -- analogous to having a capable RA sitting at your computer rather than exchanging emails with one
- A five-level hierarchy of AI coding tools ranges from browser chat (Level 0) through IDE copilots (Level 1-2), dedicated coding agents like Claude Code (Level 3), MCP-enhanced agents (Level 4), to fully autonomous containers (Level 5)
- The context window is the single most important concept: every turn appends to a growing document sent back and forth, and performance degrades as it fills up
- Intentional context management is critical -- use `/compact` to summarize, write state to files (e.g., `progress.md`), break work into focused 5-10 turn sessions rather than marathons
- Pricing tiers are Pro ($20/month), Max ($100/month), and Max 20x ($200/month); the $20 or $100 tier is sufficient for most researchers
- Privacy heuristic: if you would put data on Dropbox, the risk profile with Claude Code is similar; IRB data and PII should be walled off
- Terminal setup recommendations include Ghostty (fast terminal), Zellij (split-pane multiplexer), and Oh My Zsh (better shell with git integration)

## Summary

This article by Paul Goldsmith-Pinkham serves as the written companion to Video 1 of his Markus Academy series on AI coding tools for economists. It targets three audiences: those unfamiliar with AI tools, irregular users, and active users looking for more ideas. The central argument is twofold -- these tools dramatically accelerate the distance from research idea to empirical result (especially for tedious tasks like data cleaning and debugging), and even skeptics need to understand the capabilities to function as referees, advisers, or coauthors.

The article provides a clear conceptual framework through Kyle Jensen's "ladder" of AI tool levels, distinguishing browser chat, IDE copilots, agentic coding agents (Claude Code), MCP-enhanced workflows, and fully autonomous systems. It contrasts Claude Code with Cowork (a sandboxed, browser-like alternative that ships with the Claude desktop app) and IDE-based tools like Cursor. The key message is that Claude Code at Level 3 offers the most power for research workflows because it has full access to the filesystem, shell commands, and installed tools.

The most substantive technical section explains the context window -- how every message, file read, tool call, and response accumulates into a single growing document that is re-sent each turn. The article explains compaction (automatic summarization when the window fills), strategies for manual context management (writing progress to files, starting fresh sessions), and the rough performance relationship: longer contexts and less precision lead to worse outputs. Practical terminal setup recommendations (Ghostty, Zellij, Oh My Zsh) round out the guide for researchers willing to invest 15 minutes in a better working environment.

## Relevance to Economics Research

This is the most directly relevant setup guide for academic economists. Written by a finance/applied econometrics professor, it frames Claude Code explicitly as a research tool -- the RA analogy, the emphasis on reproducibility, the trust-but-verify principle for statistical code, and the practical tips about correcting the LLM early (e.g., "use R instead of Python") all reflect real empirical research workflows. The context window explanation is particularly valuable because it helps researchers understand why long data-analysis sessions can degrade and how to structure their AI-assisted work for better results.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/context-management]]
- [[concepts/agentic-ai]]
- [[concepts/ai-tools-landscape]]
- [[concepts/data-privacy]]

## Related Summaries

- [[summaries/getting-started-economists]]
- [[summaries/install-mac]]
- [[summaries/install-windows]]
- [[summaries/setup-vs-code]]
- [[summaries/privacy-setup]]
