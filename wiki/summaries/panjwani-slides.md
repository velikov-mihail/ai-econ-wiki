---
title: "AI Agents for Economics Research"
tags: [summary, academic-paper, ai-agents, agentic-coding, claude-code, codex]
sources:
  - "[[raw/papers/Ankit_Panjwani_AI_Agents_for_Economic_Research.pdf]]"
date_updated: 2026-04-03
date_published: 2026-03-12
---
- **Original**: [https://voxdev.org/event/ai-agents-economics-research](https://voxdev.org/event/ai-agents-economics-research)

**Authors**: Aniket Panjwani (PhD Economics, Northwestern; Director of AI/ML at Payslice)

## Key Ideas

- AI agents (Claude Code, Codex) represent a fundamentally different paradigm from chatbots or autocomplete -- they combine reasoning (chain-of-thought) with action (executing code, reading files) via the ReAct framework (Think-Act-Observe loop)
- A March 2026 poll of economists showed 51.4% use Claude Code, 18.1% use Codex, and 13.3% use other tools; Panjwani recommends Codex (GPT 5.4 model) as of the talk date
- Three common beginner mistakes: (1) not using Git, (2) underutilizing skills (reusable instruction playbooks), and (3) not making plans before executing -- all degrade agent performance
- Skills are reusable markdown files that bundle prompts, workflows, and conventions (e.g., Pedro Sant'Anna's review-paper and data-analysis skills, Chris Blattman's proposal-write skill)
- The economics job market is deteriorating (JOE postings down 31% year-over-year in 2025-26), making AI coding skills increasingly important for employability
- Supervisory attention with agents may preserve human capital better than copy-paste "vibe coding" because you must understand enough to direct and verify
- Budget matters: $200/mo for frontier models is transformative; $20/mo is limiting; free tiers are counterproductive for serious research

## Summary

Presented at a CEPR/VoxDev webinar in March 2026, these slides make the case that AI agents are a transformative development for economics research and provide practical guidance for adoption. Panjwani opens by establishing urgency through social proof: prominent economists (Paul Novosad at Dartmouth, Gauti Eggertsson at Brown, Chris Blattman at Chicago Harris, Terence Tao at UCLA) have publicly described AI as a "game changer" for their work. Blattman, a self-described non-coder, went from skeptic to building and sharing AI tools within four weeks.

The core technical contribution is distinguishing three paradigms for AI-assisted coding: vibe coding (browser chatbot, no project context, highest risk of disengagement), autocomplete (IDE-based, limited context, user drives), and agentic coding (terminal/CLI, full project exploration, user supervises). Agents combine chain-of-thought reasoning with action-based execution, grounded by an "Observe" step that reads real file contents and error messages rather than hallucinated versions. This is the ReAct framework (Yao et al. 2022).

Panjwani then covers practical advice: use Git (it gives agents memory and safe rollback), invest in skills (reusable instruction files that teach agents your preferred workflows), and plan before executing (write the plan to a file, then start a fresh session for implementation to protect the context window). He emphasizes that the rapidly evolving tool landscape means skills and CLAUDE.md/AGENTS.md files are portable across tools, providing insurance against vendor lock-in.

## Relevance to Economics Research

This presentation is one of the most practical, up-to-date guides for economists adopting agentic AI tools. It bridges the gap between the conceptual framework laid out by Korinek (2023) and actual day-to-day implementation, covering tool selection, workflow design, common pitfalls, and community resources. The emphasis on the job market and employability makes it particularly relevant for PhD students and junior faculty. Panjwani's training cohorts (MIT, NYU, Penn, and others) suggest rapid diffusion of these practices across top economics departments.

## Related Concepts

- [[concepts/ai-agents]]
- [[concepts/agentic-ai]]
- [[concepts/claude-code]]
- [[concepts/skills-vs-agents]]
- [[concepts/ai-adoption-academia]]

## Related Summaries

- [[summaries/korinek-2023]]
- [[summaries/spina-paper]]
- [[summaries/baylor-ai-taskforce]]
- [[summaries/blattman-x-post]]
