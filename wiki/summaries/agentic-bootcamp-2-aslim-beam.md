---
title: "Agentic AI Bootcamp — Session 2: Research Workflows, Teaching & Applications"
tags: [summary, claude-code-skills]
sources:
  - "[[raw/pdfs/session_2_slides.pdf]]"
date_updated: 2026-05-15
date_published: 2026-04-27
---

- **Author/Source**: Erkmen G. Aslim & Emily Beam (Department of Economics, University of Vermont)
- **Original**: Session 2 of the *Thinking with Agents* bootcamp, April 27, 2026, Old Mill A500. Course page: [thinkingwithagents.github.io](https://thinkingwithagents.github.io/). Skills used in the deck are installable via `npx skills add thinkingwithagents/skills`. See [[thinking-with-agents]] and [[agentic-bootcamp-1-aslim-beam]].

## Key Ideas

- **Setup is two installs**: (1) Anthropic's marketplace skills bundle (`/plugin marketplace add anthropics/skills` then install `document-skills@anthropic-agent-skills` — gives `pdf`, `docx`, `pptx`, `xlsx`, `frontend-design`, `skill-creator`, `algorithmic-art`); (2) the bootcamp's economist pack (`npx skills add thinkingwithagents/skills`, optionally with `--skill <name>`). Note: `/skill-creator` is not bundled with Claude Code by default — it ships inside `document-skills` and must be installed before App 3.
- **One project, three use cases.** The session uses a single in-progress paper — a Bangladesh remote-education RCT (TV instruction, adaptive edtech, data subsidies, teacher support during COVID closures, rejected from 8 journals — eight) — to demo three independently-useful workflows.
- **Code audit (Application 1)**: 51 do-files across 4 subdirectories, master file from June 2021 (5 years stale), date-and-author-stamped filenames (`_07sep`, `_eb`), no docs, no version control. *"Extremely common in economics."* One prompt to Claude (clean replication, archive everything, build a comparison test harness, no results should change) → 51 → 8 do-files, 86 old variants archived (nothing deleted), config template, Git init, full documentation. **Time: ~2 Claude Code sessions vs. days minimum by hand.**
- **The `$flags` bug** (caught by `/code-review`): a 17-element list of missing-value indicators used as controls in *every* regression. In 3 of 5 scripts, one indicator was missing the `_f_` prefix — `_c_child_work` instead of `_f_c_child_work` — so `_c_child_work` appeared *twice* in regressions and the actual missing-flag was never included. **Survived 10+ versions across 2+ years. No error, no crash — just quietly wrong.** `/code-review` found it by cross-referencing every global definition across all files in a single parallel-agents pass.
- **Paper audit with `/econ-audit` (Application 2)**: a reusable adversarial-review skill that reads the full paper (LaTeX + tables + appendix) and acts as a skeptical referee. Five check categories: identification (causal claim valid?), statistics (MHT, power, attrition), measurement, methodology consistency, presentation. Produces a structured audit in ~60 seconds.
- **AI vs. real referees (the headline result)**: 11 referee reports across 8 journals over 4 years vs. 60 seconds of `/econ-audit`. **Score: 5 full matches, 2 partial, 1 opposite recommendation, 2 misses.** Caught: high attrition (suggested Lee bounds), noisy 8-item learning measure, MHT, complex randomization, deviations from PAP. Missed: short-duration norms (4–8 weeks is unusually short for an education RCT — requires field knowledge), internal contradictions (the data arm increased tutoring more than info but only info improved learning), "COVID fatigue" (publication-landscape signal).
- **The "opposite advice" warning**: AI recommended *including* the conceptual model. Every real referee wanted it cut. **Sometimes AI gives exactly the wrong recommendation because it lacks field conventions.** Pattern: AI is reliable on statistical/econometric issues; weak on field knowledge, within-paper logic, and publication strategy.
- **`/econ-audit` vs. `/review-paper` have zero overlap** — the audit caught 6 things invisible without reading Stata code (FE discrepancy in table notes, wrong index variable in appendix, varying N across columns, CV-fold discrepancy, the `$flags` typo); the paper review caught 8 things requiring referee-style reading (attrition severity, marginal q=1.000, indirect mechanism chain, causal language too strong, IRT reliability from short test). **Run both.**
- **Lee bounds, live (Application 3)**: the most-common referee request from the audit was "do Lee bounds." One prompt to Claude — "I need Lee (2009) bounds for the App treatment arm vs. control. Outcome is the learning index. Use the endline survey flag for attrition. Write a Stata do-file, run it, show me upper/lower bounds with CIs" — produced a working `do`-file (installed `leebounds` via `ssc install`, restricted sample, built outcome, ran bounds). **Result: bounds spanned zero for all three outcomes; differential attrition (-9.6pp) was large enough to make Lee bounds uninformative. From referee comment to answer: ~10 minutes.**
- **Lecture-builder skill (Application 3 on Erkmen's side, App 3 in the deck for teaching)**: built using `/skill-creator`, which interviews the user (4–6 design questions on name, audience, inputs, outputs, edge cases, where to save), then writes `SKILL.md` + supporting scripts to `.claude/skills/lecture-builder/`.
- **Anatomy of `lecture-builder/`**: `SKILL.md` (playbook) + `parse_document.py` (PDF/DOCX reader) + `slide_template.tex` (UVM Beamer) + `notes_template.md` (notes scaffold). What `SKILL.md` enforces: chunked reading for token control, mandatory citations from source PDFs, undergrad-vs-grad tone toggle, dual output (notes + slides), reuse of UVM color palette. **Key principle: skills with Python scripts beat pure-markdown skills when tokens matter — the script reads, the LLM synthesizes.**
- **The execution prompt is concrete**: "I have a folder ./inputs/ with: gov_thinktank_ice_arrests.pdf, ice_enforcement_report.pdf, aslim_paper.pdf. Build a 50-minute undergraduate lecture on the labor and health consequences of ICE enforcement. Audience: junior/senior econ majors with intermediate micro and one applied econometrics class. Outputs to ./outputs/: (1) `lecture_notes.md` with 5 takeaways, 4 discussion prompts, 3 candidate exam questions; (2) `lecture_slides.tex` Beamer 16:9, ~20 slides, clean academic palette, in-text citations to all three PDFs. Be conservative with tokens: parse each PDF in chunks via parse_document.py, summarize per-section, then synthesize." **Audience spec + output spec + token discipline.**
- **Why a heterogeneous input mix** (policy + government + academic): forces the skill to harmonize tone, terminology, and evidence quality — mirrors how you'd actually build a lecture. The example topic (labor and health consequences of ICE enforcement) connects to ongoing UVM research.
- **Under the hood**: `parse_document.py` reads in chunks → LLM synthesizes. The principle generalizes: **skills with deterministic helper scripts > pure-prompt skills** whenever the input is large or repetitive.

## Summary

Session 2 is the applied half of the *Thinking with Agents* bootcamp, organized around three use cases on a single in-progress paper (a rejected-eight-times Bangladesh remote-education RCT) plus a parallel teaching track from Erkmen.

The research half makes a tight case for skills as professional-grade infrastructure rather than parlor tricks. The code audit reduced 51 stale do-files to 8 clean ones in two Claude sessions — and along the way `/code-review` cross-referenced every `global` definition and surfaced a missing-prefix typo in the `$flags` controls list that had quietly survived 10+ versions across two years. The paper audit with `/econ-audit` was benchmarked against 11 actual referee reports collected over four years and 8 journals; in 60 seconds it produced full matches on 5 critiques, partial on 2, and one opposite recommendation. The misses (short-duration norms, internal contradictions, "COVID fatigue") map cleanly onto field knowledge, within-paper logic, and publication strategy — exactly where one would expect AI to be weak. The session closes the loop by acting on the audit's top suggestion (Lee bounds) live in ~10 minutes, finding that differential attrition was large enough to make the bounds uninformative.

The teaching half builds rather than uses: Erkmen walks through `/skill-creator`'s 4–6-question interview to produce a `lecture-builder` skill that converts a folder of mixed PDFs (policy + government + academic) into both lecture notes and a Beamer deck in UVM colors. The architectural payoff line is "skills with Python scripts beat pure-markdown skills when tokens matter — the script reads, the LLM synthesizes," which generalizes well beyond lecture building.

## Relevance to Economics Research

This is the most concrete head-to-head benchmark in the wiki between an AI auditing skill and the actual referee process. The 11-reports-vs-60-seconds comparison is honest about both wins (5/10 full matches on statistical/econometric issues) and losses (field-norm misses, one inverted recommendation), and the recommendation pattern is the right one for a researcher: **run `/econ-audit` before submitting, but keep field-knowledgeable colleagues in the loop**. The code-audit half is a separate value proposition — for any economist sitting on a multi-year accumulated do-file pile, the 51-to-8 reorganization plus a real-bug catch is a credible argument for the time investment. The lecture-builder demo doubles as a generic template for any "convert mixed-source documents → polished output" skill.

## Related Concepts

- [[concepts/claude-code-skills]]
- [[concepts/ai-peer-review]]
- [[concepts/automated-research]]
- [[concepts/reproducibility-transparency]]
- [[concepts/ai-research-tools]]
- [[concepts/empirical-methods]]
- [[concepts/ai-in-education]]
- [[concepts/skills-vs-agents]]
- [[concepts/human-in-the-loop]]
- [[concepts/ai-limitations]]

## Related Summaries

- [[summaries/thinking-with-agents]] — course landing page
- [[summaries/agentic-bootcamp-1-aslim-beam]] — Session 1 (concepts)
- [[summaries/refine-ink-golub]] — Brunnermeier/Golub's parallel AI referee tool
- [[summaries/coarse-ink]] — Van Dijcke's open-source AI paper reviewer
- [[summaries/cc-series-44-four-criteria-referee]] — Cunningham on AI referee criteria
- [[summaries/brownbag-claude-skills]] — Spina on skills for academic researchers
- [[summaries/skill-library]] — Blattman on skill libraries
- [[summaries/building-skills]] — Blattman on building skills
- [[summaries/cc-series-13-skills-split-pdf]] — Cunningham on skills + PDF processing
- [[summaries/velikov-smeal-cop]] — parallel synthesis talk citing many of the same skills
