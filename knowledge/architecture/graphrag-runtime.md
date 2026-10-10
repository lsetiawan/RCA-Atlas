---
type: Architecture
title: Graph-RAG runtime
description: "Turns the corpus collections into one immutable PostgreSQL + pgvector build and serves bounded hybrid search, graph neighbours and tool hints behind an API key."
tags: [graph-rag, postgresql, pgvector, fastapi, embeddings]
code_refs: ["src/graphrag_runtime/**"]
sources: ["src/graphrag_runtime/README.md", "docs/codebase/chapters/graphrag-runtime.md", "docs/codebase/flows/corpus-to-index.md", "docs/codebase/flows/restore-and-run.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:18Z" }
status: stable
---

## Role

Four offline steps: `discover_corpora.py` catalogs every `data/**/manifest.json` and fingerprints the inputs; `normalize_corpus.py` builds logical nodes, chunks, links and edges keyed by `(collection_id, local_id)`; `build_embeddings.py` embeds chunks with the pinned `BAAI/bge-small-en-v1.5` model (384 dimensions); `load_postgres.py` loads the build in one transaction and activates it. A FastAPI app reads only through four `graphrag_api` SQL functions as a read-only role, behind SHA-256-hashed client keys: `/v1/search`, `/v1/neighbors`, `/v1/tools`, `/v1/context`, `/v1/answer` and an evidence page. Docker Compose runs the `db`, `loader` and `api` services.

## Talks to

- Every collection builder, through the `data/` manifests and JSONL files.
- The Ask Atlas Worker (`POST /v1/context`), the map gateway's unused `POST /chat` (`/v1/answer`), and the Model Lab and Microsoft GraphRAG layer (normalized chunks).

## More

Chapter: `docs/codebase/chapters/graphrag-runtime.md`. Flows: `docs/codebase/flows/corpus-to-index.md`, `docs/codebase/flows/restore-and-run.md`.
