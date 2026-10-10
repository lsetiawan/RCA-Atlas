---
type: Architecture
title: Axial earthquake tools
description: "Builds an exact Axial Seamount earthquake store and Graph-RAG corpus from the UW catalog and serves 13 live MCP tools for counts, searches and figures."
tags: [mcp, axial, earthquakes, seismology, live-tools]
code_refs: ["src/axial_earthquakes/**"]
sources: ["src/axial_earthquakes/README.md", "docs/codebase/chapters/axial.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_axial_corpus.py` writes the SQLite store `runtime_data/AxialEarthquakes/graphrag/events.sqlite` and the corpus `data/AxialEarthquakes/graphrag`; `build_visual_archive.py` indexes dated maps and event images. `axial_agent_tools.py` answers from the live daily HYPO71 files first and falls back to the store, labelling `evidence_mode`; its days are UTC. Events are counted as valid catalog rows and kept out of the embedding corpus. `run_mcp.sh` starts the server.

## Talks to

- The UW catalog at `axial.ocean.washington.edu`.
- The Graph-RAG runtime.
- The Ask Atlas Worker, which reimplements the daily count for the asker's local day.

## More

Chapter: `docs/codebase/chapters/axial.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the axial_earthquakes collection and its tool manifest.
