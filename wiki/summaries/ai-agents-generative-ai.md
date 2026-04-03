---
title: "AI Agents -- Generative AI for Economic Research"
tags: [summary, ai-agents, llms, reasoning-models, deep-research, coding-agents]
sources:
  - "[[raw/articles/AI Agents – Generative AI for Economic Research.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Anton Korinek (University of Virginia / Brookings), August 2025 update to the *Journal of Economic Literature* article "Generative AI for Economic Research"

- **Key Ideas**
  - Generative AI has evolved through three paradigms: (1) traditional LLMs (pattern-matching, System 1 thinking), (2) reasoning models (step-by-step System 2 thinking via reinforcement learning), and (3) agentic chatbots (autonomous tool use, planning, and execution).
  - Traditional LLM capabilities have become **commoditized** --- differentiation now occurs in reasoning and agentic capabilities.
  - Reasoning models (GPT-5, Grok-4, Gemini 2.5 Pro, Claude Opus 4.1) now approach or exceed PhD-level performance on scientific benchmarks (GPQA), and have achieved gold-medal performance at the International Mathematical Olympiad.
  - The basic agent architecture consists of an orchestrator passing prompts and tool lists to a reasoning LLM, which calls external tools (search, browser, code execution, APIs) in a Think-Act-Observe loop.
  - **Deep Research agents** use multi-agent architectures to search hundreds of internet sources and compile comprehensive reports in 5-30 minutes, but may confidently cite unreliable sources and sometimes fabricate data.
  - **Coding agents** (Claude Code, Codex CLI, Gemini CLI) enable "vibe coding" --- creating software from natural language prompts --- and also serve as powerful code reviewers for existing research codebases.
  - The article includes a complete working Python example: a FRED data retrieval agent that autonomously selects, fetches, and interprets economic data, plus a LangGraph version demonstrating graph-based agent architecture.
  - Premium AI subscriptions ($200-300/month) raise concerns about access inequality; open-source alternatives (DeepSeek, Qwen, Kimi-K2) offer near-frontier capabilities at dramatically lower cost.

- **Summary**

Korinek's comprehensive update traces the evolution of generative AI from traditional LLMs through reasoning models to agentic chatbots, mapping each paradigm's strengths onto the seven key research categories he identified in 2023 (ideation, writing, background research, coding, data analysis, math, and promotion). Traditional LLMs dominate language tasks; reasoning models excel at coding and math; agentic chatbots are best for tasks requiring external tool interaction and end-to-end workflows.

The article provides detailed coverage of the current AI landscape, including benchmark comparisons across leading labs (Google DeepMind, OpenAI, Anthropic, xAI, Meta, DeepSeek, Alibaba). It documents the rise of premium pricing tiers ($200+/month) alongside the democratizing force of open-source models like DeepSeek R1 and Kimi-K2 (100x cheaper per token than proprietary alternatives).

The technical sections are particularly valuable, providing both a clear conceptual framework (the orchestrator-reasoning engine-tools-memory architecture) and hands-on implementation. The FRED agent example demonstrates the Think-Act-Observe-Respond pattern in roughly 100 lines of Python, making agent internals concrete for economists. The LangGraph extension shows how to move from linear scripts to flexible graph-based architectures that support branching, parallel execution, and dynamic strategy adaptation.

Korinek concludes that while agents currently function best as research assistants requiring human supervision, the pace of improvement (task complexity doubling every seven months) suggests fully autonomous AI research assistants may be feasible soon. He cautions about brittleness, hallucination risks, and the importance of data security policies based on evidence rather than outdated assumptions.

- **Relevance to Economics Research**

This is the most authoritative and comprehensive academic treatment of AI agents for economists, published as an update to a *JEL* article. It provides the theoretical framework (three paradigms), practical guidance (which subscriptions to buy, how to handle data security), and hands-on code (FRED agent, LangGraph) that economics researchers need to understand and begin building agent-assisted workflows. The benchmark tables and lab comparisons offer a snapshot of the competitive landscape that informs tool selection decisions.

- **Related Concepts**
  - [[concepts/agentic-workflows]]
  - [[concepts/reasoning-models]]
  - [[concepts/deep-research]]
  - [[concepts/coding-agents]]
  - [[concepts/langgraph]]
  - [[concepts/model-context-protocol]]
  - [[concepts/ai-pricing-and-access]]

- **Related Summaries**
  - [[summaries/ai-agents-econ-research]]
  - [[summaries/claude-code-what-comes-next]]
  - [[summaries/learn-ai-coding-agents]]
  - [[summaries/agentic-everything]]
