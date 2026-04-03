---
title: "Document Collection: The 'Email as Database' Pattern"
tags: [summary, ai-tools, workflow, automation]
sources:
  - "[[raw/articles/Document Collection - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman (claudeblattman.com)

## Key Ideas

- The "email as database" pattern treats email as a searchable repository for document retrieval, applicable far beyond the tax use case demonstrated.
- The architecture involves: defining document types and sources, building broad search queries, creating a tracking checklist, running repeatedly as documents arrive, and cross-referencing against prior periods.
- Deduplication uses three checks (filename match, checklist match, content match) to handle repeated runs over weeks.
- A completeness dashboard provides a scannable interface showing collected vs. missing documents, with instructions for portal downloads.
- Income reconciliation -- comparing this year's sources against prior years -- is the most valuable automated check and caught a real missed document.
- The pattern transfers to insurance claims, real estate, grant management, conference organization, and job searches.

## Summary

This article is a deep dive into one component of Blattman's AI-powered tax workflow: automated collection of tax documents from email. The system runs four parallel Gmail searches (form-type keywords, known payer names, payment confirmations for unreported income, and miscellaneous tax-related documents), downloads attachments, extracts key data, renames files with a consistent convention, and tracks completeness. It is designed to run repeatedly over the 6-8 week window during which tax documents arrive, with conservative deduplication to avoid reprocessing.

The key design elements are a completeness dashboard that shows at a glance what has been collected and what is missing, and an income reconciliation check that compares current-year income sources against prior years. The article notes important privacy considerations -- PDF extraction sends document contents (including SSNs and account numbers) to the API -- and recommends keeping sensitive documents in locations Claude Code cannot reach year-round.

Blattman frames this as an instance of a general "email as database" pattern, providing a table of analogous use cases in other domains. The architecture is the same regardless of domain: define document types, build search queries, track completeness, run repeatedly, and cross-reference against prior periods.

## Relevance to Economics Research

While the specific use case is tax preparation, the underlying pattern is directly relevant to research workflows that involve collecting documents from multiple sources over time -- such as gathering data use agreements, IRB approvals, coauthor contributions, grant documentation, or regulatory filings. The architecture of automated search, deduplication, completeness tracking, and cross-referencing is a useful template for any researcher managing complex document flows.

## Related Concepts

- [[concepts/ai-workflows]]
- [[concepts/ai-research-tools]]
- [[concepts/prompt-engineering]]

## Related Summaries

- [[summaries/teaching-ai-your-voice]]
- [[summaries/feedback-machines]]
- [[summaries/stress-test-research-pipeline]]
