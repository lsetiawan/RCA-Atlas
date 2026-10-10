---
type: Architecture
title: Model Lab
description: A library and CLI for comparing answer and embedding models on one frozen evidence package; its answer-comparison path has no caller yet.
tags: [evaluation, llm, embeddings]
code_refs: ["src/model_eval/**"]
sources: ["src/model_eval/README.md", "docs/codebase/chapters/eval-experiments.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Role

`python -m model_eval` (with `PYTHONPATH=src`) runs `validate`, `dry-run` and `cost-report`. Providers and candidate embedding indexes are configured in `config/*.json`, naming keys by environment variable only. The 60-question set and gold answers are in `datasets/`. No code builds an evidence package from live retrieval or writes evaluation results, and the answer champion stays unselected.

## Talks to

- Model-provider APIs, with keys from the environment.
- The Graph-RAG runtime, whose pinned BGE model it records as the retrieval champion.

## More

Chapter: `docs/codebase/chapters/eval-experiments.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Records the runtime's pinned BGE model as its retrieval champion.
