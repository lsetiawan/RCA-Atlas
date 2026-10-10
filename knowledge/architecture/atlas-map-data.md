---
type: Architecture
title: Atlas map data bundle
description: "Builds the map's static data bundle in src/atlas_map/public/atlas from the restored corpus, GMRT terrain and the committed cable route."
tags: [map, bundle, terrain, build]
code_refs: ["src/atlas_map_data/**"]
sources: ["src/atlas_map_data/README.md", "docs/codebase/chapters/atlas-map-data.md", "docs/codebase/flows/atlas-bundle.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:21Z" }
status: stable
---

## Role

`python -m atlas_map_data.build_atlas_bundle` reads Instruments, FETCH, Nereus, PI portal, StationMetadata and DAS geometry from `data/`, applies the reviewed `corrections.json`, assigns status and data routes on allowlisted hosts, clusters sensors into sites within 150 m, validates, and only then writes the JSON and terrain files, `manifest.json` last. `--refresh-terrain` and `--refresh-external` refresh the GMRT, ERDDAP, EarthScope and QA/QC caches. Optional builders write the committed 1 m AUV summit tiles and `subsurface.json`; `cable/` holds the offline cable-route scripts and `rca_cable.geojson`.

## Talks to

- Corpus collections in `data/`.
- GMRT, ERDDAP, EarthScope and the QA/QC dashboard.
- The map and the gateway, which read the bundle.

## More

Chapter: `docs/codebase/chapters/atlas-map-data.md`. Flows: `docs/codebase/flows/atlas-bundle.md`.

# Related Concepts
- [Instrument inventory](instrument-inventory.md): Builds sensor records from data/Instruments.
