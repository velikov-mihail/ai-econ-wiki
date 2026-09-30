---
title: "Prompt Library (Wharton Generative AI Labs)"
tags: [summary, prompt-engineering-workflow, prompting, teaching, resources]
sources:
  - "[[raw/articles/Prompt Library.md]]"
date_updated: 2026-09-30
date_published: 2025-03-19
---

- **Author/Source**: Wharton Generative AI Labs, University of Pennsylvania. The prompts are by Ethan Mollick and Lilach Mollick.
- **Original**: [https://gail.wharton.upenn.edu/prompt-library/](https://gail.wharton.upenn.edu/prompt-library/)

- **Key Ideas**
  - **A public library of reusable, "evidence-based" prompt templates organized by purpose.** Each prompt comes with instructions, suggested use cases, and model options. The library is hosted as an embedded Notion database, so the clipped page shows the framing but not the individual prompts.
  - **Openly licensed**: the prompts, and only the prompts, are released under **CC BY 4.0**, which allows reuse, remixing, and commercial use with credit to Ethan and Lilach Mollick. The page adds: "Use prompts at your own risk, outputs may not be correct."
  - **Example: "Quiz Creator"**, which gathers the subject, student level, and learning objectives, then produces a balanced diagnostic quiz with varied question types, an answer key, and reasoning for each question. It is typical of the library's structured, interview-first prompt design.
  - **Three-stage workflow: Discover → Analyze & Test → Create & Refine.** Start with a goal and "a prepared mind." Browse the library, test prompts, then adapt them to your context.
  - **Testing checklist for prompts you'll reuse or share**: run it multiple times for consistency; consider other users; check that it stays on track in long interactions; verify the output matches expectations; **try several models**; test edge cases; confirm it serves your goal. A prompt that works in one model may not work in another, or in the same model later.
  - **Refinement checklist**: clear goals; context (information, personas, perspectives, documents); step-by-step instructions; examples of good outputs; iterate on real interactions.

- **Summary**

The Wharton Generative AI Labs Prompt Library is a curated, CC BY 4.0 collection of structured prompt templates from Ethan and Lilach Mollick, mostly aimed at teaching and learning. Examples include diagnostic quiz generation and other tutor-, coach-, and exercise-style prompts. The landing page frames prompts as reusable artifacts that need testing like software: behavior varies across models and over time, so a shared prompt should be run repeatedly, across models, with edge cases, and in long conversations before it is trusted.

The advice on building prompts is standard: goals, context, step-by-step instructions, and examples. The page's distinctive contribution is to treat a prompt as a *shareable, versioned instrument* rather than a one-off query, the same idea that later became Claude Code skills and custom GPTs.

- **Relevance to Economics Research**

The library is most useful for **teaching**. Economics instructors can adapt the ready-made, openly licensed prompts for quizzes, tutoring, and practice exercises without writing them from scratch. For research, the testing checklist carries over to any prompt used as a *measurement instrument* (e.g., LLM classification or annotation of text): multiple runs, multiple models, edge cases, and drift over time are exactly the reliability concerns raised in text-as-data work (see [[summaries/kazinnik-cemfi-day2|Kazinnik Day 2]]). It is an early (March 2025) snapshot of the chatbot-era "prompt as reusable artifact" idea, before [[concepts/claude-code-skills|skills]] turned prompts into installable, auto-loaded procedures.

- **Related Concepts**
  - [[concepts/prompt-engineering]]
  - [[concepts/ai-in-education]]
  - [[concepts/ai-skills]]
  - [[concepts/text-as-data]]

- **Related Summaries**
  - [[summaries/prompt-engineering]] — Blattman's prompting guide
  - [[summaries/prompting-insights-golub]]
  - [[summaries/guide-which-ai]] — Ethan Mollick on choosing tools in the agentic era
  - [[summaries/shape-of-ai]]
  - [[summaries/chatbot-essentials]]
  - [[summaries/skills-markus-162-6]] — skills as long prompts in markdown
