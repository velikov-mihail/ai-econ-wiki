---
title: "MCP Setup - Connecting Claude Code to External Services"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/MCP Setup - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/toolkit/mcp-setup/)

## Key Ideas

- MCP (Model Context Protocol) servers extend Claude Code by connecting it to Gmail, Google Docs, Sheets, Calendar, Drive, Zotero, WhatsApp, and Apple apps
- Google Workspace is the highest-value integration but requires 45-60 minutes of OAuth credential setup through Google Cloud Console
- Each MCP integration grants Claude access to the **entire** account for that service with no way to restrict scope to subsets
- Switching Google Cloud projects from "Testing" to "Production" mode prevents OAuth tokens from expiring every 7 days (the most common frustration)
- MCP configuration lives in `~/.claude.json` and specifies commands and credentials for each server
- Simpler integrations (Zotero, Apple apps) require only an API key and take about 10 minutes
- Claude Code works fully without MCP; integrations can be added incrementally as needed

## Summary

This article is a practical setup guide for connecting Claude Code to external services via the Model Context Protocol (MCP). Without MCP, Claude Code can only work with local files; with MCP, it can search email, read and write Google Docs and Sheets, check calendars, query Zotero reference libraries, and access WhatsApp conversations. The guide covers Google Workspace (the most involved setup, requiring OAuth credentials through Google Cloud Console), WhatsApp (QR code scan), Zotero (API key), Apple apps (Mac only, partially broken), and Granola (meeting transcripts).

The article emphasizes privacy considerations: each integration exposes the entire account to Claude, and content is sent to Anthropic's API during processing. For sensitive workflows, the author recommends enabling integrations only when needed and removing them afterward. The guide also covers multi-machine setup (OAuth tokens are per-machine, configuration JSON can sync via cloud folders) and common troubleshooting steps including expired Google auth, dropped WhatsApp sessions, and context limit management via `claude doctor`.

## Relevance to Economics Research

MCP integrations are directly useful for economics researchers who want to automate literature management (Zotero integration), coordinate with co-authors and RAs via email (Gmail), manage project timelines (Calendar), or build document-collection workflows for data gathering. The Google Workspace integration in particular enables automated email search and document management workflows that parallel the kind of systematic data collection common in empirical research projects.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/mcp-protocol]]
- [[concepts/ai-workflows]]
- [[concepts/data-privacy]]

## Related Summaries

- [[summaries/claude-code-newbies]]
- [[summaries/chatbot-essentials]]
- [[summaries/starter-templates]]
- [[summaries/my-claude-code-setup]]
