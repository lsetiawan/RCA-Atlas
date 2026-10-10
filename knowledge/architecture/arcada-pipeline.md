---
type: Architecture
title: ARCADA pipeline
description: "Converts the pinned upstream ARCADA repository's chunks and catalogs into the arcada collection, which users see as RCA Information."
tags: [corpus, arcada, rca-information]
code_refs: ["src/arcada_pipeline/**"]
sources: ["src/arcada_pipeline/PIPELINE_README.md", "docs/codebase/chapters/corpus-docs-web.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_arcada_graph.py` reads `public/chunks.json`, `catalog/instruments.json` and `catalog/papers.json` from `mhemmett/arcada` at commit `14294bca45ce5f65fd6541bea68ab40fbc870659` and writes `data/Arcada`. It keeps all 802 rows, gives six placeholder duplicates unique IDs with an audit trail (`build_audit.json`), and does not re-chunk the upstream text.

## Talks to

- The instrument inventory, which reads its documents and chunks.
- The Graph-RAG runtime.
- Ask Atlas, which resolves `ARCADA-INSTRUMENT-` IDs to map positions.

## More

Chapter: `docs/codebase/chapters/corpus-docs-web.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the arcada collection that the runtime serves as RCA Information.
