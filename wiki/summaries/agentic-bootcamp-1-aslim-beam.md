---
title: "Agentic AI Bootcamp — Session 1: From Chat to Autonomous Agents"
tags: [summary, foundations-setup]
sources:
  - "[[raw/papers/session_1_slides.pdf]]"
date_updated: 2026-05-15
date_published: 2026-04-22
---

- **Author/Source**: Erkmen G. Aslim & Emily Beam (Department of Economics, University of Vermont)
- **Original**: Session 1 of the *Thinking with Agents* bootcamp, April 22, 2026, Old Mill A500. PDF: [thinkingwithagents.github.io/Session1_Slides/session_1_slides.pdf](https://thinkingwithagents.github.io/Session1_Slides/session_1_slides.pdf). Course page: [thinkingwithagents.github.io](https://thinkingwithagents.github.io/). See [[thinking-with-agents]].

## Key Ideas

- **The AI ladder (adapted from Goldsmith-Pinkham)**: Level 0 — paste from ChatGPT into your editor; Level 1 — IDE inline completions (VS Code, Cursor, Zed); Level 2 — IDE "agent mode"; Level 3 — **dedicated coding agents** (Claude Code, Codex CLI); Level 4 — agents with web/scrape/orchestration tools; Level 5 — orchestrate teams of agents in containers. *Most economists are at Level 0–1; the bootcamp targets Level 3–4.*
- **Chat AI vs. agentic AI**: ChatGPT/Claude Web run in a sandbox — text in, text out. Claude Code/Codex run on your actual computer — read & edit files, run terminal commands, install packages. "Like texting a smart friend" vs. "like having them sit next to you and do the work."
- **Microsoft Copilot caveat for UVM**: enterprise SSO subscription is FERPA-compliant but is still chat AI ("a FERPA-compliant smart friend"). Faculty can request a paid license for tighter Office integration.
- **Tool poll (March 2026, n=459)**: 51.4% mostly Claude Code, 18.0% mostly Codex, 13.3% both equally. Recommendation: use both as complementary tools rather than picking one.
- **Division of labor by task**: Claude Code is stronger at ideation/brainstorming, code review, writing, skill creation; Codex is stronger at planning, actual implementation, "review of review of code," and OpenClaw. Plans review goes to ChatGPT/Claude Pro chat.
- **Pricing reality**: $20/month plans (Claude Pro + ChatGPT Plus) are the entry point; heavy users go Claude Max ($100–200/mo) or ChatGPT Pro ($200/mo); pay-as-you-go API runs $3–15 per million tokens. **One token ≈ 3/4 word; 200K tokens ≈ 150K words ≈ context limit.**
- **Two interfaces, one underlying agent**: terminal CLI (fastest features, lower memory, power-user flexibility) vs. desktop app (point-and-click, more approachable, currently more polished for Codex). The presenters run both simultaneously, treating them as different agents on different tasks.
- **Markdown is the lingua franca** — `.md` files are the instruction manuals that guide AI agents. Three roles: `CLAUDE.md`/`AGENTS.md` (standing rules), `PLAN.md` (strategy & roadmap), `SKILL.md` (reusable playbooks). Viewers like Obsidian (free) or Typora ($15) render them; agents can convert to `.docx`, `.tex`, `.pdf`.
- **AGENTS.md skepticism (Gloaguen et al. 2026, ETH/INSAIT)**: success-rate gains are modest across Sonnet 4.5, GPT-5.3, GPT-5.1 Mini, Qwen3-32B; too much context can hurt; `/init`-generated files are mediocre and go stale fast. Use them, but don't over-engineer.
- **The context window is the single most important concept.** Every turn the entire history (system prompt + dev messages + your prompt + thinking + tool calls + tool results + model responses) gets re-sent. ~200K tokens (~150K words) is the standard limit, climbing toward ~1M (~750K words). **Performance ≈ correctness² × completeness ÷ size** — as context grows, the model loses the thread.
- **Three rules for context management**: (1) long sessions degrade — `/clear` after ~20 turns; (2) write ideas to files — files persist, context doesn't; (3) break work into 5–10-turn focused chunks. The "start fresh" pattern: write progress to `PLAN.md`, start new session, "Read PLAN.md and continue."
- **The access spectrum**: Chat AI sandbox ← DEFAULT (works in your project folder, asks before risky things) → Clawdbot "GOD MODE" (reads/writes/sends/deletes everything, accesses email/calendar/external services). The bootcamp stays at DEFAULT; the GOD MODE warning includes a real cautionary text exchange where an autonomous agent deleted hundreds of emails before approval.
- **Permission modes (Claude Code)**: Default (prompts on first use) → Accept Edits → Plan Mode (read-only) → YOLO (skip all prompts). YOLO via `/update-config` + restart; fine-grained control via `/permissions`.
- **Four prompting rules**: (1) be specific — "load employment.csv, compute growth rates" not "analyze data"; (2) iterate, don't argue — going in circles, hit ESC, start over; (3) correct early — wrong foundations propagate; (4) trust but verify — edge cases will bite.
- **What can go specifically wrong**: confident citations that don't exist (verify every reference); code that runs but is silently wrong (reshapes/merges/filters are common culprits); hallucinated numbers (ask it to write a script and confirm). Mitigations: spot-check outputs against known cases, ask the agent to walk through the code line by line, send an adversarial agent to flag misunderstandings, use Git for version control.
- **Worth-it vs. not-worth-it heuristic**: worth the setup for repetitive weekly tasks, multi-step workflows, drafting in your voice at scale, exploring unfamiliar code/data; *not* worth it for 5-minute manual tasks, anything requiring domain judgment (identification strategy, causal interpretation), confidential data you can't share, or precise citations you don't have time to verify.
- **What the presenters have actually used it for**: built a replication package (51 do-files, found a real bug), reproducible balance tables (Stata → LaTeX), R + IPUMS API pulls, a data dictionary from a messy dataset, adversarial review of their own paper, structured literature review with memo, course website (Hugo + GitHub Pages), Quarto lecture slides, assignment prompts/rubrics from learning goals, inbox triage, email drafting in their own voice, hockey-schedule emails → Google Calendar events. *"These slides were also made with AI."*
- **What was fun but saved zero time**: a Vermont cycling route planner (never used a single route), a D&D solo campaign, a project-management system *instead of* doing the project, automated to-do list review (now they procrastinate faster).
- **Voice files (Application 1 in the deck)**: a plain Markdown file like `EB-VOICE.md` describing your tone, sentence length, openings/closings, what you avoid. Generated by feeding the AI 5+ samples of your real writing and asking it to describe your patterns. Loaded automatically via standing instructions or called on demand. Same prompt with three different contexts (no login / logged in / Claude + voice file) yields three very different drafts — *context is the difference*.
- **PLAN.md workflow**: pre-planning brainstorm → draft planning prompt → polish prompt with Claude + GPT → feed into Claude Code/Codex → save plan locally. Every fresh session starts with "Read PLAN.md and continue."

## Summary

This is the conceptual on-ramp for the *Thinking with Agents* bootcamp at the University of Vermont. Across roughly 49 slides, Aslim and Beam walk an economist audience from "what even is agentic AI" to a working mental model of context windows, planning files, and permission modes — without requiring anyone to install anything during the session.

The deck's spine is a five-step argument. First, place the audience on the AI ladder (most economists are at Level 0–1; the bootcamp aims for Level 3–4). Second, distinguish chat AI from agentic AI by where the work happens (sandbox vs. your computer). Third, introduce the tooling landscape — Claude Code vs. Codex, terminal vs. desktop app, free vs. $20 vs. $200/month — without picking a winner. Fourth, install the load-bearing concept (the context window) and derive three operating rules from it: clear after ~20 turns, write to files, break work into chunks. Fifth, walk the access spectrum and permission modes, anchored by a real cautionary-tale text exchange where an autonomous agent deleted hundreds of emails without approval.

The applications half pivots from concepts to a concrete artifact: a **voice file**. Same prompt, three contexts, three different outputs — making "context is the difference" a tangible takeaway rather than a slogan. The deck closes with the PLAN.md workflow and a candid "what we've used this for" inventory that pairs serious wins (replication package, adversarial paper review, course website) with self-deprecating misses (the cycling route planner, the D&D campaign, the project-management system built instead of doing the project).

## Relevance to Economics Research

This is a near-complete starter curriculum for any econ department running an internal AI workshop. The deck's value-add over generic "intro to LLMs" content is its calibration to the audience: the AI-ladder framing acknowledges where most faculty actually are, the cost discussion is honest ($20/month is the answer), the AGENTS.md skepticism (citing the ETH/INSAIT study) pre-empts over-investment in standing-instruction files, and the "what was fun but saved zero time" slide is the kind of self-criticism that makes an adoption pitch credible. Pair it with [[agentic-bootcamp-2-aslim-beam]] for the applied half, or with [[velikov-smeal-cop]] and [[brownbag-claude-skills]] for parallel synthesizing talks.

## Related Concepts

- [[concepts/context-management]]
- [[concepts/claude-md-files]]
- [[concepts/plan-driven-development]]
- [[concepts/claude-code]]
- [[concepts/ai-tools-landscape]]
- [[concepts/cost-and-budget]]
- [[concepts/ai-limitations]]
- [[concepts/voice-and-transcription]]
- [[concepts/ai-adoption-academia]]
- [[concepts/human-in-the-loop]]

## Related Summaries

- [[summaries/thinking-with-agents]] — course landing page
- [[summaries/agentic-bootcamp-2-aslim-beam]] — Session 2 (applications)
- [[summaries/getting-started-researchers]] — Goldsmith-Pinkham's AI-ladder source
- [[summaries/teaching-ai-your-voice]] — Blattman on voice files
- [[summaries/velikov-smeal-cop]] — parallel synthesis talk
- [[summaries/guide-which-ai]] — Mollick on tool selection
- [[summaries/cost-reality]] — Blattman on the actual costs
- [[summaries/privacy-setup]] — privacy/permissions deep dive
