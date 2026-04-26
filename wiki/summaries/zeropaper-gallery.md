---
title: "ZeroPaper Gallery: Papers Produced by an Autonomous Research Pipeline"
tags:
- summary
- finance-econometrics
- automated-research
- finance-research
- AI-pipeline
sources:
- '[[raw/articles/Gallery of papers produced by the ZeroPaper autonomous research pipeline.md]]'
date_updated: 2026-04-26
date_published: 2026-04-25
---

- **Author/Source**: Alejandro Lopez-Lira (GitHub: `alejandroll10/zeropaper-gallery`, 2026-04-25)
- **Original**: [https://github.com/alejandroll10/zeropaper-gallery](https://github.com/alejandroll10/zeropaper-gallery)

## Key Ideas

- A public gallery of 22 papers produced by ZeroPaper, Lopez-Lira's autonomous research pipeline announced earlier in 2026 (see [[summaries/automated-research-finance]]).
- Each paper is described as a single end-to-end run from problem discovery through finished LaTeX, with no human intervention between launch and the PDF.
- Every paper carries a process log under `logs/` recording stage transitions, gate verdicts, and scorer trajectories — making the pipeline's internal evaluation auditable.
- Folder names are anonymized (`paper1`, `paper2`, ...); the operator's mapping to actual research ideas is kept private.
- IDs are sticky: `papers/paperN.pdf` points to the same paper across gallery refreshes, supporting longitudinal tracking.
- The gallery spans 6–77 page papers, with self-assigned final scores ranging from 58 to 78 (one marked "Major Revision," several with no score reported). 21 of 22 are tagged `finance`; one is `macro`.
- Topics include cross-sectional asset pricing (BAB, anomaly persistence, cash-flow duration), market microstructure (Kyle models for prediction markets, benchmark gravity), banking and private credit (depositor monitoring, LP exposure to private credit funds), and meta-research on AI pipelines themselves (correlation cascades in self-assessment, optimal evaluation design).

## Summary

The ZeroPaper Gallery is the public output catalog of Alejandro Lopez-Lira's ZeroPaper pipeline — the same automated research system he previously sought collaborators to test (see [[summaries/automated-research-finance]]). Where the earlier post described the pipeline's design and offered access pathways, this gallery shows what the system has actually produced: 22 papers generated as of 2026-04-25, ranging from 6-page focused notes to a 77-page treatise on Sharpe ratios and risk premia.

Each entry includes the paper's title, length, a final score (the pipeline's own quality gate verdict), and links to both the PDF and the JSON process log. The logs document stage transitions and gate verdicts, providing an audit trail of the pipeline's internal decisions during a run. Anonymizing folder names (`paper1`, `paper2`, ...) decouples the public artifacts from the operator's private idea-to-paper mapping, presumably to preserve research priority and collaborator confidentiality.

The topical range is striking: classical asset pricing (anomaly correction, conditional BAB, cash-flow duration), microstructure and market design (Kyle models for prediction markets, benchmark composition), institutional finance (private credit LP exposure, mandatory Treasury clearing, FIMA swap decisions), accounting and disclosure (fair-value disclosure, ESG score manipulation), and self-reflective meta-papers on AI pipeline design itself (papers 6 and 7 explicitly study the autonomous-pipeline evaluation problem).

## Relevance to Economics Research

This is concrete, browsable evidence of what an autonomous research pipeline can currently produce in finance — the most direct empirical reference point available for the "automated research" question that has dominated 2025–2026 discourse (see [[concepts/automated-research]]). For researchers, three things matter:

1. **What the system actually outputs**: not abstracts or one-page demos, but full LaTeX papers ranging up to 77 pages, with theoretical models, empirical work, and proofs. Reading the PDFs lets researchers form their own quality judgments rather than relying on the system's self-assigned scores.
2. **Process transparency via logs**: the public JSON logs make ZeroPaper one of the few automated-research efforts where the internal gate verdicts and scorer trajectories can be inspected. This matters for evaluating whether self-assessment scores are well-calibrated (papers 6 and 7 in the gallery internally study exactly this concern).
3. **Topic distribution as a revealed-preference signal**: the heavy concentration in cross-sectional asset pricing, microstructure, and institutional finance suggests where the pipeline's training data and tooling (WRDS, FRED, public sources) give it the most traction — and where economists evaluating similar systems should expect the strongest output.

For [[summaries/ai-powered-scholarship]] (Novy-Marx & Velikov), [[summaries/dickerson-ai-asset-pricing]], [[summaries/ralph-wiggum-asset-pricing]], and [[summaries/project-ape]], this gallery provides a comparison point: another fully autonomous pipeline making its outputs and process logs public.

## Related Concepts

- [[concepts/automated-research]]
- [[concepts/ai-agents]]
- [[concepts/research-quality]]
- [[concepts/data-pipelines]]

## Related Summaries

- [[summaries/automated-research-finance]] — the announcement of the ZeroPaper pipeline that produced this gallery
- [[summaries/stress-test-research-pipeline]] — Lopez-Lira's earlier idea-evaluation tool, an upstream filter to the same workflow
- [[summaries/ai-powered-scholarship]] — Novy-Marx & Velikov's parallel finance-paper pipeline (30K signals → 380 LLM papers)
- [[summaries/ralph-wiggum-asset-pricing]] — Chen's open-source Ralph loop for asset pricing papers
- [[summaries/dickerson-ai-asset-pricing]] — Dickerson's multi-agent asset pricing repo
- [[summaries/project-ape]] — Social Catalyst Lab's automated policy-evaluation pipeline
- [[summaries/applications-generative-ai]] — Korinek's broader taxonomy of generative-AI uses in economics
