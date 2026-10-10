---
type: Architecture
title: Nereus integration
description: "Builds the Nereus operational snapshot and serves ten live MCP tools that use only Nereus's public, allowlisted GraphQL operations."
tags: [mcp, nereus, operations, graphql, live-tools]
code_refs: ["src/nereus_pipeline/**"]
sources: ["src/nereus_pipeline/README.md", "docs/codebase/chapters/corpus-instruments-ops.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_nereus_corpus.py` writes `data/Nereus/graphrag`: the snapshot, an instrument crosswalk and the tool manifest. `nereus_agent_tools.py` posts the allowlisted operations in `queries/` to `nereus.ooirsn.uw.edu`, redacts private network details, and falls back to snapshots for three operations when a snapshot directory is set. `run_mcp.sh` starts the stdio server `rcn-agent-nereus`.

## Talks to

- Nereus GraphQL at `nereus.ooirsn.uw.edu`.
- The instrument inventory, through the crosswalk.
- The Atlas map gateway, which imports `NereusToolkit` for `/status` without a snapshot directory.

## More

Chapter: `docs/codebase/chapters/corpus-instruments-ops.md`.

# Related Concepts
- [Instrument inventory](instrument-inventory.md): Its crosswalk joins Nereus reference designators to inventory instruments.
