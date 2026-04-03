---
title: "Architecture Patterns"
tags: [summary, ai-workflows, design-patterns, validation]
sources:
  - "[[raw/articles/Architecture Patterns - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/tax-workflow/build-your-own/architecture-patterns/)

## Key Ideas

- The Collection-Compilation-Review pipeline is the fundamental structure for any document-heavy workflow. Each stage is a separate skill so they can run independently and feedback loops allow self-correction.
- A Tracking Checklist serves as a single, machine-readable, append-only source of truth for what has been collected, what is missing, and what requires manual action.
- The Guided Interview pattern uses structured human interaction (with prior-period references and domain-specific prompts) for categorization tasks that require judgment, rather than relying on automated classification.
- The Threshold Gate pattern checks whether expensive work will matter before doing it (e.g., checking if medical expenses exceed the 7.5% AGI floor before detailed processing).
- Three-Tier Classification (auto-qualify / auto-exclude / uncertain) outperforms binary classification by routing genuinely ambiguous cases to human review, with the uncertain bucket shrinking over time.
- Historical Comparison against N prior periods catches anomalies invisible in single-period views: percentage changes >15%, sign reversals, missing items, new items, and ratio shifts.
- The Validation Stack uses four layers -- source verification, internal consistency, historical comparison, and human review -- because no single layer catches all error types. The design principle is "design for distrust."

## Summary

This article extracts eight reusable architecture patterns from a tax preparation workflow, framed as applicable to any document-heavy, multi-source, verification-critical task (expense reporting, grant management, compliance). The patterns progress from structural (the three-stage pipeline, tracking checklists) through decision-support (guided interviews, threshold gates, three-tier classification) to quality assurance (historical comparison, entry guides, validation stacks).

The most distinctive patterns are the Three-Tier Classification and the Validation Stack. The three-tier approach avoids the false-positive/false-negative trade-off of binary classification by explicitly routing ambiguous cases to human judgment, with an improvement mechanism where uncertain items are reclassified over time. The Validation Stack layers four independent checks -- source verification, internal consistency, historical comparison, and human review -- on the principle that each layer catches different error classes. The article emphasizes that PDF extraction "fails silently" by returning plausible wrong numbers, making multi-layer validation essential.

The article also provides skeleton code for each pattern and a worked example showing how they combine for expense reporting. The Entry Guide pattern bridges the gap between compiled data and downstream system entry by mapping each value to its exact destination field, addressing the observation that manual data entry -- not compilation -- is the most error-prone step.

## Relevance to Economics Research

These patterns transfer directly to empirical research workflows. The Collection-Compilation-Review pipeline maps onto data gathering, variable construction, and robustness checking. The Threshold Gate is analogous to preliminary checks before running computationally expensive estimations. Three-Tier Classification applies to any coding task where some observations are clear-cut and others require researcher judgment (e.g., industry classification, event categorization). The Validation Stack's layered approach -- source verification, internal consistency, historical comparison, human review -- mirrors best practices for data quality assurance in empirical finance and economics, where silent extraction errors in WRDS or Compustat data can propagate through an entire analysis.

## Related Concepts

- [[concepts/ai-workflows]]
- [[concepts/validation-and-verification]]
- [[concepts/design-patterns]]
- [[concepts/human-in-the-loop]]

## Related Summaries

- [[summaries/workflow-overview]]
- [[summaries/patterns]]
- [[summaries/prompt-plan-review-revise]]
