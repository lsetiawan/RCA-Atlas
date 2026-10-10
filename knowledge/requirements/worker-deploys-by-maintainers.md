---
type: Requirement
title: Only the maintainers deploy the Worker
description: "Agents and contributors do not deploy the Cloudflare Worker; Derek and Maleen deploy it, and the map must keep working against the currently deployed Worker."
tags: [deployment, cloudflare-worker, ask-atlas]
code_refs: ["src/atlas_worker/**"]
sources: ["docs/superpowers/specs/2026-09-24-ask-atlas-evidence-design.md", "commit d557fb6"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Requirement

`docs/superpowers/specs/2026-09-24-ask-atlas-evidence-design.md:152-153`: "Do not deploy the Worker; Derek/Maleen deploy." Until a new Worker is deployed, the frontend must work against the current one, which may send no `[n]`, no `excerpt` and no `events`.

## Related rule

Worker changes are additive, so the published `src/atlas_ui` page keeps working; it strips `[n]` markers (spec lines 141-146; commit `d557fb6`).

# Related Concepts
- [RCA Atlas Worker](../architecture/atlas-worker.md): Governs who deploys the Worker.
