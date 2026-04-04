---
title: "Using Claude Code for Tax Season"
tags: [summary, professional-productivity, tax, ai-workflow, document-processing]
sources:
  - "[[raw/articles/Using Claude Code for Tax Season - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---
- **Original**: [https://claudeblattman.com/tax-workflow/](https://claudeblattman.com/tax-workflow/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/tax-workflow/)

## Key Ideas

- The author built Claude Code skills for tax preparation: `/tax-guide` (personalized assessment), `/tax-collect` (document collection from Gmail), `/tax-compile` (compilation of deductions into spreadsheets), and a three-year review skill that catches anomalies by comparing against prior returns.
- What took about three hours of AI-assisted work would have cost roughly $1,000 from an accountant.
- The `/tax-guide` skill asks 8 questions and generates a personalized plan: which documents to collect, whether to self-file or hire a professional, and which parts of the workflow apply.
- Privacy is a first-class concern: the workflow explicitly addresses what data is sent to Anthropic's API, warns against pasting SSNs or bank account numbers, and notes the difference between Claude Code (API) and Claude.ai (consumer) data policies.
- The biggest value was not time savings but catching errors the author would have missed; the biggest lesson was learning exactly where AI needs human verification on every output.
- The case study uses fictional personas to demonstrate the workflow across different complexity levels.

## Summary

This article is the landing page for Blattman's AI-assisted tax preparation case study. The author, a former tax accountant, used Claude Code to handle the "grunt work" of tax season: assembling charitable contributions from a Google Sheet, compiling itemized deductions from scattered receipts across email and credit card statements, building a Schedule C for consulting income, and running cost-benefit analyses on filing options. The workflow is organized into sections covering privacy/setup, document collection, compilation and review, common AI errors, architecture patterns for building similar workflows, and reference materials.

The entry point is a `/tax-guide` skill that assesses your situation through 8 questions and generates a tailored workflow plan. The broader system includes skills for searching Gmail for tax documents, downloading and parsing attachments, extracting key figures, tracking missing documents, and compiling deductions from multiple sources into spreadsheets ready for tax software. A three-year comparison skill provides an additional verification layer. The article is careful to note that this is educational content using fictional personas, not tax advice, and directs readers with complex situations to professional help.

## Relevance to Economics Research

This case study demonstrates how Claude Code skills can be built for document-heavy professional workflows beyond research itself. For economics researchers who typically have complex returns (consulting income, multiple 1099s, international income), the workflow offers a practical template. More broadly, the architecture patterns -- document collection from email, compilation from scattered sources, multi-year comparison for anomaly detection -- transfer directly to research data management tasks like assembling datasets from multiple sources or tracking grant expenditures.

## Related Concepts

- [[concepts/claude-code-skills]]
- [[concepts/ai-workflows]]
- [[concepts/document-processing]]

## Related Summaries

- [[summaries/academic-tax-basics]]
- [[summaries/when-to-get-help]]
- [[summaries/cost-reality]]
