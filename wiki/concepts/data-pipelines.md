---
title: "Data Pipelines"
tags: [concept, data-analysis, web-scraping, tools]
sources:
  - "[[summaries/edgar-filings.md]]"
  - "[[summaries/web-scraping-economists.md]]"
  - "[[summaries/claude-wrds-tools.md]]"
  - "[[summaries/data-analysis-economists.md]]"
  - "[[summaries/empty-folder-to-figure.md]]"
  - "[[summaries/automated-research-finance.md]]"
date_updated: 2026-04-03
---

# Data Pipelines

## Definition

A **data pipeline** in the context of AI-assisted economics research is a structured sequence of steps -- data discovery, acquisition, parsing, structuring, and analysis -- orchestrated through natural language interaction with an AI coding agent. Unlike traditional pipelines built manually in Stata, R, or Python, AI-assisted pipelines can be planned and executed conversationally: the researcher describes what they need, the agent researches available data sources, proposes an architecture, and writes the code to implement it. The canonical pattern is "scrape, parse, structure, analyze," with a database (not raw files) as the reusable research asset.

The key data sources for economics researchers include SEC EDGAR (regulatory filings), WRDS (CRSP, Compustat, OptionMetrics, TAQ), FRED (macroeconomic time series), Census Bureau data, and various web-accessible government datasets. AI agents can interact with all of these, though the specific access patterns differ significantly.

## Context & Background

Before agentic AI tools, building a data pipeline from a new source -- say, parsing 10-K filings from EDGAR or merging CRSP with Compustat -- required the researcher to read API documentation, write boilerplate code, debug edge cases, and iterate on parsing logic. This work was typically delegated to research assistants and could take days or weeks. The emergence of AI coding agents in late 2025 and early 2026 compressed this timeline dramatically. Paul Goldsmith-Pinkham's demonstration of going from an empty folder to a queryable database of parsed SEC filings in 30 minutes became a reference point for what is now possible. Similarly, Piotrek Orlowski's WRDS toolkit showed that natural language queries against CRSP, Compustat, and TAQ are feasible with proper configuration.

## Key Perspectives

**Goldsmith-Pinkham ([[summaries/edgar-filings.md|EDGAR Filings]], [[summaries/web-scraping-economists.md|Web Scraping]])** provides the most detailed template. His pipeline for scraping SEC EDGAR 10-K filings uses **plan mode** -- Claude researches the API, asks the researcher three design questions, saves a written plan, clears the context window, and then executes. Seven lessons emerge: front-load context about rate limits and API structure; let Claude ask you questions rather than specifying everything; build the database schema yourself; build in resume/caching capability; generate quality reports (extraction success rates, flagged failures); use DuckDB or SQLite for text-as-data; and always push through to an actual finding.

**Goldsmith-Pinkham ([[summaries/data-analysis-economists.md|Data Analysis]], [[summaries/empty-folder-to-figure.md|Empty Folder to Figure]])** demonstrates the exploratory side: starting from a vague research question, Claude searches FRED and Census websites, overcomes HTTP errors, downloads and parses messy government spreadsheets, and produces publication-quality figures -- all in about 30 minutes. Sub-agents with separate context windows handle web research without overwhelming the main conversation.

**Orlowski ([[summaries/claude-wrds-tools.md|Claude WRDS Toolkit]])** addresses the standard academic finance data stack. Specialist agents handle different WRDS databases: `crsp-wrds-expert` for stock data, `optionmetrics-wrds-expert` for options, `taq-wrds-expert` for high-frequency data. Cross-database linking tables are built in. TAQ requires a fundamentally different workflow (SSH + SAS batch jobs on the WRDS grid) because the data is too large for direct PostgreSQL queries. Schema pre-loading avoids expensive exploratory round-trips.

**Lopez-Lira ([[summaries/automated-research-finance.md|Automated Research in Finance]])** has built a fully automated pipeline that takes a one-paragraph idea and produces a submission-ready paper, with access to WRDS, FRED, and Ken French data. This represents the extreme end of the pipeline spectrum -- full automation from idea to analysis.

## Practical Implications

For economics researchers building data pipelines with AI:

- **Front-load context**: provide the agent with API documentation, rate limits, authentication requirements, and known gotchas before it starts writing code. This prevents expensive debugging cycles.
- **Use plan mode**: separate planning (research the data source, design the architecture) from execution. Save the plan to a file and clear the context window before coding.
- **Build in resilience**: cache downloaded files so that fixing a parsing error does not require re-downloading the entire dataset. This is especially important for rate-limited APIs like EDGAR.
- **Use databases, not CSVs**: DuckDB or SQLite provide SQL-queryable, portable, single-file storage that handles relational structure naturally. This is a significant upgrade over the CSV-based workflows common in economics.
- **Generate quality reports**: extraction success rates, word count distributions, and flagged failures catch parsing errors early, before they propagate into analysis.
- **WRDS access requires configuration**: PostgreSQL service files, SSH keys, and careful handling of interactive authentication (Duo 2FA) are needed for seamless agent access to WRDS.

## Open Questions

- How should researchers handle data provenance and documentation when AI agents build the pipeline? The code is reproducible, but the conversational process that generated it is not.
- What are the best practices for validating AI-constructed data against known benchmarks before using it in published research?
- As AI agents become more capable, will WRDS and other data providers need to adapt their access patterns (e.g., offering agent-friendly APIs)?
- How should the cost of API tokens consumed during data pipeline construction factor into research budgets?

## Sources

- [[summaries/edgar-filings.md|EDGAR Filings]] -- Complete EDGAR scraping pipeline with seven lessons
- [[summaries/web-scraping-economists.md|Web Scraping for Economists]] -- Video demonstration of the EDGAR pipeline
- [[summaries/claude-wrds-tools.md|Claude WRDS Toolkit]] -- Natural language access to CRSP, Compustat, OptionMetrics, TAQ
- [[summaries/data-analysis-economists.md|Data Analysis for Economists]] -- Empty-folder-to-figure workflow
- [[summaries/empty-folder-to-figure.md|Empty Folder to Figure]] -- Detailed data acquisition and visualization walkthrough
- [[summaries/automated-research-finance.md|Automated Research in Finance]] -- Full pipeline from idea to paper
