---
title: "EconYoloBox: Sandboxed YOLO-Mode Environment for Economics Research"
tags: [summary, foundations-setup, sandboxing, docker, claude-code, codex, autonomous-agents]
sources:
  - "[[raw/articles/chenandrewyEconYoloBox.md]]"
date_updated: 2026-10-27
date_published: 2026
---

- **Author/Source**: Andrew Y. Chen (Federal Reserve Board), GitHub repo
- **Original**: [https://github.com/chenandrewy/EconYoloBox](https://github.com/chenandrewy/EconYoloBox)

- **Key Ideas**
  - **AI use is a risk-return tradeoff.** Chen's chart puts *no AI → web copy-paste → manual approval mode → YOLO with no container* along a frontier. YOLO mode *inside a container* is meant to sit above that frontier: close to full autonomy with much less risk.
  - **Two containers, one workspace.** A **YOLO** container runs Claude Code and Codex with no permission prompts, behind a firewall allowlist (`.devcontainer/init-firewall.sh`) with filtered system calls. A **normie** container has open internet and uses Claude auto mode or Codex `auto_review` for work YOLO blocks, such as browsing arbitrary sites and installing packages. Both mount the same files and can run at the same time.
  - **Shared package volumes, read-only in YOLO.** R, Python, TeX Live and the VS Code extensions live in Docker volumes. Normie can write to them; YOLO can only read them. Anything installed in normie works in YOLO, but a YOLO agent can't install a package, including a malicious one.
  - **One box for all research.** Chen prefers one large container over one per project, especially for volatile projects synced through Dropbox. Active projects live in `workshop/`, finished ones in `hangar/` and literature in `cellar/`. Each project is its own git repo, and the outer repo ignores all three folders.
  - **One command interface.** Paired host shortcuts open each tool in either mode: `ybe`/`nbe` (shell), `ybcode`/`nbcode` (VS Code), `ybcc`/`nbcc` (Claude Code), `ybgpt`/`nbgpt` (Codex). There is a security caveat: run YOLO agents from a host terminal, because attaching VS Code to the YOLO container can expose its host credential relay.
  - **Economics tooling built in:** an image tuned for fast R and Python package installs, a custom **OpenAlex** citation-lookup tool, **Mistral OCR** PDF-to-Markdown conversion (credited to Don Bowen), and credential setup for WRDS, Mistral and OpenRouter.
  - **Practical costs:** macOS plus Docker Desktop plus VS Code Dev Containers (Windows and Linux untested), about 1.5 GB for the image plus about 5.7 GB of volumes, and the AI CLIs live in a persistent volume and must be updated by hand.
  - **"AIs are like human co-authors"** and **"AI changes constantly"**: the repo will change often, with dated release tags (`vYYYY.MM.DD`), and Chen warns against pulling blindly.

- **Summary**

EconYoloBox is Chen's personal research environment, published as a dev-container template. Chen says it was "built by obsessively improving my research workflow (instead of doing actual research work)." Its premise is that the efficient way to use coding agents is to let them run without approval prompts, and that this is only reasonable when the environment itself limits the damage. It builds on the sandboxing arguments in [[summaries/permissions-sandboxes-substack]] and [[summaries/claude-container]] but adds two refinements. First, it pairs a locked-down YOLO container with a permissive normie container on the same files, so the usual reasons for leaving the sandbox (installing a package, reading a blocked website) never require turning the sandbox off. Second, the package stacks are writable only from normie, which closes the supply-chain risk of an unattended agent installing whatever it finds.

The README is mostly a setup walkthrough: install Docker Desktop and VS Code, reopen the cloned repo in its dev container (build normie first), create projects under `/yolobox/workshop/`, start agents in normie for the first login, then register the host `yolobox` commands for everyday YOLO use. Optional steps add research credentials, the rest of the R, Python and TeX package stack, and notes on Docker storage and garbage-collection budgets.

- **Relevance to Economics Research**

This is the most complete off-the-shelf sandbox in the wiki for economists who want agents to run long, unattended jobs such as data cleaning, replication and paper builds without approving every command and without giving the agent their whole home directory. The single-box design suits how many economists actually work: many concurrent projects synced through Dropbox, sharing one R, Python and LaTeX stack. The built-in OpenAlex and OCR tools cover two common bottlenecks, reliable citations and reading PDFs. Note that the container limits what the agent can *do*, not what data it *sees*. Confidential data mounted into the box still goes to the model provider (see [[concepts/data-privacy]]).

- **Related Concepts**
  - [[concepts/agent-sandboxing]]
  - [[concepts/claude-code]]
  - [[concepts/data-privacy]]
  - [[concepts/ide-and-terminal]]
  - [[concepts/citation-hallucination]]
  - [[concepts/document-processing]]

- **Related Summaries**
  - [[summaries/claude-container]]
  - [[summaries/permissions-sandboxes-substack]]
  - [[summaries/permissions-openclaw-markus-162-7]]
  - [[summaries/privacy-setup]]
  - [[summaries/ralph-wiggum-asset-pricing]]
  - [[summaries/prompts-to-paper]]
  - [[summaries/backman-vscode-guide]]
