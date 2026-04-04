---
title: "Agents vs Skills"
tags: [summary, ai-agents, skills, claude-code, self-bias]
sources:
  - "[[raw/articles/Agents vs Skills - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
date_published: 2026-03
---

- **Author/Source**: Chris Blattman (University of Chicago, Harris School of Public Policy), via claudeblattman.com
- **Original**: [https://claudeblattman.com/system/agents-vs-skills/](https://claudeblattman.com/system/agents-vs-skills/)

- **Key Ideas**
  - Claude Code has two building blocks: **skills** (slash commands running in the main conversation with full history) and **agents** (subprocesses running in a fresh, isolated context).
  - Skills are best for tasks needing conversation context, user interaction, multi-step workflows with checkpoints, or state modification (writing files, sending emails).
  - Agents are best for tasks benefiting from fresh perspective (review/critique), parallel evaluations, context isolation, and clear input/output boundaries.
  - The **self-bias problem** is the most important reason to use agents for review: when Claude reviews its own work in the same conversation, it systematically finds its own output acceptable because it "knows what it meant."
  - **Agent debates** are a powerful pattern: assign agents distinct identities (methodological traditions, named colleagues, opposing stakeholders) and let disagreements surface unexamined assumptions.
  - Practical example: Blattman set up agents impersonating three behavioral economists (Imas, Bursztyn, Thaler) to debate a study design, generating nine new measures none of which were in the original design.

- **Summary**

Blattman provides a concise decision framework for when to use skills versus agents in Claude Code. Skills run in the main conversation, sharing full context and enabling interactive workflows --- ideal for multi-step processes where user decisions are needed at each stage. Agents run in isolated subprocesses with fresh context, making them ideal for review and critique tasks where prior conversation creates blind spots.

The article's most compelling contribution is the agent debate pattern, illustrated with two research examples. In one, two agents with different qualitative research traditions (grounded theory vs. thematic analysis) analyzed pilot field data from a Bogota study, flagging contradictions between survey numbers and student memos in twenty minutes. In another, three agents impersonating named behavioral economists each reframed the same study data as a fundamentally different paper --- one about reference points, one about revealed preference, one about choice architecture. The value lies not in any single perspective but in where they clash, surfacing assumptions the researchers had not examined.

- **Relevance to Economics Research**

This article is directly relevant to economics researchers using Claude Code for paper writing, study design, and data analysis. The self-bias problem is particularly important: any economist who uses AI to draft analysis and then asks the same session to review it is getting a systematically biased assessment. The agent debate pattern offers a practical method for stress-testing research designs, analogous to presenting at a seminar but available on demand. The skill vs. agent distinction also has implications for how economists structure their coding workflows --- using skills for interactive data analysis and agents for parallel code review.

- **Related Concepts**
  - [[concepts/skills-vs-agents]]
  - [[concepts/agentic-workflows]]
  - [[concepts/claude-code]]
  - [[concepts/sycophancy-and-bias]]
  - [[concepts/agentic-ai]]

- **Related Summaries**
  - [[summaries/learn-ai-coding-agents]]
  - [[summaries/ai-agents-econ-research]]
  - [[summaries/claude-code-what-comes-next]]
  - [[summaries/agentic-everything]]
