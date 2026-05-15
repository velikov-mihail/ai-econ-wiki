---
title: "Why No One Can Agree About AI Progress Right Now"
tags: [summary, institutional-societal, ai-adoption, mental-model]
sources:
  - "[[raw/articles/Why no one can agree about AI progress right now.md]]"
date_updated: 2026-05-15
date_published: 2026-03-03
---

- **Author/Source**: Brian Heseung Kim, DAAF Guide (Substack)
- **Original**: [https://daafguide.substack.com/p/ai-progress-mental-model](https://daafguide.substack.com/p/ai-progress-mental-model)

- **Key Ideas**
  - Two camps dominate AI discourse: "LLMs are fundamentally flawed and will never threaten serious work" vs. "we are months from full labor-market collapse." Kim argues both are partially correct because **AI progress is not one measure but three intertwined ones**.
  - The mental model: **Mind / Body / Instructions**.
    - **Mind** — base model capability. The visible frontier (GPT-5.3, Opus 4.6, Gemini 3.1 Pro) most users see in marketing.
    - **Body** — orchestration frameworks and tooling (Claude Code, Codex, Cowork, Antigravity, MCP, subagents, skills, contracts). What lets models actually do things.
    - **Instructions** — user prompting skill: how a person explains what they want, intervenes for revisions, points the model at the right context.
  - **Each piece is necessary; alone, insufficient.** A super-intelligent humanoid robot with Lego-claw hands (incapable Body) cannot fold laundry regardless of intelligence; the same robot with perfect hands but a vague "get to work!" (bad Instructions) also fails.
  - The Body and Instructions dimensions are now changing **faster than the model frontier**, in obscure ways. Recent counterintuitive results: providing context can make LLMs *worse* than no context; Anthropic explicitly recommends against overly thorough prompts; **simply copy-pasting your prompt twice** uniformly improves performance on many models; PDF instead of Markdown can fully corrupt the document understanding.
  - True frontier best practice is no longer set by traditional experts. It's emerging from weekend tinkerers on Reddit, X, GitHub — "Foot_sniffer6467 was king for a week back in January" for discovering a subagent communication pattern. **Information gradient drives capability gradient**.
  - November 2025 (Opus 4.5 launch) marked the qualitative shift. "It's been anyone's game since."
  - The flywheel: Body/Instructions advances feed back into Mind (OpenAI's Codex now accelerates its own development). We are firmly in exponential phase, but the public still mostly sees only the Mind dimension and therefore both overestimates and underestimates what AI can do.
  - Prescription: build prompting skill (Instructions) first; push into more advanced frameworks (Body) second; let Claude/Codex teach you to use Claude/Codex. The luddite stance is increasingly untenable; the boat is moving fast and getting harder to catch.

- **Summary**

Kim's piece is the most-circulated framing of why expert opinion on AI is so visibly bimodal. The Mind / Body / Instructions decomposition is intentionally simple and is the article's most quotable contribution. The empirical observations he lists in the "everything is weirder than you think" section — context can hurt, more-thorough prompts can hurt, copy-pasting the prompt twice helps, PDFs corrupt understanding — are individually well-known to power users but rarely assembled in one place as evidence that "best practice" is genuinely chaotic right now.

The deeper argument is sociological: the people setting the frontier of capability are not traditional experts but tinkerers in semi-private online communities, and the rate at which this frontier moves means the gap between "knows the November 2025 frontier" and "has heard of AI" now produces an enormous capability gradient. This is why the people who think AI can already do their job and the people who think AI is useless are looking at the same models and reaching opposite conclusions: they're operating at different points on the Body/Instructions axis.

- **Relevance to Economics Research**

This is the cleanest piece of conceptual scaffolding currently available for explaining to non-power-user colleagues why "I tried ChatGPT and it was bad" is not informative about current AI capability. The three-axis model is directly useful in teaching settings (master class slides, faculty Community-of-Practice talks) where audiences are calibrating their own AI expectations. The information-gradient observation also has implications for how economists should allocate research time: investing in Body/Instructions skill (Claude Code skills, MCP servers, subagent patterns) compounds faster than waiting for the next model release, and the weekend-tinkerer-as-frontier dynamic means published academic papers will systematically lag the actual best practice. Pair with [[agentic-everything|Svoronos's "Agentic Everything"]] for a similar November-2025-was-the-shift argument from a Harvard Kennedy School perspective.

- **Related Concepts**
  - [[concepts/ai-tools-landscape]]
  - [[concepts/ai-adoption-academia]]
  - [[concepts/ai-skills]]
  - [[concepts/jagged-frontier]]
  - [[concepts/agentic-workflows]]

- **Related Summaries**
  - [[summaries/agentic-everything]]
  - [[summaries/ai-normal-technology]]
  - [[summaries/ai-people-right-a-lot]]
  - [[summaries/sign-of-future-gpt55]]
