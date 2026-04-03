---
title: "What AI Got Wrong"
tags: [summary, institutional-societal]
sources:
  - "[[raw/articles/What AI Got Wrong - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Original**: [https://claudeblattman.com/tax-workflow/case-study/what-ai-got-wrong/](https://claudeblattman.com/tax-workflow/case-study/what-ai-got-wrong/)


**Author/Source**: Chris Blattman (economist, University of Chicago), claudeblattman.com, 2026

**Key Ideas**:
- AI is good at structured data extraction, pattern matching, and organizing information; it is bad at context-dependent judgment, ambiguous categorization, and knowing what it does not know
- PDF extraction errors occurred in roughly 1 in 10 documents, with about half being potentially significant (wrong dollar amounts)
- AI "hallucinated" plausible but fabricated numbers in 2 instances during the workflow -- the most dangerous error category because the numbers looked reasonable
- Email-based document search is necessary but not sufficient; income reconciliation against prior-year payers is the real safety net
- AI suggested plausible but wrong expense categorizations (e.g., confusing deductible consulting travel with employer-reimbursed travel)
- The meta-lesson: every error follows the pattern of (1) AI does something plausible but wrong, (2) the error requires domain knowledge to catch, (3) a review mechanism catches it
- AI makes tax preparation faster but not easier -- you still need to understand your tax situation well enough to catch errors

**Summary**:
Blattman, an economist who went from AI skeptic to building a complete AI workflow toolkit, documents the specific errors AI made in a tax preparation case study using Claude. The article is structured around five error categories: PDF extraction failures, missed documents in email search, wrong expense categorizations, medical expense misclassification from credit card data, and outright hallucinated dollar amounts. Each category includes a concrete example with a fictional persona, an explanation of how the error was caught, and the defensive mechanism built into the workflow.

The most valuable insight is the "meta-lesson" that unifies all five categories. AI errors are consistently plausible -- they look right to someone who is not carefully checking against source documents. A fabricated mortgage interest figure was within the normal range; a wrong expense category was a reasonable guess given the description. This means that the workflow's safety depends entirely on human review steps being taken seriously. Blattman's uncomfortable conclusion: "AI makes tax preparation faster. It does not make tax preparation easier. You still need to understand your tax situation well enough to catch errors." The difference is that you are reviewing organized data instead of building it from scratch -- review is faster than construction, but only if you actually do it. He recommends starting with the three-year comparison review (which catches the most errors), adding confidence scores to extractions, and maintaining a running error log for year-over-year improvement.

**Relevance to Economics Research**:
This article provides a concrete, granular case study of AI error patterns that is directly transferable to economics research workflows. The same error categories -- extraction errors from messy data, plausible but wrong categorizations, hallucinated numbers -- will appear when researchers use AI to process financial data, classify variables, or extract information from PDFs and databases. The key insight for economists is that AI errors are systematically plausible rather than random, making them harder to catch without domain expertise and deliberate verification procedures. The workflow design principles (mandatory verification gates, prior-period reconciliation, three-tier confidence classification) offer a template for building robust AI-assisted research pipelines.

**Related Concepts**:
- [[concepts/jagged-frontier]]
- [[concepts/human-ai-collaboration]]
- [[concepts/agentic-ai]]
- [[concepts/ai-adoption-academia]]

**Related Summaries**:
- [[summaries/shape-of-ai]]
- [[summaries/academics-wake-up-2]]
- [[summaries/train-left-station]]
- [[summaries/ai-normal-technology]]
