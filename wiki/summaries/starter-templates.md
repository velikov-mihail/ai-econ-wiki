---
title: "Starter Templates for AI Workflow Skills"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Starter Templates - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/tax-workflow/build-your-own/starter-templates/)

## Key Ideas

- Five downloadable skill templates generalize the architecture patterns from the tax workflow case study into domain-agnostic building blocks
- Template 1 (Document Collector) automates searching email for documents, downloading, renaming, extracting key data, and tracking completeness via a checklist
- Template 2 (Compilation Skill) guides users through a structured interview to compile data from multiple sources, with period-over-period comparison
- Template 3 (Multi-Period Review) performs anomaly detection by comparing current-period outputs against prior periods, flagging large changes and sign reversals
- Template 4 (Tracking Checklist) provides a markdown-based system for monitoring document collection progress with reconciliation tables
- Template 5 (Privacy Policy) offers a CLAUDE.md addition for workflows handling sensitive data, specifying what to extract vs. what to never display

## Summary

This article provides five generic, downloadable skill templates that users can adapt for any document-collection and compilation workflow. The templates are extracted from Blattman's tax preparation case study but stripped of tax-specific content, making them reusable for expense reporting, grant management, compliance tracking, or any recurring document-heavy process. Each template is a markdown file saved to `~/.claude/commands/` that Claude Code interprets as a slash command.

The templates follow a consistent pattern: search for inputs (typically via Gmail MCP), present findings interactively for user approval, process and rename documents, generate structured outputs (often Excel files with summary and detail tabs), and run verification checks including period-over-period anomaly detection. The privacy template addresses workflows with sensitive data by defining explicit rules about what Claude may and may not extract, display, or store. The article notes that email search templates assume Gmail MCP, but compilation and review templates work with any provider since they operate on local files.

## Relevance to Economics Research

These templates map directly onto common research workflows in economics: collecting data files from email (e.g., co-author submissions, RA deliverables, IRB documents), compiling information from multiple sources into structured datasets, and performing period-over-period quality checks on data updates. The anomaly detection template mirrors the kind of data validation economists routinely perform when updating panel datasets, and the privacy template is relevant for researchers handling IRB-protected or proprietary financial data.

## Related Concepts

- [[concepts/claude-code-skills]]
- [[concepts/ai-workflows]]
- [[concepts/mcp-protocol]]
- [[concepts/prompt-engineering]]

## Related Summaries

- [[summaries/mcp-setup]]
- [[summaries/claude-code-newbies]]
- [[summaries/chatbot-essentials]]
