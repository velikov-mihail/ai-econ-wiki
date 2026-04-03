---
title: "Data Access"
tags: [concept, data, tools]
sources:
  - "[[summaries/automated-research-finance.md]]"
date_updated: 2026-04-03
---

# Data Access

Data access in the AI research context covers how AI tools connect to and query research data sources — from institutional databases like WRDS to public APIs like FRED and EDGAR.

## Context & Background

Effective AI-assisted research requires the AI tool to access the same data sources researchers use. This can happen through:

- **API integration**: Direct connections to data providers (WRDS Python API, FRED API)
- **MCP servers**: Model Context Protocol connections that give AI tools database access
- **File-based access**: Loading data files (CSV, Parquet) into the AI's working context
- **Database queries**: AI-generated SQL or API calls to retrieve specific data

## Practical Implications

- **Set up API credentials**: Configure WRDS, FRED, and other API access in your environment
- **Use MCP for database access**: Connect Claude Code to databases via MCP for seamless queries
- **Respect data agreements**: Ensure AI tool use complies with data provider terms
- **Cache aggressively**: Store downloaded data locally to reduce API calls and ensure reproducibility

## Related Concepts

- [[concepts/data-pipelines|Data Pipelines]]
- [[concepts/wrds-data-access|Wrds Data Access]]
- [[concepts/mcp-protocol|Mcp Protocol]]
