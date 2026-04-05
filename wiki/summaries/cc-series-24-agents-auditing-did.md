---
title: "Claude Code 24: Multiple Agents Auditing Your Diff-in-Diff Code (Part 1)"
tags: [summary, academic-research, code-audit, diff-in-diff, cross-language-replication, verification, hallucination]
sources:
  - "[[raw/articles/Claude Code 24 Multiple Agents Auditing Your Diff-in-Diff Code (Part 1).md]]"
date_updated: 2026-04-05
date_published: 2026-02-25
---

- **Author/Source**: Scott Cunningham (Baylor University), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-24-multiple-agents-auditing](https://causalinf.substack.com/p/claude-code-24-multiple-agents-auditing)

- **Key Ideas**
  - LLM hallucination in code generation can be modeled as classical measurement error — random syntax mistakes that cascade through pipelines
  - If hallucination errors are independent across programming languages, replicating analysis in multiple languages makes joint failure probability vanishingly small (product of individual error rates)
  - The proposed workflow: replicate entire research pipelines in Stata, R, and Python, then have an agent verify outputs match across all three
  - Five diff-in-diff packages tested: `csdid` (Stata), `csdid2` (Stata), `did` (R), `diff-diff` (Python), `differences` (Python)
  - Cross-language replication works for deterministic code (OLS, merges, cleaning) but not for stochastic methods (bootstraps, MCMC, random forests)
  - Classic Stata pitfall illustrated: `replace x = 10 if x > 10` also replaces missing values — a syntax-specific error that would not appear in R or Python
  - Code audits and cross-language replication are two separate verification tasks that complement each other

- **Summary**

Cunningham proposes a formal framework for using Claude Code to verify research code by treating LLM hallucination as classical measurement error. If code errors are random and language-specific (syntax mistakes in Stata are independent of syntax mistakes in R or Python), then replicating an entire analysis pipeline in multiple languages provides a powerful check: the probability that all three languages produce the same wrong result is the product of their individual error rates — a very small number.

He demonstrates this with a case study using five difference-in-differences packages across three languages, applied to a Brazilian study on mental health deinstitutionalization and homicides. The essay distinguishes between two complementary verification tasks: (1) having antagonistic subagents audit code logic and reasoning, and (2) having Claude Code replicate the entire pipeline — from data cleaning through estimation — in two additional languages, then comparing outputs digit-by-digit. He is careful to note the limitation: this approach works only for deterministic computations (OLS, fixed effects, merges, summary statistics) and breaks down for stochastic methods like bootstrapping or MCMC where random seeds differ across languages.

- **Relevance to Economics Research**

This directly addresses the reproducibility crisis and code verification in empirical economics. The insight that cross-language replication exploits independence of syntax-specific errors is both formally justified and practically implementable with AI agents. The diff-in-diff application is immediately relevant to the large community of applied researchers using Callaway and Sant'Anna estimators, and the framework generalizes to any deterministic empirical method.

- **Related Concepts**
  - [[concepts/cross-language-replication]]
  - [[concepts/reproducibility-transparency]]
  - [[concepts/human-in-the-loop]]
  - [[concepts/empirical-methods]]
  - [[concepts/coding-with-llms]]

- **Related Summaries**
  - [[summaries/cc-series-21-attention-congestion]]
  - [[summaries/cc-series-25-autonomous-agents]]
  - [[summaries/cc-series-17-zero-profit]]
