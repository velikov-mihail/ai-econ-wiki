---
title: "Verifying LLM Output — for Academic Economists (Bäckman)"
tags: [summary, academic-research, verification, empirical-methods, git, claude-code]
sources:
  - "[[raw/articles/Verifying LLM output — for academic economists.md]]"
date_updated: 2026-09-30
date_published: 2026-08
---

- **Author/Source**: Claes Bäckman (Aarhus University), a guide on his personal site, maintained as a living document (undated; clipped August 2026)
- **Original**: [https://claesbackman.com/verifying-llm-output.html](https://claesbackman.com/verifying-llm-output.html)

- **Key Ideas**
  - **Verification is now the bottleneck for empirical research.** Agents are fast, cheap, and competent at code, even in languages you don't know. There have been plenty of worries about verification, but no practical guide collecting concrete checks. This page is meant to be that guide.
  - **First principle: you have to read the code, or some version of it.** The code *is* the analysis, and once it produces numbers in the paper you are responsible for it. The errors to hunt for are not crashes, which agents fix on their own. They are **plausible-looking outputs produced by a shortcut**.
  - **Git is a prerequisite.** A reviewer pointed at a `git diff` knows exactly what changed. One pointed at the whole codebase spreads its attention thin and gives generic answers at higher token cost. Git is optional for *running* Claude Code but not for *verifying* its output.
  - **Check 01: a fresh agent attacks the diff.** The agent that wrote the code has too much context to judge it fairly. A subagent works, but the parent writes its brief and summarizes its report, so a new session you brief yourself is more isolated. **Have the reviewer report, not fix**: a fixing reviewer hands you a second diff optimized for closing findings, and confident false positives are common.
  - **Check 02: use a different model.** Two instances of the same model share training data and habits of thought, so their errors are correlated. It's like two referees from different subfields versus two students of the same advisor. Keep one shared project context (`CLAUDE.md` ↔ `AGENTS.md`) so both work from the same sample definitions.
  - **Check 03: make the agent quiz you.** Adapting Geoffrey Litt's *explain-diff* skill, a `/quiz-me` skill writes a self-contained HTML explainer (before/after, consequences for which samples, coefficients, and tables, a code walkthrough) ending in five multiple-choice questions. At least two must be about **empirical consequences**, and the distractors must be plausible misunderstandings. There's also a 30-second version: "ask me three questions about the last commit; don't tell me I was close."
  - **Check 04: reimplement in another language** (Stata ↔ R ↔ Python), the check Scott Cunningham has championed. It is the most expensive and the strongest, because it catches code that faithfully implements *something other than what the paper says*. Independence must be enforced by **removing context**, not by asking the model to "ignore" it. Use a fresh folder with only `spec.md` (with results deleted) and a data `README.md`, have the agent stop at ambiguities, and **run the script yourself**, since an agent that sees an implausible number will "debug towards plausibility." Reserve it for main exhibits and error-invisible steps.
  - **Near-free checks**: a sample-construction table and merge diagnostics (verify the data, not just the code), external benchmarks, numbers in the prose vs. numbers in the tables, and reference verification (e.g., Reviewer3).
  - **The cheapest verification happens during writing.** Ask for a numbered plan rather than code. Make the agent ask every question it needs answered, including the defaults it would have chosen. Implement one step at a time and look at the counts after each. Ask *why*, not *what*: list three decisions where a reasonable person would differ, then **re-run** each alternative side by side.
  - **"The questions are the deliverable."** Log the ambiguities and your answers in `decisions.md`, pointed to from `CLAUDE.md` but kept out of it. A context file that grows without limit gets followed less closely. That log becomes your sample-definition appendix.

- **Summary**

Bäckman's guide pulls together a practical toolkit for checking agent-written empirical code before it reaches a paper. It builds on Geoffrey Litt's argument that *understanding* is the new bottleneck and on Paul Goldsmith-Pinkham's integration-and-collaboration protocol. It starts from two premises: the researcher is responsible for code that produces reported results, and the dangerous errors are silent ones. Git diffs make the work tractable. On top of them sit four escalating checks: a fresh adversarial agent, a second model from a different developer, a comprehension quiz for the human, and a fully independent reimplementation in another language. These are backed by cheap habitual checks on data, benchmarks, internal consistency, and citations. The suggested default is to plan and question before coding, set a git baseline each session, have a fresh agent review every diff, run a second model over anything that appears in the paper, and independently reimplement the main table.

The last section changes the frame. After-the-fact checks put the author in a referee's position, reverse-engineering reasoning from 400 lines of output. Building the analysis in small, executed, discussed steps means you already know what the code does, so later checks confirm rather than discover. Bäckman argues this is not slower on net: time saved by one long prompt is "borrowed against the debugging session where you discover, three tables later, that the deflator was applied twice."

- **Relevance to Economics Research**

This is the most complete practical verification protocol in the wiki for empirical economists. Its advice is concrete and copy-pasteable (prompts, a full `SKILL.md`, folder layouts), and it is honest about costs, matching the strength of each check to the stakes of each output. Several ideas are sharper than elsewhere. Subagent review is only partly independent. Asking a model to "ignore" context does nothing. Letting the agent run its own verification script defeats the test. And comprehension of empirical consequences, not just syntax, is what the human must verify. It fits naturally with Goldsmith-Pinkham's verification-debt framing and Cunningham's cross-language replication, and the `decisions.md` habit produces the documentation that pre-registration and replication packages need.

- **Related Concepts**
  - [[concepts/verifying-ai-output]]
  - [[concepts/cross-language-replication]]
  - [[concepts/version-control-research]]
  - [[concepts/human-in-the-loop]]
  - [[concepts/reproducibility-transparency]]
  - [[concepts/plan-driven-development]]
  - [[concepts/context-management]]
  - [[concepts/citation-hallucination]]

- **Related Summaries**
  - [[summaries/integration-collaboration-substack]] — Goldsmith-Pinkham's verification-debt protocol, which Bäckman builds on
  - [[summaries/integration-collaboration-markus-162-8]]
  - [[summaries/cc-series-24-agents-auditing-did]] — Cunningham's multi-agent, cross-language DiD audit
  - [[summaries/cc-series-12-empirical-research]]
  - [[summaries/matray-ai-guide]] — Matray's verification mindset and independence principle
  - [[summaries/koren-theorist-toolbox]] — the same principles applied to proofs
  - [[summaries/ai-research-feedback-skills]] — Bäckman's skill collection (review-paper consistency checks)
  - [[summaries/backman-vscode-guide]]
  - [[summaries/kohler-agentic-reproduction]]
