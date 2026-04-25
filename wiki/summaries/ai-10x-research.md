---
title: "AI Is Already 10x-ing Academic Research. How Do We Get to 100x?"
tags: [summary, institutional-societal]
sources:
  - "[[raw/articles/AI is already 10x-ing academic research. How do we get to 100x.md]]"
date_updated: 2026-04-25
date_published: 2026-04-16
---

- **Author/Source**: Andy Hall (Davies Family Professor of Political Economy, Stanford GSB; Hoover Institution), Roots of Progress Institute, "Intelligence Age" series
- **Original**: [https://newsletter.rootsofprogress.org/p/ai-is-already-10x-ing-academic-research](https://newsletter.rootsofprogress.org/p/ai-is-already-10x-ing-academic-research)

- **Key Ideas**
  - Hall's lab has stood up ~10 fellows worldwide, each with Claude Code, producing more substantive output in two months than would have been possible in a year previously --- and the bottleneck is *humans*, not agents.
  - Concrete 10x demonstration: replicating + extending his own 2020 PNAS vote-by-mail study (DiD on CA/UT/WA counties) end-to-end (data scrape, regressions, tables, draft) in under one hour vs. months originally. UCLA hand-replication audit found correlation > .99 with Claude's data.
  - Three-layer architecture for getting from 10x to 100x: (1) **quantitative benchmarks** that let agents iterate autonomously (Netflix Prize analogy); (2) **prototype-and-test** rather than purely retrospective inference --- AI lets you *build* political tools and measure them in the world; (3) **open, forkable, machine-verifiable research artifacts** as living documents instead of static PDFs.
  - Examples of the new mode: Yiqing Xu and Leo Yang's automated empirical-replication workflow (compresses 3--4-year projects); refine.ink (Calvó López & Golub) doing referee-level review on John Cochrane's inflation paper; David Yanagizawa-Drott's Project APE attempting fully autonomous policy evaluation; Bridgewater's AIA Labs multi-agent forecasting; Karpathy's AutoResearch loop.
  - Three risks: (1) **speed kills rigor** --- AI-accelerated research can shape policy before errors are caught; AI review (refine.ink) might be the counter; (2) **AI narrows social science** by pulling research toward what's countable and away from interpretive/theoretical/qualitative; (3) **incentives lag** --- of 70 forks of Hall's open replication repo, Claude found "virtually none" did anything substantive; gating remains in journals and tenure committees.
  - Calls to action: AI labs should fund embedded researchers and train against replication packages; funders should redirect a small fraction of endowed-chair money to compute-funded open-research labs; researchers should stop waiting for permission.

- **Summary**

Hall, a Stanford political economist, frames the current moment as a step change in social-science research productivity, illustrated by the speed of his own work and his fellows'. The headline claim is that individual researchers are already producing roughly 10x as much rigorous empirical output as a year ago, but that getting to 100x requires building new institutions, not just using the tools harder.

The most concrete demonstration is Hall's auto-replication of his 2020 vote-by-mail PNAS study: Claude Code scraped Secretary-of-State data from California, Utah, and Washington, pulled ACS demographics, identified policy-adoption events, ran the DiD specification, and produced a draft paper --- replicating all twelve coefficients exactly --- in under an hour. A UCLA PhD student then audited every line against a manual replication and found > .99 correlation. Hall layers in many other examples (Joshua Gans going AI-first; Yascha Mounk drafting publishable political theory in two hours; Project APE; refine.ink finding a sign error in Cochrane's differential equation).

Most of the piece is a design proposal for what a "100x research institution" would look like: quantitative benchmarks for the subset of social-science questions where they're feasible (election forecasting, policy effects, model-bias evaluation); a shift toward prototype-and-test research where AI lets you *build* political tools rather than only study existing variation (Hall's lab built a Dictatorship Eval, an election-night trading dashboard, and an experiment on whether AI agents become "Marxist" under bad working conditions); and open, forkable, continuously-updated research artifacts replacing static PDFs.

He is candid about the obstacles. The forking story is striking: 70 forks of his open replication repo, virtually all dormant. Tools are not the bottleneck; incentives are.

- **Relevance to Economics Research**

Highly relevant. Hall's vote-by-mail replication is the cleanest published demonstration to date that an agent can run a full DiD pipeline (web scraping, panel construction, fixed-effects regression, table production, draft writing) at near-zero marginal cost on data the original researcher hadn't already curated. For empirical economists, this directly raises the question of what the *new* publishable bar should be. The piece also names tools the wiki has been tracking: refine.ink (Golub), Project APE (Yanagizawa-Drott), Xu's automated-replication system, AutoResearch (Karpathy), and Bridgewater's multi-agent forecasting. The risk that AI narrows social science toward the quantifiable is the most actionable concern for econ specifically: the credibility revolution already favors clean identification over big questions, and AI may amplify that drift.

- **Related Concepts**
  - [[concepts/agentic-workflows]]
  - [[concepts/automated-research]]
  - [[concepts/ai-adoption-academia]]
  - [[concepts/ai-peer-review]]
  - [[concepts/ai-research-tools]]

- **Related Summaries**
  - [[summaries/academics-wake-up-3]]
  - [[summaries/andrews-ai-research]]
  - [[summaries/automated-research-finance]]
  - [[summaries/prompts-to-paper]]
  - [[summaries/ai-powered-scholarship]]
  - [[summaries/agentic-everything]]
