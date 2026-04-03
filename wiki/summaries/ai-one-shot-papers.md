---
title: "AI One-Shot Papers"
tags: [summary, academic-research, empirical-methods, diff-in-diff, ai-limitations]
sources:
  - "[[raw/articles/AI one-shot papers.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Paul Goldsmith-Pinkham (Substack, 2026-03-21)

## Key Ideas

- Automated AI systems for empirical policy evaluation lean heavily on difference-in-differences (DiD), far more than the existing literature does.
- Of 592 papers on David Yanagizawa-Drott's APE (AI Policy Evaluation) platform, 64.2% are self-reported DiD/event study and 20% are RDD.
- By comparison, only ~35% of NBER working papers in empirical micro mention DiD, with 44% using other quasi-experimental methods.
- DiD is the easiest "plug-and-chug" empirical estimator, but it requires substantial researcher taste, discretion, and care to execute properly.
- The central concern is whether an automated AI system can exercise the careful judgment that credible DiD analysis demands.
- AI one-shotting of papers will tend to gravitate toward methods that appear mechanical but are actually judgment-intensive.

## Summary

Paul Goldsmith-Pinkham examines the methodological composition of AI-generated empirical papers, using data from the APE platform created by David Yanagizawa-Drott for automated policy evaluation. He finds that AI systems overwhelmingly default to difference-in-differences designs -- nearly 74% of APE papers mention DiD methods at least three times, compared to about 35% for NBER working papers. This pattern reflects the fact that DiD is the most formulaic causal inference method, making it the natural choice for automated systems, even though doing DiD well requires significant human judgment about parallel trends, treatment timing, and identification assumptions.

The post is concise but makes a sharp point: the methods that AI finds easiest to automate are precisely the ones where researcher discretion matters most. This creates a tension at the heart of AI-generated empirical research -- the apparent ease of automation masks the difficulty of doing credible causal inference.

## Relevance to Economics Research

This is directly relevant to applied microeconomics and empirical finance, where DiD and event studies are workhorse methods. The finding that AI defaults to DiD at much higher rates than human researchers raises important questions about the credibility of AI-generated empirical work and whether automated systems can substitute for the institutional knowledge and identification judgment that distinguish good applied work.

## Related Concepts

- [[concepts/vibe-research]]
- [[concepts/ai-limitations]]
- [[concepts/empirical-methods]]
- [[concepts/p-hacking]]

## Related Summaries

- [[summaries/research-in-time-of-ai]]
- [[summaries/can-ai-replace-researchers]]
- [[summaries/vibe-research]]
- [[summaries/reflections-vibe-research]]
