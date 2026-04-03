---
title: "Continuous Improvement"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/Continuous Improvement - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/system/continuous-improvement/)

## Key Ideas

- AI setups drift without a system: prompting patterns learned on Tuesday are forgotten by Thursday and rediscovered months later
- The solution is a four-step pipeline acting as a rate-limiting layer between discovery and action: scout, capture, curate, integrate
- `/tips-scout` analyzes coverage gaps in your tips log and generates targeted search prompts for AI search tools like Grok DeepSearch
- `/tips-curate` fetches @ToSelf emails, follows links, rates tips (High/Medium/Low), and appends approved ones to a persistent searchable tips log
- `/tips-integrate` converts tips into two proposal types: Type A (direct config edits with before/after diffs) and Type B (investigation tasks landing in a learning catalog)
- The learning catalog uses a tiered system (INBOX, HIGH, MEDIUM, LOW, DONE, REJECTED) to track decisions and prevent re-evaluation of dismissed items
- The system also learns reactively from user corrections and overrides during normal work, not just from proactive scouting

## Summary

This article describes a systematic pipeline for continuously improving an AI-assisted workflow system. The core problem it addresses is that without a structured approach, useful discoveries about AI techniques either get tried immediately (creating instability) or get forgotten (missing real improvements). The solution is a four-step pipeline: scout for new techniques using `/tips-scout` to generate targeted search prompts, capture findings by emailing yourself with an `@ToSelf` Gmail label, curate captured items using `/tips-curate` which rates and enriches each tip, and integrate the best items using `/tips-integrate` which generates specific config change proposals.

The pipeline produces two key artifacts. The tips log is a dated, tagged markdown file that grows over time, serving as institutional memory that survives across sessions -- after six months, the author's log had 85+ entries searchable by keyword or tag. The learning catalog tracks decisions about what to implement, using a tiered priority system where items always enter via INBOX and are never deleted (even when rejected), preventing redundant re-evaluation.

The article provides a concrete example tracing a tip from email capture through to an integration proposal, showing how a blog post about a "research-annotate-implement" workflow becomes a proposal to design a new skill. The recommended cadence is weekly scouting and curation, with biweekly integration. Importantly, the pipeline also learns reactively -- when users override classifications or substantially edit AI drafts during normal work, a self-improvement protocol proposes targeted changes on the spot.

## Relevance to Economics Research

The continuous improvement pipeline addresses a fundamental challenge in research methodology: systematically incorporating new techniques without disrupting ongoing work. Economics researchers constantly encounter new econometric methods, data sources, and computational tools, but lack a systematic way to evaluate and adopt them. The scout-capture-curate-integrate cycle provides a structured alternative to the ad hoc approach most researchers use. The tips log concept is particularly valuable as a form of research journal that tracks methodological discoveries, and the learning catalog's tier system mirrors how researchers prioritize which new techniques to invest time learning. The principle of "collect continuously, evaluate weekly, act when you have evidence" is directly applicable to managing a research agenda.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/continuous-improvement]]
- [[concepts/ai-workflow-automation]]
- [[concepts/prompt-engineering]]

## Related Summaries

- [[summaries/building-skills]]
- [[summaries/build-your-own]]
- [[summaries/skill-library]]
- [[summaries/real-claude-md]]
