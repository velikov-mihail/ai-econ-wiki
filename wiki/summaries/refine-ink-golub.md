---
title: "Refine.ink: AI-Powered Referee Reports for Academic Papers"
tags: [summary, ai-tools, refine-ink, peer-review, quality-control, academic-research]
sources:
  - "[[raw/articles/Refine.ink Modern AI for Economics Research with Benjamin Golub  Markus Academy  Ep. 154.md]]"
date_updated: 2026-04-03
---

- **Author/Source**: Benjamin Golub (Northwestern University, co-founder of Refine.ink) and Markus Brunnermeier (Princeton University), *Markus' Academy*, Episode 154, December 23, 2025

## Key Ideas

- **Refine.ink** automates deep technical referee reports for academic papers, going far beyond what generalist LLMs like ChatGPT Pro can do in a single session.
- The tool excels at detecting **cross-paper inconsistencies** (e.g., a definition on page 3 used incompatibly in an appendix on page 42) and **subtle mathematical errors** (sign errors, non-sequiturs in proofs).
- Accelerated research with AI makes quality control more important, not less -- researchers spend less time with pencil-and-paper deep thinking, so automated verification fills a critical gap.
- **Theory papers** get the strongest results; **empirical papers** also benefit (checking standard errors, IV explanations) but performance is limited by imperfect parsing of tables and charts.
- For empirical papers, uploading the TeX source with tables in text-readable form works better than PDF.
- **Privacy guarantee**: Refine.ink contractually ensures that uploaded papers are never shared, used for training, or accessed by third parties -- addressing concerns raised by journal editors about AI tool usage.
- Several journals are piloting Refine.ink as a complement to the review process. Editors are generally open to its use.
- Testimonials from economists (Omar, Drew Fudenberg) highlight that Refine catches subtle issues that would take a human expert many hours to find, even with ChatGPT Pro.

## Summary

In this segment of his Markus' Academy presentation, Benjamin Golub introduces Refine.ink, a specialized AI tool he co-founded that generates deep technical referee reports for academic papers. The core motivation is that AI-accelerated research increases the need for quality control: when researchers work faster with AI assistance, they may lack the deep contextual understanding that comes from slow, careful manual work, making automated verification more valuable. Refine.ink addresses this by taking a paper and producing a thorough technical review that checks logical consistency, mathematical correctness, and cross-references across the entire document.

Golub demonstrates the tool on one of his own theory papers, showing how it catches both obvious errors (sign mistakes) and substantive logical gaps (assertions that do not follow from stated conditions). He emphasizes that Refine.ink consistently outperforms frontier generalist models like ChatGPT Pro because it employs specialized scaffolding -- multi-step pipelines that invest far more "attention" on each paper than a single chatbot session could. The tool works best on reasoning-heavy papers (theory, applied math, physics) but also provides value for empirical work by checking standard error clustering, instrumental variable explanations, and internal consistency. The main limitation for empirical papers is imperfect parsing of tables and figures from PDFs.

On ethics and practical usage, Golub notes that Refine.ink's ironclad privacy guarantees address concerns about uploading unpublished research to AI tools. He recommends using Refine.ink before submission, when correctness matters most, and reports that multiple journals are piloting it as a complement to human peer review. The free preview offers 10 comments per paper to let researchers evaluate the tool on their own work.

## Relevance to Economics Research

Refine.ink directly addresses a pain point in the economics publication process: ensuring that papers are logically consistent and technically correct before submission and during review. For theory-oriented researchers, it serves as an automated proof-checker that catches subtle errors across long appendices. For empirical researchers, it offers a consistency check on methodology descriptions and statistical specifications. As AI accelerates the pace of research production, tools like Refine.ink may become essential infrastructure for maintaining quality standards in the profession.

## Related Concepts

- [[concepts/ai-peer-review]]
- [[concepts/quality-control-ai]]
- [[concepts/academic-research-ai]]

## Related Summaries

- [[summaries/using-llms-cursor]]
- [[summaries/prompting-insights-golub]]
- [[summaries/llm-collaboration]]
- [[summaries/guide-which-ai]]
