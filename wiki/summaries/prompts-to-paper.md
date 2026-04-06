---
title: "Prompts-to-Paper: Hedging the AI Singularity"
tags: [summary, academic-research, automated-research, llm, ai-collaboration]
sources:
  - "[[raw/articles/Prompts-to-Paper Code used in Chen (2025), Hedging the AI Singularity.md]]"
date_updated: 2026-04-05
date_published: 2025-04
---

- **Author/Source**: Andrew Y. Chen (Federal Reserve Board), via GitHub
- **Original**: [https://github.com/chenandrewy/Prompts-to-Paper](https://github.com/chenandrewy/Prompts-to-Paper)

- **Key Ideas**
  - A single researcher uses AI as "junior co-authors" to write a complete economics paper on hedging negative AI singularity risk, with o1 handling theory, Sonnet handling writing, and ChatGPT Deep Research handling literature reviews.
  - The project prioritizes quality over quantity (contrast with Novy-Marx and Velikov's mass-generation approach): generates N drafts and picks the best one, rather than trying to prompt-engineer a perfect paper.
  - Zero hallucinated citations achieved by building literature reviews from ChatGPT Deep Research and Claude Web Search, though mis-citations (misinterpretation of cited papers) still occur roughly once per 15–20 citations.
  - Iterative model development with AI: early formalizations were "terrible" — o1 patiently explained why a neoclassical growth model with sudden capital share increase was a bad model, eventually converging on a simplified Barro-Rietz disaster model.
  - Writing the paper "would have been much easier if I had done more of the work myself" — honest assessment that AI collaboration has its own overhead, similar to human coauthor coordination costs.
  - On the future of peer review: author reputation still disciplines quality; fears of AI slop inundating journals may be overblown because researchers won't put their names on low-quality output.

- **Summary**

Chen documents his process of writing an economics paper about hedging AI catastrophe risk, using AI models as collaborators. Inspired by Novy-Marx and Velikov (2025) and Chris Lu et al. (2024), Chen's goal differs: instead of generating many papers, he aims to produce one paper worth reading. The workflow uses o1 for mathematical derivations, Claude Sonnet for writing, and ChatGPT Deep Research / Claude Web Search for literature reviews, with the prompts and iteration history fully documented in the repository.

The paper itself uses a simplified Barro-Rietz disaster model with two agents to argue that if AI causes large disruptions to human capital, tech stocks provide a partial hedge. The model went through several failed iterations before converging — an honest account of how AI-assisted theory development works in practice. Chen generates 5 draft versions and selects the best, acknowledging that writing quality varies across runs.

The README provides candid reflections on AI's current limitations: sub-par economic reasoning (failing to recognize when a model misses an important channel), inability to generate satisfying models independently, and insufficiently careful literature discussions. Chen speculates about "economics on tap" — a future where 2024-style analysis is available on demand from a chatbot — and its implications for the economics labor market.

- **Relevance to Economics Research**

A transparent, first-person account of using AI to write a complete theory paper in finance/macro. Valuable as a case study in AI-human collaboration for theoretical work, complementing the more empirical demonstrations from other sources. The honest assessment of limitations — and the observation that writing with AI was *harder* than doing it alone — provides important counterbalance to more optimistic accounts.

- **Related Concepts**
  - [[concepts/automated-research]]
  - [[concepts/human-ai-collaboration]]
  - [[concepts/ai-limitations]]
  - [[concepts/research-quality]]
  - [[concepts/ai-writing]]

- **Related Summaries**
  - [[summaries/ai-powered-scholarship]]
  - [[summaries/ai-one-shot-papers]]
  - [[summaries/openai-automated-researcher]]
  - [[summaries/vibe-research]]
  - [[summaries/feedback-machines]]
