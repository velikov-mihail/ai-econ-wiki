---
title: "Large Datasets: Claude Code for Economists (Video)"
tags: [summary, data-analysis, duckdb, parquet, video, markus-academy]
sources:
  - "[[raw/articles/Large Datasets Claude Code for Economists with Paul Goldsmith-Pinkham  Markus Academy  Ep. 162-4.md]]"
date_updated: 2026-04-05
date_published: 2026-04-05
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale School of Management), Markus Academy Ep. 162-4
- **Original**: [https://www.youtube.com/watch?v=4uwI1-9DafU](https://www.youtube.com/watch?v=4uwI1-9DafU)

- **Key Ideas**
  - Live walkthrough of building a 291-million-row mortgage database from HMDA data using Claude Code in the terminal — the companion video to the [[summaries/large-datasets-economists|Substack post]].
  - Demonstrates sub-agent behavior in real time: Claude launches parallel agents for project exploration and data format research; the explorer agent persistently tries to access the parent directory despite user denials, because the sub-agent's prompt (written by the main agent) didn't include the user's constraint.
  - Shows plan mode in action: Claude automatically enters plan mode for complex projects, designing a six-file Python architecture before writing any code; plan mode prevents file edits, and the plan is saved to `~/.claude/plans/` for persistence.
  - CSV-to-Parquet compression shown live: 2017 file goes from 1.7 GB to 114 MB; 2024 from 4.3 GB to 450 MB.
  - Claude uses `sleep 60` to self-schedule background checks on long-running conversion jobs — a practical pattern for tasks that take minutes.
  - The fintech lender classification section shows Claude spending 75,000 tokens researching HMDA Panel files before proposing a feasible implementation plan.
  - DuckDB metadata explained for non-technical audience: like Stata variable labels, but queryable and self-documenting.

- **Summary**

This Markus Academy video (Episode 4 of 7) is a live screen-share demonstration of the workflow described in Goldsmith-Pinkham's [[summaries/large-datasets-economists|companion Substack post]]. Goldsmith-Pinkham works through the entire pipeline in real time: pasting a detailed prompt into Claude Code, watching it spawn sub-agents, entering plan mode, writing pipeline code, converting CSVs to Parquet, building a DuckDB database, and finally classifying fintech lenders.

The video is particularly valuable for showing the *interaction patterns* — how to handle persistent sub-agents that ignore constraints, when to use plan mode (Shift+Tab), how background tasks work, and how to ask Claude to assess feasibility before diving into implementation. Markus Brunnermeier asks clarifying questions throughout, making technical concepts (Parquet, DuckDB, FIPS codes, HHI) accessible to a general economics audience.

- **Relevance to Economics Research**

The most detailed available video demonstration of AI-assisted large-scale data engineering for economists. Particularly useful for researchers who learn by watching rather than reading, and for those unfamiliar with DuckDB/Parquet workflows. The sub-agent troubleshooting sections provide practical lessons on managing AI coding agents.

- **Related Concepts**
  - [[concepts/data-pipelines]]
  - [[concepts/agentic-workflows]]
  - [[concepts/context-management]]
  - [[concepts/plan-driven-development]]

- **Related Summaries**
  - [[summaries/large-datasets-economists]]
  - [[summaries/edgar-filings]]
  - [[summaries/data-analysis-economists]]
  - [[summaries/getting-started-economists]]
  - [[summaries/cc-series-38-plug-paulgp]]
