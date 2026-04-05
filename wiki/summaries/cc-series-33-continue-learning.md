---
title: "Claude Code 33: Help Claude Help Us By Continue Learning"
tags: [summary, claude-code-skills, human-capital, domain-expertise, ai-limitations, diff-in-diff]
sources:
  - "[[raw/articles/Claude Code 33 Help Claude Help Us By Continue Learning.md]]"
date_updated: 2026-04-05
date_published: 2026-03-19
---

- **Author/Source**: Scott Cunningham (Baylor University), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-33-help-claude-help-us](https://causalinf.substack.com/p/claude-code-33-help-claude-help-us)

- **Key Ideas**
  - AI is not the Matrix: you cannot download skills passively. Learning still requires resistance and struggle, just as building muscle requires resistance.
  - AI works best as a "rocket strapped to your back" in domains where you already have deep expertise; it becomes dangerously unreliable when you lack the background to interrogate its output.
  - Claude Code confidently made a fundamental diff-in-diff error -- computing only between-group differences instead of difference-in-differences -- and presented it with the same confidence as correct work.
  - The debugging strategy of stripping problems down to pencil-and-paper calculations (4-5 observations, manual ATT computation) remains essential for catching AI errors.
  - Human capital depreciates just like physical capital; if AI does the work, the incentive to maintain the expertise needed to verify AI's work erodes -- but we are not yet at AGI, and domain expertise remains critical.

- **Summary**

Cunningham reflects on returning to a stale research project that used Callaway and Sant'Anna's diff-in-diff estimator in an unusual individual-level worker data application. When Claude Code audited the code, it confidently claimed the Stata `csdid` implementation had miscoded a treated group as never-treated -- a plausible but ultimately incorrect diagnosis. Cunningham's deep knowledge of CS let him push back systematically: he forced Claude to strip away covariates, compute ATT(g,t) values manually, and check against the known-correct `csdid` output. Eventually Claude discovered its own error -- it had been computing only cross-sectional comparisons (treated mean minus control mean) rather than actual difference-in-differences. It was, as Cunningham puts it, "a pure zero on the exam."

The article draws a parallel to a workshop attendee who had been told by a reasoning model that double-robust estimation allows different covariates in the outcome regression and propensity score model. The code turned out to be including propensity score variables additively inside a TWFE regression -- a fundamental misspecification that looked professional but was deeply wrong. The common thread: AI output looks professional and runs without errors, but the calculations can be completely wrong, and only domain expertise reveals it.

Cunningham rejects the Matrix metaphor for AI-assisted learning. He argues there is no free lunch in skill acquisition -- you cannot gain knowledge without struggle. AI can complete cognitive tasks without you learning anything, making you either an overeducated button-pusher or the blind leading the blind. The conclusion is optimistic but guarded: AI is transformative, replication failures will likely collapse, but human capital investment remains essential because the technology works best when you are the most informed version of yourself.

- **Relevance to Economics Research**

This article provides a critical cautionary tale for empirical economists using AI agents for econometric work. The specific diff-in-diff debugging example illustrates exactly how AI can fail at the most basic level while appearing sophisticated, and demonstrates the verification strategies (manual computation, ground-truth comparison) that domain experts should employ. It is directly relevant to anyone using Claude Code for causal inference.

- **Related Concepts**
  - [[concepts/ai-limitations]]
  - [[concepts/research-quality]]
  - [[concepts/claude-code]]
  - [[concepts/ai-adoption-academia]]

- **Related Summaries**
  - [[summaries/cc-series-29-finding-facts]]
  - [[summaries/cc-series-27-research-vs-publishing]]
  - [[summaries/building-skills]]
