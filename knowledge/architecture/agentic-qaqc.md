---
type: Architecture
title: Agentic QA/QC tools
description: "MCP tools that join instrument identity from the inventory with the live RCA QA/QC dashboard's plot index and human-in-the-loop notes, plus an opt-in vendored plot pipeline."
tags: [mcp, qaqc, dashboard, live-tools]
code_refs: ["src/agentic_qaqc/**"]
sources: ["src/agentic_qaqc/README.md", "src/agentic_qaqc/UPSTREAM.md", "docs/codebase/chapters/agentic-qaqc.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`qaqc_agent_tools.py` (`QAQCToolkit`) reads `QAQC_plots/index.json` and `HITL_notes/` from `ec2.qaqc.ooi-rca.net`, parses plot file names, and serves ten tools over stdio (`run_mcp.sh`). The plot index stays in memory for the life of the process. `build_agentic_graph.py` writes the static `data/QAQC/graphrag` layer. `vendor/rca_data_tools/` is upstream code pinned in `UPSTREAM.md`; running it needs `QAQC_AGENT_ALLOW_PIPELINE=1`.

## Talks to

- The QA/QC dashboard.
- `data/Instruments`.
- The Atlas map gateway (`/plots`) and the bundle build, which use the toolkit.

## More

Chapter: `docs/codebase/chapters/agentic-qaqc.md`.

# Related Concepts
- [Instrument inventory](instrument-inventory.md): Resolves instruments through data/Instruments.
