---
type: Architecture
title: Standalone Ask Atlas page
description: "A standalone page that sends questions to the same Worker, strips citation markers, lists sources and draws its own 2D evidence graph."
tags: [web-app, ask-atlas]
code_refs: ["src/atlas_ui/**"]
sources: ["docs/codebase/chapters/ask-atlas.md", "docs/codebase/flows/ask-atlas.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Role

`src/atlas_ui/src/main.jsx` posts to the Worker without a time zone, so "today" is the UTC day there; it does not place evidence on a map, and it reads `answer_links`. It works only when served from `https://coszo.org`; where it is hosted is not recorded in the repository.

## Talks to

- The Cloudflare Worker's `POST /v1/answer`.

## More

Chapter: `docs/codebase/chapters/ask-atlas.md`. Flows: `docs/codebase/flows/ask-atlas.md`.

# Related Concepts
- [RCA Atlas Worker](atlas-worker.md): Posts questions to the Worker's /v1/answer.
