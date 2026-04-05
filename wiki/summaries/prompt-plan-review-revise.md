---
title: Prompt, Plan, Review, Revise
tags:
- summary
- prompt-engineering-workflow
- ai-workflows
- prompt-engineering
- plan-review
sources:
- '[[raw/articles/Prompt, Plan, Review, Revise - Claude Blattman · AI for Professionals
  Who Don''t Code.md]]'
date_updated: 2026-04-03
date_published: 2026-03
---
- **Original**: [https://claudeblattman.com/workflows/first-session-skills/](https://claudeblattman.com/workflows/first-session-skills/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/workflows/first-session-skills/)

## Key Ideas

- The core workflow is a four-step loop: `/prompt` (structure your thinking), Plan mode (think before acting), `/review-plan` (stress-test with a fresh agent), and `/done` (capture session context for continuity).
- Most people treat AI as one-shot interactions; the loop turns it into a repeatable process where each step compensates for the limitations of the previous one.
- `/prompt` takes rough, stream-of-consciousness input and reformats it into a structured prompt with Role, Context, Task, Constraints, Output Format, and Bookend sections -- then executes it.
- Plan mode (Shift+Tab in Claude Code) forces the AI to read, explore, and propose approaches without executing anything, creating a deliberate pause for review.
- `/review-plan` spins up a separate agent in a fresh context that has never seen the conversation, providing genuinely independent critique -- like external peer review rather than self-review.
- `/done` captures decisions, open questions, and follow-ups so the next session starts with context rather than from scratch, building a searchable history across sessions.
- The persona technique assigns multiple expert perspectives (e.g., web designer + skills engineer) to debate and converge on a plan before committing.

## Summary

This article describes a four-step iterative workflow for getting high-quality output from Claude Code. The method was demonstrated by building the claudeblattman.com website in 90 minutes on a plane. The author brain-dumped a rough description, used `/prompt` to structure it, assigned two personas (web designer and Claude Code skills engineer) to debate the plan in Plan mode, then ran `/review-plan` twice with different reviewer personas to catch blind spots.

The intellectual centerpiece is the `/review-plan` step, which addresses a fundamental limitation of AI self-review: an AI critiquing its own plan in the same conversation has seen all the reasoning and cannot identify its own blind spots. By spinning up a fresh agent that reads the plan cold, the workflow mimics external peer review. The article provides concrete examples of what these reviews catch -- missing prerequisites, assumed knowledge, structural errors, and usability problems. Each review round takes about five minutes.

The `/done` step addresses session continuity. It writes structured handoff notes so future sessions begin with context. The `project` variant anchors the handoff to a specific directory and auto-loads when Claude Code opens in that directory. Combined with a CLAUDE.md file that provides persistent personal context, the loop creates a system where AI interactions compound rather than starting fresh each time.

## Relevance to Economics Research

The prompt-plan-review-revise loop maps naturally onto research workflows. Economists can use `/prompt` to structure rough ideas for grant proposals or paper sections, Plan mode to outline an empirical strategy before committing to code, `/review-plan` to stress-test a research design with simulated referee personas, and `/done` to maintain continuity across multi-week projects. The persona technique is especially relevant: assigning "methodologist" and "applied researcher" personas to debate an identification strategy before implementation mirrors the value of co-author feedback in the research process.

## Related Concepts

- [[concepts/prompt-engineering]]
- [[concepts/plan-driven-development]]
- [[concepts/ai-workflows]]
- [[concepts/context-management]]
- [[concepts/ai-agents]]

## Related Summaries

- [[summaries/prompt-engineering]]
- [[summaries/patterns]]
- [[summaries/your-claude-md]]
- [[summaries/workflows]]
