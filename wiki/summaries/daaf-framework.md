---
title: "DAAF: Data Analyst Augmentation Framework"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/DAAF-Contribution-Communitydaaf DAAF, the Data Analyst Augmentation Framework An open-source, extensible workflow for Claude Code that allows skilled researchers to rapidly scale their expertise and accelerate data analysis by as much as 5-10x -.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Brian Heseung Kim, [GitHub: DAAF-Contribution-Community/daaf](https://github.com/DAAF-Contribution-Community/daaf)

## Key Ideas

- DAAF is a free, open-source instructions framework for Claude Code that claims to accelerate data analysis 5-10x while maintaining transparency, rigor, and reproducibility
- Five core design principles: transparent (file-first, all reasoning stored as comments and plan documents), scalable (extensible skills inject domain-specific best practices), rigorous (hyper-atomic code steps with adversarial review), reproducible (every file, script, and output automatically stored), responsible (proper citation, AI disclosure via GUIDE-LLM standard, human researcher as final authority)
- Eight engagement modes ranging from data onboarding and lookup to full research pipelines, reproducibility verification, and framework self-improvement
- Runs in Docker for safety sandboxing with destructive command prevention and secret/credential scanning
- Ships with 40+ education datasets from the Urban Institute Education Data Portal and built-in support for major social science methods (diff-in-diff, IV, RDD, synthetic control, event studies, propensity score matching, etc.)
- Includes automatic citation propagation tracking data sources, methods, and software throughout the analysis pipeline
- Licensed under LGPL-3.0 -- free for any use, with open-source requirements only applying to distributed modifications of the core framework

## Summary

DAAF (Data Analyst Augmentation Framework) is an open-source workflow system built on top of Claude Code, designed to help researchers conduct rigorous data analysis with AI assistance. The framework positions itself as a "force-multiplying exoskeleton" for human researchers, explicitly acknowledging that LLMs are susceptible to hallucination, sycophancy, and corner-cutting, and building guardrails to mitigate these risks. All data operations are drafted as actual Python files with verbose comments, all reasoning is stored in plan documents, and the human researcher retains authority over all analytical decisions.

The framework provides eight engagement modes that cover the full research lifecycle. Data Onboarding creates documentation skills from new datasets. Data Lookup and Discovery modes answer questions about onboarded data. Ad Hoc Collaboration provides a more knowledgeable research partner for flexible sessions. The Full Pipeline mode handles everything from research question to results -- data scoping, analytic planning, code review, analysis, visualization, and report writing -- producing a pre-analysis plan and fully reproducible end-to-end analysis. Revision and Extension modes iterate on prior work, and Reproducibility Verification re-runs and re-verifies completed pipelines. A Framework Development mode allows DAAF to improve its own functionality.

DAAF comes with extensive built-in capabilities including support for major econometric and statistical methods, expertise in numerous Python libraries (polars, pyfixest, linearmodels, statsmodels, scikit-learn, geopandas, plotly, and more), and additional features like interactive dashboards, reactive notebooks (marimo), R/Stata-to-Python code translation, and Git version control. The Docker-based architecture provides safety sandboxing, and the system includes automatic citation tracking following the GUIDE-LLM reporting standard for AI use disclosure.

## Relevance to Economics Research

DAAF is one of the most directly relevant tools for economics researchers in this wiki. It provides built-in support for the core econometric methods used in applied economics (difference-in-differences, instrumental variables, regression discontinuity, event studies, synthetic control) and integrates with key Python libraries used in empirical finance and economics (pyfixest, linearmodels, statsmodels). The framework's emphasis on reproducibility -- storing every script, output, and decision -- aligns with the growing reproducibility movement in economics. The R/Stata-to-Python translation feature addresses a practical barrier for economists transitioning from these languages. The pre-analysis plan review and full pipeline modes map directly onto the empirical research workflow from question formulation through to results. The Docker sandboxing and file-first execution approach address legitimate concerns about using AI for data analysis in research contexts where errors have consequences for published findings.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/ai-for-research]]
- [[concepts/reproducibility]]
- [[concepts/human-in-the-loop]]
- [[concepts/data-analysis-workflows]]

## Related Summaries

- [[summaries/ai-research-feedback-skills]]
- [[summaries/building-skills]]
- [[summaries/compilation-review]]
- [[summaries/build-your-own]]
