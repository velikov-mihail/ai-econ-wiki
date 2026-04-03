---
title: "Web Scraping: Claude Code for Economists with Paul Goldsmith-Pinkham (Markus Academy Ep. 162-3)"
tags: [summary, web-scraping, claude-code, economists, SEC, EDGAR]
sources:
  - "[[raw/articles/Web scraping Claude Code for Economists with Paul Goldsmith-Pinkham  Markus Academy  Ep. 162-3.md]]"
date_updated: 2026-04-03
---

- **Original**: [https://www.youtube.com/watch?v=wqLZrKdevHs](https://www.youtube.com/watch?v=wqLZrKdevHs)


**Author/Source**: Paul Goldsmith-Pinkham, presented via Markus Academy video series (Ep. 162, Part 3). Published 2026-03-28.

## Key Ideas

- Claude Code can plan and execute a multi-step web scraping pipeline: researching the EDGAR API, designing a database schema, downloading 10-K filings, parsing HTML for specific sections, and storing structured results -- all from a single conversational session.
- **Plan mode** is critical for complex projects: Claude enters a planning phase where it researches APIs, proposes architecture, and asks the researcher clarifying questions (database format, keyword approach, user-agent identity) before writing any code.
- Front-loading domain context in the prompt (rate limits, API endpoints, user-agent requirements) prevents costly debugging cycles later.
- Claude's **caching** of downloaded files means that fixing errors (e.g., a wrong ticker symbol) requires re-downloading only the affected files, not the entire dataset.
- The plan is saved to a file and the context window is cleared before execution, implementing the "research, plan, execute" pattern that preserves context budget.
- Iterative debugging of regex-based text extraction (e.g., handling "Item 1A" and "Risk Factors" on separate lines) illustrates the "95% fast, last 5% requires judgment" pattern common in text-as-data work.

## Summary

This video demonstrates building a structured database from SEC EDGAR filings using Claude Code. The task is to study how tariff-related risk disclosures in 10-K Item 1A (Risk Factors) sections changed from 2022 to 2025 for approximately 30 trade-exposed firms. Goldsmith-Pinkham provides Claude with specific context about the EDGAR API, including rate limits and user-agent requirements, and Claude enters plan mode to design the full pipeline before writing code.

During the planning phase, Claude asks three key design questions: database format (DuckDB was chosen), keyword approach (keyword search rather than LLM classification), and user-agent identity. The host, Markus Brunnermeier, suggests adding "liberation day" to the tariff keyword list, which Claude incorporates immediately. After the plan is finalized and saved to a file, Claude clears its context window and begins implementation, writing approximately 480 lines of Python.

The scraping run successfully processes 29 of 30 firms (Gap Inc. failed due to a ticker symbol mismatch, which Claude diagnoses and fixes). The text extraction initially captures 112 of 120 filings, with failures traced to formatting edge cases in Honeywell and Intel filings where regex patterns needed adjustment. After fixes, 119 of 120 filings are successfully parsed. The resulting DuckDB database enables immediate querying: Deere leads in tariff mentions, manufacturing firms mention tariffs most, and Walmart only began mentioning tariffs in 2025. Extending the analysis to 2010 reveals that while tariff mentions existed then, the vocabulary has shifted from narrow trade terms to broader policy-risk language.

## Relevance to Economics Research

This demonstration is directly relevant to the growing text-as-data literature in economics and finance. The pipeline mirrors the workflow needed for research on policy uncertainty measurement (Baker, Bloom & Davis), corporate risk disclosure, and regulatory text analysis. The ability to go from a research question to a queryable database of parsed SEC filings in 30 minutes dramatically lowers the barrier to entry for text-based empirical work. The structured output (a DuckDB file) can be joined to standard datasets like CRSP or Compustat for further analysis.

## Related Concepts

- [[concepts/data-pipelines]]
- [[concepts/web-scraping]]
- [[concepts/claude-code]]
- [[concepts/plan-driven-development]]
- [[concepts/text-as-data]]

## Related Summaries

- [[summaries/edgar-filings]]
- [[summaries/data-analysis-economists]]
- [[summaries/getting-started-economists]]
