---
type: Architecture
title: Microsoft GraphRAG candidate layer
description: Exports normalized Atlas chunks as input for an external Microsoft GraphRAG pilot whose output stays a reviewed candidate layer.
tags: [evaluation, graphrag, candidate-graph]
code_refs: ["src/microsoft_graphrag_layer/**"]
sources: ["src/microsoft_graphrag_layer/README.md", "docs/codebase/chapters/eval-experiments.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Role

`prepare_input.py` writes one text file per chunk plus `atlas_source_manifest.jsonl` (chunk ID, collection, source URL, content hash). `settings.template.yaml` configures the pilot, which uses its own key. Nothing in the repository reads the pilot's output, and the README's example filter `figures_datasheets` matches no collection.

## Talks to

- The Graph-RAG runtime's normalized `chunks.jsonl`.

## More

Chapter: `docs/codebase/chapters/eval-experiments.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Exports the runtime's normalized chunks to the pilot.
