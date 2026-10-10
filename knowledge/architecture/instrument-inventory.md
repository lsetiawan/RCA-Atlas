---
type: Architecture
title: Instrument inventory
description: "Compiles data/Instruments, the instrument-level inventory of RCA and COSZO instruments that nearly every other component joins on."
tags: [corpus, instruments, inventory, refdes]
code_refs: ["src/instrument_inventory/**"]
sources: ["src/instrument_inventory/PIPELINE_README.md", "docs/codebase/chapters/corpus-instruments-ops.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_instrument_inventory.py` builds instrument, chunk, entity, relationship, type and infrastructure files from the ARCADA collection and archived OOI site inventories, with hard-coded evidence IDs for COSZO and PI facts. It keeps each source's catalog status wording, infers nothing about current operation, and keeps junction boxes out of instrument counts.

## Talks to

- Reads `data/Arcada` and archived OOI site-inventory HTML in `source_material/`.
- Feeds the Graph-RAG runtime, the Atlas map data build, the QA/QC tools, OOI M2M search, the PI-portal builder, the Nereus crosswalk and the literature candidate graph.

## More

Chapter: `docs/codebase/chapters/corpus-instruments-ops.md`.

# Related Concepts
- [ARCADA pipeline](arcada-pipeline.md): Reads the ARCADA documents and chunks to build instrument records.
- [Graph-RAG runtime](graphrag-runtime.md): Writes the instruments collection that the runtime loads.
