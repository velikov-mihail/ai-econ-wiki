---
title: "Theorist Toolbox: Claude Code Skills for Economic Theory (Koren)"
tags: [summary, academic-research, claude-code-skills, economic-theory, multi-agent, verification]
sources:
  - "[[raw/Clippings/A toolkit of Claude Code skills for doing economic theory with LLMs math-proof (single-pass proving), codex-math (adversarial verification), and co-math (multi-agent proof projects). With a VCG-for-grade-inflation case s.md]]"
date_updated: 2026-09-30
date_published: 2026-06
---

- **Author/Source**: Moran Koren (Ben-Gurion University of the Negev), GitHub repository with companion paper *Theorist Toolbox: Tools for Agent-Based LLM-Assisted Economic Theory Research* (arXiv:2606.22337)
- **Original**: [https://github.com/morankor/theorist-toolbox](https://github.com/morankor/theorist-toolbox) · paper: [arxiv.org/abs/2606.22337](https://arxiv.org/abs/2606.22337)

- **Key Ideas**
  - **The theory-side equivalent of empiricists' shared tooling.** Applied economists learn their craft from reusable, opinionated tools; theorists rarely got that. The toolbox encodes *how* to push an LLM through a proof "without letting the model hand-wave."
  - **Three skills, three bets on the same problem** — how to get machine help on a theorem you don't already know how to prove, and trust the answer:
    - `math-proof` — *one careful pass*: state what you'll show before showing it, sign every term, no "clearly," no generalizing from examples. Fastest, cleanest, but unchecked.
    - `codex-math` — *two minds, one adversarial*: Claude drives OpenAI Codex (gpt-5.5) as a co-processor and **hostile verifier** (propose → try to break → triage). Governing rule: Codex is "a brilliant, unreliable mathematician; every output is a lead, not a verdict." Most reliable per claim.
    - `co-math-init` / `co-math-status` — *a research team, not a chat*: scaffolds a proof project (`paper.tex`, goals, decisions log, workstreams) in **strict mode**, where every gap is flagged `\unproven{}` and nothing is complete without reviewer sign-off. Architecture follows Zheng et al. (2026), *AI co-mathematician* (Google DeepMind). Broadest coverage, and it can **reject its own work**.
  - **A six-agent co-math team**: `project-coordinator` (front door, dispatches workstreams), `literature-reviewer`, `prover` (every step justified, cited, or `\unproven{}`), `coder` (numerical checks with tests and golden values), `lean-prover` (formalizes lemmas in Lean 4; a green `lake build` is the strongest "proven" the system allows), and `paper-reviewer` (adversarial gate that must write an explicit approval file).
  - **A verification ladder**: informal proof → Lean-verified → readable. The `proof-readability` skill runs *only after* verification, in six layers (architecture, signposting, line-level justification, notation, intuition, grammar), and never changes the mathematics. A suspected gap sends the workstream back to the prover instead of being quietly patched.
  - **Hooks are "the teeth."** Strict mode is enforced by Claude Code hooks (`paper_tex_guard.py`, `workstream_complete_guard.py`, `blocked_workstreams_notice.py`) rather than by prompt instructions alone.
  - **`second-brain`**: agentic RAG over a local library of theory papers, with LaTeX-aware chunking that keeps theorems and proofs together with their custom macros and prerequisite definitions, hybrid search, and an MCP server Claude Code can query.
  - **Case study**: all three approaches were applied to one problem, turning Gans & Kominers' (2026) *eigengrade* into a VCG-style mechanism against grade inflation. Two of the three independently rediscovered the same externality kernel. The third's reviewer gate killed one of its own sub-goals.
  - **Cross-platform**: ports ship for OpenAI Codex (skills plus custom-agent profiles) and ChatGPT (custom-GPT instructions and a prompt pack). MIT-licensed, with a module contract for contributions.

- **Summary**

Koren's Theorist Toolbox is a set of Claude Code skills and sub-agents built for economic theory rather than empirical work. It is organized as three alternative strategies that trade off speed, verification, and coverage. `math-proof` is a writing discipline for a single gap-free pass. `codex-math` pairs Claude with Codex in an explicitly adversarial prover/breaker loop. `co-math` turns a proof into a managed project with a coordinator, specialist agents, a decisions log, and a reviewer who must sign off before any workstream closes. A `proof-readability` pass and a `second-brain` literature engine complete the kit.

The design choices are about making unverified claims visible and blocking them from counting as done. Gaps are typed (`\unproven{}`), completion is gated by a separate reviewer, the Lean agent's build result outranks any informal argument, and file-system hooks enforce the rules even when the model would rather move on. The case study shows why this matters. The disciplined multi-agent setup was the one that caught and discarded its own flawed sub-goal, and the independent rediscovery of the same kernel by two methods is itself a form of cross-validation.

- **Relevance to Economics Research**

Most AI tooling in this wiki targets empirical pipelines: data, regressions, replication. This is one of the few serious, installable toolkits for **theorists**, and it puts into practice ideas that the [[summaries/theory-miniseries-markus-166|Markus Academy theory miniseries]] discusses more loosely: prover/verifier separation, model diversity as a check, and treating AI proof output as leads, not results. The architecture carries over directly to empirical work. A reviewer gate that must approve before "done," typed placeholders for unverified steps, and hooks that enforce the rules mechanically are the same verification principles that [[summaries/verifying-llm-output|Bäckman]] and [[summaries/integration-collaboration-substack|Goldsmith-Pinkham]] recommend for code. It also makes the case that Lean formalization is becoming a practical option for economic theorists, not just mathematicians.

- **Related Concepts**
  - [[concepts/verifying-ai-output]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/claude-code-skills]]
  - [[concepts/llm-reasoning]]
  - [[concepts/retrieval-augmented-generation]]
  - [[concepts/human-in-the-loop]]

- **Related Summaries**
  - [[summaries/theory-miniseries-markus-166]]
  - [[summaries/theory-core-uses-markus-166-1]]
  - [[summaries/prompts-swarms-markus-166-4]] — Sandomirskiy's prover/verifier/judge pattern and agent swarms
  - [[summaries/which-model-markus-166-3]]
  - [[summaries/prompts-to-paper]] — Chen's AI-coauthored theory paper
  - [[summaries/vibe-research-2]] — Grégoire on closed-form proofs with Fable 5
  - [[summaries/cc-changed-how-i-work-3]] — devil's-advocate agents for adversarial review
