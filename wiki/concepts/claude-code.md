---
title: "Claude Code"
tags: [concept, tools, claude-code, setup]
sources:
  - "[[summaries/claude-code-newbies.md]]"
  - "[[summaries/my-claude-code-setup.md]]"
  - "[[summaries/how-scientists-use-claude-code.md]]"
  - "[[summaries/claude-code-what-comes-next.md]]"
  - "[[summaries/claude-code-hacks.md]]"
  - "[[summaries/ai-agents-econ-research.md]]"
  - "[[summaries/cc-changed-how-i-work-3.md]]"
  - "[[summaries/cc-changed-how-i-work-4.md]]"
  - "[[summaries/cc-changed-how-i-work-5.md]]"
  - "[[summaries/cc-series-6-video-explainer.md]]"
  - "[[summaries/cc-series-7-beautiful-decks.md]]"
  - "[[summaries/cc-series-9-bib-files.md]]"
date_updated: 2026-04-05
---

## Definition

**Claude Code** is Anthropic's command-line agentic coding tool that runs in a terminal or inside a code editor (VS Code, Cursor). Unlike browser-based chatbots, Claude Code operates directly on the user's local filesystem -- reading, writing, and executing files -- and can integrate with external services via the [[concepts/mcp-protocol|Model Context Protocol]]. It is the primary tool discussed across the majority of sources in this wiki.

Claude Code is installed via `npm install -g @anthropic-ai/claude-code` and requires a paid Anthropic account (Claude Pro minimum). It operates in three modes: Default (proposes edits, user confirms), Plan Mode (explores without touching files), and Auto-Accept (applies edits autonomously). These modes can be cycled with Shift+Tab, giving the user fine-grained control over how much autonomy the AI has.

## Context & Background

Claude Code emerged as a qualitative leap beyond chatbot-era AI tools. Ethan Mollick explains that the capability jump was driven by two advances: models that are far better at autonomous self-correcting work (Opus 4.5/4.6), and an "agentic harness" of tools including compacting (structured note-taking when context fills), skills (on-demand specialized instruction sets), sub-agents (parallel isolated processes), and MCP (third-party integrations). METR data shows that the length of tasks AI can complete autonomously has been increasing exponentially.

As of February 2026, approximately 2.1% of scientists with ORCID-linked GitHub profiles use Claude Code, with economists and social scientists the highest adopters by field (up to 3.4%). Adoption follows a U-shaped curve by seniority: early-career and senior (post-tenure) scientists adopt at higher rates than mid-career researchers, likely reflecting higher risk aversion during the tenure-track period.

## Key Perspectives

**Blattman** ([[summaries/claude-code-newbies.md]]) provides the primary onboarding guide for non-technical users. He frames the terminal as the biggest hurdle and systematically addresses it, explaining the three operating modes and structuring setup as a five-step sequence: install Claude Code, optionally install VS Code, create a [[concepts/claude-md-files|CLAUDE.md]] file, and configure [[concepts/mcp-protocol|MCP integrations]]. The end result is an AI system with email, calendar, and document integrations that improves over time.

**Sant'Anna** ([[summaries/my-claude-code-setup.md]]) presents the most sophisticated academic setup: a "contractor mode" orchestrator with 10 specialized agents, an adversarial critic-fixer loop (5 rounds, hard role separation), 22 slash commands, and 18 context-aware rules. The template covers the full academic lifecycle (slides, papers, data analysis, replication packages) and has been adopted by 15+ research groups. This represents the ceiling of what a well-configured Claude Code environment can do.

**Yang** ([[summaries/how-scientists-use-claude-code.md]]) provides the only empirical measurement of adoption among scientists. The data shows that economists are the highest adopters, that adoption is still very early (significant first-mover advantage available), and that enterprise access remains a barrier AI labs have not cracked.

**Mollick** ([[summaries/claude-code-what-comes-next.md]]) provides the conceptual framework for non-programmers, explaining compacting, skills, sub-agents, and MCP as the "magic tricks" that make sustained autonomous work possible. His demonstration -- building a functional e-commerce website from a single prompt in 74 minutes -- illustrates the ceiling of autonomous capability.

**Van Horn** ([[summaries/claude-code-hacks.md]]) represents the power-user perspective: 4-6 parallel Claude Code sessions, voice input, bypass permissions, and audio notifications. His core principle -- "plan first, always" -- means every idea immediately becomes a plan.md file before any implementation begins.

**Panjwani** ([[summaries/ai-agents-econ-research.md]]) provides budget-conscious guidance for economists, noting that at $20/month Codex may be preferable to Claude Code, but at $200/month Claude Code's capabilities justify the investment since learning speed is proportional to usage.

## Practical Implications

- **Low barrier to entry**: Installation requires Node.js and a single npm command. No coding experience is required to use Claude Code productively.
- **Start in Plan Mode**: For newcomers, Plan Mode (Shift+Tab) is the safest way to explore -- it reads and proposes without changing anything.
- **Configure a CLAUDE.md**: Without persistent configuration, every session starts cold. A [[concepts/claude-md-files|CLAUDE.md file]] gives Claude context about your identity, projects, and preferences from the first interaction.
- **Build incrementally**: Start with the basic prompt-plan-review loop, add MCP integrations as needed, and build skills over time. Workflows compound.
- **Use Git**: Claude Code is dramatically more powerful with version control. Git provides safety (rollback), memory (commit history), and parallelism (worktrees).
- **Budget for usage**: Researchers who invest $200/month report learning curves that are qualitatively steeper than those at $20/month.

## Open Questions

- Will Claude Code remain the dominant agentic coding tool, or will Codex, Cursor, and others converge on similar capabilities?
- How should universities structure institutional access and token budgets for researchers and graduate students?
- What is the right balance between Auto-Accept mode (speed) and Default mode (oversight) for different research tasks?
- How will the 2.1% adoption rate among scientists evolve, and what will drive the transition from early adopters to mainstream?

## Sources

- [[summaries/claude-code-newbies.md]] -- Blattman's setup guide for non-technical users
- [[summaries/my-claude-code-setup.md]] -- Sant'Anna's comprehensive academic workflow template
- [[summaries/how-scientists-use-claude-code.md]] -- Yang's empirical adoption data
- [[summaries/claude-code-what-comes-next.md]] -- Mollick's explanation of the agentic harness
- [[summaries/claude-code-hacks.md]] -- Van Horn's power-user techniques
- [[summaries/ai-agents-econ-research.md]] -- Panjwani's practical guide for economists
