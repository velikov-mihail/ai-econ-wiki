---
title: "AI Agents"
tags: [concept, ai-agents, tools]
sources:
  - "[[summaries/automated-research-finance.md]]"
  - "[[summaries/baylor-ai-taskforce.md]]"
  - "[[summaries/claude-code-hacks.md]]"
  - "[[summaries/guide-which-ai.md]]"
  - "[[summaries/llm-collaboration.md]]"
  - "[[summaries/my-claude-code-setup.md]]"
  - "[[summaries/panjwani-slides.md]]"
  - "[[summaries/project-ape.md]]"
date_updated: 2026-04-03
---

# AI Agents

AI agents are software systems built on top of large language models that can perceive their environment (read files, access APIs), reason about what to do, and take actions (write code, run commands, query databases). They go beyond simple prompt-response interactions by maintaining goals and state across multiple steps.

## Context & Background

The distinction between a chatbot and an agent is primarily about action. A chatbot answers questions; an agent accomplishes tasks. In the research context, AI agents can autonomously navigate codebases, run statistical analyses, scrape websites, and compile results — all guided by natural language instructions.

Major frameworks and tools for building research agents include Claude Code (Anthropic), Cursor (IDE-integrated), ChatGPT with code interpreter, and open-source frameworks like LangGraph. Each offers different trade-offs between autonomy, cost, and control.

## Key Perspectives

The economics research community has rapidly adopted AI agents for tasks ranging from data collection to paper writing. VoxDev's coverage of AI agents for economic research highlights their potential to democratize research capabilities, while also raising concerns about quality control and reproducibility.

## Practical Implications

- **Start with bounded tasks**: Give agents well-defined goals with clear success criteria
- **Use plan-driven approaches**: Have the agent outline its plan before executing
- **Verify empirical outputs**: Never trust agent-generated statistics without checking
- **Version control everything**: Agents should work within git repositories so changes are trackable
- **Understand costs**: Agent workflows involve many LLM calls; monitor token usage

## Related Concepts

- [[concepts/agentic-ai|Agentic Ai]]
- [[concepts/agentic-workflows|Agentic Workflows]]
- [[concepts/skills-vs-agents|Skills Vs Agents]]
- [[concepts/claude-code|Claude Code]]
