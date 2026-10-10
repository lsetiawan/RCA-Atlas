---
type: Architecture
title: Literature pipeline
description: Reconciles the COSZO bibliography and two OOI Zotero collections into one canonical literature catalog and the graph files the runtime loads.
tags: [corpus, literature, zotero, crossref]
code_refs: ["src/literature_pipeline/**"]
sources: ["src/literature_pipeline/README.md", "src/DATA_CORPUS_METHOD.md", "docs/codebase/chapters/literature-corpus.md", "docs/codebase/chapters/literature-batches.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

Two trees of one-off, numbered batches (`code/coszo_abstracts/`, `code/coszo_products/`) gathered COSZO abstracts and product lists; they hard-code paths on the author's machine and cannot run from the repository alone. `code/zotero_expansion/` assembles and audits the Zotero additions. `code/build_graph_corpus.py` writes documents, chunks (520 words, 50 overlap), entities, relationships and citations beside `data/Literature/literature.jsonl` (336 works and 398 citation occurrences in the committed manifest). `reports/` keeps the QA audits.

## Talks to

- Public scholarly APIs: Crossref, OpenAlex, Europe PMC, Semantic Scholar and PubMed.
- The Graph-RAG runtime and the literature full-text tools.

## More

Chapter: `docs/codebase/chapters/literature-corpus.md`, `docs/codebase/chapters/literature-batches.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the literature collection's graph files that the runtime loads.
