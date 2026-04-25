---
title: "AI for Business & Economic Research: From Chatbots to Agents"
tags: [summary, academic-research]
sources:
  - "[[raw/papers/main_velikov_smeal_cop.tex]]"
date_updated: 2026-04-25
date_published: 2026-04-06
---

- **Author/Source**: Mihail Velikov (Penn State, Smeal College of Business)
- **Original**: [github.com/velikov-mihail/ai-econ-wiki/tree/main/presentations/smeal-cop](https://github.com/velikov-mihail/ai-econ-wiki/tree/main/presentations/smeal-cop) — Beamer source for the talk presented at the Penn State Smeal AI Community of Practice in Research, April 6, 2026. Companion wiki: [velikov-mihail.github.io/ai-econ-wiki](https://velikov-mihail.github.io/ai-econ-wiki/)

## Key Ideas

- **The arc of AI-assisted research compresses fast.** Six opening quotes track the timeline: Novy-Marx & Velikov (2024, mass-produced finance papers) → Andrew Chen (early 2025, AI as junior co-author) → Joshua Gans (full-year 2025 vibe research) → Vincent Gregoire (Feb 2026, paper in 4 days) → Paul Novosad (2026, paper in 3 hours) → Project APE (March 2026, zero human involvement). Years → weeks → days → hours → zero.
- **Three paradigms of generative AI**: (1) **Traditional LLMs** — pattern-matching, "System 1," now commoditized; (2) **Reasoning models** — chain-of-thought, "System 2," PhD-level on GPQA (94.3%), IMO gold, ~75% SWE-Bench; (3) **Agentic AI** — LLM + tools + loop + goal, autonomous tool use, sub-agents.
- **Frontier model landscape (March 2026)**: OpenAI (Instant 5.3 / Thinking 5.4 / Codex), Anthropic (Sonnet 4.6, Opus 4.6, Claude Code), Google (Gemini 3 Flash, 3.1 Pro, Deep Think, Gemini CLI, Antigravity). Top GPQA scores cluster 91–94%; PhD experts score ~65%.
- **The harness matters more than the model.** Same model behaves very differently across CLI agents (Claude Code, OpenAI Codex, Gemini CLI) vs. agent-native IDEs (Cursor, Windsurf, VS Code+extensions, Zed, Antigravity). CLI agents do search-on-demand; Cursor builds a RAG index over the codebase. They complement each other.
- **The think–act–observe loop**, illustrated by a ~100-line FRED Agent (Korinek): the LLM picks a series code (`FPCPITOTLZGUSA` for U.S. inflation), calls `fred.get_series`, observes the latest value (2.8%), and responds. The "intelligence" lives in the prompts, not the orchestration.
- **Configuration stack**: `User CLAUDE.md` (preferences, persistent) → `Project CLAUDE.md` (rules, persistent) → Skills (on-demand workflows) → Plan/Conversation (ephemeral). The agent improves as project infrastructure improves, not as prompts get longer.
- **Plan mode** (Sant'Anna's plan-first workflow): the agent enters read-only exploration, writes `PLAN.md`, awaits approval — non-trivial tasks "always" start in plan mode. Plans survive context compression.
- **Skills as on-demand research workflows**: Sant'Anna's `/review-paper`, `/data-analysis`, `/lit-review`, `/research-ideation`, `/interview-me` plus 10 specialized agents (proofreader, slide auditor, pedagogy reviewer, R reviewer, TikZ critic, domain reviewer, adversarial QA pair, translator, verifier) — adopted by 15+ research groups.
- **Use cases across the research pipeline**: planning (project files), ideation (Karpathy's "LLM mirror" — have AI argue against your hypothesis), lit review (Deep Research, with caveats about fabricated citations), data (Orlowski's Claude WRDS toolkit; Goldsmith-Pinkham's "empty folder to figure" in 6:21), iteration ("follow Kieran Healy best practices" prompt), writing (voice files; Blattman's ban list of AI-isms), review (refine.ink for cross-paper inconsistencies and math errors).
- **Full automated pipelines**: Gregoire's "Vibe Research" (4-day paper using Claude + Codex + Gemini multi-agent review), Project APE (592 papers, 64.2% DiD by default — methodological monoculture risk), Lopez-Lira (1-paragraph idea → submission-ready finance paper with simulated peer review).
- **Quality control warning** (Gans): subtle equilibrium-concept errors, idea inflation (lower costs → weaker ideas), seductiveness of confident-but-wrong results. Guardrails: cooling-off period (1+ month), more peer feedback, explicit go/no-go decisions. Human taste matters *more*, not less.
- **The jagged frontier** (Mollick): "shockingly capable at some hard things, embarrassingly bad at seemingly simple things." Verify, don't trust.
- **Six low-risk first projects** at $20/month: reorganize a messy repo, make slides from a paper, write a paper from a codebase, create a voice file, get an AI referee report, translate code across languages.
- **Economists to follow on X**: Imas, Blattman, Yanagizawa-Drott, Mollick, Bryan, Kustov, Mele, Zhang, Panjwani, Cunningham, Sant'Anna, Gans, Bell, Velikov.

## Summary

This is the Beamer source for Mihail Velikov's talk delivered at the Penn State Smeal AI Community of Practice in Research (April 6, 2026). Across roughly 46 slides, the deck synthesizes the major threads of the wiki it ships alongside into a single overview tailored for a faculty audience deciding whether and how to start using agentic AI for empirical research.

The deck opens with six "voices from the field" quotes that compress the 2024–2026 acceleration into a single arc, then steps through three sections that build conceptually: (1) the evolution from traditional LLMs to reasoning models to agents, (2) how an agent actually works (the think–act–observe loop, illustrated by Korinek's ~100-line FRED Agent), and (3) the tooling landscape (CLI agents vs. agent-native IDEs, with a side-by-side architectural contrast between Claude Code's on-demand search and Cursor's RAG-indexed codebase).

The middle of the talk turns practical: a configuration-stack visual showing how `User CLAUDE.md` → `Project CLAUDE.md` → Skills → Plan/Conversation layer from persistent to ephemeral; a tour of plan mode, skills, and git integration in Claude Code; and concrete economist-relevant examples (Orlowski's Claude WRDS toolkit, Goldsmith-Pinkham's empty-folder-to-figure run). The use-cases section walks the research pipeline (planning → ideation → design → data → analysis → writing → review → publication) with one or two anchor examples per stage.

The closing section is calibrated to encourage adoption without overselling: full automated pipelines (Gregoire, Project APE, Lopez-Lira) sit next to Gans's three pitfalls (subtle errors, idea inflation, seductiveness) and Mollick's "jagged frontier" image. The deck closes with six low-risk starter projects at $20/month and a list of economists to follow on X. The final slide pulls a Blattman quote — "Holy crap" — on first using Claude Code.

## Relevance to Economics Research

This deck is itself a piece of the wiki it documents — the Smeal Community-of-Practice talk is the synthesizing artifact that pulls the wiki's individual summaries (Korinek, Mollick, Sant'Anna, Goldsmith-Pinkham, Cunningham, Blattman, Gans, Gregoire, Lopez-Lira, Orlowski, Project APE, refine.ink) into a single 50-minute narrative aimed at faculty colleagues. For an economics audience, it functions as a curated reading-list-with-commentary: every cited claim has a corresponding wiki summary, and the structure (paradigms → architecture → tools → workflows → quality control → starter projects) is a defensible template for any econ department's "AI for research" onboarding session.

## Related Concepts

- [[concepts/ai-agents]]
- [[concepts/agentic-workflows]]
- [[concepts/claude-code]]
- [[concepts/claude-md-files]]
- [[concepts/claude-code-skills]]
- [[concepts/ai-tools-landscape]]
- [[concepts/jagged-frontier]]
- [[concepts/vibe-research]]
- [[concepts/automated-research]]
- [[concepts/ai-adoption-academia]]

## Related Summaries

- [[summaries/ai-agents-generative-ai]]
- [[summaries/applications-generative-ai]]
- [[summaries/guide-which-ai]]
- [[summaries/claude-code-what-comes-next]]
- [[summaries/my-claude-code-setup]]
- [[summaries/ai-project-folders]]
- [[summaries/empty-folder-to-figure]]
- [[summaries/edgar-filings]]
- [[summaries/claude-wrds-tools]]
- [[summaries/teaching-ai-your-voice]]
- [[summaries/refine-ink-golub]]
- [[summaries/vibe-research]]
- [[summaries/reflections-vibe-research]]
- [[summaries/automated-research-finance]]
- [[summaries/project-ape]]
- [[summaries/ai-powered-scholarship]]
- [[summaries/panjwani-slides]]
- [[summaries/kansoy-ai-future-research]]
