---
title: "From an Empty Folder to a Figure using Claude Code"
tags: [summary, data-analysis, claude-code, visualization, workflow]
sources:
  - "[[raw/articles/From an Empty Folder to a Figure using Claude Code.md]]"
date_updated: 2026-04-03
---

- **Original**: [https://paulgp.substack.com/p/from-an-empty-folder-to-a-figure](https://paulgp.substack.com/p/from-an-empty-folder-to-a-figure)


**Author/Source**: Paul Goldsmith-Pinkham, published on Substack (paulgp.substack.com). Published 2026-03-29.

## Key Ideas

- A complete empirical workflow -- from an empty directory to a polished figure -- can be executed through natural language conversation with Claude Code, including data source discovery, downloading, parsing messy government spreadsheets, and iterative figure design.
- Claude uses **sub-agents** with separate context windows for web research, preventing the main conversation from being overwhelmed by search results. The sub-agent reads just enough of each data source to understand the structure, then writes a parser.
- Referencing a known style authority (e.g., "follow Kieran Healy's best practices") is more effective than specifying individual plotting parameters; Claude translates the reference into concrete principles (clean ggplot2, direct labeling, minimal chart junk, thoughtful color).
- **Claude Code vs. Cowork**: both find the same data sources, but Cowork's sandboxed environment prevents it from executing download scripts that require web access. Claude Code's local execution model is a clear advantage for data acquisition.
- Five practical lessons: (1) let Claude do data acquisition, (2) reference styles you like, (3) iterate in small steps rather than one massive specification, (4) always generate scripts (not just outputs) for reproducibility, (5) the judgment -- which comparisons matter, what story to tell -- remains the researcher's.

## Summary

This written companion to the Markus Academy video series documents a data analysis workflow using Claude Code, starting from an empty folder. The motivating question is how the age distribution of U.S. homeowners has changed over 50 years, connecting to Goldsmith-Pinkham's own research on gender gaps in housing returns with Kelly Shue. The prompt is deliberately vague -- the researcher knows the Census Bureau publishes the data but does not specify exact table numbers or series IDs.

Claude's first attempt targets FRED, where it finds the overall homeownership rate but struggles to locate age-specific breakdowns. It then switches to the Census Bureau website, encounters a 403 error (the site blocks non-browser requests), and fixes the issue by adding a user-agent header. Ultimately it identifies two useful tables: Table 19 (quarterly rates by age, 1994-present, broad groups) and Table 12 (annual household counts by detailed age, 1982-present, requiring rate computation). Claude pulls both, parses the messy Excel formatting, and produces clean CSVs in about six minutes.

For figure generation, Goldsmith-Pinkham uses his "number one cheat": telling Claude to follow Kieran Healy's visualization best practices. Claude writes 77 lines of R/ggplot2 code, debugs font rendering issues with the Cairo graphics device, and produces a first-draft figure. When asked to switch to an age-distribution view with finer age buckets, Claude re-downloads more granular data, re-parses it, and regenerates the figure -- even catching and fixing overlapping year labels on its own. The final product shows homeownership rates by age at different points in time, revealing the post-crisis decline among younger households and the 2004 peak.

## Relevance to Economics Research

This article provides a concrete template for the exploratory data analysis phase of empirical economics projects. The workflow -- vague question to data acquisition to figure iteration -- maps directly to how researchers scope new projects. The emphasis on generating reproducible scripts (rather than interactive one-off outputs) and retaining researcher judgment over presentation choices makes this approach compatible with the norms of academic research. The comparison between Claude Code and Cowork is particularly useful for researchers deciding which tool to adopt.

## Related Concepts

- [[concepts/data-pipelines]]
- [[concepts/claude-code]]
- [[concepts/agentic-ai]]
- [[concepts/context-management]]
- [[concepts/prompt-engineering]]
- [[concepts/visualization]]

## Related Summaries

- [[summaries/data-analysis-economists]]
- [[summaries/web-scraping-economists]]
- [[summaries/edgar-filings]]
