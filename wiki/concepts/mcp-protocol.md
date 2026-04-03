---
title: "Model Context Protocol (MCP)"
tags: [concept, infrastructure, integrations, tools]
sources:
  - "[[wiki/summaries/mcp-setup.md]]"
  - "[[wiki/summaries/claude-code-what-comes-next.md]]"
  - "[[wiki/summaries/claude-code-newbies.md]]"
  - "[[wiki/summaries/learn-ai-coding-agents.md]]"
  - "[[wiki/summaries/workflows.md]]"
date_updated: 2026-04-03
---

## Definition

The **Model Context Protocol (MCP)** is a standard that lets AI agents connect to external services and tools. MCP servers extend Claude Code beyond local file operations, enabling it to search email, read and write Google Docs and Sheets, check calendars, query reference libraries (Zotero), access WhatsApp conversations, and interact with any service that implements the protocol. Ethan Mollick describes MCP as the standard that lets "any company give AI agents instructions and access to their products" -- scientific papers, financial data, software tools.

Without MCP, Claude Code can only work with files on the user's local filesystem. With MCP, it becomes a hub that can orchestrate across email, documents, calendars, reference managers, and potentially domain-specific data sources like WRDS or FRED. MCP configuration lives in `~/.claude.json` and specifies commands and credentials for each server.

## Context & Background

MCP emerged as the answer to a practical problem: agentic AI systems are only as useful as the data and services they can access. A coding agent confined to local files cannot help with email triage, literature management, or calendar coordination -- tasks that consume substantial researcher time. MCP provides a standardized way for third-party services to make themselves accessible to AI agents, analogous to how APIs standardized web service integration.

The protocol is part of what Mollick calls the "agentic harness" -- alongside compacting, skills, and sub-agents -- that enables Claude Code to sustain complex, multi-hour workflows. For researchers, MCP transforms Claude Code from a coding assistant into a general-purpose research assistant that can search literature (Zotero), coordinate with co-authors (Gmail, Calendar), manage project documents (Google Drive, Docs), and potentially access research databases.

## Key Perspectives

**Blattman (MCP Setup)** ([[wiki/summaries/mcp-setup.md]]) provides the definitive setup guide. Google Workspace is the highest-value integration but requires 45-60 minutes of OAuth credential setup through Google Cloud Console. The most common frustration is OAuth tokens expiring every 7 days; the fix is switching the Google Cloud project from "Testing" to "Production" mode. Key privacy concern: each MCP integration grants Claude access to the **entire** account for that service with no way to restrict scope. Blattman recommends enabling integrations only when needed and removing them afterward for sensitive workflows. Simpler integrations (Zotero, Apple apps) require only an API key and take about 10 minutes.

**Mollick** ([[wiki/summaries/claude-code-what-comes-next.md]]) places MCP within the broader conceptual architecture of agentic AI. MCP is one of four "magic tricks" that make sustained autonomous work possible (alongside compacting, skills, and sub-agents). The implication for researchers is that MCP could eventually enable agents to access WRDS, FRED, or other domain-specific data sources directly, collapsing the data retrieval step of the research pipeline.

**Blattman (Claude Code for Newbies)** ([[wiki/summaries/claude-code-newbies.md]]) positions MCP as the fourth step in the setup sequence: install Claude Code, optionally set up VS Code, create a CLAUDE.md file, then configure MCP integrations. This framing emphasizes that Claude Code works fully without MCP -- integrations can be added incrementally as needs arise.

**Mele** ([[wiki/summaries/learn-ai-coding-agents.md]]) notes that MCP is part of the broader agent infrastructure alongside skills and rules. The protocol enables the "tool" dimension of agents: while skills provide knowledge and rules provide configuration, MCP provides the ability to act on external systems.

**Blattman (Workflows)** ([[wiki/summaries/workflows.md]]) shows how MCP enables progressively more sophisticated workflows. The simplest workflow (Prompt/Plan/Review/Revise) needs no MCP. The Executive Assistant workflow (email triage, morning briefings, calendar queries) requires Google Workspace MCP. Project Management builds on the Executive Assistant, adding multi-project oversight. The pattern is that MCP unlocks workflow layers that cannot exist without external service access.

## Practical Implications

- **Start without MCP**: Claude Code is fully functional for local file work. Add integrations incrementally based on your biggest pain points.
- **Google Workspace first**: Gmail, Calendar, and Drive integrations provide the highest value for most researchers. Budget 45-60 minutes for initial setup.
- **Switch to Production mode**: The single most common MCP frustration is Google OAuth tokens expiring every 7 days. Switching your Google Cloud project to "Production" mode prevents this.
- **Manage privacy carefully**: Each MCP integration exposes the entire account to Claude, and content is sent to Anthropic's API during processing. For IRB-protected data or sensitive communications, enable integrations only when needed.
- **Zotero integration for literature**: Connecting Zotero to Claude Code enables automated literature searches, citation management, and bibliography construction -- high-value for active researchers.
- **Multi-machine considerations**: OAuth tokens are per-machine. The `~/.claude.json` configuration can sync via cloud folders, but credentials may need per-machine setup.

## Open Questions

- Will MCP servers emerge for academic data sources (WRDS, FRED, Census, BLS), and how would data licensing interact with AI agent access?
- How should universities handle the privacy implications of AI agents accessing institutional email and document systems?
- Can MCP scope be narrowed (e.g., granting access to specific email labels or Drive folders rather than entire accounts)?
- Will MCP become a cross-platform standard, or will different AI providers develop competing integration protocols?
- How will MCP interact with data governance requirements for IRB-protected research data?

## Sources

- [[wiki/summaries/mcp-setup.md]] -- Blattman's definitive MCP setup guide with troubleshooting
- [[wiki/summaries/claude-code-what-comes-next.md]] -- Mollick's explanation of MCP as part of the agentic harness
- [[wiki/summaries/claude-code-newbies.md]] -- MCP in the Claude Code setup sequence
- [[wiki/summaries/learn-ai-coding-agents.md]] -- MCP as part of the agent infrastructure
- [[wiki/summaries/workflows.md]] -- How MCP enables progressively more sophisticated workflows
