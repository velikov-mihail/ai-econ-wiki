---
title: "Privacy, Data, and Setup Decisions for AI Workflows"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Privacy & Setup - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---
- **Original**: [https://claudeblattman.com/tax-workflow/before-you-start/privacy-and-setup/](https://claudeblattman.com/tax-workflow/before-you-start/privacy-and-setup/)


**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/tax-workflow/before-you-start/privacy-and-setup/)

## Key Ideas

- When Claude Code reads local files, the text content is sent to Anthropic's API as part of the conversation context -- CLAUDE.md rules prevent display but do not prevent transmission
- SSNs, bank account numbers, and other high-sensitivity data should never enter the AI workflow; redact PDFs or enter figures manually for documents containing them
- Gmail MCP grants access to your entire inbox, not just tax-related emails; consider enabling it only during active use or restricting searches to a dedicated label
- A "temporary access, permanent separation" pattern is recommended: create a dedicated working folder, use it during the active workflow, then delete it and archive outputs to secure storage
- Anthropic's API may retain inputs for up to 30 days for safety monitoring; users should verify the latest data retention policy themselves
- Claude Code can access any locally-synced cloud folder (Dropbox, iCloud, Google Drive) -- sensitive documents should not sit in synced folders year-round
- The article provides pre-flight and post-season checklists for managing data exposure

## Summary

This article addresses the privacy and data security decisions researchers must make before using Claude Code (or any AI tool) with sensitive documents. Although framed around a tax preparation workflow, the principles apply broadly to any scenario involving confidential data -- including research with human subjects, financial records, or proprietary datasets.

The core framework distinguishes three data flows: local files (stay on your machine), conversation context sent to Anthropic's API (includes any text Claude reads), and data flowing through Google's APIs if Gmail or Google Sheets MCP integrations are enabled. The article emphasizes that CLAUDE.md instructions can prevent Claude from displaying sensitive values but cannot prevent them from being transmitted to the API when Claude reads a document. The only true protections are redacting documents before giving them to Claude or entering sensitive figures manually.

The recommended operational pattern is "temporary access, permanent separation": create a dedicated working folder for the active task, populate it only with needed documents, do the work, then archive outputs and delete the working folder. The article provides concrete shell commands for each phase and includes detailed checklists for both setup and cleanup. It also discusses Gmail MCP's broad inbox access and recommends either enabling it only when needed or using a label-based approach to limit exposure.

## Relevance to Economics Research

Researchers routinely handle sensitive data -- IRB-protected survey responses, proprietary financial datasets, confidential firm data under NDA. This article's framework for thinking about what data touches which AI system is directly applicable. The "temporary access" pattern and the distinction between display prevention and transmission prevention are especially important for economists who may want to use Claude Code for data analysis while maintaining compliance with IRB protocols or data use agreements. The heuristic of treating AI API exposure as comparable to cloud storage (e.g., Dropbox) risk provides a useful mental model for calibrating comfort levels.

## Related Concepts

- [[concepts/data-privacy]]
- [[concepts/claude-code]]
- [[concepts/mcp-protocol]]
- [[concepts/data-privacy]]

## Related Summaries

- [[summaries/install-mac]]
- [[summaries/install-windows]]
- [[summaries/getting-started-researchers]]
- [[summaries/getting-started-economists]]
