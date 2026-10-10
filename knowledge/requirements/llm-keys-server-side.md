---
type: Requirement
title: Model and Graph-RAG keys never reach the browser
description: "The Gemini key goes only to the Graph-RAG API container and the Worker's secrets, and no model or Graph-RAG key is ever exposed to a browser or the public Pages preview."
tags: [security, secrets, llm]
code_refs: ["src/graphrag_runtime/app/**", "src/atlas_worker/src/index.js"]
sources: ["src/graphrag_runtime/README.md", "src/atlas_worker/README.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:22Z" }
status: stable
---

## Requirement

`src/graphrag_runtime/README.md:20-21`: the Gemini key is passed only to the API container and never exposed to a browser or the public Pages preview. `src/atlas_worker/README.md:7`: the Worker never exposes the Gemini or Graph-RAG credentials to the browser. The evidence page keeps its API key in memory only.

## Caveat

Both server-side Gemini callers put the key in the request URL (`docs/codebase/configuration.md`).

# Related Concepts
- [Graph-RAG runtime](../architecture/graphrag-runtime.md): The API container holds the Gemini key.
- [RCA Atlas Worker](../architecture/atlas-worker.md): The Worker holds its keys as secrets.
