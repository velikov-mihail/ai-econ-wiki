---
title: From EDGAR Filings to a Structured Database using Claude Code
tags:
- summary
- data-analysis
- web-scraping
- EDGAR
- SEC
- data-pipelines
- claude-code
- text-as-data
sources:
- '[[raw/articles/From EDGAR Filings to a Structured Database using Claude Code.md]]'
date_updated: 2026-04-03
date_published: 2026-03
---

- **Original**: [https://paulgp.substack.com/p/from-edgar-filings-to-a-structured](https://paulgp.substack.com/p/from-edgar-filings-to-a-structured)


**Author/Source**: Paul Goldsmith-Pinkham, published on Substack (paulgp.substack.com). Published 2026-03-29.

## Key Ideas

- The article presents a complete pipeline for scraping SEC EDGAR 10-K filings, parsing Item 1A (Risk Factors), building a structured DuckDB database, and running keyword-based analyses of tariff-related risk disclosures -- all orchestrated through Claude Code.
- **Plan mode** is the key workflow innovation: Claude researches the EDGAR API, asks the researcher three design questions (database format, keyword approach, user-agent), and saves a written plan before clearing context and executing.
- Front-loading context about rate limits, authentication, and API structure before code generation avoids debugging cycles. Caching downloaded HTML ensures resilience to failures.
- The "scrape, parse, structure, analyze" pattern applies to any text-as-data project. The database (not the raw HTML) is the reusable research asset.
- Quality reports (extraction success rates, word count distributions, flagged short extractions) are essential for catching parsing errors early.
- DuckDB (or SQLite) is recommended over CSV-based workflows for text-as-data research: zero configuration, SQL-queryable, handles relational structure naturally, and is portable as a single file.
- The descriptive finding -- tariff keyword frequency increased from 2010 to 2025, vocabulary shifted from narrow trade terms to broader policy-risk language, Walmart only mentioned tariffs starting in 2025 -- demonstrates that even simple analyses can motivate deeper research.

## Summary

This written companion to the Markus Academy video series provides a detailed account of building a research dataset from SEC EDGAR filings using Claude Code. The motivating question is whether firms increased tariff-related language in 10-K Risk Factors sections after the 2025 tariff escalation, connecting to the Baker-Bloom-Davis policy uncertainty literature and the Campbell et al. (2014) work on risk factor disclosure.

The article walks through four phases. First, Claude enters plan mode, researches the EDGAR API, and asks the researcher three design questions before proposing a complete pipeline architecture. The plan is saved to disk and the context window is cleared -- implementing the "research, plan, execute" pattern that maximizes context budget. Second, Claude writes approximately 480 lines of Python implementing CIK lookup, filing index queries, document downloading with caching, HTML parsing with BeautifulSoup, and DuckDB storage. The script handles 29 of 30 firms on the first run, with the Gap Inc. ticker mismatch diagnosed and fixed in under a minute thanks to cached downloads. Third, iterative regex debugging improves Item 1A extraction from 112/120 to 119/120 filings, with the single remaining failure (3M) flagged for manual review. Fourth, DuckDB queries reveal the descriptive findings.

Goldsmith-Pinkham distills seven lessons: front-load context for scraping tasks; let Claude ask you questions rather than specifying everything upfront; build (or approve) the database schema yourself; build in resume/caching capability; generate quality reports; use DuckDB or SQLite for text-as-data; and always push through to an actual finding. The final project structure is a clean, reproducible pipeline with separate scripts for downloading, extraction, and analysis, plus a DuckDB database as the primary deliverable.

## Relevance to Economics Research

This article provides a practical template for any economist working with regulatory filings, earnings calls, or other text-based data sources. The pipeline pattern (scrape, parse, structure, analyze) and the emphasis on DuckDB as a research-ready database format are directly applicable to text-as-data research in finance and economics. The 30-minute turnaround from research question to queryable database, with the ability to extend to the full S&P 500 without changing the pipeline, represents a significant reduction in the fixed costs of empirical text analysis.

## Related Concepts

- [[concepts/data-pipelines]]
- [[concepts/web-scraping]]
- [[concepts/claude-code]]
- [[concepts/plan-driven-development]]
- [[concepts/text-as-data]]
- [[concepts/context-management]]

## Related Summaries

- [[summaries/web-scraping-economists]]
- [[summaries/empty-folder-to-figure]]
- [[summaries/data-analysis-economists]]
