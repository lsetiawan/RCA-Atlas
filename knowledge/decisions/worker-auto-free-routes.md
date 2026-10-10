---
type: Decision
title: Deployed Auto mode stays on free routes
description: "The deployed Worker's Auto mode uses only Gemini and then Groq; the OpenAI fallback is opt-in for local development through .dev.vars."
tags: [ask-atlas, llm, cost, cloudflare-worker]
code_refs: ["src/atlas_worker/src/index.js"]
sources: ["commit 0fcd16d", "src/atlas_map/README.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Decision

Commit `0fcd16d` (2026-09-24): "The OpenAI fallback for Auto is opt-in for local development; the deployed Worker stays on its free routes." `AUTO_FALLBACK_OPENAI_MODEL` is set in `src/atlas_worker/.dev.vars` only, never in `wrangler.toml` or as a deployed secret (`src/atlas_worker/src/index.js:353-354`; `src/atlas_map/README.md:27-29`).

# Related Concepts
- [RCA Atlas Worker](../architecture/atlas-worker.md): Sets the deployed Worker's model fallback chain.
