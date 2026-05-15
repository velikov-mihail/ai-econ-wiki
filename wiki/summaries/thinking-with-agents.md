---
title: "Thinking with Agents (UVM Agentic AI Bootcamp)"
tags: [summary, foundations-setup]
sources:
  - "[[raw/articles/Thinking with Agents.md]]"
date_updated: 2026-05-15
date_published: 2026-04-22
---

- **Author/Source**: Erkmen G. Aslim & Emily Beam (Department of Economics, University of Vermont)
- **Original**: [thinkingwithagents.github.io](https://thinkingwithagents.github.io/) — landing page for a two-session agentic-AI bootcamp delivered at UVM in April 2026, with companion slide PDFs, prep guide, and an applications gallery of reusable skills

## Key Ideas

- **A two-session agentic-AI bootcamp for economists**, hosted by the UVM Department of Economics. Session 1 (April 22, "Getting Started with AI Tools") is the conceptual on-ramp; Session 2 (April 27, "Research Workflows, Teaching & Applications") is the applied demo of reusable skills on a live paper.
- **No installation required to attend** — the prep guide ([Getting Set Up](https://thinkingwithagents.github.io/prep.html)) handles install for those who want to follow along, and an [Outside Resources](https://thinkingwithagents.github.io/resources.html) page collects further reading.
- **Session 1 covers the core agentic concepts**: chat AI vs. agentic tools, the context window, standing instructions, planning, voice files, skills, and live demos (website redesign + custom skill creation). Detailed in [[agentic-bootcamp-1-aslim-beam]].
- **Session 2 is the applied half**, organized around two streams: Emily on **research workflows** (auditing a replication package with [`/code-review`](https://thinkingwithagents.github.io/applications.html#code-review), paper auditing with [`/econ-audit`](https://thinkingwithagents.github.io/applications.html#econ-audit) and [`/review-paper`](https://thinkingwithagents.github.io/applications.html#review-paper), running Lee bounds live), and Erkmen on **teaching & applications** (lecture-builder skill via [`/academic-beamer-deck`](https://thinkingwithagents.github.io/applications.html#academic-beamer-deck), idea stress-testing with [`/research-brainstorm`](https://thinkingwithagents.github.io/applications.html#research-brainstorm), web scraping with [`/find-data`](https://thinkingwithagents.github.io/applications.html#find-data)). Detailed in [[agentic-bootcamp-2-aslim-beam]].
- **"What to try next" homework** is concrete and low-stakes: try a data-exploration → analysis-plan workflow on your own data, draft an assignment, run `/econ-audit` on a paper before submission, or use Claude Code to revise a draft.
- **Skills are distributed as an installable bundle** — `npx skills add thinkingwithagents/skills` pulls the full economist pack; individual skills can be added with `--skill <name>`. This makes the bootcamp's playbooks reusable across institutions, not just UVM.

## Summary

This is the landing page for *Thinking with Agents*, a two-session agentic-AI bootcamp run by Erkmen G. Aslim and Emily Beam at the University of Vermont's Department of Economics in April 2026. The page is a thin index — its real content lives in the two slide decks (linked) and a separate [applications gallery](https://thinkingwithagents.github.io/applications.html) where each `/`-named skill (e.g., `/code-review`, `/econ-audit`, `/research-brainstorm`, `/find-data`, `/academic-beamer-deck`) gets its own page with the SKILL.md spec and a usage walkthrough.

The pedagogical structure is "concepts first, applications second." Session 1 takes attendees from chat-AI to agentic tools, introduces the context window as the load-bearing concept, walks through planning files, and lands on safety/permissions. Session 2 then demos those concepts on a real paper-in-progress (a Bangladesh remote-education RCT) — code audit, adversarial paper review, and a live "do Lee bounds" exercise from referee comment to results — followed by a teaching-side build of a `lecture-builder` skill via `/skill-creator`.

The site is positioned as a course-in-a-box: anyone can install the skill bundle, run through the prep guide, and replicate the bootcamp at their own institution. It is the closest thing in the wiki to a turn-key agentic-AI-for-economists curriculum.

## Relevance to Economics Research

Most "AI for economists" resources in the wiki are individual posts or talks. *Thinking with Agents* is unusual because it ships **executable infrastructure** — installable skills with versioned SKILL.md files — alongside the slides. For a faculty member running an internal AI workshop, this is a near-complete starter kit: two 90-minute sessions of slides, a prep guide, an outside-resources reading list, and a one-line install for the skills demoed. The bootcamp also models a realistic adoption arc (concepts → research workflows → teaching tools), making it useful both as a curriculum to copy and as a pattern for what to teach in what order.

## Related Concepts

- [[concepts/ai-skills]]
- [[concepts/claude-code-skills]]
- [[concepts/claude-code]]
- [[concepts/ai-agents]]
- [[concepts/ai-workflows]]
- [[concepts/ai-adoption-academia]]
- [[concepts/ai-in-education]]

## Related Summaries

- [[summaries/agentic-bootcamp-1-aslim-beam]] — Session 1 deck (concepts: chat vs. agentic AI, context, planning, safety, voice files)
- [[summaries/agentic-bootcamp-2-aslim-beam]] — Session 2 deck (applications: /code-review, /econ-audit, Lee bounds, /skill-creator, /find-data)
- [[summaries/brownbag-claude-skills]] — Spina's parallel skills-for-academics brownbag
- [[summaries/baylor-ai-taskforce]] — Cunningham on encouraging faculty AI adoption
- [[summaries/velikov-smeal-cop]] — Velikov's Smeal Community-of-Practice talk (similar adoption-oriented synthesis)
