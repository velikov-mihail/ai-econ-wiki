---
title: "AI Project Folders"
tags: [summary, context-management, prompt-engineering, productivity]
sources:
  - "[[raw/articles/AI Project Folders - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---
- **Original**: [https://claudeblattman.com/essentials/project-folders/](https://claudeblattman.com/essentials/project-folders/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/essentials/project-folders/)

## Key Ideas

- A project folder stores stable preferences, hard constraints, and behavioral rules for a recurring domain in a single file. Every new conversation starts from that file instead of from scratch.
- The three-step build process: (1) narrate your situation in a messy dump, (2) ask the AI to interview you with 12 structured questions covering preferences, avoids, constraints, thresholds, and past evidence, (3) ask the AI to synthesize everything into a canonical file under 500 words.
- "Avoids" per person or category are the true constraints; threshold numbers ("flag anything over 85F") beat adjectives ("we don't like heat").
- Project files follow a predictable development arc: messy dump (conversations 1-2), failure-driven refinement (conversations 3-5), and maintenance mode (conversation 6+) where updates are 1-2 lines.
- The pattern works for both personal domains (travel, shopping, health) and professional work (research writing, proposals, course prep).
- ChatGPT Deep Research is highlighted as potentially the single most valuable AI tool for faculty when paired with well-engineered prompts.
- A good test: start a completely new conversation in the project and check whether at least one option is explicitly eliminated or flagged because it violates a file constraint. If all suggestions look generically good, the file is not specific enough.

## Summary

This article describes how to build reusable instruction files for AI chatbot projects in ChatGPT or Claude.ai. The core idea is that for any recurring task domain, there are stable preferences and constraints that should not need to be re-explained every conversation. The article walks through a three-step process: dumping everything you know about the domain, having the AI interview you with structured questions to fill gaps, and synthesizing the results into a concise canonical file.

The article provides three detailed examples at different complexity levels. A family travel folder demonstrates the full system with per-person preferences, avoids, temperature thresholds, logistics constraints, and an evidence bank of past trips tagged with why they worked or failed. A health consultation folder shows how uploaded reference files (health baseline, labs, medications) complement the instruction file for deep research and quick consultations. A shopping folder illustrates a simpler instructions-only approach focused on decision posture (durability over price), recommendation format (curated shortlists of 3-5), and explicit handling of failure modes (junk brands, invented facts, too many options).

A key insight is that the canonical file develops through use, not upfront design. Failures teach the rules: the file improves most when the AI recommends something that violates an unstated constraint, prompting the user to make that constraint explicit. The article also compares ChatGPT and Claude for this pattern, noting that ChatGPT excels at research-heavy planning with web browsing while Claude produces better-organized canonical files and excels at recurring automated processes.

## Relevance to Economics Research

The project folder pattern applies directly to recurring research tasks. An economics researcher could build canonical files for literature review requests (specifying field, methodology preferences, and journal quality filters), referee report drafting (encoding the researcher's standards for identification, robustness, and presentation), or grant proposal writing (capturing funder preferences, budget constraints, and institutional boilerplate). The three-step build process -- dump, interview, synthesize -- is an efficient way to externalize the tacit knowledge that researchers accumulate about how they want research tasks executed. The emphasis on threshold numbers over adjectives parallels the empirical research principle of specifying testable criteria rather than vague quality standards.

## Related Concepts

- [[concepts/context-management]]
- [[concepts/prompt-engineering]]
- [[concepts/ai-workflows]]
- [[concepts/research-productivity]]

## Related Summaries

- [[summaries/prompt-engineering]]
- [[summaries/your-claude-md]]
- [[summaries/workflows]]
- [[summaries/prompt-plan-review-revise]]
