---
type: Decision
title: Operational values come from live tools
description: "Stable knowledge is indexed in Graph-RAG, while operational values that change after a build are queried through live MCP tools with labelled, timestamped snapshot fallback."
tags: [live-tools, snapshots, graph-rag]
code_refs: ["src/nereus_pipeline/**", "src/axial_earthquakes/**", "src/agentic_qaqc/**", "src/coszo_hub_tools/**"]
sources: ["src/DATA_CORPUS_METHOD.md", "src/nereus_pipeline/README.md", "src/axial_earthquakes/README.md", "commit 37044ae"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Decision

`src/DATA_CORPUS_METHOD.md:74-76`: "Stable knowledge is indexed in Graph-RAG. Operational values that can change after a build are queried through MCP tools, with timestamped snapshot fallback where available." Nereus state, telemetry, notes and histories are queried live (`src/nereus_pipeline/README.md:7-8`), and current-day Axial questions use the live tools, with the store as history and fallback (`src/axial_earthquakes/README.md:66`).

## Implication

Results carry their evidence mode, and a snapshot answer is never presented as a live check: the map labels it "from Nereus snapshot" (commit `37044ae`).

# Related Concepts
- [Nereus integration](../architecture/nereus-pipeline.md): Nereus status is queried live with a labelled snapshot fallback.
- [Axial earthquake tools](../architecture/axial-earthquakes.md): Current-day counts come from the live catalog, with the store as fallback.
