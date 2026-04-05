---
title: "Agentic Workflows"
tags: [concept, ai-agents, workflows, automation]
sources:
  - "[[summaries/agentic-everything.md]]"
  - "[[summaries/ai-agents-econ-research.md]]"
  - "[[summaries/claude-code-what-comes-next.md]]"
  - "[[summaries/agents-vs-skills.md]]"
  - "[[summaries/how-scientists-use-claude-code.md]]"
  - "[[summaries/learn-ai-coding-agents.md]]"
  - "[[summaries/cc-changed-how-i-work-3.md]]"
  - "[[summaries/cc-changed-how-i-work-4.md]]"
  - "[[summaries/cc-series-6-video-explainer.md]]"
date_updated: 2026-04-05
---

## Definition

An **agentic workflow** is one in which an AI model runs tools in a loop to achieve a goal, autonomously planning steps, executing them, evaluating results, and iterating until the task is complete. This contrasts with traditional chatbot interactions where the human drives each step. Simon Willison's widely cited definition captures the core idea: an agent is an LLM that runs tools in a loop to achieve a goal. In practice, agentic workflows involve the AI reading files, writing code, running tests, spawning sub-agents for parallel work, and self-correcting errors -- often running autonomously for 25-30 minutes or longer at a stretch.

The shift from chat-based AI to agentic AI is qualitative, not merely quantitative. Where a chatbot assists with individual steps, an agentic system can own an entire task end-to-end: planning the approach, executing each stage, testing outputs, and delegating subtasks to specialized sub-agents. This changes the researcher's role from operator to supervisor.

## Context & Background

November 2025 marked what Teddy Svoronos calls the start of a "categorically different thing" -- agents that work with local files, calendars, and metadata, map out multi-step plans, and spawn sub-agents for complex decisions. The METR benchmarks tracked by Ethan Mollick show that the length of tasks AI can complete autonomously at 50% reliability has been increasing exponentially, with large leaps in recent months. Tools like Claude Code, Codex CLI, and Claude Cowork represent this new generation.

For economics researchers, the agentic paradigm changes the production function of research. Tasks that previously required hours of hands-on coding -- data cleaning, robustness checks, literature searches, formatting -- can now be delegated to agents. But this delegation requires its own skill set: knowing how to decompose tasks, write effective plans, review agent output, and intervene when things go wrong. As multiple sources emphasize, domain expertise becomes *more* important in the agentic era, not less.

## Key Perspectives

**Svoronos** ([[summaries/agentic-everything.md]]) frames the shift through a teaching lens. He describes feeling like he is "supervising a fleet of researchers" and argues that using agentic tools is a separate, practice-intensive skill distinct from domain expertise. He advocates teaching the two as separate units rather than interleaving them.

**Panjwani** ([[summaries/ai-agents-econ-research.md]]) provides the most practical guidance for economists. He identifies three beginner mistakes: not using Git (which makes agents 10x more powerful via safe rollback and project memory), underutilizing skills (reusable instruction sets for domain-specific tasks), and not planning before implementation (which causes context window degradation). He recommends separating planning and execution into distinct sessions.

**Mollick** ([[summaries/claude-code-what-comes-next.md]]) explains the technical architecture that makes agentic workflows possible: compacting (structured notes when context fills), skills (on-demand specialized instruction sets), sub-agents (parallel isolated processes), and MCP (third-party tool integration). Together, these create a system where a generalist AI can apply specialized knowledge and sustain work across hours.

**Blattman** ([[summaries/agents-vs-skills.md]]) distinguishes between skills (which share the main conversation context) and agents (which run in isolated sub-processes). The key insight is the **self-bias problem**: an agent reviewing its own work in the same conversation systematically finds its output acceptable. Fresh-context agents provide genuinely independent critique, analogous to external peer review.

**Mele** ([[summaries/learn-ai-coding-agents.md]]) clarifies the configuration hierarchy: skills add knowledge (like a recipe book), sub-agents parallelize work (like hiring a contractor). The full priority stack runs from organization policies through user CLAUDE.md, project AGENTS.md, task-level skills, to the immediate prompt.

## Practical Implications

- **Start with Git**: Agentic workflows are dramatically safer and more powerful with version control. Git provides rollback, project memory via commit history, and worktrees for parallel agent sessions.
- **Separate planning from execution**: Write a plan to a file, review it, then start a fresh session for implementation. This preserves context window quality and forces deliberation before action.
- **Use sub-agents for review**: Never have the same session review its own output. Spin up fresh-context agents for critique to avoid self-bias.
- **Build reusable skills**: Domain-specific instruction sets (e.g., `/data-analysis`, `/review-paper`) encode your conventions and can be shared across projects and collaborators.
- **Invest in learning the toolchain**: Directing agents effectively is a distinct skill from domain expertise. Budget dedicated practice time.

## Open Questions

- How should tenure and promotion committees evaluate research produced with heavy agentic assistance?
- What is the optimal level of agent autonomy for different research tasks (data cleaning vs. identification strategy)?
- As agents improve, which research tasks will remain resistant to delegation?
- How do we train PhD students to be effective agent supervisors without atrophying their foundational skills?
- What institutional infrastructure (enterprise agreements, data privacy frameworks) do universities need for responsible adoption?

## Sources

- [[summaries/agentic-everything.md]] -- Svoronos on the qualitative leap to agentic AI and pedagogical implications
- [[summaries/ai-agents-econ-research.md]] -- Panjwani's practical guide for economists starting with agentic coding
- [[summaries/claude-code-what-comes-next.md]] -- Mollick on the technical architecture enabling agentic workflows
- [[summaries/agents-vs-skills.md]] -- Blattman on skills vs. agents and the self-bias problem
- [[summaries/how-scientists-use-claude-code.md]] -- Yang's empirical data on scientist adoption of Claude Code
- [[summaries/learn-ai-coding-agents.md]] -- Mele's guide to skills, rules, and configuration hierarchy
