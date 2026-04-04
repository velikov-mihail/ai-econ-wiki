---
title: "AI Research Feedback Skills"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/claesbackmanAI-research-feedback A collection of Claude Code skills for academic research review. These tools were developed by Claes Bäckman.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---
- **Original**: [https://github.com/claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)


- **Author/Source**: Claes Backman, [GitHub: claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)

## Key Ideas

- A collection of five Claude Code skills specifically designed for academic research review: paper review, light paper check, paper-code reproducibility review, pre-analysis plan review, and grant proposal review
- The full `/review-paper` skill runs six specialized agents in parallel covering style, internal consistency, unsupported claims, mathematics, tables/figures, and an adversarial journal-specific referee persona
- Supports targeting specific journals (AER, QJE, JPE, Econometrica, REStud, JF, JFE, RFS, JFQA, and macro journals) to simulate that journal's editorial standards
- `/review-paper-code` checks reproducibility and paper-code alignment across Stata, R, and Python, verifying that empirical claims in the paper match the analysis code
- `/review-pap` reviews pre-analysis plans against registry standards (AEA, EGAP, OSF) or journal standards, evaluating specification completeness, identification strategy, and statistical analysis
- `/review-grant` runs a six-agent panel review for grant proposals targeted at specific funders (NSF, NIH, ERC, Horizon Europe)
- All skills auto-detect main files (`.tex`, proposal documents) and produce dated, versioned output reports

## Summary

This repository provides a set of Claude Code skills purpose-built for the academic research review workflow. The flagship skill, `/review-paper`, simulates a pre-submission referee report by running six specialized review agents in parallel. Each agent focuses on a distinct dimension: spelling and academic style, internal consistency and cross-references, unsupported claims and identification integrity, mathematics and notation, tables and figures, and a contribution evaluation from an adversarial referee persona calibrated to a specific journal. Users can target journals from top-5 economics (AER, QJE, JPE, Econometrica, REStud), finance (JF, JFE, RFS, JFQA), or macro (AEJMacro, JME, RED), and the skill adjusts its standards accordingly.

The collection also includes a lighter-weight `/review-paper-light` that runs just two agents for quick iteration on contribution and identification issues, and `/review-paper-code` which maps a paper's empirical claims to analysis code and checks for reproducibility issues across Stata, R, and Python codebases. Two additional skills address earlier stages of the research lifecycle: `/review-pap` evaluates pre-analysis plans against trial registry standards (AEA, EGAP, OSF, ClinicalTrials) or journal standards, checking specification completeness, identification strategy, and statistical analysis plans; and `/review-grant` runs a six-agent panel review of grant proposals targeted at specific funders.

All skills follow consistent design patterns: automatic file discovery, configurable depth and targeting, dated and versioned output files, and the ability to add project-specific context via local `CLAUDE.md` files. The tools require Claude Code with subagent access and work primarily with LaTeX source files, though some accept PDF and DOCX inputs.

## Relevance to Economics Research

This is among the most directly useful tools for economics researchers in this wiki. The skills address exactly the workflow gaps that academics face: getting structured feedback before submission, checking paper-code alignment for reproducibility, reviewing pre-analysis plans before registration, and pressure-testing grant proposals. The journal-specific calibration for top economics and finance journals (including JF, JFE, RFS, and JFQA) means the feedback is tailored to the standards researchers actually face. The `/review-paper-code` skill is particularly valuable given the growing emphasis on replication in economics -- it systematically checks whether the code produces what the paper claims. For researchers working with coauthors, these skills provide a fast way to get structured feedback between rounds of revision without waiting for colleagues' availability.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/skills-vs-agents]]
- [[concepts/ai-research-tools]]
- [[concepts/reproducibility-transparency]]
- [[concepts/ai-writing]]

## Related Summaries

- [[summaries/daaf-framework]]
- [[summaries/building-skills]]
- [[summaries/skill-library]]
- [[summaries/build-your-own]]
