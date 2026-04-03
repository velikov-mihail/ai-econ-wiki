---
title: "Skill Library"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/articles/Skill Library - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/setup/skill-reference/)

## Key Ideas

- Skills (slash commands) are reusable markdown prompt files stored in `~/.claude/commands/` that require no code -- just saved prompts with shortcuts
- The library spans four workflow categories: First Session basics (`/done`, `/prompt`, `/review-plan`), Executive Assistant (`/morning-brief`, `/checkin`, `/triage-inbox`, `/schedule-query`, `/post-meeting`), Project Management (`/goals-review`, `/weekly-review`, `/proposal-write`, `/proposal-revise`, `/setup-project-management`), and Advanced self-improvement tools (`/tips-scout`, `/tips-curate`, `/tips-integrate`)
- Many skills depend on MCP (Model Context Protocol) integrations with Gmail, Google Calendar, and Granola for meeting transcripts
- The library also includes agents (subprocesses for writing and methodology review) and configuration templates (CLAUDE.md, goals, email policy, calendar policy, triage config)
- Skills accept arguments for customization (e.g., `/done quick`, `/checkin no-triage`, `/triage-inbox days:14`)

## Summary

This article is a comprehensive reference catalog of all publicly available skills (slash commands) and agents for the Claude Blattman system. Skills are markdown files that contain structured instructions Claude Code follows when invoked via `/skillname`. The library is organized into workflow categories: First Session skills for new users (`/done` for session capture, `/prompt` for formatting and executing natural language requests, `/review-plan` for stress-testing plans), Executive Assistant skills for daily productivity (`/morning-brief`, `/checkin`, `/triage-inbox`, `/schedule-query`, `/post-meeting`, `/todo-add`, `/todo-queue`, `/todo-review`), and Project Management skills for research workflows (`/goals-review`, `/weekly-review`, `/proposal-write`, `/proposal-revise`, `/setup-project-management`).

Each skill entry documents what it does, its MCP dependencies, installation commands (simple `curl` downloads), usage patterns with argument options, and customization points. The library demonstrates a tiered complexity model: simple skills like `/done` have no dependencies, while comprehensive skills like `/checkin` integrate multiple MCPs and reference several configuration files. The article also covers agents -- specialized subprocesses for writing review and methodology review that run in fresh context -- and templates for core configuration files that skills depend on.

The Advanced category includes a self-improvement pipeline (`/tips-scout`, `/tips-curate`, `/tips-integrate`) that systematically discovers, evaluates, and integrates new techniques into the system configuration -- a meta-workflow for making the AI system itself get better over time.

## Relevance to Economics Research

Several skills are directly relevant to academic economics workflows. The `/proposal-write` and `/proposal-revise` skills map onto grant writing, while `/weekly-review` and `/setup-project-management` support managing multi-year research projects with RAs. The review agents for writing and methodology could serve as pre-submission quality checks. The `/prompt` skill's ability to convert dictated natural language into structured prompts is valuable for researchers who think through problems verbally. The overall architecture -- modular, configuration-driven, incrementally improvable -- provides a template for building research-specific AI workflows.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/skills-vs-agents]]
- [[concepts/mcp-integrations]]
- [[concepts/ai-workflow-automation]]

## Related Summaries

- [[summaries/building-skills]]
- [[summaries/build-your-own]]
- [[summaries/continuous-improvement]]
- [[summaries/real-claude-md]]
- [[summaries/ai-research-feedback-skills]]
