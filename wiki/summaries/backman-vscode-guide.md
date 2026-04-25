---
title: "Claude Code in VS Code — For Academic Economists"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Claude Code in VS Code — For Academic Economists.md]]"
  - "[[raw/articles/Claude Code in VS Code — For Academic Economists 1.md]]"
date_updated: 2026-04-25
date_published: 2026-04
---

- **Author/Source**: Claes Bäckman (Aarhus University), [claesbackman.com](https://claesbackman.com/claude-code-guide.html)
- **Original**: [https://claesbackman.com/claude-code-guide.html](https://claesbackman.com/claude-code-guide.html)

## Key Ideas

- A five-step VS Code installation walkthrough specifically aimed at empirical economists working in R, Stata, Python, and LaTeX — open the Extensions panel, install the official Claude Code extension, sign in, and open your **full project folder** (not a single file) so the agent can see the whole tree.
- A "starter pack" of VS Code extensions covering the empirical research stack: `tmonk.stata-workbench` (with its MCP server so Claude can run Stata commands and inspect stored results), the standard Python toolchain (`ms-python.python`, `pylance`, `debugpy`, `python-envs`), `james-yu.latex-workshop` for LaTeX, `mechatroner.rainbow-csv` for data files, and `tomoki1207.pdf` for inline PDF viewing.
- A practical case for **installing Python even if you don't write Python**: many everyday research-friction tasks (PDF→markdown, reshaping CSVs, scraping tables, pulling FRED series) are best solved by short Python scripts that Claude writes and runs on your behalf. Python becomes "general-purpose glue."
- A file-format triage table — which formats Claude reads natively (`.md`, `.txt`, `.tex`, `.bib`, `.csv`, `.py`, `.R`, `.do`, `.ipynb`), which need conversion (`.docx` via `pandoc`, `.xlsx`/`.dta`/`.rds` via short scripts), and which are problem cases (PDFs, especially scanned or equation-heavy ones).
- Detailed PDF guidance: born-digital PDFs are usually fine; long PDFs (50+ pages) should be converted to markdown first to save context; scanned PDFs need OCR (`ocrmypdf`); equation/table-heavy PDFs are the hardest case — prefer the `.tex` source if available. Tools recommended: `pandoc`, `marker`, `MinerU`, `docling`, or a custom `/pdf-to-markdown` skill.
- `CLAUDE.md` is presented as the highest-leverage one-time setup: a project-root file that loads automatically every session and tells Claude about data, sample definitions, conventions, and writing voice. The article distinguishes computer-level (`~/.claude/CLAUDE.md`) from folder-level files, and recommends `/init` to bootstrap one.
- **Skills as reusable workflows**: each skill is a folder containing a `SKILL.md` file; the folder name becomes the slash command. The article points readers to three economist-relevant skill libraries: Bäckman's own `AI-research-feedback`, Cunningham's `MixtapeTools` (with `/beautiful_deck`), and Blattman's `/done` and other research-workflow skills.
- A LaTeX cleanup snippet for `.vscode/settings.json` that auto-deletes `.aux`, `.bbl`, `.log`, `.fls`, etc. after every successful build via `latex-workshop.latex.autoClean.run`.
- Context-window management advice: scope reads to the file you're editing (`@02_analysis.R fix the clustering`), use `+`/`/clear` for fresh conversations, and check `/context` for usage. `CLAUDE.md` keeps prompts short by avoiding repeated re-explanation.

## Summary

This is a practical, end-to-end onboarding guide written by Claes Bäckman (Aarhus University) for academic economists who want to use Claude Code inside VS Code rather than as a bare terminal CLI. The piece is organized as a roadmap: install in five steps, install the right extensions for your research stack, configure file-format conventions, set up persistent context with `CLAUDE.md`, build reusable workflows as skills, and finally manage the context window so performance doesn't degrade on large projects. Mac/Windows differences are flagged inline.

The extension recommendations are unusually specific to economics workflows. The Stata section pushes `tmonk.stata-workbench` and emphasizes its MCP server, which lets Claude execute Stata commands and read stored results — a meaningful jump beyond Claude just reading `.do` files as text. The LaTeX section pairs `latex-workshop` with a `markdown-pdf` companion for quick memos, and includes a `settings.json` snippet to auto-clean build artefacts. The Python section makes the case for installing Python even if you don't write it: Claude treats Python as a universal glue language for converting documents, scraping tables, and pulling APIs.

The middle of the guide is a file-format reference (native vs. needs-conversion vs. problem) with detailed PDF handling — born-digital, long, scanned, and equation/table-heavy each get tailored advice. The closing sections cover `CLAUDE.md` (computer-level vs. folder-level, with templates), skills (with a community-skill library and a pointer to `disable-model-invocation` for users who don't want auto-invocation), git integration (the agent is git-aware but git is optional — Dropbox folders work too), and context-window hygiene.

## Relevance to Economics Research

This is one of the most directly empirical-economist-focused setup guides in the wiki. Where Goldsmith-Pinkham, Sant'Anna, and Blattman emphasize particular workflows, Bäckman fills the gap of a complete, opinionated VS Code starter — including the Stata-via-MCP path, which most other guides do not cover. The PDF-handling section is especially relevant: PDFs of codebooks, FOMC statements, and 10-Ks are common research inputs, and the rule of "convert once, commit the markdown" is good hygiene that translates immediately to project workflow. The community-skill pointers (Bäckman's own `AI-research-feedback`, Cunningham's `MixtapeTools`, Blattman's `/done`) give a curated entry point into the economist Claude Code ecosystem.

## Related Concepts

- [[concepts/claude-code]]
- [[concepts/claude-md-files]]
- [[concepts/claude-code-skills]]
- [[concepts/ide-and-terminal]]
- [[concepts/document-processing]]
- [[concepts/context-management]]

## Related Summaries

- [[summaries/setup-vs-code]]
- [[summaries/install-mac]]
- [[summaries/install-windows]]
- [[summaries/my-claude-code-setup]]
- [[summaries/feedback-machines]]
- [[summaries/ai-research-feedback-skills]]
- [[summaries/getting-started-economists]]
- [[summaries/real-claude-md]]
