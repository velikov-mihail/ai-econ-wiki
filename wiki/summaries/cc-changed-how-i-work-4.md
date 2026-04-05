---
title: "Claude Code Changed How I Work (Part 4): Boris Cherny, Claude Code's Origin, and Latent Knowledge"
tags: [summary, claude-code-skills, latent-knowledge, polanyi-paradox, ai-history, agentic-ai]
sources:
  - "[[raw/articles/How Claude Code Has Changed My Work (Part 4-ish) More about Claude Code, its Creator, and Latent Knowledge.md]]"
date_updated: 2026-04-05
date_published: 2026-01-11
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/how-claude-code-has-changed-my-work](https://causalinf.substack.com/p/how-claude-code-has-changed-my-work)

- **Key Ideas**
  - Boris Cherny, an economics major from UCSD turned principal engineer at Meta, created Claude Code as a side project after joining Anthropic in September 2024.
  - The key discovery: when Cherny gave Claude access to the filesystem and bash, Claude immediately knew how to navigate codebases -- opening files, following imports, tracing dependencies -- without being programmed to do so.
  - This emergent capability reflects David Autor's framework and the Polanyi paradox: LLMs access latent knowledge embedded in human output that humans themselves cannot articulate.
  - LLMs are bad at algorithmic tasks (precise recall, deterministic steps) but good at extracting inchoate meaning from massive corpora -- code contains not just syntax but the tacit knowledge of how programmers actually work on projects.
  - Claude Code is categorically different from chatbots (ChatGPT) and autocomplete tools (GitHub Copilot, Cursor) because it acts on the filesystem autonomously.

- **Summary**

Cunningham traces the origin story of Claude Code. Boris Cherny, who studied economics at UCSD and taught himself programming, spent eight years at Meta as a principal engineer before joining Anthropic in September 2024 -- not to build Claude Code, but to work on the chatbot. As a habitual side-project builder, Cherny created a terminal tool connecting to the Claude API. After a conversation with PM Cat Wu about AI agents, he gave Claude access to the filesystem and bash. The result surprised him: Claude immediately began autonomously navigating codebases, following imports, and understanding project structure without any explicit programming.

Cunningham connects this to David Autor's work on computerization and the Polanyi paradox ("we know more than we can tell"). Traditional computers excel at algorithmic tasks that can be specified as step-by-step instructions. LLMs invert this: they are poor at algorithms (hence hallucinations and arithmetic errors) but excel at extracting latent, tacit knowledge from human output. Because Claude was trained on billions of lines of code in context -- tutorials, Stack Overflow, GitHub repositories with full histories -- it absorbed not just syntax but the implicit knowledge of how programmers work on projects. Code is never the goal; the project is the goal, and Claude has reviewed the projects.

- **Relevance to Economics Research**

The Autor/Polanyi framework is directly from labor economics and provides the theoretical grounding for understanding why LLMs are transformative for project-based empirical work. The distinction between algorithmic tasks (where computers always dominated) and tacit-knowledge tasks (where LLMs now compete) maps onto the social scientist's workflow: data cleaning scripts are algorithmic, but the judgment calls in building a research project are tacit. Understanding this distinction helps researchers calibrate expectations for when AI will help versus hallucinate.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/jagged-frontier]]
  - [[concepts/agentic-workflows]]
  - [[concepts/human-ai-collaboration]]
  - [[concepts/ai-adoption-academia]]
  - [[concepts/hard-vs-easy-tasks]]

- **Related Summaries**
  - [[summaries/cc-changed-how-i-work-1]]
  - [[summaries/cc-changed-how-i-work-2]]
  - [[summaries/cc-changed-how-i-work-3]]
  - [[summaries/cc-changed-how-i-work-5]]
  - [[summaries/cherny-code]]
