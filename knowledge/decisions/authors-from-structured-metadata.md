---
type: Decision
title: Author and citation edges only from structured metadata
description: The literature graph creates author nodes only from verified structured names and never parses inconsistent citation strings to invent authors or work-to-work citation edges.
tags: [literature, graph, authors]
code_refs: ["src/literature_pipeline/code/build_graph_corpus.py"]
sources: ["src/literature_pipeline/README.md", "src/DATA_CORPUS_METHOD.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Decision

`src/literature_pipeline/README.md:14` and `src/DATA_CORPUS_METHOD.md:268-270`: citation strings are too inconsistent to parse, so author identities and work-to-work citation edges are never guessed from them. Topical edges use curated literal matches that keep their evidence text.

# Related Concepts
- [Literature pipeline](../architecture/literature-pipeline.md): Governs the literature graph's author and citation edges.
