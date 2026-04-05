---
description: "Search the wiki for a topic and return a structured answer with sources. Args: <search term or question>"
user_invocable: true
---

# /query — Search the wiki

Search across summaries and concepts to answer a question or find everything related to a topic.

## Trigger

User runs `/query <topic or question>` or asks what the wiki knows about something.

## Steps

1. **Parse the query**: Extract the key terms or question from the argument.

2. **Search summaries and concepts**: Grep across `wiki/summaries/` and `wiki/concepts/` for matching content. Also check tags in frontmatter for relevant matches.

3. **Rank and organize results**: Group findings by relevance:
   - **Direct matches** — pages primarily about the topic
   - **Mentions** — pages that reference the topic in passing

4. **Synthesize an answer**: Write a concise response (3–8 sentences) that answers the query by drawing from the matched pages. Cite each claim with a [[wikilink]] to its source page.

5. **List sources**: After the synthesis, list all matched pages with one-line descriptions:
   ```
   === Sources ===
   - [[summaries/page-slug]] — brief description
   - [[concepts/concept-slug]] — brief description
   ```

6. **Suggest next steps**:
   - If the answer is thin: "The wiki has limited coverage on this. Consider adding sources to `raw/` and running `/ingest`."
   - If related concepts exist: "See also: [[concept-link]]"
   - Offer `/file-back output` if the user wants to save the query result.

## Key Rules

- Never fabricate information — only report what's actually in the wiki.
- If nothing matches, say so clearly: "No wiki pages match this query."
- Keep the synthesis concise; the user can follow wikilinks for depth.
- For broad queries (e.g., "AI agents"), cap the source list at 15 most relevant pages.
