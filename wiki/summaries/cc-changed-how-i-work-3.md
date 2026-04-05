---
title: "Claude Code Changed How I Work (Part 3): Creating Devil’s Advocate Agents"
tags: [summary, claude-code-skills, ai-agents, adversarial-review, debugging, sub-agents]
sources:
  - "[[raw/articles/Claude Code Changes How I work (Part 3) Creating Devil's Advocate Agents for Tough Problems.md]]"
date_updated: 2026-04-05
date_published: 2026-01-01
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-changes-how-i-work-part](https://causalinf.substack.com/p/claude-code-changes-how-i-work-part)

- **Key Ideas**
  - When Claude Code is confident and the problem is complex, spawning a second agent as a "devil's advocate" catches vulnerabilities that the primary agent misses.
  - The devil's advocate protocol: one agent proposes a solution, a second agent systematically challenges it in "good faith," and the first agent responds honestly -- iterated ten times.
  - Of ten failure modes the devil's advocate identified in a web-scraping coordination system, five were real vulnerabilities (no disk sync, silent failures, race conditions, overly broad exception handling, unprotected output files).
  - Claude Code's overconfidence is a feature (speed) and a bug (treats symptoms, misses deeper issues). Structured self-argument is the user's tool for slowing it down.
  - Working with AI agents is "relational coding" -- building a working dynamic through trial and error -- not prompt engineering in the "find the magic words" sense.

- **Summary**

Cunningham describes a web-scraping project (academic genealogy data) where ten parallel worker bots coordinated via a shared queue. After six hours of silent failure, Claude Code diagnosed the problem as an aggressive timeout setting and fixed it quickly. Cunningham was suspicious of the speed and confidence of the fix, so he asked Claude Code to spawn a second agent -- a "devil's advocate" -- whose job was to challenge the proposed solution systematically and in good faith.

The devil's advocate identified ten potential failure modes. The primary Claude Code agent dismissed five as inapplicable or low-priority, but acknowledged five as genuine vulnerabilities: no data sync after writes (crash could corrupt the queue), silent failures with no error logging, race conditions on startup when multiple workers initialized simultaneously, overly broad exception handling that swallowed serious errors, and no file locking on output files. Without the adversarial protocol, only the timeout bug would have been fixed, leaving five latent problems.

Cunningham draws four lessons: Claude Code's best debugger is often itself, but the conversation must be structured; framing matters ("good faith" produced useful challenges rather than pedantic objections); this is relational coding, not prompt engineering; and when you find a workflow that catches bugs, document it in the project README for future sessions.

- **Relevance to Economics Research**

Directly relevant to any researcher running complex automated pipelines (web scraping, parallel computation, simulation). The devil's advocate pattern is a practical technique for quality-assuring AI-generated code in contexts where silent failures can waste hours or corrupt data. The emphasis on documenting workflow patterns in project files parallels best practices in reproducible research.

- **Related Concepts**
  - [[concepts/claude-code]]
  - [[concepts/agentic-workflows]]
  - [[concepts/claude-code-skills]]
  - [[concepts/human-ai-collaboration]]
  - [[concepts/ai-limitations]]
  - [[concepts/web-scraping]]
  - [[concepts/cognitive-load-and-ai]]

- **Related Summaries**
  - [[summaries/cc-changed-how-i-work-1]]
  - [[summaries/cc-changed-how-i-work-2]]
  - [[summaries/cc-changed-how-i-work-4]]
