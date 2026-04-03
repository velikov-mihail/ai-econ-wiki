---
title: "Compilation, Categorization, and Multi-Year Review"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/Compilation & Review - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/tax-workflow/case-study/compilation-and-review/)

## Key Ideas

- The article describes a "multi-source compilation with validation" pattern: gathering data from different formats, structuring it consistently, and cross-checking against historical data
- Three distinct sub-patterns for data compilation: guided interview (Schedule C expenses requiring human judgment), spreadsheet export (charitable contributions from an existing Google Sheet), and threshold gate (medical expenses that check whether compilation is worthwhile before proceeding)
- The guided interview pattern deliberately avoids automation for expense categorization because it requires judgment AI cannot reliably make (e.g., consulting vs. employer-reimbursed travel)
- A three-year review comparison serves as a safety net, flagging year-over-year anomalies like a 180% jump in travel expenses or a 22% drop in itemized deductions
- All outputs follow a consistent spreadsheet design: summary tab, detail tab, and an entry guide tab mapping compiled figures to specific tax software fields
- The three-tier classification system (auto-qualify, auto-exclude, uncertain) for credit card transactions reduced false positives from 10% to 5% by routing ambiguous items to human review

## Summary

This article presents a case study of AI-assisted tax preparation workflows, focusing on the compilation and review phase where collected documents become organized spreadsheets. It demonstrates three distinct architectural patterns for data compilation. The guided interview pattern (used for Schedule C business expenses) deliberately keeps the human in the loop for categorization decisions that require judgment, while providing structure, historical context, and arithmetic. The spreadsheet export pattern (used for charitable contributions) automates extraction from an existing Google Sheet, requiring no judgment since the source of truth is already maintained. The threshold gate pattern (used for medical expenses) calculates whether the deduction will exceed the relevant threshold before investing time in full compilation.

The article pays special attention to a three-year review mechanism that compares the current tax return against two prior years to flag anomalies. This caught real errors in the case study: employer-reimbursed trips mistakenly listed as consulting expenses (revealed by a 180% year-over-year jump), and a missing charitable donation entered with the wrong year (revealed by a 22% drop in itemized deductions). The article argues that most tax errors are systematic rather than random, making historical comparison an effective detection method.

A particularly instructive detail is the evolution of the credit card transaction classifier from two tiers to three. Adding an "uncertain" middle tier for ambiguous transactions significantly reduced false positives by routing genuinely ambiguous cases to human review rather than forcing AI classification. The article concludes by mapping the compilation pattern to other domains: grant reporting, expense reports, annual reviews, and project audits.

## Relevance to Economics Research

The multi-source compilation pattern transfers directly to empirical economics workflows. Researchers routinely merge data from CRSP, Compustat, and other sources with different formats and conventions, requiring both automated matching and human judgment for ambiguous cases. The three-year review mechanism maps onto data validation in panel datasets, where year-over-year anomalies in variables like firm revenue or employment can reveal coding errors. The threshold gate pattern is relevant for deciding whether to pursue computationally expensive analyses (e.g., bootstrap inference) based on preliminary results. The three-tier classification system (auto-qualify, uncertain, human-review) offers a practical framework for handling ambiguous variable coding or firm-industry matching in large datasets.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/ai-workflows]]
- [[concepts/research-quality]]
- [[concepts/human-in-the-loop]]

## Related Summaries

- [[summaries/building-skills]]
- [[summaries/skill-library]]
- [[summaries/workflow-overview]]
- [[summaries/daaf-framework]]
