---
type: Architecture
title: Axial monitoring website tools
description: Archives the OSU Axial monitoring pages as the axial_monitoring collection and serves three live MCP tools for their plots.
tags: [mcp, axial, monitoring, live-tools]
code_refs: ["src/axial_monitoring_website/**"]
sources: ["docs/codebase/chapters/axial.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_axial_monitoring_graph.py` reads an archived snapshot in `source_material/original_documents/AxialCEOAS/` and writes `data/AxialMonitoring`. `axial_monitoring_tools.py` fetches only allowlisted plot streams, which are volatile, pre-QA displays rather than evidence. `mcp_server.py` has no launcher script.

## Talks to

- The OSU monitoring site.
- The Graph-RAG runtime.

## More

Chapter: `docs/codebase/chapters/axial.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the axial_monitoring collection that the runtime loads.
