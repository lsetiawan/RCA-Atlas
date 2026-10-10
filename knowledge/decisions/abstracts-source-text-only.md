---
type: Decision
title: "Abstracts are source text, never generated"
description: "A literature record's abstract is the source's own text; a work without a reliable abstract keeps a bibliographic chunk and a null abstract, never generated text."
tags: [literature, provenance, abstracts]
code_refs: ["src/literature_pipeline/code/**"]
sources: ["src/DATA_CORPUS_METHOD.md", "docs/codebase/chapters/literature-corpus.md", "docs/codebase/chapters/literature-batches.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Decision

`src/DATA_CORPUS_METHOD.md:251-253`: records without a reliable abstract keep a bibliographic retrieval chunk instead of fabricated text. The merge step labels its text "a source abstract, not an agent-generated summary", and descriptions, standfirsts, manuals, books, grants, datasets and websites are not promoted to abstracts (`docs/codebase/chapters/literature-corpus.md`, `docs/codebase/chapters/literature-batches.md`).

# Related Concepts
- [Literature pipeline](../architecture/literature-pipeline.md): Governs what the catalog's abstract field may hold.
