---
type: Architecture
title: Data maintenance scripts
description: "Three scripts keep data/ to Markdown, JSON, JSONL and images, strip private network details from the corpus, and audit it before a release."
tags: [data, sanitization, audit, release]
code_refs: ["src/data_maintenance/**"]
sources: ["src/DATA_CORPUS_METHOD.md", "docs/codebase/chapters/repo-ops-data.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`clean_data_folder.py` moves originals to `source_material/` and databases and `.gz` files to `runtime_data/`, so `data/` holds only Markdown, JSON, JSONL, PNG and JPEG; it also writes `data/StationMetadata/` from StationXML. `sanitize_sensitive_network_info.py` removes private network fields and addresses from the corpus but does not touch `source_material/`, which still ships in releases. `audit_sensitive_network_info.py` reports what remains; a release should pass only with zero findings, but no script enforces that gate.

## Talks to

- `data/`, `source_material/` and `runtime_data/`, before the release scripts pack them.
- The Graph-RAG runtime and the Atlas map data build, which read `data/StationMetadata/`.

## More

Chapter: `docs/codebase/chapters/repo-ops-data.md`.

# Related Concepts
- [Data and release lifecycle](data-release-lifecycle.md): Cleans and audits data/ before the release scripts pack it.
