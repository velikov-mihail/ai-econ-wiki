---
title: "Large Datasets and Structured Databases: Claude Code for Economists"
tags: [summary, data-analysis, duckdb, parquet, data-pipelines, context-engineering]
sources:
  - "[[raw/articles/Large Datasets and Structured Databases Claude Code for Economists.md]]"
date_updated: 2026-04-05
date_published: 2026-04-05
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale School of Management), via Substack
- **Original**: [https://paulgp.substack.com/p/large-datasets-and-structured-databases](https://paulgp.substack.com/p/large-datasets-and-structured-databases)

- **Key Ideas**
  - The fixed cost of doing data engineering properly has collapsed: with an AI coding agent, you can describe what you want in plain English and get a professional-grade pipeline (download, harmonize, build database with metadata) in an afternoon.
  - DuckDB + Parquet is the right stack for datasets in the tens-of-gigabytes range — a 70 GB CSV dataset compressed to 6 GB of Parquet files (15x compression), and DuckDB queries 291 million rows in seconds without loading everything into memory.
  - **Metadata tables are context engineering for data**: store schema, descriptions, value labels, and documentation *in the database itself* so that future Claude sessions (or coauthors) can query the metadata and immediately understand the dataset without re-explanation.
  - Plan mode before code is essential for complex pipelines — Claude designed a six-file architecture before writing any code, then saved the plan and cleared context for a clean coding session.
  - Sub-agents are powerful but imperfect: the main agent's "stay in this directory" constraint didn't propagate to the explorer sub-agent's prompt, illustrating how sub-agent instructions can diverge from user intent.
  - "Ask what's feasible before committing" — when adding fintech lender classification, asking Claude to assess feasibility first surfaced three problems (no lender names, no cross-era ID crosswalk, need for panel files) before any code was written.

- **Summary**

Goldsmith-Pinkham demonstrates how to take the HMDA (Home Mortgage Disclosure Act) dataset — 291 million rows across 18 years, 70 GB of raw CSVs — and build a clean, documented, queryable database using Claude Code. The pipeline downloads data from two different CFPB sources (pre-2018 and post-2018 formats with different column names and coding schemes), converts CSVs to Parquet, harmonizes the schema via a crosswalk, and assembles everything into a DuckDB database with a metadata table documenting every column.

The post then extends the project into research territory by classifying mortgage lenders as fintech vs. traditional banks, starting from the Fuster, Plosser, Schnabl and Vickery (2019) classification. Claude researched where to find lender names (HMDA Panel files), downloaded them, and built a classification table. The resulting figure shows fintech origination share rising from 1.1% in 2007 to a peak of 16.3% during the 2021 COVID refi boom.

The conceptual contribution is the idea of metadata tables as "context engineering for data" — the same principle as writing state to files for context window management, but applied to datasets. The metadata survives compaction, session restarts, and coauthor handoffs.

- **Relevance to Economics Research**

Directly addresses a common pain point: most applied economists work with messy flat CSVs and are not trained as data engineers. Shows that the barrier to proper data infrastructure has dropped to near zero, making DuckDB + Parquet + metadata the new baseline for large administrative datasets (HMDA, IPEDS, patents, trade data). The "ask what's feasible" pattern models effective delegation to AI research assistants.

- **Related Concepts**
  - [[concepts/data-pipelines]]
  - [[concepts/context-management]]
  - [[concepts/data-analysis-with-ai]]
  - [[concepts/plan-driven-development]]
  - [[concepts/agentic-workflows]]

- **Related Summaries**
  - [[summaries/edgar-filings]]
  - [[summaries/data-analysis-economists]]
  - [[summaries/getting-started-economists]]
  - [[summaries/empty-folder-to-figure]]
  - [[summaries/claude-wrds-tools]]
