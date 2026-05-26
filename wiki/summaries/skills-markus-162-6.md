---
title: "Skills: Claude Code for Economists (Markus Academy 162-6)"
tags: [summary, claude-code-skills, claude-code, skills]
sources:
  - "[[raw/articles/Skills Claude Code for Economists with Paul Goldsmith-Pinkham  Markus Academy  Ep. 162-6.md]]"
date_updated: 2026-05-26
date_published: 2026-05-25
---

- **Author/Source**: Paul Goldsmith-Pinkham (Yale SOM, NBER), Markus Academy Ep. 162-6 (6th of 8 in mini-series)
- **Original**: [https://www.youtube.com/watch?v=a03ehomPqMA](https://www.youtube.com/watch?v=a03ehomPqMA)

- **Key Ideas**
  - **A skill = a reusable instruction bundle**, written as a single `SKILL.md` file inside a named folder. The file is "just a long prompt" — what you'd write the first time you described the task to Claude — encoded once and reloaded every time the skill is triggered.
  - Skills are **standardization, not new capability**: they don't give the model new powers, only consistent thinking. Quoting an unnamed Substack commentator, they are a way of *specifying how an agent should think* (see [[skills-specifying-thinking|companion piece]]).
  - **Two installation scopes**: global (`~/.claude/skills/`) makes the skill available in every project; project-level (`.claude/skills/` in the repo) keeps it scoped. **Trade-off**: every globally-installed skill loads its name + description into the initial prompt's context window, so a thousand global skills bloats startup. Goldsmith-Pinkham installs very few globally on purpose.
  - **Skill structure**: each skill lives in its own folder (folder name = skill name); the folder always contains a `SKILL.md` with frontmatter (name + description) and a body that gets pasted verbatim into the prompt when the skill triggers. The **description** is the *trigger* — Claude reads it during preamble loading and fires the skill when user requests match.
  - **Live demo: a `paper-summary` skill.** Goldsmith-Pinkham builds it on-screen. Inputs: PDF URL or local path. Output: a one-page LaTeX-compiled PDF summary with "intuition translated so even a non-expert in the subfield could understand." Runs the skill on one of Brunnermeier's working papers (*Optimal Unconventional Monetary Policy*) and the result captures the gist (two market failures, two channels) though it inherits Goldsmith-Pinkham's empirical-paper structure and is awkward on a theory paper — illustrating that a skill encodes a specific point of view, not a neutral procedure.
  - **Editing a skill** is editing the markdown directly. The body of the demo skill is human-readable: acquire PDF, verify, read abstract → results (with a note that theorists may want to jump to the model first), write LaTeX, compile, with style nudges. Easy to nudge in either direction.
  - **Skill packs / app-store ecosystem**: open-source GitHub repos publish bundles. The headline example is **"Superpowers"** by jesseduffield (referenced as the popular early example), a software-development-flavored framework. The author shows its `brainstorming` skill, which forces every "creative work" task through a designed flow: explore project → visual questions → clarifying questions → propose approaches → present design → spawn a sub-agent reviewer that checks for completeness, consistency, clarity. This is the contrast to a simple "do this task once" skill: it is *how to think* about an open-ended problem.
  - **Useful pattern**: a skill that role-plays an adviser pushing back on the researcher's argument — "ask me questions about this research thing, push on anything weak, flag things to develop further, then plan next steps." A solo-PI version of a brown-bag discussant.
  - **Sharing within a research group**: build a GitHub repo of project-specific skills, share with coauthors and RAs as a way to standardize workflow. Yale SOM is doing this internally.
  - **Two cautions**: (1) Don't load too many skills — context-window cost and accidental triggering from overlapping descriptions; (2) **third-party skills are a supply-chain risk**: a malicious skill could instruct the model to delete files, exfiltrate data, etc. They're plain text and inspectable, but you should read them before installing.

- **Summary**

This episode is the conceptual cornerstone of Goldsmith-Pinkham's Claude Code series. After five episodes of demoing specific workflows, episode 6 stops and asks "what *is* a skill" — and lands on a useful definition: a skill is a markdown file containing a long prompt, organized into a named folder, with a description that controls when Claude loads and fires it. The body is "just text" that gets pasted into the prompt; the discipline is in writing the description precisely enough that triggering is accurate, and writing the body explicitly enough that the agent doesn't have to re-derive the procedure each time.

The live `paper-summary` demo is the heart of the episode. Goldsmith-Pinkham asks Claude to build the skill, accepts the generated SKILL.md mostly as written, runs it on Brunnermeier's *Optimal Unconventional Monetary Policy*, and discusses the output honestly — the summary is structurally fine but inherits the author's empirical-paper habits, and a theorist might want to edit the body to "jump to the model first" rather than "read the results section." The exercise demonstrates the right level of trust: the skill saves the re-explanation cost, but the researcher's editorial judgment is still load-bearing.

The contrast with Superpowers is the second key teaching moment. A `paper-summary` skill is a *recipe* — fixed inputs, fixed steps, fixed output shape. The Superpowers `brainstorming` skill is a *thinking framework* — it forces every creative task through a brainstorm → design → review → implement loop, including spawning a sub-agent reviewer that checks completeness and consistency. These are two different uses of the skill machinery, and Goldsmith-Pinkham is candid that he uses the first kind much more than the second. The closing safety note — third-party skills are inspectable plain text, but they're still a supply-chain attack surface — anticipates the security framing of [[permissions-openclaw-markus-162-7|episode 7]].

- **Relevance to Economics Research**

For empirical economists, the `paper-summary` recipe maps cleanly onto the weekly-NBER-working-paper-list use case Goldsmith-Pinkham flags ("rather than read the abstracts, write a skill that takes the email list and gives me the key results from this week's papers"). The same recipe transposes to: discussant-prep skills, referee-report skills (already covered in episode 5), pre-seminar-visit literature checks, and replication-package audit skills. The group-skill-repo pattern is genuinely useful for coauthored projects — a shared `.claude/skills/` folder under git becomes the team's collective workflow memory. The supply-chain warning is the under-appreciated point: a research group adopting a public skills pack is implicitly trusting it the same way they would trust a Stata package, but with weaker norms around vetting. Read the SKILL.md before installing.

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/claude-code]]
  - [[concepts/multi-agent-systems]]
  - [[concepts/agentic-workflows]]
  - [[concepts/context-management]]

- **Related Summaries**
  - [[summaries/skills-specifying-thinking]]
  - [[summaries/writing-thinking-markus-162-5]]
  - [[summaries/writing-thinking-ai-assistance]]
  - [[summaries/permissions-openclaw-markus-162-7]]
  - [[summaries/permissions-sandboxes-substack]]
  - [[summaries/getting-started-economists]]
