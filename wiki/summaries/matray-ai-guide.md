---
title: "AI Guide for Economists: Working with AI — A Philosophy (Matray)"
tags: [summary, foundations-setup, claude-code, verification, mindset, claude-md]
sources:
  - "[[raw/articles/AI Guide for Economists.md]]"
date_updated: 2026-09-30
date_published: 2026-09
---

- **Author/Source**: Adrien Matray, the opening "philosophy" chapter of his multi-part guide to Claude Code for economists (undated site; clipped September 2026)
- **Original**: [https://adrienmatray-ai.com/index.html](https://adrienmatray-ai.com/index.html) · next chapter: [Getting Started](https://adrienmatray-ai.com/getting-started.html)

- **Key Ideas**
  - **Mindset before tooling.** AI multiplies output when used well and multiplies mistakes when used carelessly. Matray says the difference is "not talent or experience with technology; it is mindset." Read the philosophy first and come back to it when something goes wrong.
  - **The mental model: an over-eager, overconfident, and quietly lazy collaborator.** The *laziness* is the subtle part. The model picks the quick fix over the sound one, resolves ambiguity in whatever direction takes least effort, declares data "redundant" or "reconstructable" to skip harder work without checking, and relies on training-data memory instead of using its tools to inspect your current data and code. So there are two failure modes to watch for: *"is this wrong?"* and *"is this cutting corners?"*
  - **The first question for any output is "where IS this wrong, and how do I check?"** Not whether it sounds right, since sounding right is exactly what makes AI dangerous. "Your skepticism is the only quality filter in this system."
  - **Just ask (and show).** No magic prompts. Talk to it like a colleague, paste screenshots (Claude Code reads images), and dictate with voice tools such as Wispr Flow. *"Lower the barrier to asking; raise the bar for accepting."*
  - **The personalization thesis.** Generic AI tips are mostly useless. The value comes from a `CLAUDE.md` that encodes *your* conventions, tools, and verification habits. Start by writing down the mental checklists you already run silently on repeated tasks.
  - **The verification mindset**, with three concrete econ failure cases: a *silent merge failure* (half the observations dropped, county FE used instead of firm FE, nothing flagged); *sample shrinkage* (a "clean" balanced panel made by deleting every incomplete firm-year, cutting 40% of the sample); and a *wrong specification* (a "replication" with similar magnitudes but the wrong clustering level, a missing interaction, and a different sample restriction).
  - **The independence principle.** The same conversation cannot both produce and verify. Review cold in a new conversation, and later, with adversarial review agents.
  - **Context hygiene.** Conversations degrade: the model forgets instructions, repeats itself, and contradicts itself. Keep one focused task per conversation and clear often. *Handoff trick:* before clearing, ask for a short markdown summary of where you are, what was done, and what's left, then paste it into the fresh session.
  - **The automation principle.** Correct the same thing three times and it becomes a permanent rule. Give the same instruction every session and it gets automated. Do three steps together every time and they become one command. Matray's own examples: "Tables in PDFs must never break across pages" and "Always use full country names in figures and tables, never ISO3 codes."
  - **What the guide won't teach**: prompt tricks, jailbreaks, or avoiding thinking. The goal is "a reliable collaborative workflow where you remain the expert and the AI remains the tool."

- **Summary**

This is the opening chapter of Adrien Matray's guide for economists using Claude Code. It deliberately comes before any installation instructions. Its core claim is that reliable AI-assisted research depends less on tool skill than on the researcher's stance toward the tool. Matray's portrait of the model as over-eager, overconfident, and quietly *lazy* is more useful than the usual "it hallucinates" warning, because it predicts a specific kind of error: plausible shortcuts, such as dropped observations, convenient fixed effects, and silently balanced panels, that produce reasonable-looking coefficients.

The chapter then sets out six working principles. *Ask freely, accept skeptically*: low friction on input, a high bar on output. *Personalize* through `CLAUDE.md`. *Verify* every output along an independent path. *Separate producer and verifier* across conversations. *Keep contexts short* with markdown handoffs. *Automate recurring corrections* so mistakes compound into rules rather than recurring weekly. Together they amount to a philosophy of supervision: the researcher stays the expert, and the AI stays a fast but untrustworthy tool whose output is always a hypothesis.

- **Relevance to Economics Research**

Matray writes for empirical economists, and his failure cases (merges, panel balancing, clustering, specification replication) are the errors that most often invalidate results without anyone noticing. That makes the chapter a useful first reading for PhD students and RAs before they touch an agent, and a compact statement of the norms a lab might adopt. The "quietly lazy" framing complements [[summaries/verifying-llm-output|Bäckman's verification protocol]], which supplies the concrete checks. The automation principle is the same compounding-configuration idea found in [[summaries/continuous-improvement|continuous improvement]] and [[summaries/your-claude-md|CLAUDE.md]] guides, stated as a simple three-strikes rule.

- **Related Concepts**
  - [[concepts/verifying-ai-output]]
  - [[concepts/claude-md-files]]
  - [[concepts/context-management]]
  - [[concepts/human-in-the-loop]]
  - [[concepts/ai-limitations]]
  - [[concepts/voice-and-transcription]]
  - [[concepts/domain-expertise-vs-ai-skills]]

- **Related Summaries**
  - [[summaries/verifying-llm-output]] — concrete checks that put the verification mindset into practice
  - [[summaries/integration-collaboration-substack]]
  - [[summaries/your-claude-md]]
  - [[summaries/continuous-improvement]]
  - [[summaries/getting-started-researchers]]
  - [[summaries/claude-code-newbies]]
  - [[summaries/voice-dictation]]
  - [[summaries/cc-series-33-continue-learning]] — Cunningham's cautionary tale on domain expertise and verification
