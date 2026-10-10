---
type: Architecture
title: Figures and datasheets pipelines
description: "Builds the curated figures and instrument-datasheets collections, linking each image or datasheet page to sites, products and inventory instruments."
tags: [corpus, figures, datasheets, ocr]
code_refs: ["src/figures_datasheets_pipeline/**"]
sources: ["src/figures_datasheets_pipeline/README.md", "docs/codebase/chapters/corpus-docs-web.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_figures_graph.py` adds curated descriptions, OCR labels and cross-corpus image matches without copying the images, and refuses a new image that has no curated entry. `build_datasheets_graph.py` extracts and OCRs datasheet PDFs and links them to products, software, standards and the inventory; it needs Python 3.12 or later. Outputs are `data/Figures/graphrag` (`figures`) and `data/Datasheets/graphrag` (`datasheets`).

## Talks to

- The instrument inventory.
- The Graph-RAG runtime.

## More

Chapter: `docs/codebase/chapters/corpus-docs-web.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the figures and datasheets collections that the runtime loads.
