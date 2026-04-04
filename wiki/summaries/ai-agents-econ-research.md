---
title: "AI Agents for Economic Research (VoxDev Webinar)"
tags: [summary, ai-agents, agentic-coding, economists, skills]
sources:
  - "[[raw/articles/AI Agents for Economic Research.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---

- **Author/Source**: Aniket Panjwani (economist, PhD Northwestern; Director of AI/ML at PaySlice), presented via VoxDev webinar (2026-03-12)
- **Original**: [https://www.youtube.com/watch?v=YPv9BqweQIo](https://www.youtube.com/watch?v=YPv9BqweQIo)

- **Key Ideas**
  - Agentic coding is not just for software engineers --- development economists, theorists, and applied researchers can all benefit immediately.
  - For budget-constrained researchers ($20/month), Codex (OpenAI) is recommended over Claude Code due to better model performance (GPT 5.4), more generous usage limits, and a friendlier desktop app.
  - **Practical first exercise**: use a coding agent to clean up, refactor, and reorganize existing messy project directories, with Git for safety and rollback.
  - Three beginner mistakes: (1) not using Git (it provides safety, memory, and worktrees for parallel work); (2) underutilizing skills (reusable instruction sets like Pedro Santana's `review-paper` and `data-analysis` skills); (3) not planning before implementation (separate planning and execution sessions to protect context windows).
  - Skills are "saved playbooks" that let agents perform domain-specific tasks (e.g., paper review, data analysis, grant writing) using your preferred conventions.
  - The economics job market declined 31% year-over-year; learning agentic tools is framed as essential for future employability.

- **Summary**

Panjwani delivers a practical, opinionated guide for economists getting started with agentic coding tools. He opens by documenting rapid adoption among economists (Paul Novasad writing a paper in 3 hours, Chris Blattman's workflow transformation in four weeks, Terrence Tao's observations on AI solving open math problems) to argue that even theorists should engage with these tools. He then gives concrete setup instructions: choose Codex or Claude Code, install Git, create a GitHub account, and configure your tool to work with Stata or R.

The bulk of the talk covers three beginner mistakes. First, not using Git --- Panjwani argues Git makes agents 10x more powerful by enabling safe rollback, providing the agent with project memory via commit history, and enabling worktrees for parallel agent sessions. Second, underutilizing skills --- he walks through real economist-made skills (paper review, data analysis, proposal writing) and emphasizes that skills are easy to create and customize. Third, not making plans --- long unstructured sessions degrade agent performance as context windows fill; writing a plan to a file and starting a fresh session for execution preserves quality.

He concludes with advice on learning (follow AI-economist accounts on X, not Bluesky), budget allocation (push toward $200/month if possible since learning speed is proportional to usage), and data privacy strategies (mock data, anonymization, local models, enterprise agreements).

- **Relevance to Economics Research**

This is the most directly actionable resource for economists starting with agentic coding. It addresses the specific tools, budget constraints, and workflow patterns relevant to empirical economic research (Stata projects, messy code directories, co-author collaboration via Dropbox, data privacy with IRB-protected data). The emphasis on Git integration and skills as reusable playbooks provides a concrete framework for building reproducible, agent-assisted research workflows.

- **Related Concepts**
  - [[concepts/agentic-workflows]]
  - [[concepts/claude-code]]
  - [[concepts/skills-vs-agents]]
  - [[concepts/version-control-research]]
  - [[concepts/agentic-ai]]

- **Related Summaries**
  - [[summaries/agents-vs-skills]]
  - [[summaries/learn-ai-coding-agents]]
  - [[summaries/agentic-everything]]
  - [[summaries/claude-code-what-comes-next]]
