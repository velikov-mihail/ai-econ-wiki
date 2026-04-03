---
title: "Every Claude Code Hack I Know (March 2026)"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Every Claude Code Hack I Know (March 2026).md]]"
date_updated: 2026-04-03
---

**Author/Source**: @mvanhorn (Matt Van Horn), [X/Twitter thread](https://x.com/mvanhorn/status/2035857346602340637), March 22, 2026

## Key Ideas

- The core workflow is "plan first, always": every idea immediately becomes a plan.md file via `/ce:plan`, flipping the traditional 80/20 coding-to-planning ratio
- The Compound Engineering plugin enables a plan-then-build loop where `/ce:plan` launches parallel research agents and `/ce:work` implements the plan with test verification
- Voice input (via Monologue or WhisperFlow) is a critical productivity multiplier because Claude Code is smart enough to interpret imperfect transcription
- Running 4-6 parallel Claude Code sessions simultaneously is the author's default working mode, requiring bypass permissions and audio notifications to manage
- Three essential settings: "dangerously skip permissions" for autonomous operation, sound hooks for completion alerts, and Zed autosave at 500ms for real-time co-editing
- `/last30days` skill searches Reddit, X, YouTube, HN, and more in parallel to ground plans in current community knowledge rather than stale training data
- Meeting transcripts (via Granola) can be turned into structured product proposals by cross-referencing against the codebase and prior strategy documents

## Summary

This article is a practitioner's guide to power-using Claude Code, written as an X/Twitter thread by a software developer and open source contributor. The central thesis is that AI-assisted work should be plan-driven: every idea, bug, or feature request immediately becomes a structured plan.md file before any implementation begins. The Compound Engineering plugin operationalizes this by launching parallel research agents that analyze the codebase, search past solutions, and produce a grounded plan with acceptance criteria. Implementation then becomes mechanical execution of the plan via `/ce:work`.

The article describes an intensive workflow: 4-6 parallel Claude Code sessions running simultaneously in separate terminal windows, with voice dictation replacing typing, bypass permissions enabling autonomous operation, and audio notifications signaling task completion. The author runs `/last30days` research queries before planning to ground decisions in current community knowledge. Meeting transcripts from Granola are processed into structured proposals by cross-referencing against codebases and prior strategy documents. The piece concludes with a Disney World trip-planning example that demonstrates the full workflow (research, plan, build, deploy, automate reminders) applied to a non-coding task, emphasizing that the approach is domain-agnostic.

## Relevance to Economics Research

While written from a software development perspective, several techniques transfer directly to economics research. The plan-first discipline maps onto research design documents and pre-analysis plans. The `/last30days` research tool could be used to survey current discussions around methodological debates or policy topics before starting a project. Voice-driven workflows reduce friction for researchers who think faster than they type. The meeting-to-proposal pipeline (Granola transcript to structured document) is relevant for converting seminar discussions or co-author meetings into actionable research plans. The parallel-session approach suits researchers juggling multiple papers simultaneously.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/ai-workflows]]
- [[concepts/voice-and-transcription]]
- [[concepts/ai-agents]]
- [[concepts/plan-driven-development]]

## Related Summaries

- [[summaries/my-claude-code-setup]]
- [[summaries/claude-code-newbies]]
- [[summaries/chatbot-essentials]]
- [[summaries/ai-for-professionals]]
