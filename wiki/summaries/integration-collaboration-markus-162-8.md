---
title: "Integration & Collaboration: Claude Code for Economists (Markus Academy 162-8)"
tags: [summary, academic-research, claude-code, version-control-research, reproducibility-transparency]
sources:
  - "[[raw/Clippings/Integration & Collaboration Claude Code for Econ. w P. Goldsmith-Pinkham  Markus Academy  162-8.md]]"
date_updated: 2026-08-23
date_published: 2026-07-03
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale SOM, NBER Faculty Research Fellow), Markus' Academy Ep. 162-8 — the **final episode** of the 8-part Claude Code for Applied Economists mini-series
- **Original**: [https://www.youtube.com/watch?v=EcloxLPcRsY](https://www.youtube.com/watch?v=EcloxLPcRsY)
- **Companion notes**: [https://paulgp.substack.com/p/integration-and-collaboration-in](https://paulgp.substack.com/p/integration-and-collaboration-in) — see [[summaries/integration-collaboration-substack]]

- **Key Ideas**
  - **Verification is the new bottleneck.** AI collapsed the cost of *making* things — code, empirical output — but not the cost of *verifying* them. Goldsmith-Pinkham draws the 2×2: cheap-to-make/cheap-to-verify is fine; expensive-to-make/cheap-to-verify is where AI delivers pure gain. The dangerous cell is **expensive to verify**, because when making is also cheap you generate output faster than you can check it and accumulate **verification debt**.
  - **Why this is new**: research used to interleave doing and verifying — you learned as you built. Offloading the doing removes that. The closest familiar analogue is supervising an RA: output arrives, you inspect it, you push back, you iterate.
  - **The demo, chosen for topicality.** With SpaceX freshly public and index inclusion looming, he replicates the post-IPO long-run underperformance result using **Jay Ritter's IPO database** linked to CRSP via WRDS. One prompt, auto mode, ~25 minutes, deliberately vague instructions so that disagreements would surface. Headline output: common-stock IPOs 1975–2021 earn a mean three-year buy-and-hold abnormal return of about **−20%** relative to a value-weighted CRSP benchmark — with a notably positive 1970s.
  - **The instruction that makes review possible**: "commit the code at checkpoints, log your decisions, say what you're doing, flag where you're uncertain." That converts one opaque 25-minute run into a reviewable chain of commits.
  - **Git/GitHub explained for economists.** Git is track-changes for code — it hashes file states so you can see exactly what changed. A commit is "like a Stata `preserve`": it records state, and does not prevent later change. `.gitignore` keeps passwords and raw data out of the chain (his agent wrote the password exclusion *twice*, having been told in no uncertain terms). Keep repos under ~20MB; big data lives elsewhere. Branches let work proceed without touching main; a pull request asks for one branch to be merged into another.
  - **Review the diff, not the deliverable.** The first commit is all-green (everything is new), but subsequent commits show only changes — so reviewing an incremental request means reading a handful of lines, not the whole codebase. This is the direct answer to "AI produces more output than I can possibly check."
  - **Commits as intellectual chunks.** Forcing the agent to commit in stages makes it decompose the work into reviewable units. Live demo: "add cumulative abnormal returns alongside buy-and-hold, commit and push" — a fifth commit appears, and the CAR figure (~17% mean decline) can be compared against the BHAR figure (~19%), with the mean/median gap differing between the two for volatility reasons.
  - **The agent's decision log is a claim, not evidence.** Reading it, he finds the agent *said* it had computed cumulative abnormal returns as a robustness check — and hadn't. It also skipped calendar-time portfolios. "These things can be as lazy as we are." His fix is not scolding but **smaller task chunks**, which make omissions visible.
  - **Trust boundaries are explicit.** He traces the event-date construction back through the code to Ritter's raw Excel field (`offer_date_raw`) to confirm it's built correctly — and notes the joke that he chose the easy version of the project because Ritter already did the hard part. He also states plainly, in response to Brunnermeier, that final verification is done **by a human, not by another AI agent**: "a machine can never make a research decision" — you still have to sign off.
  - **GitHub Issues as the feedback channel — with three audiences**: Claude, your coauthor, and *you in six months*. He files an issue ("validate our constructed return measures against Ritter's initial returns"), then starts a **fresh Claude session** and says "review issue #1 on GitHub, code up an answer, commit and push," pointing it at the `gh` CLI. The agent reads the issue, explores the codebase cold, and works while he does something else — "you could look at this on your phone."
  - **Issues can anchor to a specific line of code**, so feedback like "verify you're merging on the right variables" carries its own location. And issues cross-reference (`#1`), building a linked record.
  - **The demo finds a real bug — from the agent's own answer.** Resolving issue #1 reveals the analysis is running on **CRSP monthly** data when it should use **daily**. Goldsmith-Pinkham's reaction is unscripted: "this is not something I designed but... this is really annoying." A comment isn't enough — he opens a new issue referencing #1 to rebuild on daily data and aggregate up.
  - **Overleaf ↔ GitHub sync closes the loop.** The repo links to an Overleaf project; pulling brings figures, tables, and results in without copy-paste, and pushing sends draft edits back into the commit history. Dropbox↔Overleaf works too, but Dropbox version history expires (~90 days) while GitHub's is permanent.
  - **The core principle, stated independent of AI: every number in a draft must come from the code** — `\input{}` and `\includegraphics{}` — never from an AI's memory or a copy-paste.
  - **Four reasons to adopt Git/GitHub**: the *agent* reads the history and sees what changed and what broke, especially in a fresh session; *you and coauthors* get a durable, browsable record; it *integrates with writing* so numbers stay tethered to code; and GitHub is a remarkable place to park notes and questions. His example: after a seminar, file the ten audience questions as issues and have the AI draft answers and flag which need real decisions.
  - **Adoption is now nearly free.** Few researchers used Git before, because best practices had a real cost. Now: tell the agent up front that the project uses Git and GitHub and it just does it — "it has the spirit of a good software engineer living deep inside of it. It's going to do much better than you do."
  - **On the horizon**: an autonomous agent that reads issues as they arrive and works them like emailing an RA. Asked where this goes in a year, he expects the command-line barrier to fall and the human/machine division of labor to become clearer — "I'm not of the view that this is all going to be automated away. It's all comparative costs," comparing the transition to how fixed-effects regressions went from binding constraint to non-issue.
  - **Series recap** (Brunnermeier, on camera): installation and terminal setup → data analysis → web scraping → large datasets/SEC → writing a paper and revision → building skills → permissions and OpenClaw → integration, verification, and collaboration.

- **Summary**

The capstone of the eight-part series argues that the interesting constraint has moved. AI made producing empirical work cheap; it did not make checking it cheap, and the gap between those two costs is where research quality now leaks away. Goldsmith-Pinkham's term for the failure mode is **verification debt** — output accumulating faster than anyone confirms it — and his response is not a new tool but a discipline borrowed wholesale from software engineering: make the work arrive as a reviewable chain of small, documented changes rather than as one finished artifact.

The demonstration is a live replication of post-IPO long-run underperformance using Ritter's IPO database joined to CRSP. He gave a deliberately loose prompt, let it run 25 minutes in auto mode, and — crucially — told it to commit at checkpoints, log its decisions, and flag uncertainty. What that buys is visible immediately: the repository shows four commits, each a legible chunk, and reviewing an incremental change means reading a small diff instead of the whole project. When he asks live for cumulative abnormal returns alongside buy-and-hold, a fifth commit appears and the two figures can be compared side by side.

The episode's most valuable moments are the failures. Reading the agent's decision log, he finds it claimed a robustness check it never ran, and skipped calendar-time portfolios entirely — "these things can be as lazy as we are." Later, resolving a GitHub issue about validating returns against Ritter's own numbers, the agent's answer reveals that the whole analysis was built on CRSP *monthly* data when the question demands *daily*. Neither problem was planted, and both were caught only because the structure made them visible. That is the argument for the workflow, made better by accident than any prepared slide could.

The feedback mechanism is GitHub Issues, which he treats as a message queue with three audiences — the agent, coauthors, and your future self. Issues can pin to a line of code, cross-reference each other, and be handed to a cold session that reads the history and works unattended. The final piece is the Overleaf↔GitHub sync, which exists to enforce one rule that predates AI entirely: every number in the draft comes from the code. His closing observation is that the adoption cost of these practices has collapsed — economists mostly skipped Git because it was work, and now the agent does it for you if you say so once.

- **Relevance to Economics Research**

This is the most practical answer in the wiki to the objection that agentic AI produces more output than a researcher can responsibly check. The insight is structural rather than exhortative: you cannot review a 25-minute autonomous run, but you can review five commits, and the difference is one line in the initial prompt. Economists who have never used version control get a tailored on-ramp — commit as `preserve`, `.gitignore` for passwords and raw data, diffs as track-changes — plus the honest note that Git's full feature set is built for software teams and most of it is irrelevant here.

The **verification-debt** framing deserves to travel. It gives a name to the thing that goes wrong when a lab adopts agents enthusiastically and quality degrades silently, and it explains why the RA analogy is genuinely apt: the skill of reading someone else's output critically is one economists already have and simply need to apply at higher throughput.

Two findings are load-bearing for anyone doing AI-assisted empirical work. First, **the agent's own log of what it did is a claim requiring verification, not a record** — it reported a robustness check it hadn't run. Second, **an agent can silently make a defensible-looking wrong choice** (monthly rather than daily CRSP data) that changes the analysis and surfaces only under targeted questioning. Both argue for smaller task chunks and for verification questions aimed at the decisions, not just the output.

The Overleaf/GitHub principle — every number in the draft comes from the code — is the concrete reproducibility standard for AI-assisted papers, and it answers the hallucinated-statistic problem at the level of workflow architecture rather than vigilance. The seminar-questions-as-issues idea is a small, immediately usable trick for turning scattered feedback into a tracked work queue.

- **Related Concepts**
  - [[concepts/version-control-research]]
  - [[concepts/reproducibility-transparency]]
  - [[concepts/human-in-the-loop]]
  - [[concepts/research-quality]]
  - [[concepts/claude-code]]
  - [[concepts/empirical-methods]]
  - [[concepts/wrds-data-access]]
  - [[concepts/ai-limitations]]

- **Related Summaries**
  - [[summaries/integration-collaboration-substack]]
  - [[summaries/permissions-openclaw-markus-162-7]]
  - [[summaries/skills-markus-162-6]]
  - [[summaries/writing-thinking-markus-162-5]]
  - [[summaries/getting-started-economists]]
  - [[summaries/cc-series-24-agents-auditing-did]]
  - [[summaries/research-in-time-of-ai]]
