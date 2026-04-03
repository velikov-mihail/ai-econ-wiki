---
title: "Building an AI Executive Assistant"
tags: [summary, professional-productivity, executive-assistant, email-triage, workflow-automation]
sources:
  - "[[raw/articles/Building an AI Executive Assistant - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---
- **Original**: [https://claudeblattman.com/toolkit/executive-assistant/](https://claudeblattman.com/toolkit/executive-assistant/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/toolkit/executive-assistant/)

## Key Ideas

- An AI executive assistant (EA) can be assembled from modular Claude Code skills that compound over time: inbox triage, morning briefings, meeting prep/follow-up, schedule management, session capture, to-do management, and goals tracking.
- The author went from 5,000 unread emails to six in about 36 hours, by first setting up a reminder system (Apple Reminders), then using Claude Code to categorize and process the backlog.
- Written policy files (what Claude can and cannot do) are essential; a "graduated autonomy" pattern starts with read-only access and progressively grants write permissions.
- The recommended adoption path is incremental: start with `/triage-inbox`, add `/checkin` after a week, then layer on meeting processing and goals tracking.
- Each skill required roughly three weeks of iteration before working well; calibration against real data (not upfront rule-writing) is what makes them accurate.
- Direct time savings are estimated at 1-2 hours/week for inbox triage alone, but the psychological benefit (reduced stress, inbox zero) may be more valuable.
- The system draws on several open-source reference implementations including Claude Chief of Staff, Dex, LangChain EAIA, and Claude Code Personal Assistant.

## Summary

This article presents a comprehensive guide to building an AI executive assistant using Claude Code skills and MCP (Model Context Protocol) integrations. The system manages email, calendar, meetings, to-dos, and goals through a set of modular slash commands that can be installed individually but compound when combined. The author details the full stack: inbox triage that categorizes and auto-archives low-value email, a daily check-in that wraps triage with calendar review and meeting prep, post-meeting follow-up that extracts decisions and action items from transcripts, and goals tracking that aligns daily work with quarterly objectives.

A central design principle is the policy file -- explicit written rules defining what the AI may and may not do (e.g., never send email without approval, never mark as read without instruction). The "graduated autonomy" pattern (propose, then approve, then automate) emerges as a consensus best practice across serious EA implementations. The article also covers a one-time digital cleanup (email backlog, disk audit, cloud storage inventory, calendar consolidation) that took about 36 hours and created the clean foundation the recurring workflows depend on.

The author emphasizes that no skill works perfectly on day one. The value comes from iterative refinement: running the skill, noticing errors, correcting them, and repeating. After a month of daily use, the system performs meaningfully better than at launch. The article includes detailed install instructions, a week-by-week progression plan, and a "daily ritual stack" showing how the skills fit into an actual workday.

## Relevance to Economics Research

For economics researchers managing multiple projects, collaborators, and administrative demands, this system addresses a real pain point: the overhead of email triage, meeting follow-up, and project tracking. The inbox triage and meeting processing skills are directly applicable to academics who juggle teaching, research meetings, referee reports, and grant administration. The graduated autonomy pattern and policy files are especially relevant for researchers handling sensitive communications (recommendation letters, tenure cases, IRB correspondence) where AI errors carry high costs.

## Related Concepts

- [[concepts/claude-code-skills]]
- [[concepts/prompt-engineering]]
- [[concepts/ai-workflows]]
- [[concepts/mcp-protocol]]

## Related Summaries

- [[summaries/meeting-transcription]]
- [[summaries/project-management]]
- [[summaries/cost-reality]]
- [[summaries/voice-dictation]]
- [[summaries/example-noise-canceling]]
