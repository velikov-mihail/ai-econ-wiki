---
title: "AI-Powered (Finance) Scholarship"
tags: [summary, finance-econometrics, automated-research, llm, asset-pricing]
sources:
  - "[[raw/articles/AI-Powered-Scholarship Code used in Novy-Marx and Velikov (2024), AI-Powered (Finance) Scholarship.md]]"
date_updated: 2026-04-05
date_published: 2024-12
---

- **Author/Source**: Robert Novy-Marx (University of Rochester) & Mihail Velikov (Penn State), via GitHub
- **Original**: [https://github.com/velikov-mihail/AI-Powered-Scholarship](https://github.com/velikov-mihail/AI-Powered-Scholarship)
- **Paper**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5060022](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5060022)

- **Key Ideas**
  - Mines 30,000+ potential stock return predictor signals from accounting data and applies the Novy-Marx and Velikov (2024) "Assaying Anomalies" protocol to identify 95 signals that pass rigorous filtering criteria.
  - For each surviving signal, uses state-of-the-art LLMs to generate four complete academic papers, each with a different theoretical framework: slow diffusion of information, production-based pricing, consumption-based pricing, and unrestricted/free-form.
  - The pipeline has three stages: (1) MATLAB data mining and template report generation via the Assaying Anomalies toolkit, (2) Python-based LLM signal naming, and (3) Python-based paper generation with multiple theoretical frameworks.
  - Each template report benchmarks a signal against 200+ published anomalies with comprehensive statistical tests.
  - Repository provides full reproducibility: MATLAB scripts for data processing, Python scripts for LLM orchestration, and all prompts used for paper generation.

- **Summary**

Novy-Marx and Velikov build an end-to-end pipeline that combines systematic empirical asset pricing with large language models. Starting from the universe of accounting ratios and differences in CRSP/Compustat, they construct over 30,000 candidate signals and run each through the Assaying Anomalies protocol — a standardized battery of portfolio sorts, cross-sectional regressions, and robustness checks. The 95 signals that survive all filters receive automated LaTeX template reports.

The LLM stage takes each template and generates creative, economically meaningful signal names, then produces four distinct complete papers per signal. Each paper version frames the same empirical finding through a different theoretical lens — behavioral finance (slow diffusion), production-based, consumption-based, or unconstrained. The code supports both OpenAI and Anthropic APIs, with configurable parameters for model selection, token limits, and hypothesis frameworks.

The project demonstrates that the combination of rigorous empirical protocols and LLM-powered writing can produce hundreds of plausible academic papers at scale, raising important questions about the future of peer review, the role of human judgment in research, and the economics profession's capacity to absorb AI-generated output.

- **Relevance to Economics Research**

This is a direct demonstration of automated research at scale in finance. It shows both the power (systematic exploration of the signal space, standardized quality control) and the provocative implications (hundreds of "publishable-looking" papers from a single pipeline). The project forces the profession to confront questions about what makes research valuable when execution costs approach zero.

- **Related Concepts**
  - [[concepts/automated-research]]
  - [[concepts/research-quality]]
  - [[concepts/ai-limitations]]
  - [[concepts/empirical-methods]]

- **Related Summaries**
  - [[summaries/automated-research-finance]]
  - [[summaries/stress-test-research-pipeline]]
  - [[summaries/ai-one-shot-papers]]
  - [[summaries/openai-automated-researcher]]
