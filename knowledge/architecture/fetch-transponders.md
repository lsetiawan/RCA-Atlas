---
type: Architecture
title: FETCH transponders
description: "Builds the FETCH collection: the three acoustic ranging transponders on Axial Seamount, with no depth or manufacturer claimed."
tags: [corpus, fetch, axial, geodesy]
code_refs: ["src/fetch_transponders/**"]
sources: ["src/DATA_CORPUS_METHOD.md", "docs/codebase/chapters/corpus-instruments-ops.md"]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-09T23:57:20Z" }
status: stable
---

## Role

`build_fetch_corpus.py` reads the archived AxialFetch README and `config.py` from `source_material/` and writes `data/FETCH` (`fetch`). Raw time series stay in source material, and the graph does not state depth or manufacturer because the snapshot does not establish them.

## Talks to

- The Graph-RAG runtime.
- The Atlas map data build, which draws FETCH stations with fixed repository routes.

## More

Chapter: `docs/codebase/chapters/corpus-instruments-ops.md`.

# Related Concepts
- [Graph-RAG runtime](graphrag-runtime.md): Writes the fetch collection that the runtime loads.
