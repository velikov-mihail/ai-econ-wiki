---
title: "Workflow Overview: From Inbox to Organized Return"
tags: [summary, ai-workflows, case-study, validation]
sources:
  - "[[raw/articles/Workflow Overview - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---
- **Original**: [https://claudeblattman.com/tax-workflow/case-study/the-workflow-overview/](https://claudeblattman.com/tax-workflow/case-study/the-workflow-overview/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/tax-workflow/case-study/the-workflow-overview/)

## Key Ideas

- The tax workflow follows a four-stage pipeline: Document Collection, Compilation, Three-Year Review, and Manual Entry/Filing. Every AI-generated output is reviewed by a human before affecting the tax return.
- Document Collection searches email, downloads attachments, extracts key figures, updates a tracking checklist, and runs income reconciliation against prior years to catch missing 1099s. It is designed to run repeatedly as documents arrive over 6-8 weeks.
- Compilation uses sub-commands for different tax components (Schedule C, charitable, medical) with a guided interview approach for expense categorization and a threshold gate for medical expenses.
- The Three-Year Review is identified as the single highest-value step: it extracts key figures across three years, displays side-by-side comparisons, and flags anomalies (>15% changes, sign reversals, missing items).
- Manual entry remains deliberately non-automated as the final verification layer -- typing each number forces one last look.
- Every stage has mandatory human review points that cannot be automated (e.g., only the user knows which trips were for consulting vs. employer-reimbursed).
- Realistic time savings are approximately 50% (12 hours to 6 hours), but the main value is error reduction and feasibility of the three-year review, which most people skip entirely.

## Summary

This article describes the complete pipeline of an AI-assisted tax preparation workflow, using three fictional personas of increasing complexity: Elena (simple W-2 + 1099), James (salary + consulting + investments, the primary case study), and Priya (foreign income, rental property, K-1 -- the escalation case requiring a CPA). The workflow demonstrates how AI assists at each stage while maintaining human control over all consequential decisions.

The four stages illustrate a general pattern for document-heavy workflows. Collection is additive and runs multiple times over weeks. Compilation uses different approaches per component -- guided interviews for judgment-dependent categorization (Schedule C expenses), automated extraction for structured data (charitable contributions from Google Sheets), and threshold gates to skip work that will not affect the outcome (medical expenses below the 7.5% AGI floor). The three-year review catches errors invisible in single-year views by flagging statistical anomalies across periods.

The article is explicit about what the workflow does not do: it does not log into financial portals, does not automate tax software entry, and does not replace professional advice for complex situations. The time savings table shows realistic estimates rather than aspirational ones, and the author notes that the main value is not time savings but error reduction and enabling the three-year review that most people never perform manually.

## Relevance to Economics Research

The four-stage pipeline (collect, compile, review, enter) is a general template for any data-intensive research task. The income reconciliation step -- comparing this year's data sources against last year's to catch missing items -- is analogous to checking that all expected firm-year observations appear in a panel dataset. The three-year review pattern maps directly onto checking regression results across specifications or time periods for anomalies. The deliberate choice to keep manual entry as a verification layer reflects the empirical research principle that the last human review before submission often catches errors that automated checks miss.

## Related Concepts

- [[concepts/ai-workflows]]
- [[concepts/research-quality]]
- [[concepts/human-in-the-loop]]
- [[concepts/design-patterns]]

## Related Summaries

- [[summaries/architecture-patterns]]
- [[summaries/workflows]]
- [[summaries/patterns]]
