---
title: "Retrieval-Augmented Generation (RAG)"
tags: [concept, technology, tools]
sources:
  - "[[summaries/llm-collaboration.md]]"
  - "[[summaries/using-llms-cursor.md]]"
date_updated: 2026-04-03
---

# Retrieval-Augmented Generation (RAG)

Retrieval-augmented generation (RAG) is a technique that combines document retrieval with LLM generation — the model first searches a knowledge base for relevant information, then generates a response grounded in those retrieved documents.

## Context & Background

RAG addresses a key limitation of LLMs: their tendency to hallucinate or rely on potentially outdated training data. By retrieving relevant documents before generating a response, RAG systems can:

- **Ground responses in sources**: Cite specific documents rather than generating from memory
- **Access current information**: Work with documents newer than the model's training cutoff
- **Reduce hallucination**: Constrain the model to information actually present in retrieved documents
- **Enable domain expertise**: Give the model access to specialized research papers or datasets

## Practical Implications

- **Use RAG for literature-heavy tasks**: When accuracy of citations matters, RAG systems outperform vanilla LLMs
- **Curate your knowledge base**: RAG is only as good as the documents it can retrieve
- **Verify attribution**: Check that the model's claims actually appear in the cited sources
- **Consider tools like NotebookLM**: Purpose-built RAG tools for research document analysis

## Related Concepts

- [[concepts/document-processing|Document Processing]]
- [[concepts/ai-limitations|Ai Limitations]]
- [[concepts/literature-review-ai|Literature Review Ai]]
