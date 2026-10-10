---
type: Decision
title: The Chronfix correction applies only to the HYS14 OBS clock
description: "The bundled Chronfix clock correction belongs to the OO.HYS14 Hydrate Ridge ocean-bottom seismometer and is never applied to PREST, VEL3D, other instruments or already-corrected UTC."
tags: [coszo-hub, chronfix, seismology, timing]
code_refs: ["src/coszo_hub_tools/coszo_hub_agent_tools.py", "src/coszo_hub_tools/chronfix_model.py"]
sources: ["src/coszo_hub_tools/README.md", "docs/codebase/chapters/coszo-hub-core.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Decision

`src/coszo_hub_tools/README.md:138-145`: the model was derived and validated on `OO.HYS14..MHZ`; because the error belongs to the instrument clock it applies to every channel of that OBS, and never to PREST pressure, VEL3D current-meter, other-instrument or already-corrected UTC timestamps.

## Caveat

The code keeps the rule fully only when a target instrument is passed. Without one, substring keyword routing (`obs`, `wave`) can apply the correction to other timestamps (`docs/codebase/chapters/coszo-hub-core.md`, open question 6).

# Related Concepts
- [COSZO Hub tools](../architecture/coszo-hub-tools.md): Scopes the Chronfix correction that the COSZO Hub tools apply.
