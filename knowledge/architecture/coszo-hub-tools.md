---
type: Architecture
title: COSZO Hub tools
description: "The COSZO Hub snapshot builder and MCP server, plus live adapters for the PI portal, OOI M2M and EarthScope FDSN that the same server exposes."
tags: [mcp, coszo-hub, pi-portal, ooi-m2m, earthscope, live-tools]
code_refs: ["src/coszo_hub_tools/**"]
sources: ["src/coszo_hub_tools/README.md", "src/coszo_hub_tools/OOI_M2M_SOURCES.md", "docs/codebase/chapters/coszo-hub-core.md", "docs/codebase/chapters/coszo-hub-sources.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_coszo_hub_graph.py` writes `data/COSZOHub` from checkouts of the `coszo-hub` repositories (PREST, VEL3D, Chronfix, Dive Index), and `build_pi_portal_graph.py` writes `data/PIPortal`. `mcp_server.py` serves 41 tools: 19 from `coszo_hub_agent_tools.py`, which rescans live output trees into `runtime_data/COSZOHub/output_index.sqlite` and applies the HYS14 Chronfix clock correction, and 22 from the PI portal, OOI M2M and EarthScope adapters. Downloads go under `runtime_data/`; live OOI calls need `OOI_USERNAME` and `OOI_TOKEN`.

## Talks to

- Repository checkouts in `source_material/repositories/coszo-hub/`.
- The PI portal, OOI M2M and EarthScope FDSN services.
- The Graph-RAG runtime.
- The Atlas map gateway, which imports the PI portal and EarthScope toolkits.

## More

Chapter: `docs/codebase/chapters/coszo-hub-core.md`, `docs/codebase/chapters/coszo-hub-sources.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the coszo_hub and pi_portal collections that the runtime loads.
