---
title: "Getting Started: Claude Code for Economists (Markus Academy Ep. 162-1)"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Getting Started Claude Code for Economists with Paul Goldsmith-Pinkham  Markus Academy  Ep. 162-1.md]]"
date_updated: 2026-04-03
---
- **Original**: [https://www.youtube.com/watch?v=HzgByl5ZsWE](https://www.youtube.com/watch?v=HzgByl5ZsWE)


**Author/Source**: Paul Goldsmith-Pinkham and Markus' Academy, [YouTube](https://www.youtube.com/watch?v=HzgByl5ZsWE) (published 2026-03-28)

## Key Ideas

- Claude Code lets you type natural language in the terminal and have it converted into code that operates on your local files -- like having an RA at your computer rather than exchanging emails with one
- The miniseries covers seven planned videos: (1) setup and overview, (2) simple data analysis with web data, (3) scraping Edgar filings, (4) big data and HPC clusters, (5) writing and referee responses, (6) customization, and (7) best practices and git workflows
- A five-level hierarchy of AI tools is introduced: browser chat, IDE copilots, agentic IDEs (Cursor), dedicated coding agents (Claude Code), and fully autonomous containers
- Claude Code vs. Cowork: Claude Code has full filesystem and internet access; Cowork is sandboxed with restricted IP access, safer but less powerful -- do not judge AI capabilities based on the restricted version
- The context window degrades with length; intentional compaction (using `/compact`) and writing state to files keeps performance high
- Privacy stance: treat Claude Code API exposure as comparable to Dropbox; wall off IRB/PII/HIPAA data; do not paste API keys or passwords
- Subscription pricing starts at $20/month (Pro), which already includes Claude Code access; $100/month (Max) for heavy users

## Summary

This is the transcript of the first video in Paul Goldsmith-Pinkham's Markus Academy miniseries on using Claude Code for applied economics research. The conversation between Goldsmith-Pinkham and Markus Brunnermeier covers the same ground as the companion blog post but in a more conversational, Q&A format that surfaces additional nuances through Markus's questions.

The video opens with two motivations for economists to engage with AI coding tools: first, execution speed (the distance from idea to empirical result shrinks dramatically, and tedious work like data cleaning and debugging gets much faster); second, calibration (even skeptics need to understand what is and is not possible, whether as referees, advisers, or coauthors). Goldsmith-Pinkham then walks through Kyle Jensen's hierarchy of AI tool levels, carefully distinguishing between browser chat, IDE copilots like GitHub Copilot (clarifying the naming confusion with Microsoft Copilot in response to Markus's question), agentic IDEs like Cursor, and dedicated coding agents like Claude Code.

The discussion of Claude Code vs. Cowork is particularly useful: Goldsmith-Pinkham explains that Cowork is a sandboxed Chromium-based app that restricts internet access to specific IP addresses, making it safer but significantly less capable out of the box. He warns against forming opinions about AI capabilities based on the restricted version. The context window explanation includes an interactive exchange where Markus asks whether you can guide what the LLM remembers during compaction -- yes, via `/compact` with specific instructions. The video concludes with practical tips: be specific (like instructing an RA), iterate without arguing, correct direction early, and trust but verify.

## Relevance to Economics Research

This video is explicitly designed for academic economists and frames everything through that lens. The miniseries roadmap -- covering data analysis, Edgar scraping, big data on HPC clusters, referee response management, and git workflows -- maps directly onto the daily work of empirical researchers. The conversational format between two economists surfaces practical concerns (Do I need R/Python installed? Is it running in the cloud?) that a written guide might skip. The RA analogy is central and well-developed: Claude Code is fast and capable, but like any RA, its output needs verification, especially at statistical edge cases.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/context-management]]
- [[concepts/agentic-ai]]
- [[concepts/data-privacy]]
- [[concepts/ai-tools-landscape]]

## Related Summaries

- [[summaries/getting-started-researchers]]
- [[summaries/install-mac]]
- [[summaries/install-windows]]
- [[summaries/setup-vs-code]]
- [[summaries/privacy-setup]]
