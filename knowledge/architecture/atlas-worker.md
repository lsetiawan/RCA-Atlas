---
type: Architecture
title: RCA Atlas Worker
description: "The Cloudflare Worker that is RCA Atlas's public boundary: it answers Ask Atlas questions from Graph-RAG evidence and an LLM, and proxies allowlisted live-data paths."
tags: [service, cloudflare-worker, ask-atlas, llm]
code_refs: ["src/atlas_worker/**"]
sources: ["src/atlas_worker/README.md", "docs/superpowers/specs/2026-09-24-ask-atlas-evidence-design.md", "docs/codebase/chapters/ask-atlas.md", "docs/codebase/flows/ask-atlas.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Role

`src/atlas_worker/src/index.js` accepts `POST /v1/answer` only from `ALLOWED_ORIGIN` (`https://coszo.org`). Axial earthquake-count questions are answered directly from the UW daily catalog files for the asker's time zone. Other questions call Graph-RAG `POST /v1/context`, rank and number the sources, and ask Gemini (then Groq under Auto) for an answer that cites them as `[n]`. `GET /v1/live/*` forwards allowlisted paths to `ATLAS_MAP_GATEWAY_ORIGIN`. Keys are Wrangler secrets, and the maintainers deploy it.

## Talks to

- The Graph-RAG API, through a Cloudflare Tunnel.
- Gemini, Groq and OpenAI.
- The UW Axial catalog.
- The map gateway.

## More

Chapter: `docs/codebase/chapters/ask-atlas.md`. Flows: `docs/codebase/flows/ask-atlas.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Calls POST /v1/context for evidence.
- [Atlas map gateway](atlas-map-gateway.md): Proxies allowlisted /v1/live paths to the gateway.
- [Axial earthquake tools](axial-earthquakes.md): Reimplements the daily earthquake count, for the asker's local day instead of UTC.
