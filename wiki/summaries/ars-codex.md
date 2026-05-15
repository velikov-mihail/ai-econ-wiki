---
title: "Academic Research Skills for Codex (ARS-Codex)"
tags: [summary, ai-tools, codex, academic-pipeline]
sources:
  - "[[raw/articles/Academic Research Skills for Codex.md]]"
date_updated: 2026-05-15
date_published: 2026-05
---

- **Author/Source**: Edward Cheng-I Wu, GitHub
- **Original**: [https://github.com/Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex)

- **Key Ideas**
  - Codex-native sibling distribution of [[ars-claude-code|Academic Research Skills]]. Same workflow content; repackaged as a single Codex skill `$academic-research-suite` with `ars-*` aliases.
  - Vendors the upstream ARS suite verbatim under `skills/academic-research-suite/ars/`, plus a Codex router in `SKILL.md` and OpenAI agents YAML at `agents/openai.yaml`.
  - Codex package version `0.1.6` tracks independently of the vendored ARS version (currently pinned to a specific upstream commit recorded in `manifest.source_repositories[]`).
  - Single-line install via the Codex skill installer: `python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Imbad0202/academic-research-skills-codex --ref main --path skills/academic-research-suite --method git`.

- **Summary**

Codex packaging of the ARS pipeline. The vendored content is identical to the Claude Code version; the value of the separate repo is purely distribution: Codex's skill system uses a single-suite layout rather than the multi-skill directory layout that Claude Code expects, and a single Codex skill router replaces Claude Code's `/plugin` marketplace flow. Users who prefer Codex CLI / Codex desktop for academic writing get the same agent rosters, integrity gates, anti-sycophancy protocols, and journal references without juggling two toolchains.

- **Relevance to Economics Research**

A reminder that the Codex ecosystem has reached feature parity with Claude Code for skill-based workflows. For economists committed to the OpenAI stack (e.g., GPT-5.3-Codex users following [[panjwani-codex-course|Panjwani's course]]), this is the canonical port of the most-elaborate academic-research skill bundle. The cross-platform port also documents an interesting pattern: when the Claude Code and Codex skill formats diverge, vendoring the upstream and writing a thin adapter is more sustainable than dual-maintaining the workflow content.

- **Related Concepts**
  - [[concepts/claude-code-skills]]
  - [[concepts/automated-research]]
  - [[concepts/ai-tools-landscape]]

- **Related Summaries**
  - [[summaries/ars-claude-code]]
  - [[summaries/panjwani-codex-course]]
  - [[summaries/codex-101-bilal]]
