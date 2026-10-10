---
type: Requirement
title: No private network details leave the Nereus adapter
description: "Private network fields and private addresses are redacted from Nereus live results, caches, snapshots and the corpus, and no MCP switch overrides this."
tags: [security, nereus, redaction]
code_refs: ["src/nereus_pipeline/**"]
sources: ["src/nereus_pipeline/README.md", "src/DATA_CORPUS_METHOD.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Requirement

`src/nereus_pipeline/README.md:9`: private-network fields and private addresses in free text are always redacted from live-tool results, caches, snapshots and the normalized corpus, and the MCP schemas expose no override. `src/DATA_CORPUS_METHOD.md:751-753`: the sanitizer is recursive because operational-note prose can carry an address after the structured fields are removed.

## Implication

Any new Nereus operation, cache or output path must run the sanitizer before returning or caching data.

# Related Concepts
- [Nereus integration](../architecture/nereus-pipeline.md): Constrains every Nereus result, cache and snapshot.
