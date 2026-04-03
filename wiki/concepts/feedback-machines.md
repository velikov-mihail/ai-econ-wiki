---
title: "Feedback Machines"
tags: [concept, academic-research, writing, peer-review]
sources:
  - "[[summaries/feedback-machines.md]]"
  - "[[summaries/ai-research-feedback-skills.md]]"
  - "[[summaries/agents-vs-skills.md]]"
  - "[[summaries/vibe-research.md]]"
  - "[[summaries/my-claude-code-setup.md]]"
date_updated: 2026-04-03
---

## Definition

**Feedback machines** refers to the use of AI tools to provide structured, multi-dimensional feedback on academic papers, research designs, and grant proposals. Rather than treating AI as a drafting tool, this approach uses it as a systematic reviewer -- simulating referee reports, checking internal consistency, identifying unsupported claims, and stress-testing identification strategies. The term captures both the mechanistic nature of the process (structured, repeatable, multi-pass) and the aspiration to supplement the traditionally slow and scarce supply of expert feedback in academia.

The core insight is that AI feedback is most valuable not as a single-pass review but as a layered system: multiple specialized agents, each examining a different dimension of the work, producing reports that the human researcher evaluates and selectively incorporates. This mirrors the peer review process but runs in minutes rather than months.

## Context & Background

Academic researchers face a chronic feedback bottleneck. Getting substantive comments on a paper before submission typically requires waiting for co-author availability, conference presentations, or seminar slots -- processes that take weeks to months. Referee reports take even longer. AI feedback does not replace expert human review, but it fills a gap: it provides structured, immediate critique that catches the kinds of errors humans often miss (notation inconsistencies, unsupported claims, cross-reference errors) and surfaces the kinds of questions that help researchers refine their arguments before human reviewers see the work.

The approach has evolved from simple "review my paper" prompts to sophisticated multi-agent systems with specialized reviewer personas, adversarial critique loops, and journal-specific calibration. The most advanced implementations (Backman's skills, Sant'Anna's template) run six or more parallel review agents, each focused on a distinct dimension, producing dated, versioned output reports.

## Key Perspectives

**Backman (Feedback Machines)** ([[summaries/feedback-machines.md]]) describes a structured workflow progressing from high-level to fine-grained: (1) full referee-style report on the complete draft, (2) section-by-section evaluation for inconsistencies, (3) identification of unsupported claims and missing robustness checks, (4) notation and reference consistency across the entire project, (5) professional editing for clarity and tone. He also uses AI to evaluate journal fit and suggest target journals. Key limitation: AI reports tend to be overly negative (even a published RFS paper received a "major revisions" recommendation), and AI can make text sound polished while the underlying argument remains weak. His advice: exercise independent judgment and learn to ignore some feedback, just as with human reviewers.

**Backman (AI Research Feedback Skills)** ([[summaries/ai-research-feedback-skills.md]]) provides the most complete tooling. His five Claude Code skills cover paper review, light paper check, paper-code reproducibility, pre-analysis plan review, and grant proposal review. The flagship `/review-paper` runs six parallel agents: style, internal consistency, unsupported claims, mathematics, tables/figures, and an adversarial journal-specific referee persona. Users can target specific journals (AER, QJE, JPE, Econometrica, REStud, JF, JFE, RFS, JFQA), and the skill adjusts standards accordingly. The `/review-paper-code` skill checks reproducibility by mapping empirical claims in the paper to analysis code.

**Blattman (Agents vs Skills)** ([[summaries/agents-vs-skills.md]]) explains why fresh-context agents are essential for review. The **self-bias problem** means that when Claude reviews its own work in the same conversation, it systematically finds its output acceptable because it "knows what it meant." Spinning up a fresh agent provides genuinely independent critique. The agent debate pattern -- assigning distinct identities to multiple agents and letting their disagreements surface assumptions -- generated nine new measures that were not in the original study design.

**Gregoire** ([[summaries/vibe-research.md]]) used multi-agent review loops in his four-day paper production: Claude Code, Codex CLI, and OpenCode/Gemini independently reviewed the paper, code, and proofs, producing consolidated reports. He then directed Claude Code to implement fixes and repeated the cycle many times. This demonstrates feedback machines as integral to rapid AI-assisted research production, not just a pre-submission polish.

**Sant'Anna** ([[summaries/my-claude-code-setup.md]]) implements the most rigorous quality assurance: an adversarial critic-fixer loop where two agents check each other's work across up to 5 rounds, with hard role separation (the critic cannot fix, the fixer cannot approve). A scoring system requires every output to achieve 80+ on a 0-100 scale before shipping.

## Practical Implications

- **Use fresh-context agents for review**: Never ask the same session that produced the work to review it. Spin up a separate agent that reads the output cold.
- **Layer reviews from high-level to fine-grained**: Start with a full referee-style report, then move to section-level evaluation, then claim-level checking, then consistency and polish.
- **Calibrate to target journals**: If you are aiming for a specific journal, tell the reviewer agent. This focuses feedback on the standards that matter for your submission.
- **Treat AI feedback as candidate edits**: Not every suggestion is correct. Hallucinated results and fabricated explanations are common. The skill of using AI feedback is the skill of knowing which feedback to accept.
- **Check paper-code alignment**: Use reproducibility-focused skills to verify that empirical claims in the paper match the analysis code -- an increasingly important check as replication standards tighten.
- **Build in adversarial review**: Assign a "hostile referee" persona to catch the weaknesses that a supportive reviewer would miss. Multiple sources find this is where the highest-value feedback emerges.

## Open Questions

- Can AI feedback become a credible substitute for human referee reports, or will it always be a complement?
- How should researchers disclose the use of AI feedback in their submission process?
- Do AI reviews systematically miss certain kinds of problems (conceptual novelty, institutional context, field-specific conventions) that human reviewers catch?
- As AI feedback tools become widespread, will the baseline quality of submitted papers rise, making the refereeing process even more competitive?
- Can adversarial AI review loops catch the kind of "seductive" formal results that Gans describes -- results that look correct but are subtly wrong?

## Sources

- [[summaries/feedback-machines.md]] -- Backman's structured feedback workflow and limitations
- [[summaries/ai-research-feedback-skills.md]] -- Backman's five Claude Code skills for academic review
- [[summaries/agents-vs-skills.md]] -- Blattman on self-bias and agent debates for review
- [[summaries/vibe-research.md]] -- Gregoire's multi-agent review loops in rapid paper production
- [[summaries/my-claude-code-setup.md]] -- Sant'Anna's adversarial critic-fixer loop with quality scoring
