---
title: "Project Management with AI"
tags: [summary, professional-productivity, project-management, research-workflow]
sources:
  - "[[raw/articles/Project Management - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/workflows/project-management/)

## Key Ideas

- A four-layer system transforms scattered information across five platforms into living project dashboards: (1) organize the project folder, (2) capture everything via meeting transcription, (3) run weekly reviews that synthesize across all sources, (4) generate proposals and reports on demand.
- The foundation is a structured project folder with a Google Doc hub containing a "Research Design and Progress" living document -- part research design, part project history, part pre-analysis plan.
- The weekly review skill (`/weekly-review`) pulls from meeting transcripts, emails, Google Docs, and optionally WhatsApp, then produces a strategic dashboard and detailed weekly log.
- Proposal writing skills (`/proposal-write`, `/proposal-revise`) leverage the accumulated project context to draft funding proposals, with agent-based QA reviewers providing independent critique.
- Each layer took about three weeks of iteration; none worked perfectly on day one.
- The system was developed for quantitative research projects (RCTs, survey-based studies) but adapted to qualitative projects with modest adjustments.

## Summary

This article describes how the author went from managing research projects across scattered emails, documents, and messaging platforms to a structured AI-powered project management system. The system is built in four layers, each building on the previous one. Layer 1 uses a `/setup-project-management` skill to walk through an interactive discovery process, pull materials into a single project folder, and create a Google Doc hub with a living research design document. Layer 2 adds meeting transcription via Granola, ensuring that decisions and action items are no longer lost after meetings.

Layer 3 is where the system "comes alive": a weekly review skill collects data from all sources and synthesizes it into a project dashboard organized around strategic priorities, operational objectives, team to-dos, and critical success factors. The dashboard answers key questions: what are the strategic goals, how do this week's tasks serve them, and what absolutely must happen? Layer 4 builds on this accumulated context to generate funding proposals, donor reports, and status updates on demand, with built-in voice consistency and agent-based quality assurance.

The author emphasizes that each layer works independently -- you can start with just folder organization and get value. The key insight is that the weekly review's value comes from organizing around strategic priorities rather than chronological events, and that every skill required iterative refinement with Claude Code to adapt to specific projects and team needs.

## Relevance to Economics Research

This system directly addresses the project management challenges faced by empirical economists running field experiments, surveys, or multi-collaborator research projects. The weekly review and living research design document serve as institutional memory for projects where decisions accumulate over months or years. The proposal writing layer is particularly relevant for researchers who write multiple grant applications and need to maintain consistency across versions while tailoring framing to different funders.

## Related Concepts

- [[wiki/concepts/ai-workflow-design]]
- [[wiki/concepts/claude-code-skills]]
- [[wiki/concepts/ai-research-workflows]]

## Related Summaries

- [[wiki/summaries/ai-executive-assistant]]
- [[wiki/summaries/meeting-transcription]]
- [[wiki/summaries/project-manager-claude]]
- [[wiki/summaries/example-project-dashboard]]
- [[wiki/summaries/example-research-design]]
