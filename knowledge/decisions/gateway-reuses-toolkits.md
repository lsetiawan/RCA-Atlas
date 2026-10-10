---
type: Decision
title: The map gateway reuses the agent toolkits
description: "The Atlas map gateway calls the Nereus, QA/QC, PI portal and EarthScope toolkits through their public methods instead of reimplementing them, so it inherits their host allowlists, bounds and sanitizers."
tags: [atlas-map, gateway, toolkits]
code_refs: ["src/atlas_map_gateway/**"]
sources: ["docs/superpowers/specs/2026-09-23-atlas-map-design.md", "docs/codebase/chapters/atlas-map-gateway.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Decision

`docs/superpowers/specs/2026-09-23-atlas-map-design.md:177-184`: the gateway "imports his existing toolkits rather than reimplementing them" and calls each through its public methods.

## Known gaps

`QAQCToolkit` has no host allowlist, the gateway builds the Nereus toolkit without a snapshot directory, and the gateway re-applies exact matches after the toolkits' substring matches (`docs/codebase/chapters/atlas-map-gateway.md`; `docs/codebase/flows/live-panel.md`).

# Related Concepts
- [Atlas map gateway](../architecture/atlas-map-gateway.md): Sets how the gateway reaches its upstream sources.
