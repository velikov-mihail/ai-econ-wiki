---
title: "Agentic AI"
tags: [concept, ai-agents, automation]
sources:
  - "[[summaries/academics-wake-up-2.md]]"
  - "[[summaries/academics-wake-up.md]]"
  - "[[summaries/agents-vs-skills.md]]"
  - "[[summaries/ai-agents-econ-research.md]]"
  - "[[summaries/ai-agents-generative-ai.md]]"
  - "[[summaries/ai-normal-technology.md]]"
  - "[[summaries/cherny-code.md]]"
  - "[[summaries/claude-code-what-comes-next.md]]"
date_updated: 2026-04-03
---

# Agentic AI

Agentic AI refers to AI systems that operate with a degree of autonomy — planning their approach, executing multi-step tasks, using tools, and iterating on results without constant human direction. Unlike simple chatbot interactions, agentic systems can break down complex goals into subtasks, manage state across steps, and recover from errors.

## Context & Background

The shift from conversational AI to agentic AI represents a fundamental change in how researchers interact with AI tools. Rather than asking one question at a time, agentic systems can be given a high-level goal (e.g., "analyze this dataset and produce summary statistics") and autonomously determine the steps needed.

Key capabilities that define agentic AI include:

- **Planning**: Breaking complex tasks into ordered subtasks
- **Tool use**: Calling external APIs, reading files, running code
- **Iteration**: Reviewing own output and refining it
- **Memory**: Maintaining context across a multi-step workflow
- **Delegation**: Spawning sub-agents for parallel work (cowork-and-dispatch patterns)

## Key Perspectives

Several sources in this wiki explore agentic AI from different angles. The concept of "coding agents" — AI systems that can write, test, and debug code autonomously — is a practical manifestation that many economists encounter first through tools like Claude Code. Sub-agent architectures allow a primary agent to delegate specialized tasks (data collection, analysis, writing) to focused sub-processes.

The "agent debates" pattern, where multiple AI agents argue different positions, offers a way to stress-test research ideas and reduce the risk of AI sycophancy.

## Practical Implications

For economists and social scientists:

- **Research automation**: Agentic systems can handle multi-step data pipelines end-to-end
- **Quality through iteration**: Agents that review their own work catch errors that single-pass generation misses
- **Supervision remains critical**: Autonomy does not mean correctness — researchers must verify agent outputs, especially for empirical claims
- **Cost awareness**: Agentic workflows consume more tokens than simple prompts due to multi-step reasoning

## Related Concepts

- [[concepts/agentic-workflows|Agentic Workflows]]
- [[concepts/skills-vs-agents|Skills Vs Agents]]
- [[concepts/ai-agents|Ai Agents]]
- [[concepts/human-in-the-loop|Human In The Loop]]
