---
title: "OpenAI Codex Full Course (4 Hours): Build & Ship"
tags: [summary, foundations-setup, codex, full-stack, course]
sources:
  - "[[raw/articles/OpenAI Codex Full Course 4 Hours Build & Ship.md]]"
date_updated: 2026-05-15
date_published: 2026-05-02
---

- **Author/Source**: Aniket Panjwani (Director of AI/ML at Paylice; teaches AI MBA Pro)
- **Original**: [https://www.youtube.com/watch?v=j7d5rs0iMlE](https://www.youtube.com/watch?v=j7d5rs0iMlE)

- **Key Ideas**
  - 4-hour video course covering Codex from first install through deploying a full-blown web app. Aimed at non-technical users — "no coding background required."
  - Panjwani's headline recommendation: "regardless of budget — $20, $100, or $200 — your first agentic-coding subscription should be ChatGPT, which gets you access to Codex." Justification: "Codex is the best model. It has the best usage limits and the best interface for agentic coding."
  - Focus is the **Codex desktop application** specifically, not the CLI or VS Code extension — "the best interface for agentic coding, but nobody has put out materials that teach people how to use it yet." The desktop app supports parallel Codex agents on different parts of a project and background automations on a timer.
  - **Five practical primitives of agentic coding**: command-line interfaces, skills, MCPs, plugins, sub-agents. Course structure walks through each in turn.
  - **Computer Use plugin**: lets Codex control every application on the user's computer.
  - **Cloud delegation** + **GitHub Issues** + **automations** combine into a "run on a timer in the cloud" workflow — e.g., every few hours check for new bugs and start drafting solutions to simple ones automatically.
  - Web app build uses Next.js (front-end), Convex (backend), Vercel (hosting). Introduces **git worktrees** as a way to parallelize work across an entire repo (not just within one repo, like subagents).
  - Final build: a "Creator Carousel Studio" — a social-media content automation. The point of the build is the methodology (simpler hands-on workflows vs. more automated hands-off workflows), not the specific app.

- **Summary**

Panjwani's stated philosophy is "little bits of theory, then immediately to practice." The course front-loads installation and basic agentic patterns (context windows, compaction, voice input, permissions, terminals, `AGENTS.md`) before pushing into the five primitives. The middle third explores skills and MCPs as alternatives for connecting to external systems, plus subagents for parallel work. The final third bridges from local automations to cloud delegation, GitHub Issues as a project-management substrate, scheduled automations, git worktrees, and a full-stack app build.

The course is notable for being one of the few public Codex-specific full-stack walkthroughs aimed at non-engineers, and for explicitly recommending the Codex *desktop app* over the CLI for newcomers. Panjwani's strong "Codex first" stance is the major contested claim — most academic Claude Code advocates (e.g., Cunningham, Goldsmith-Pinkham, Blattman, Spina) recommend the opposite default. Panjwani's framing centers usage limits and the desktop interface; the academic Claude Code advocates emphasize model quality on long-context document work.

- **Relevance to Economics Research**

For economists evaluating Codex against Claude Code, this is the most comprehensive Codex-side advocacy piece currently public. The strongest transferable pieces are: (1) the five-primitives taxonomy (CLI/skills/MCPs/plugins/subagents), which provides a cleaner mental map of agentic coding than most ecosystem-specific tutorials; (2) cloud delegation via GitHub Issues + automations, which generalizes to any periodic empirical task (re-run robustness checks, monitor data freshness, draft response letters); and (3) git worktrees, which solve a real pain point for any economist iterating on multiple branches of a paper (alternative specifications, referee response drafts) without context-switching the entire repo. The full-stack web-app section is mostly not relevant to economics research but useful background for teaching.

- **Related Concepts**
  - [[concepts/ai-tools-landscape]]
  - [[concepts/agentic-workflows]]
  - [[concepts/claude-code-skills]]
  - [[concepts/mcp-protocol]]

- **Related Summaries**
  - [[summaries/codex-101-bilal]]
  - [[summaries/codex-102-bilal]]
  - [[summaries/ars-codex]]
  - [[summaries/ai-agents-econ-research]]
