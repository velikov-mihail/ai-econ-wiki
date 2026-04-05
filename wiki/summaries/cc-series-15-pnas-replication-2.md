---
title: "Claude Code 15: The Results Are In -- Can LLMs Replicate a PNAS Paper? (Part 2)"
tags: [summary, data-analysis, text-classification, replication, nlp, zero-shot-classification, openai-batch-api]
sources:
  - "[[raw/articles/Claude Code 15 The Results Are In Can LLMs Replicate a PNAS Paper (Part 2).md]]"
date_updated: 2026-04-05
date_published: 2026-02-06
---

- **Author/Source**: Scott Cunningham (Baylor), via Substack ("Causal Inference")
- **Original**: [https://causalinf.substack.com/p/claude-code-15-the-results-are-in](https://causalinf.substack.com/p/claude-code-15-the-results-are-in)

- **Key Ideas**
  - 69% agreement between gpt-4o-mini (zero-shot) and the original fine-tuned RoBERTa classifier on 304,995 speech segments
  - Total cost: $10.99; batch processing time: 2.6 hours (expected 24); total project time: ~4.6 hours
  - The LLM is more cautious: when uncertain, it classifies as NEUTRAL rather than picking a side; direct PRO-to-ANTI polarity flips are rare (only ~4%)
  - The polarization finding from Card et al. is robust -- both classifiers show Democrats and Republicans diverging sharply since the 1970s
  - Country-of-origin patterns replicate with the same ordering (Italy > China > Mexico in positivity)
  - Human annotators themselves agreed at only Krippendorff's alpha = 0.48, providing context for the 69% machine-machine agreement
  - LLMs as viable zero-shot classifiers: for exploratory text analysis without resources to fine-tune, gpt-4o-mini is a practical option
  - Referee 2 was used from within the same session (violating the protocol), caught only by a reader -- illustrating how easy it is to break one's own workflow

- **Summary**

This is the results post for the PNAS replication experiment. Cunningham reports that gpt-4o-mini agreed with the original RoBERTa classifier on 69% of the 304,995 congressional and presidential speech segments. The batch job completed in 2.6 hours rather than the expected 24, at a cost of $10.99. The transition matrix reveals a systematic pattern: when the two classifiers disagree, the LLM almost always moves toward NEUTRAL (33% of PRO speeches and 44% of ANTI speeches reclassified as NEUTRAL), while direct polarity flips (PRO to ANTI or vice versa) are rare at around 4%. Cunningham interprets this as the LLM being appropriately cautious on marginal, ambiguous speeches.

The substantive findings from the original paper survive: partisan polarization on immigration rhetoric since the 1970s is clearly visible in both the original and LLM classifications. Country-of-origin analysis also replicates, with the same ordering of sentiment toward Italian, Chinese, and Mexican immigrants. A Texas-specific analysis shows the same polarization pattern with more noise. Cunningham contextualizes the 69% agreement by noting that human annotators themselves achieved only moderate agreement (Krippendorff's alpha = 0.48).

The post concludes that LLM-based zero-shot classification is now a viable path for researchers who lack resources to fine-tune custom models. The cost barrier ($11), time barrier (4.6 hours total), and expertise barrier (Claude Code handled the infrastructure) are all dramatically lower than traditional approaches.

- **Relevance to Economics Research**

This post provides direct evidence that off-the-shelf LLMs can replicate trained NLP classifier results well enough to preserve substantive conclusions in economics research. The $11 / 4.6-hour benchmark makes computational text analysis accessible to solo researchers without ML expertise or GPU infrastructure. The finding that qualitative conclusions are robust even when point-level agreement is imperfect is important for economists considering LLM-based measurement of sentiment, framing, or rhetoric in large text corpora. The candid admission about accidentally violating the Referee 2 protocol is also instructive about the discipline required to maintain rigorous AI-assisted workflows.

- **Related Concepts**
  - [[concepts/llm-text-classification]]
  - [[concepts/verification-validation]]
  - [[concepts/ai-agent-workflows]]
  - [[concepts/replication]]

- **Related Summaries**
  - [[summaries/cc-series-14-pnas-replication-1]]
  - [[summaries/cc-series-12-empirical-research]]
