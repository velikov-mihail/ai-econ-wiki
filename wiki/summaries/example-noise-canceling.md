---
title: "Example: Organizational Noise Canceling"
tags: [summary, professional-productivity, email-triage, workflow-example]
sources:
  - "[[raw/articles/Example Noise Canceling - Claude Blattman · AI for Professionals Who Don't Code.md]]"
date_updated: 2026-04-03
---

**Author/Source**: Chris Blattman, [claudeblattman.com](https://claudeblattman.com/workflows/school-digest/)

## Key Ideas

- High-volume email sources (schools, employers, nonprofits) can be compressed into a 30-second digest using an AI classification and summarization skill, solving the problem of important deadlines buried in noise.
- Calibration is the product: you cannot write classification rules upfront. The author rated 50 real emails alongside Claude, and the disagreements taught more than the agreements. The resulting 120-line rules file could not have been written without that calibration process.
- Source quoting at extraction time is a critical technique: by forcing the model to copy the verbatim text stating a deadline alongside its summary, date corruption during downstream processing is caught immediately.
- The "quote the source at extraction time, carry the quote through to output" pattern is generalizable to any AI summarization task where specific facts must survive (meeting transcripts, grant deadlines, legal filings).
- Organizations treat everything as equally important; your triage rules encode the gap between their priorities and yours, and that gap must be measured, not inferred.
- When the cost of missing something is high and the cost of flagging it is low, classify upward.

## Summary

This article walks through building an AI skill that compresses high-volume organizational email (school announcements in the author's case) into a prioritized digest. The author's two children's schools generated 30-50 emails per digest period, and the family was missing deadlines because important items were buried in noise. The solution is a classification and summarization skill powered by Gmail MCP.

The article emphasizes two transferable lessons. First, calibration against real data is essential: the author and Claude independently rated 50 emails, resolved disagreements, and iteratively built a rules file that matched the author's actual priorities. The resulting rules file was 120 lines and could not have been written a priori. Second, source quoting at extraction time prevents fact corruption: by requiring the model to copy the exact wording of any deadline from the source email alongside its summary, discrepancies between the summary and the original are immediately visible in the output. The article includes the full extraction prompt, a sample digest output, and step-by-step instructions for building a similar skill for any high-volume email source.

## Relevance to Economics Research

The two transferable techniques -- calibration against real data before deploying classification rules, and source quoting to prevent fact corruption in AI summaries -- apply directly to research workflows. Economists who use AI to summarize literature, extract data from documents, or process meeting transcripts face the same risk of fact corruption during summarization. The source-quoting pattern ("extract the verbatim text alongside the structured data") is a practical defense against hallucinated or corrupted facts in any extraction pipeline.

## Related Concepts

- [[wiki/concepts/prompt-engineering]]
- [[wiki/concepts/ai-workflow-design]]
- [[wiki/concepts/claude-code-skills]]

## Related Summaries

- [[wiki/summaries/ai-executive-assistant]]
- [[wiki/summaries/meeting-transcription]]
- [[wiki/summaries/project-management]]
