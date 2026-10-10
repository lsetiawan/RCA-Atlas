---
type: Architecture
title: OOI DAS geometry
description: Publishes the channel geometry of the RCA fibre-optic DAS cables and reads the saved-interval masks in MultiDAS file headers.
tags: [corpus, das, fibre-optic, geometry]
code_refs: ["src/ooi_das_geometry/**"]
sources: ["src/DATA_CORPUS_METHOD.md", "docs/codebase/chapters/corpus-instruments-ops.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_ooi_das_geometry.py` writes `data/OOIDASGeometry` (channel locations, chunks, `tools.jsonl`) for the OptaSense QuantX geometry only, never for Silixa channels. `extract_multidas_mask_metadata.py` reads only file headers over HTTP; `chunk_meta.masked` names intervals that were saved, not masked out. `ooi_das_geometry_tools.py` is a lookup library with no caller outside its tests. No tracked script names the producer of `multidas_unmasked_coverage.jsonl`.

## Talks to

- The Graph-RAG runtime.
- The Atlas map data build, which draws DAS overlays.

## More

Chapter: `docs/codebase/chapters/corpus-instruments-ops.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the ooi_das_geometry collection that the runtime loads.
