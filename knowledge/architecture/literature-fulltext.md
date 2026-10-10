---
type: Architecture
title: Literature full-text tools
description: "MCP tools that fetch bounded, cached open full-text passages for a work only when its abstract is relevant but insufficient."
tags: [mcp, literature, full-text, live-tools]
code_refs: ["src/literature_fulltext/**"]
sources: ["src/literature_fulltext/README.md", "docs/codebase/chapters/literature-fulltext.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`literature_fulltext_tools.py` serves `literature_full_text_status` and `literature_full_text_evidence` over stdio (`run_mcp.sh`). Fetches are SSRF-checked and bounded in size and pages, cached under `runtime_data/Literature/full_text_cache/`, and returned as at most 10 passages with page or section locators. Batch scripts acquire open full text (gated by `--confirm-open-access`), import licensed PDFs, build a candidate paper-to-RCA graph, and write the tool manifest.

## Talks to

- `data/Literature/literature.jsonl`.
- Unpaywall and publisher sites.
- The overlay release that ships the cache.

## More

Chapter: `docs/codebase/chapters/literature-fulltext.md`.

# Related Concepts
- [Literature pipeline](literature-pipeline.md): Resolves works against the canonical literature catalog.
