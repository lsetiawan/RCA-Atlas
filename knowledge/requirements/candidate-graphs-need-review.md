---
type: Requirement
title: Candidate graphs never write to the authoritative graph
description: "Machine-derived candidate graphs, from Microsoft GraphRAG or the literature full-text matcher, stay outside the authoritative PostgreSQL graph until evaluation, review and a separately approved merge."
tags: [graph, review, provenance, evaluation]
code_refs: ["src/microsoft_graphrag_layer/**", "src/literature_fulltext/build_candidate_graph.py"]
sources: ["src/microsoft_graphrag_layer/README.md", "src/literature_fulltext/README.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:22Z" }
status: stable
---

## Requirement

`src/microsoft_graphrag_layer/README.md:3-9`: candidate entities, relationships, communities and reports never write into the authoritative graph directly, and candidate edges must keep the Atlas chunk ID, collection, source URL and content hash. `src/literature_fulltext/README.md:50-55`: the full-text candidate graph remains a candidate layer until graph validation approves a merge.

## Open

Who evaluates and approves merges is not recorded (`docs/codebase/open-questions.md`).

# Related Concepts
- [Microsoft GraphRAG candidate layer](../architecture/microsoft-graphrag-layer.md): Keeps the pilot's output a candidate layer.
- [Literature full-text tools](../architecture/literature-fulltext.md): Keeps the full-text candidate graph out of the canonical graph.
