---
title: "Data Analysis: Claude Code for Economists with Paul Goldsmith-Pinkham (Markus Academy Ep. 162-2)"
tags: [summary, data-analysis, claude-code, economists, workflow]
sources:
  - "[[raw/articles/Data Analysis Claude Code for Economists with Paul Goldsmith-Pinkham  Markus Academy  Ep. 162-2.md]]"
date_updated: 2026-04-03
---

- **Original**: [https://www.youtube.com/watch?v=Rp17XUPxa4I](https://www.youtube.com/watch?v=Rp17XUPxa4I)


**Author/Source**: Paul Goldsmith-Pinkham, presented via Markus Academy video series (Ep. 162, Part 2). Published 2026-03-28.

## Key Ideas

- Claude Code can handle a complete data analysis workflow from scratch: finding data sources on the web, downloading and parsing messy government spreadsheets, and producing publication-quality figures -- all from natural language instructions in the terminal.
- The tool uses **sub-agents** with their own context windows to perform web searches and data acquisition without blowing out the main conversation's context.
- When scraping government websites (e.g., Census Bureau), Claude must handle practical obstacles like 403 errors by adding user-agent headers to HTTP requests.
- Referencing a known style guide (e.g., Kieran Healy's *Data Visualization*) when requesting figures is far more effective than specifying individual plotting parameters.
- Claude Code has a clear advantage over Claude Cowork for data acquisition tasks because Cowork runs in a sandboxed environment that restricts web access and local script execution.
- The iterative conversational workflow -- requesting a first draft, then refining with follow-up instructions -- mirrors how a researcher would direct a research assistant.

## Summary

This video walkthrough demonstrates a complete data analysis workflow using Claude Code. Paul Goldsmith-Pinkham starts in an empty folder and asks Claude to find and download Census Bureau data on U.S. homeownership rates by age over the last 50 years. Despite a deliberately vague initial prompt, Claude searches both FRED and the Census website, overcomes a 403 access error by adding a user-agent header, identifies two relevant data tables (quarterly rates from 1994 and annual household counts from 1982), and produces clean CSV files -- all in about six minutes.

The second phase focuses on figure generation. Goldsmith-Pinkham asks Claude to create an R script following Kieran Healy's visualization best practices. Claude produces a ggplot2 figure, debugs font rendering issues, and iterates on the design when asked to switch from a time-series view to an age-distribution view with finer age buckets. The conversational iteration -- adjusting axes, adding detail, refining styling -- replaces the traditional cycle of hand-editing plotting code.

Throughout, the video compares Claude Code running locally with Claude Cowork running in a browser sandbox. Both find the same data sources, but Cowork struggles to execute download scripts due to its sandboxed environment. The key takeaway is that Claude Code's local execution model gives it a significant practical advantage for data acquisition and analysis tasks, while the researcher retains judgment over which comparisons matter and how to present findings.

## Relevance to Economics Research

This demonstration directly addresses one of the most common tasks in empirical economics: acquiring publicly available data, cleaning it, and producing exploratory figures. The workflow shown -- from a vague research question to a polished figure in under 30 minutes -- dramatically compresses the time typically spent on scoping analyses. For economists who routinely work with Census, FRED, or other government data, Claude Code offers a way to delegate the mechanical parts of data acquisition and figure production while retaining control over research design decisions.

## Related Concepts

- [[concepts/data-pipelines]]
- [[concepts/claude-code]]
- [[concepts/agentic-ai]]
- [[concepts/context-management]]
- [[concepts/prompt-engineering]]

## Related Summaries

- [[summaries/empty-folder-to-figure]]
- [[summaries/web-scraping-economists]]
- [[summaries/getting-started-economists]]
