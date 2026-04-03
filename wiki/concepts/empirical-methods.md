---
title: "Empirical Methods and AI"
tags: [concept, methodology, research]
sources:
  - "[[summaries/ai-one-shot-papers.md]]"
  - "[[summaries/research-in-time-of-ai.md]]"
date_updated: 2026-04-03
---

# Empirical Methods and AI

The intersection of AI and empirical methods raises important methodological questions about how AI tools affect the rigor and validity of empirical research in economics.

## Context & Background

AI makes it dramatically easier to run many specifications, test numerous hypotheses, and explore data in ways that raise concerns about:

- **P-hacking acceleration**: AI can quickly generate hundreds of regression specifications, making it tempting to search for significant results
- **Specification searching**: Automated exploration of control variables, sample restrictions, and functional forms
- **HARKing**: Hypothesizing After Results are Known becomes easier when AI can rapidly generate post-hoc explanations
- **Data mining**: AI-assisted pattern finding without theoretical grounding

At the same time, AI can improve empirical methods through better data cleaning, more comprehensive robustness checks, and automated replication verification.

## Practical Implications

- **Pre-register analyses**: Commit to specifications before running them, especially when using AI
- **Document all specifications**: Record every analysis the AI ran, not just the ones you report
- **Use AI for robustness**: After finding your main result, use AI to thoroughly stress-test it
- **Maintain theoretical discipline**: Let theory guide hypotheses, not AI-discovered correlations
- **Transparency about AI involvement**: Report how AI was used in the empirical analysis

## Related Concepts

- [[concepts/research-quality|Research Quality]]
- [[concepts/reproducibility-transparency|Reproducibility Transparency]]
- [[concepts/pre-analysis-plans|Pre Analysis Plans]]
- [[concepts/ai-limitations|Ai Limitations]]
