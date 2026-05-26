---
title: "Skills: Specifying How an Agent Should Think (Substack companion)"
tags: [summary, claude-code-skills, claude-code, skills, sops]
sources:
  - "[[raw/articles/Skills Specifying How an Agent Should Think.md]]"
date_updated: 2026-05-26
date_published: 2026-05-23
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale SOM), Substack — companion to Markus Academy Ep. 162-6
- **Original**: [https://paulgp.substack.com/p/skills-specifying-how-an-agent-should](https://paulgp.substack.com/p/skills-specifying-how-an-agent-should)

- **Key Ideas**
  - Written companion to [[skills-markus-162-6|Markus Academy 162-6]], same five-part structure (what a skill is, where they live, how to develop one, where to find others, two warnings) but tightened and with explicit links to the Caldeisearch / "SOPs as Show Other People" framing.
  - **A skill = a long prompt as markdown**: "There is no separate skill engine." A skill is text that gets pulled into the context window when triggered. No new model capability — only standardized thinking across runs.
  - **Caldeisearch framing** (quoted): *"When you create a Claude Skill, you're not automating a task — you're teaching Claude your decision-making process… SOPs as 'Show Other People.' Whether those 'people' are junior employees or AI agents doesn't matter."*
  - **Folder structure**: `skills/paper-summary/` contains `SKILL.md` (instructions + frontmatter), and optionally `template.tex`, `examples/`, etc. The folder name = the skill name; `SKILL.md` is always the entry point.
  - **User-level vs project-level install**: `~/.claude/skills/` is available everywhere; `.claude/skills/` lives in a repo and travels with it (RAs and coauthors who clone get the skill). The author installs *very few* skills globally — descriptions of all global skills get loaded into every session's startup context, and overlapping triggers cause unwanted firings.
  - **Frontmatter discipline**: the description field is the *trigger*. "Use when the user says 'summarize this paper,' 'prep me for this seminar,' or hands over an econ paper" is a trigger. "Paper summary tool" is a title. Triggers belong in descriptions; titles belong in the body or filename.
  - **Five-step development workflow**: notice a task with recurring instructions → decide inputs → decide output structure (this is where most of the value lives) → write instructions (have Claude draft first, then edit) → test on real examples and revise.
  - **Worked example reproduced verbatim**: the `paper-summary` skill, run on Brunnermeier's *Optimal Unconventional Monetary Policy*. The TL;DR Claude produced is quoted in full ("continuous-time macro-finance model with sticky prices and heterogeneous balance sheets… balance sheet policy plays a preparatory role, prepositioning who bears duration risk…"). Markus confirmed the summary was accurate. The exercise of running it on a real coauthor paper surfaces theory-vs-empirical structure mismatches that the first draft of the skill missed.
  - **Claude Code's built-in skills** (named in the post): `init` (generate CLAUDE.md), `update-config` (settings.json), `keybindings-help`, `fewer-permission-prompts` (auto-allowlist common tool calls), `claude-api` (Anthropic SDK migrations), `loopschedule` (recurring/cron). Check what already ships before writing your own.
  - **Skill marketplace pointers**: `obra/superpowers` (most well-known, software-engineering-flavored); `anthropics/skills` (official, well-tested); domain-specific packs. **Underexploited academic use case**: a shared-group skill pack on GitHub so every new RA inherits the group's institutional knowledge in skill form.
  - **Two extremes of skill design**: `paper-summary` is one extreme (small, simple, repeatable task with a tight output shape). Superpowers' `brainstorming` skill is the other extreme — a multi-step thinking framework with a flow diagram, a "visual companion" for mockups, and a dispatched reviewer sub-agent that checks the plan for completeness/consistency/clarity. "Structurally close to how you'd run a planning meeting with a co-author."
  - **The "demanding adviser" skill** (`mattpocock/skills/grill-me`): a role-play skill that pushes on weak parts of a research idea, flags thin sections, and proposes next steps. The solo-PI version of a hostile discussant.
  - **Two warnings**: (1) Skills fill the context window — even just descriptions of installed skills accumulate, and overlapping triggers cause cross-firing; (2) third-party skills are someone else's instructions running in your environment — Anthropic-published is reasonable to trust; a random three-star repo is not. **Read the SKILL.md before installing.**

- **Summary**

This is the written companion to Markus Academy 162-6 and is, paragraph for paragraph, denser than the video. The conceptual frame — *skills are how you specify how an agent should think* — is sharper here because Goldsmith-Pinkham puts Caldeisearch's "SOPs as Show Other People" quote in the lead position. The implication is that an SOP and a skill are the same artifact for different consumers: a junior RA or a Claude session reading the same markdown file. Writing a skill is therefore the act of converting tacit research workflow into legible procedure, which is valuable independent of any AI use.

The five-step development workflow is the cleanest formulation in the series so far: notice the recurring instruction, lock the inputs and outputs (output structure is where most of the value lives), have Claude draft the first SKILL.md, then iterate on real cases. The Brunnermeier paper test is the load-bearing demonstration — it shows that the first version of the skill missed an important edge case (theory papers want "jump to the model first," not "read abstract → results"), and the fix is one line in the markdown.

Two pieces are written-form only. First, the explicit list of Claude Code's *built-in* skills (`init`, `update-config`, `keybindings-help`, `fewer-permission-prompts`, `claude-api`, `loopschedule`) — these activate automatically when requests match, so checking what already ships before writing a custom skill is the right first move. Second, the "demanding adviser" pattern with a direct GitHub link to `mattpocock/skills/grill-me` is a concrete, copy-pasteable example of a skill that does qualitatively different work from a paper-summary recipe.

The closing security note is more pointed than in the video: a third-party skill is "someone else's instructions running in your environment." The mitigation is mundane — read the SKILL.md before installing, prefer Anthropic-published packs, treat random GitHub skills the way you'd treat any other piece of unvetted software.

- **Relevance to Economics Research**

For empirical economists this is the most actionable single-document treatment of skills in the series. The five-step workflow scales directly: write SOPs for the things you already explain to RAs (referee-report triage, robustness-check menus, replication audits, NBER-weekly-email summarizers), keep them in the project repo so coauthors inherit them on `git clone`, and read third-party skills before installing them. The SOP framing turns skill-writing into an explicit-knowledge exercise that pays off whether or not the agent ever runs — even a human RA benefits from the documented procedure. The shared-group skill pack idea (the author flags it as an underexploited academic use case) is a concrete way for a PI to standardize the "house style" of a lab across hires and across projects.

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/claude-code]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/agentic-workflows]]
  - [[concepts/context-management]]

- **Related Summaries**
  - [[summaries/skills-markus-162-6]]
  - [[summaries/writing-thinking-markus-162-5]]
  - [[summaries/writing-thinking-ai-assistance]]
  - [[summaries/permissions-openclaw-markus-162-7]]
  - [[summaries/permissions-sandboxes-substack]]
  - [[summaries/building-skills]]
