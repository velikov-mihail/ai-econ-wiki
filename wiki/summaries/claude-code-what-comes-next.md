---
title: "Claude Code and What Comes Next"
tags: [summary, claude-code, ai-agents, skills, subagents, agentic-workflows]
sources:
  - "[[raw/articles/Claude Code and What Comes Next.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Ethan Mollick (Wharton School, University of Pennsylvania), via One Useful Thing Substack (2026-01-07)
- **Original**: [https://www.oneusefulthing.org/p/claude-code-and-what-comes-next](https://www.oneusefulthing.org/p/claude-code-and-what-comes-next)

- **Key Ideas**
  - Claude Code, powered by Opus 4.5, represents a sudden capability leap driven by two advances: models that are far better at autonomous self-correcting work, and an "agentic harness" of tools and approaches.
  - METR tracks that the length of tasks AI can complete autonomously (at 50% reliability) has been increasing exponentially, with large leaps in recent months.
  - **Compacting**: when Claude Code's context window fills, it stops, takes notes on its progress, clears its context, and the fresh instance reads those notes to continue --- like the protagonist of *Memento* reading his tattoos.
  - **Skills**: instruction sets the AI decides when to load, containing not just prompts but the tools needed for a task. Analogized to Neo in *The Matrix* uploading kung fu --- the AI acquires specialized capabilities on demand.
  - **Subagents**: Claude Code can launch specialized AI instances to handle subtasks, enabling delegation to cheaper/faster models, parallel processing, and specialized contexts (e.g., separate research and image-creation agents).
  - **Model Context Protocol (MCP)**: a standard that lets any company give AI agents instructions and access to their products (scientific papers, financial data, software tools).
  - Mollick built a working startup website (selling prompt packs for $39) with a single prompt; Claude Code worked autonomously for 74 minutes, producing hundreds of code files and a deployable site.

- **Summary**

Mollick provides an accessible overview of Claude Code for non-programmers, explaining why these new coding agents represent more than incremental improvement. The article opens with a striking demonstration: a single prompt instructing Claude Code to "develop a startup that will make me $1000 a month" resulted in 74 minutes of autonomous work producing a fully functional, deployed e-commerce website. Mollick emphasizes that this touched only a fraction of the tool's capabilities --- he then had Claude Code do user testing by controlling his web browser, scrolling through the site like a human would.

The core of the article explains the "magic tricks" in Claude Code's agentic harness. Compacting solves the context window limitation by having the AI take structured notes before clearing its memory. Skills solve the prompt management problem by letting the AI load specialized instruction sets on demand, choosing when each is relevant. Subagents enable parallel work and specialization. MCP enables third-party tool integration. Together, these create a system where a smart generalist AI can apply specialized knowledge, use diverse tools, and sustain work across hours.

Mollick concludes with practical guidance for non-programmers: Claude Desktop now offers an easier interface, and he encourages experimentation with everything from data visualization to game development ("vibe coding"). He flags that while these tools are currently built for programmers, new harnesses for other knowledge tasks are coming soon, and the resulting changes will be significant.

- **Relevance to Economics Research**

Mollick's explanation of the agentic harness (compacting, skills, subagents, MCP) provides the conceptual foundation economists need to understand *why* coding agents can now sustain complex, multi-hour research workflows. The practical implication is clear: economists can use these tools for end-to-end tasks --- data retrieval, analysis, visualization, report writing --- without touching code, as long as they understand how to direct the agent. The MCP concept is particularly relevant for researchers who want agents to access WRDS, FRED, or other domain-specific data sources.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/agentic-workflows]]
  - [[concepts/skills-vs-agents]]
  - [[concepts/agentic-ai]]
  - [[concepts/mcp-protocol]]
  - [[concepts/context-management]]

- **Related Summaries**
  - [[summaries/claude-dispatch]]
  - [[summaries/agentic-everything]]
  - [[summaries/ai-agents-generative-ai]]
  - [[summaries/how-scientists-use-claude-code]]
