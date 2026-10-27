---
title: "Practical AI for Academics & Teaching (Bäckman Workshops)"
tags: [summary, academic-research, teaching, claude-code, skills, verification, workshop]
sources:
  - "[[raw/Clippings/Practical AI for Academics.md]]"
date_updated: 2026-10-27
date_published: 2026
---

- **Author/Source**: Claes Bäckman (Aarhus University), [claesbackman.com](https://claesbackman.com/ai_workshop/)
- **Original**: [https://claesbackman.com/ai_workshop/](https://claesbackman.com/ai_workshop/) · slides: [Research S1](https://claesbackman.com/ai_workshop/AI_Workshop_Session1.pdf), [Research S2](https://claesbackman.com/ai_workshop/AI_Workshop_Session2.pdf), [Teaching S1](https://claesbackman.com/ai_workshop/teaching_session1.pdf), [Teaching S2](https://claesbackman.com/ai_workshop/teaching_session2.pdf)

- **Key Ideas**
  - **Two workshops, each with a conceptual session and a hands-on session.** *Practical AI for Academics* covers agentic AI in empirical research. *Practical AI for Teaching* is a one-day workshop for university teachers.
  - **Research Session 1 (foundations)**: what an LLM is and why it sounds confident when it is wrong; chat versus agentic tools; Claude Code versus Codex; pricing and model tiers; how the agent loop works; context windows; and **four checks for errors that do not crash**.
  - **Research Session 2 (workflows)**, built on Bäckman's own skills:
    - a referee report on your own draft with `/review-paper`, then a **subagent that critiques the report**
    - slides and explorable explanations from a paper with `/explorable-deck` (see [[summaries/beamer-parrot]])
    - a **`voice.md`** built from your own writing so AI edits sound like you
    - checking that the code does what the paper says with `/review-paper-code`, and why **git diffs help agents**
    - a quiz bank from your lecture notes
    - working with an agent when the data sits on a **secure server it cannot reach**
  - **Teaching design**: in the morning an agent writes a thesis live during the lecture. In the afternoon participants assess that thesis with a rubric, get a second opinion on their feedback, draft defence questions, build a skill from their own rubric, write a course AI policy, and update a course.
  - **Teaching topics**: Copilot Chat versus Claude Code, AI detectors and their limits, why **take-home grades stopped measuring learning**, replication packages and verification, hallucination, copyright, and plagiarism.
  - Exercise files are public: the agent-written thesis ([paper.pdf](https://claesbackman.com/ai_workshop/teaching_materials/paper.pdf)) and an example [rubric.md](https://claesbackman.com/ai_workshop/teaching_materials/rubric.md).

- **Summary**

This page is the hub for two workshop series by Claes Bäckman. The research series runs over two sessions. The first is conceptual: it explains how LLMs and agents work, compares the main agentic tools (Claude Code, Codex) and their costs, and gives a short protocol for catching silent errors, the "errors that do not crash." The second is practical and walks through the workflows Bäckman has written about elsewhere: AI referee reports on your own draft with a critic subagent ([[summaries/ai-research-feedback-skills]], [[summaries/feedback-machines]]), explorable slide decks ([[summaries/beamer-parrot]]), a personal voice file, code-versus-paper consistency checks using git diffs ([[summaries/verifying-llm-output]]), and a pattern for restricted data that the agent cannot see directly.

The teaching workshop builds the day around one artifact: a thesis that an agent writes during the morning lecture. That makes the problem concrete. Participants see what students can now produce, then spend the afternoon on it: grading it against a rubric, getting a second AI opinion on their own grading, drafting oral-defence questions, and turning their rubric into a reusable skill. The morning also covers why take-home assessment no longer measures learning and why AI detectors cannot fix that.

- **Relevance to Economics Research**

This is a ready-made curriculum for introducing economists to agentic AI, from an applied economist who uses the tools in his own research. The research session covers what most faculty need: self-review before submission, presentation materials, verification that code matches the paper, and confidential-data constraints that are common in administrative and register-data work. The teaching session takes on assessment directly, which is the hardest part of AI in economics teaching, and gives faculty concrete outputs (a rubric skill, a course AI policy, defence questions) instead of general advice.

- **Related Concepts**
  - [[concepts/ai-in-education]]
  - [[concepts/ai-peer-review]]
  - [[concepts/claude-code-skills]]
  - [[concepts/verifying-ai-output]]
  - [[concepts/ai-writing]]
  - [[concepts/data-privacy]]
  - [[concepts/version-control-research]]

- **Related Summaries**
  - [[summaries/ai-research-feedback-skills]]
  - [[summaries/beamer-parrot]]
  - [[summaries/feedback-machines]]
  - [[summaries/verifying-llm-output]]
  - [[summaries/backman-vscode-guide]]
  - [[summaries/teaching-ai-your-voice]]
  - [[summaries/velikov-edhec]]
  - [[summaries/agentic-everything]]
