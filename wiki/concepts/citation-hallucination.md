---
title: "Citation Hallucination"
tags: [concept, academic-research, quality, ai-limitations]
sources:
  - "[[summaries/ars-claude-code.md]]"
  - "[[summaries/katmer-code.md]]"
  - "[[summaries/haaland-reviewer.md]]"
  - "[[summaries/kohler-agentic-reproduction.md]]"
date_updated: 2026-05-15
---

# Citation Hallucination

Citation hallucination is the failure mode in which LLMs fabricate references — inventing plausible-looking author/title/year combinations, getting one or more bibliographic fields wrong on an otherwise-real source, or deploying real references in support of claims the cited papers do not actually make.

## Context & Background

Zhao et al. (2026-05) audited 111M references across 2.5M papers on arXiv, bioRxiv, SSRN, and PMC and conservatively estimated 146,932 hallucinated citations for 2025 alone, with a mid-2024 inflection. A five-type taxonomy is now in common use:

- **TF** — Total Fabrication: the cited work does not exist
- **PAC** — Plausible Author Composition: real author, but never wrote the cited paper
- **IH** — Identity Hallucination: real paper attributed to wrong authors or year
- **PH** — Partial Hallucination: real paper but title/venue/year garbled
- **SH** — Source Hallucination: real reference used to support a claim it does not actually make (most insidious — passes Tier 0 existence checks)

Standard mitigation is multi-tier verification: a programmatic API check against Semantic Scholar / CrossRef / OpenAlex catches TF/PAC/IH/PH at low cost; SH requires reading the cited source and is much harder to automate.

## Practical Implications

- **Never trust LLM parametric memory for citations.** Verify every reference against an authoritative bibliographic database before publication.
- **Use multi-source verification** — Semantic Scholar + CrossRef + OpenAlex disagree often enough that triangulation matters.
- **External post-publication audit beats internal checks.** ARS reports a real case where post-publication WebSearch verification found 21/68 reference issues (31% error rate) that survived three rounds of integrity checks.
- **Anti-leakage protocol**: when an AI agent has a session corpus, force it to prefer session materials over its memory; flag `[MATERIAL GAP]` for missing content rather than filling from training data.
- **Don't aggregate citations across model sessions** without re-verification — verified references in one session are not verified in the next.

## Key Sources

- [[summaries/ars-claude-code|Academic Research Skills for Claude Code]] — Tier 0 Semantic Scholar API verification, 5-type taxonomy, post-publication audit case
- [[summaries/katmer-code|KatmerCode]] — `/cite-verify` checks every reference against CrossRef, Semantic Scholar, OpenAlex
- [[summaries/haaland-reviewer|Reviewer (Haaland)]] — Schema-validated reviewer outputs with parser-quality preflight
- [[summaries/kohler-agentic-reproduction|Read the Paper, Write the Code]] — ETH benchmark on AI replication fidelity

## Related Concepts

- [[concepts/ai-limitations|AI Limitations]]
- [[concepts/ai-peer-review|AI-Assisted Peer Review]]
- [[concepts/human-in-the-loop|Human in the Loop]]
- [[concepts/jagged-frontier|Jagged Frontier]]
