---
title: "Project APE: Can Policy Evaluation Be Automated?"
tags: [summary, automated-research, policy-evaluation, AI-agents]
sources:
  - "[[raw/articles/Project APE Can policy evaluation be automated Or is hallucinated slop unavoidable Let's find out.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---

- **Author/Source**: Social Catalyst Lab (ape.socialcatalystlab.org)
- **Original**: [https://ape.socialcatalystlab.org/methodology](https://ape.socialcatalystlab.org/methodology)

## Key Ideas

- Project APE is a fully automated pipeline that produces economics research papers using real data from public APIs -- it never simulates or fabricates data
- The core engine is Claude Code (Claude Opus 4.6), which drives the entire pipeline: generating ideas, writing R scripts, fetching data, running analysis, drafting LaTeX, and revising based on feedback
- A multi-model ensemble of 11 models from 7 providers handles idea ranking, multi-stage review, code auditing, and tournament evaluation -- no single model evaluates its own work
- Every paper enters a head-to-head tournament against published research from top economics journals, judged by Gemini 3.1 Flash Lite (a non-Anthropic model chosen to avoid self-preference bias)
- Papers undergo a six-stage review process: advisor review, theory review, exhibit review, prose review, referee review, and revision
- Integrity checks include code scanning for fabricated data and replication testing, with penalties (virtual losses) for papers that fail

## Summary

Project APE (Automated Policy Evaluation) is an ambitious experiment in fully automated economics research. The system uses Claude Code as its core engine to autonomously plan, execute, and iterate through the entire research pipeline -- from generating research questions to producing submission-ready LaTeX papers with complete replication materials. All analysis uses real data from public APIs, and the system is designed to pivot to a different research question if data is unavailable rather than fabricate anything.

A key design principle is the use of a multi-model ensemble to avoid single-model blind spots. Eleven external models from seven providers are orchestrated by Claude Code across various roles including idea ranking, review, and code auditing. The tournament evaluation system pits AI-generated papers against published work from top economics journals using TrueSkill ratings and position-swapped judging. The judge (Gemini 3.1 Flash Lite) is deliberately chosen from a different provider than the paper generator.

The review process mirrors academic peer review with six stages, including parallel independent advisor checks, theory verification for structural models, visual feedback on exhibits, prose quality review, and simulated referee reports. Papers that pass all stages enter the tournament. The project maintains full transparency with complete replication materials and git audit trails.

## Relevance to Economics Research

Project APE represents one of the most systematic attempts to automate the full economics research pipeline, from ideation to peer-review-ready output. It directly tests whether AI can produce research that competes with human-authored work published in top journals. The project's emphasis on real data, replication, and multi-model evaluation addresses key concerns about AI-generated research quality and hallucination. Its findings will be informative for understanding how AI might reshape the production of economic knowledge and what guardrails are needed.

## Related Concepts

- [[concepts/automated-research]]
- [[concepts/ai-agents]]
- [[concepts/reproducibility-transparency]]
- [[concepts/llm-reasoning]]

## Related Summaries

- [[summaries/automated-research-finance]]
- [[summaries/applications-generative-ai]]
- [[summaries/thread-arindube]]
