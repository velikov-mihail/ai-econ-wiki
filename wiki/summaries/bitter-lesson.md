---
title: "The Bitter Lesson"
tags: [summary, institutional-societal]
sources:
  - "[[raw/articles/The Bitter Lesson.md]]"
date_updated: 2026-04-03
---

- **Original**: [http://www.incompleteideas.net/IncIdeas/BitterLesson.html](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)


**Author/Source**: Rich Sutton (University of Alberta), published March 2019

**Key Ideas**:
- The biggest lesson from 70 years of AI research is that general methods leveraging computation ultimately dominate methods that encode human domain knowledge
- This pattern recurs across chess, Go, speech recognition, and computer vision -- hand-crafted, human-knowledge-based approaches are consistently overtaken by scaled computation
- The two most important technique classes for utilizing massive computation are search and learning
- Researchers persistently try to build in how they think humans think, which helps in the short term but plateaus and inhibits long-term progress
- AI should build in meta-methods that discover and capture complexity, not encode the discoveries themselves
- The contents of minds are "tremendously, irredeemably complex" and should not be simplified into built-in representations

**Summary**:
Sutton's influential 2019 essay identifies a recurring pattern in AI history: researchers invest heavily in encoding human domain knowledge into AI systems, only to see those approaches surpassed by simpler methods that scale with computation. In chess, knowledge-based approaches were defeated by Deep Blue's massive search. In Go, the same pattern played out 20 years later with AlphaGo. In speech recognition, statistical methods based on hidden Markov models beat systems built on phonemic and vocal tract knowledge, and deep learning later extended this trend. In computer vision, hand-engineered features like SIFT were replaced by convolutional neural networks that learn representations from data.

The "bitter" part of the lesson is that these outcomes are emotionally unsatisfying to researchers who invested in human-centric approaches. Researchers want methods based on human understanding to win, and are disappointed when brute computation prevails. Yet the pattern is consistent: short-term gains from domain knowledge are overtaken by long-term gains from scaling general methods. Sutton argues the field still has not fully internalized this lesson, and continues to make the same mistakes. The prescription is to focus on building meta-methods -- systems that can discover structure autonomously -- rather than trying to encode human discoveries directly.

**Relevance to Economics Research**:
The bitter lesson has direct implications for how economists approach machine learning in research. It suggests that general-purpose, computation-heavy methods (large language models, deep learning) will outperform hand-crafted econometric approaches for prediction tasks, even if domain-specific models seem more interpretable or theoretically grounded in the short term. For empirical finance and economics, this frames the tension between structural models encoding economic theory versus flexible ML models that learn patterns from data. It also informs the debate about whether AI tools for research should encode domain expertise or leverage general capabilities.

**Related Concepts**:
- [[concepts/ai-adoption-academia]]
- [[concepts/jagged-frontier]]
- [[concepts/human-ai-collaboration]]

**Related Summaries**:
- [[summaries/ai-normal-technology]]
- [[summaries/shape-of-ai]]
- [[summaries/something-big-happening]]
