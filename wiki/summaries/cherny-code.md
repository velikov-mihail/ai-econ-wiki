---
title: 'ChernyCode: Boris Cherny''s Productivity Tips for AI-Assisted Coding'
tags:
- summary
- claude-code-skills
- claude-code
- cursor
- productivity
- skills
- agents
- best-practices
sources:
- '[[raw/articles/meleantonioChernyCode.md]]'
date_updated: 2026-04-03
date_published: 2026-02-11
---

- **Original**: [https://github.com/meleantonio/ChernyCode](https://github.com/meleantonio/ChernyCode)


**Author/Source**: Antonio Mele (GitHub: meleantonio), synthesizing recommendations from Boris Cherny (creator of Claude Code). Repository: meleantonio/ChernyCode.

## Key Ideas

- This template repository packages Boris Cherny's productivity recommendations for Claude Code and Cursor into ready-to-use configuration files, including memory files (CLAUDE.md/AGENTS.md), reusable skills, and specialist subagents.
- **Memory files** (CLAUDE.md) provide persistent context across sessions at three levels: project-level (shared via git), personal (~/.claude/CLAUDE.md for preferences across all projects), and local (gitignored per-project overrides). The key practice is to update CLAUDE.md after every correction so Claude learns from mistakes.
- **Skills** are reusable workflows invoked with slash commands (/commit-push-pr, /techdebt, /code-simplifier, etc.) -- any task done more than once a day should become a skill.
- **Subagents** run in their own context windows for parallel execution and context isolation: code-reviewer (read-only), test-writer, doc-generator, and verifier (fast model).
- Cherny's top tips: (1) start in plan mode for complex tasks, (2) work in parallel using git worktrees with 3-5 simultaneous sessions, (3) create skills for repeated workflows, (4) give Claude verification methods (tests, linters, git diff), (5) continuously update CLAUDE.md, (6) use voice dictation for faster, more detailed prompts.

## Summary

ChernyCode is a template repository created by Antonio Mele that packages the productivity recommendations of Boris Cherny, the creator of Claude Code, into installable configuration files for both Claude Code and Cursor. The repository synthesizes advice from Cherny's public threads on how the Claude Code team itself uses the tool, translating high-level tips into concrete files: CLAUDE.md templates for project memory, skill definitions for common workflows, and subagent definitions for specialized tasks.

The repository is organized around three core concepts. Memory files (CLAUDE.md for Claude Code, AGENTS.md for Cursor) provide persistent context that the AI reads at the start of every session. The recommended practice of updating these files after every correction -- "Update CLAUDE.md so you don't make that mistake again" -- creates a feedback loop where Claude's error rate measurably drops over time. Skills are reusable workflow definitions stored in ~/.claude/skills/ and invoked via slash commands; the repository includes skills for committing and creating PRs, finding technical debt, simplifying code, enforcing code style, and managing git workflows. Subagents are specialist agents that run in their own context windows, enabling parallel execution (e.g., a code reviewer running alongside a test writer) without consuming the main session's context budget.

Cherny's six top-level tips form the conceptual backbone. Starting in plan mode (Shift+Tab twice in Claude Code) for complex tasks ensures that the AI develops a thorough approach before writing code. Working in parallel via git worktrees with 3-5 simultaneous Claude sessions maximizes throughput. Giving Claude verification methods (running tests, checking linter output, reviewing git diff) ensures quality. Using voice dictation (fn-fn on macOS) produces prompts that are 3x faster to create and tend to be more detailed than typed prompts.

## Relevance to Economics Research

While primarily aimed at software engineering workflows, ChernyCode's patterns are directly transferable to research coding. The CLAUDE.md memory file concept is valuable for encoding project-specific conventions (variable naming, data sources, coding standards) that persist across sessions. Skills can encode common research workflows (data download, portfolio construction, regression pipelines). The emphasis on plan mode and verification methods addresses a key concern for researchers: ensuring that AI-generated code produces correct results. The parallel worktree approach is relevant for researchers juggling multiple projects or running sensitivity analyses simultaneously.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/skills-vs-agents]]
- [[concepts/claude-md-files]]
- [[concepts/plan-driven-development]]
- [[concepts/agentic-ai]]
- [[concepts/prompt-engineering]]

## Related Summaries

- [[summaries/claude-code-skills]]
- [[summaries/getting-started-economists]]
- [[summaries/your-claude-md]]
