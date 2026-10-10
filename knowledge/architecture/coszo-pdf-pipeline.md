---
type: Architecture
title: COSZO PDF pipeline
description: "Converts the COSZO project PDFs into a page-bounded Graph-RAG collection with native text, OCR, rendered pages and entity links."
tags: [corpus, pdf, ocr, coszo]
code_refs: ["src/coszo_pdf_pipeline/**"]
sources: ["src/coszo_pdf_pipeline/README.md", "docs/codebase/chapters/corpus-docs-web.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_coszo_pdf_graph.py` reads the top-level PDFs in `--source-dir`, extracts native text, OCRs scans with Tesseract, renders pages with Poppler, and writes chunks, entities, links, a manifest and a validation report to `data/coszo/graphrag`, which the runtime discovers as `coszo_documents`. Duplicate content is linked with `SAME_CONTENT_AS`, not removed.

## Talks to

- The instrument inventory's `instruments.jsonl` (optional), for instrument links.
- The Graph-RAG runtime.

## More

Chapter: `docs/codebase/chapters/corpus-docs-web.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the coszo_documents collection that the runtime discovers and loads.
