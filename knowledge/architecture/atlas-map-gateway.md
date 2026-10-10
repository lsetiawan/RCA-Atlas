---
type: Architecture
title: Atlas map gateway
description: "A local FastAPI service on 127.0.0.1:8787 that answers the map's live lookups only for ids listed in the bundle, with TTL caches, per-source limits and one error shape."
tags: [service, fastapi, live-data, gateway]
code_refs: ["src/atlas_map_gateway/**"]
sources: ["src/atlas_map_gateway/README.md", "docs/superpowers/specs/2026-09-23-atlas-map-design.md", "docs/codebase/chapters/atlas-map-gateway.md", "docs/codebase/flows/live-panel.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Role

Routes: `/status/{refdes}` (Nereus), `/series/...` (ERDDAP), `/plots/{refdes}` (QA/QC), `/files/{instrumentKey}` (PI portal), `/waveform/{station}` and `/waveform/{station}/health` (EarthScope), and an unused `POST /chat`. It reads `sensors.json` once at start and calls the Nereus, QA/QC, PI portal and EarthScope toolkits through their public methods.

## Talks to

- The bundle's `sensors.json`.
- Toolkits from `nereus_pipeline`, `agentic_qaqc` and `coszo_hub_tools`.
- ERDDAP, directly.
- Callers: the Vite proxy in development and the Worker's `/v1/live` in production.

## More

Chapter: `docs/codebase/chapters/atlas-map-gateway.md`. Flows: `docs/codebase/flows/live-panel.md`.

# Related Concepts
- [Atlas map data bundle](atlas-map-data.md): Builds its id allowlist from the bundle's sensors.json.
- [Nereus integration](nereus-pipeline.md): Imports NereusToolkit for /status.
- [Agentic QA/QC tools](agentic-qaqc.md): Imports QAQCToolkit for /plots.
- [COSZO Hub tools](coszo-hub-tools.md): Imports the PI portal and EarthScope toolkits for /files and /waveform.
