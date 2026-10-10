---
type: Decision
title: "ARCADA is shown as RCA Information, with its internal id kept"
description: "The arcada collection is presented to users as RCA Information, while its stable internal ID arcada, upstream identifiers and source URLs stay unchanged for reproducibility and attribution."
tags: [naming, arcada, provenance]
code_refs: ["src/graphrag_runtime/discover_corpora.py", "src/arcada_pipeline/**"]
sources: ["src/DATA_CORPUS_METHOD.md", "commit 29dca19"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Decision

`src/DATA_CORPUS_METHOD.md:194-199` and commit `29dca19` ("Present Arcada corpus as RCA Information"). The mapping lives in `src/graphrag_runtime/discover_corpora.py:24-26`; the evaluation set was renamed in the same commit.

# Related Concepts
- [ARCADA pipeline](../architecture/arcada-pipeline.md): Names the collection this pipeline builds.
- [Graph-RAG runtime](../architecture/graphrag-runtime.md): The runtime maps the arcada id to its display name.
