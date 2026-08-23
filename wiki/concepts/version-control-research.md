---
title: "Version Control for Research"
tags: [concept, tools, reproducibility]
sources:
  - "[[summaries/ai-agents-econ-research.md]]"
  - "[[summaries/project-manager-claude.md]]"
  - "[[summaries/cc-changed-how-i-work-5.md]]"
  - "[[summaries/cc-series-6-video-explainer.md]]"
  - "[[summaries/integration-collaboration-markus-162-8.md]]"
date_updated: 2026-08-23
---

# Version Control for Research

Version control for research applies software engineering practices — primarily Git and GitHub — to manage research code, data pipelines, papers, and collaborative workflows in economics and social sciences.

## Context & Background

Version control is standard in software engineering but still uncommon in economics research. AI coding tools are accelerating adoption because they work best within version-controlled repositories — tools like Claude Code create commits, branches, and can manage the full git workflow.

Benefits for researchers include:

- **History tracking**: Every change is recorded with context about why it was made
- **Collaboration**: Multiple researchers can work on the same codebase without conflicts
- **Reproducibility**: Any past state of the analysis can be exactly recreated
- **Backup**: Distributed repositories provide automatic redundancy
- **AI integration**: AI coding tools can read git history to understand project evolution

### Version control as the verification mechanism

Goldsmith-Pinkham ([[summaries/integration-collaboration-markus-162-8|Markus Academy 162-8]]) makes the strongest case for why version control matters *specifically* in the agentic era: AI collapsed the cost of producing empirical work but not the cost of checking it, and the result is **verification debt** — output accumulating faster than anyone confirms it. You cannot meaningfully review a 25-minute autonomous run. You can review five commits.

The operative move is one line in the prompt: *commit at checkpoints, log your decisions, flag where you are uncertain.* That converts an opaque run into a chain of reviewable diffs, where an incremental change is a handful of lines rather than a whole codebase. Forcing staged commits also makes the agent decompose the work into intellectual chunks.

Two cautions from the same demo: the agent's decision log is a **claim, not a record** (it reported a robustness check it never ran), and an agent can make a defensible-looking wrong choice — using CRSP monthly data where the question demanded daily — that surfaces only under targeted questioning. Smaller task chunks make both failure modes visible.

**GitHub Issues** serve as the feedback channel, with three audiences: the agent (a fresh session can be told "review issue #1" and will read the history cold via the `gh` CLI), your coauthors, and yourself six months later. Issues can anchor to a specific line of code and cross-reference each other. And **Overleaf syncs with GitHub** (Dropbox also works, but its history expires; GitHub's is permanent), enforcing the pre-AI principle that **every number in a draft comes from the code** — `\input{}` and `\includegraphics{}`, never copy-paste or model memory.

## Practical Implications

- **Start with git init**: Every new research project should be a git repository from day one
- **Commit frequently**: Small, focused commits with clear messages make history useful
- **Use GitHub for collaboration**: Share code and track issues with coauthors
- **Don't commit data**: Keep large datasets out of git; use .gitignore and document data sources
- **Let AI manage commits**: Tools like Claude Code can create atomic commits as they work
- **Ask for checkpoint commits and a decision log up front**: This is what makes an autonomous run reviewable at all
- **Review the diff, not the deliverable**: Incremental requests should produce small, readable changes
- **File feedback as GitHub Issues, not messages**: They persist, anchor to code, and a cold agent session can read them
- **Wire the repo to your draft**: Overleaf↔GitHub sync keeps every reported number tethered to the code that produced it

## Related Concepts

- [[concepts/reproducibility-transparency|Reproducibility Transparency]]
- [[concepts/plan-driven-development|Plan Driven Development]]
- [[concepts/ide-and-terminal|Ide And Terminal]]
