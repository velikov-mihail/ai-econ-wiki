---
title: "Claude Code 29: Can Claude Code Find Facts? And If So, Should I Believe Them?"
tags: [summary, academic-research, epistemology, automated-research, causal-inference, peer-review]
sources:
  - "[[raw/articles/Claude Code 29 Can Claude Code Find Facts And If So, Should I Believe Them.md]]"
date_updated: 2026-04-05
date_published: 2026-03-05
---

- **Author/Source**: Scott Cunningham (Baylor University), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-29-can-claude-code-find](https://causalinf.substack.com/p/claude-code-29-can-claude-code-find)

- **Key Ideas**
  - Cunningham live-demonstrates a fully automated paper (marijuana legalization and labor markets) produced in ~3.5 hours while watching Netflix, using real BLS/CDC data and Callaway-Sant'Anna diff-in-diff.
  - The right question is not whether AI papers can compete at the AER, but whether they can get past the desk at field journals like JHR, JOLE, or Journal of Health Economics -- where most economists actually publish.
  - When marginal cost of econometric analysis drops to zero, causal inference methods will be applied to trivially low-value questions far down the demand curve.
  - The epistemological puzzle: if the data is real, the methods are standard, and the code is audited, does it matter that no human designed the study? At what point does a "finding" become a "fact"?
  - Human capital is still essential for catching bugs (e.g., a Sun-Abraham aggregation error), but the incentive to maintain that human capital erodes as AI does more of the work.

- **Summary**

This is the companion piece to Post 27 (research vs. publishing). Cunningham recounts prompting Claude Code with a vague research interest in labor, mental health, and drug policy, then going to bed. By morning he had a complete manuscript on marijuana legalization's effects on employment, wages, and overdose mortality, using diff-in-diff with Callaway and Sant'Anna plus robustness via TWFE, Sun-Abraham, and Gardner estimators. He submitted it to Refine.ink, had Claude fix the issues (including a real Sun-Abraham aggregation bug and 295 false zeros in incarceration data), and audited the code by replicating in multiple languages.

The deeper argument is about what happens when the marginal cost of producing a manuscript hits zero. Cunningham argues that causal inference will migrate into tasks where it was never previously worth the effort -- policy memos, city council questions, PTA meetings. The entire graduate curriculum was built around methods that took months to implement; that scarcity was itself a screening device. With that filter gone, the question becomes what replaces it. He invokes Al Roth's three purposes of empirical work (establishing facts, informing theory, whispering in the ears of princes) and asks whether machine-produced results qualify under any of them without peer review.

The article closes with a tension: Cunningham's domain expertise let him catch the bugs, but that expertise exists only because of years of effortful learning. If the machine does the work, the incentive to invest in the human capital that enables quality control depreciates -- a free-rider problem that cuts both ways.

- **Relevance to Economics Research**

This piece raises foundational questions about the epistemology of empirical economics in an AI era. It is directly relevant to debates about replication, the role of peer review as a truth-certification mechanism, and whether the diffusion of causal inference methods to low-value applications changes the meaning of "research." The concrete demonstration of a fully automated paper is an important data point for the profession.

- **Related Concepts**
  - [[concepts/automated-research]]
  - [[concepts/vibe-research]]
  - [[concepts/research-quality]]
  - [[concepts/ai-peer-review]]
  - [[concepts/ai-adoption-academia]]

- **Related Summaries**
  - [[summaries/cc-series-27-research-vs-publishing]]
  - [[summaries/cc-series-31-satisfaction-discovering]]
  - [[summaries/cc-series-32-modest-proposal-editors]]
  - [[summaries/cc-series-33-continue-learning]]
