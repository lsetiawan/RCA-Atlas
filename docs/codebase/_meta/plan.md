# RCA Atlas knowledge base: chapter plan

As of `1047fc8` (branch `lsetiawan/explore`): 1,168 tracked files, split into 17 chapters of roughly
3,000 lines of code each. Each chapter is written by one documenter and checked by one verifier, per
[brief.md](brief.md).

## How to read the Paths column

Every path is a git pathspec, so `git ls-files -- <paths>` lists exactly the chapter's files:

- `dir/` matches every file beneath `dir`; a file name matches that file.
- In a plain pathspec `*` matches any characters, `/` included. Every plain `*` below sits in a
  directory without subdirectories, so it matches the same files as a shell glob.
- `:(glob)` makes `*` stay within one directory: `:(glob)*` is the top-level files only.
- `:(exclude)` removes matches from the chapter.

**Skim** in the notes marks lockfiles, `*.gz` tiles, binaries, large data files and vendored code: open
them with `head` only, or not at all, and describe them as a group.

`python3 docs/codebase/_meta/check_plan.py` expands the paths with `git ls-files` and confirms that every
tracked path outside `docs/codebase/` matches exactly one chapter. `--list <id>` prints one chapter's files.

## Changes from the starting table

- `src/atlas_map/src/scene/EvidenceLayer.js`, `evidenceMath.js`, `evidenceMath.test.js` and `evidence.css`
  move from atlas-map-scene to ask-atlas. The Ask Atlas design spec names `scene/EvidenceLayer.js` as part
  of that feature and says "Ask Atlas owns the map's evidence"
  (`docs/superpowers/specs/2026-09-24-ask-atlas-evidence-design.md`), the files arrived with the Ask Atlas
  evidence work (`61e4daf`), and the move brings atlas-map-scene from ~3,400 to ~2,900 lines.
- No other drift: every `src/` component and doc in the tree appears in the starting table.

## Chapters

| id | title | role | paths | notes |
|---|---|---|---|---|
| repo-ops-data | Repository, data releases and agent tooling | How the repo, its data releases and machine restores work, plus the agent tooling. | `:(glob)*` `scripts/` `data/` `runtime_data/` `source_material/` `.agents/` `.claude/` `knowledge/` `src/DATA_CORPUS_METHOD.md` `src/data_maintenance/` | `src/DATA_CORPUS_METHOD.md` and `data/CORPUS_METHOD.md` are near-duplicates: summarize once and list their differences. `.claude/skills` is a symlink to `../.agents/skills`. Skim: `pixi.lock` |
| corpus-docs-web | Document, figure, website and ARCADA collections | Collection builders: COSZO PDFs, figures and datasheets, websites, ARCADA. | `src/coszo_pdf_pipeline/` `src/figures_datasheets_pipeline/` `src/website_pipeline/` `src/arcada_pipeline/` | Skim: `src/website_pipeline/selection_log.jsonl` `src/website_pipeline/discovery_failures.json` `src/arcada_pipeline/build_audit.json` |
| corpus-instruments-ops | Instrument, operations and DAS collections | Instrument, operations and DAS collections, and the live tools beside them. | `src/instrument_inventory/` `src/nereus_pipeline/` `src/fetch_transponders/` `src/ooi_das_geometry/` | Skim: `src/nereus_pipeline/queries/metadata.json` |
| literature-corpus | Literature corpus and graph build | Builds the literature collection's graph artifacts and audits the Zotero expansion that grew it. | `src/literature_pipeline/` `:(exclude)src/literature_pipeline/code/coszo_abstracts/` `:(exclude)src/literature_pipeline/code/coszo_products/` | Per its README, `code/build_graph_corpus.py` reproduces the graph artifacts. Skim: `src/literature_pipeline/reports/` |
| literature-batches | COSZO abstract and product retrieval batches | Numbered retrieval batches that gathered COSZO abstracts and data products for the literature collection. | `src/literature_pipeline/code/coszo_abstracts/` `src/literature_pipeline/code/coszo_products/` | Numbered retrieval batches: document the stages and what each batch did, rather than every script line by line. |
| literature-fulltext | On-demand literature full text | MCP tools that fetch bounded open full-text passages when an abstract is not enough. | `src/literature_fulltext/` | |
| graphrag-runtime | Graph-RAG runtime: build, database and API | The core: corpus discovery, normalization, embeddings, the PostgreSQL + pgvector load, and the API with its evidence UI. | `src/graphrag_runtime/` | |
| eval-experiments | Model Lab and Microsoft GraphRAG layer | Compares answer and embedding models on fixed evidence, plus an optional Microsoft GraphRAG candidate layer. | `src/model_eval/` `src/microsoft_graphrag_layer/` | Skim: `src/model_eval/datasets/` |
| coszo-hub-core | COSZO Hub MCP server and core tools | The COSZO Hub snapshot graph, and the MCP server and tools that query COSZO Hub outputs live. | `src/coszo_hub_tools/README.md` `src/coszo_hub_tools/mcp_server.py` `src/coszo_hub_tools/run_mcp.sh` `src/coszo_hub_tools/coszo_hub_agent_tools.py` `src/coszo_hub_tools/build_coszo_hub_graph.py` `src/coszo_hub_tools/chronfix_model.py` `src/coszo_hub_tools/gap_detection.py` `src/coszo_hub_tools/extract_das_hdf5_metadata.py` `src/coszo_hub_tools/test_coszo_hub_agent_tools.py` `src/coszo_hub_tools/test_extract_das_hdf5_metadata.py` | |
| coszo-hub-sources | COSZO Hub sources: PI portal, OOI M2M, EarthScope FDSN | Tools and graph builders for the PI portal, OOI M2M and EarthScope FDSN sources that the COSZO Hub MCP server also serves. | `src/coszo_hub_tools/*pi_portal*` `src/coszo_hub_tools/*ooi_m2m*` `src/coszo_hub_tools/OOI_M2M_SOURCES.md` `src/coszo_hub_tools/*earthscope_fdsn*` | Read `src/coszo_hub_tools/README.md` first (it belongs to coszo-hub-core). |
| agentic-qaqc | Agentic QA/QC | MCP tools that join Graph-RAG context with live RCA QA/QC plots and notes and a pinned rca-data-tools backend. | `src/agentic_qaqc/` | `vendor/rca_data_tools/` is vendored upstream code: cover its purpose, its pin (`UPSTREAM.md`) and the entry points this chapter's code calls, not its internals. Skim: `src/agentic_qaqc/vendor/` |
| axial | Axial Seamount earthquakes and monitoring | Axial Seamount earthquake-catalog and monitoring-website collections and their live MCP tools. | `src/axial_earthquakes/` `src/axial_monitoring_website/` | |
| atlas-map-scene | Atlas map: shell and 3D scene | The React + three.js map website: its shell and 3D scene. | `:(glob)src/atlas_map/*` `src/atlas_map/public/` `src/atlas_map/e2e/atlas.spec.js` `src/atlas_map/e2e/mocks.js` `src/atlas_map/src/App.jsx` `src/atlas_map/src/main.jsx` `src/atlas_map/src/api/` `src/atlas_map/src/data/` `src/atlas_map/src/scene/` `:(exclude)src/atlas_map/src/scene/EvidenceLayer.js` `:(exclude)src/atlas_map/src/scene/evidenceMath.js` `:(exclude)src/atlas_map/src/scene/evidenceMath.test.js` `:(exclude)src/atlas_map/src/scene/evidence.css` `src/atlas_map/src/styles/` `src/atlas_map/src/test/setup.js` `src/atlas_map/src/test/fixtures.js` `docs/superpowers/specs/2026-09-23-atlas-map-design.md` | `public/` holds the committed 1 m Axial summit terrain tiles: describe their layout only. The scene's evidence files belong to ask-atlas. Skim: `src/atlas_map/package-lock.json` `src/atlas_map/public/` |
| atlas-map-panels | Atlas map: panels, HUD and overlays | Side panels with live data, the HUD controls, map overlays. | `src/atlas_map/src/panels/` `src/atlas_map/src/ui/` `src/atlas_map/src/overlay/` `docs/superpowers/specs/2026-09-24-hud-dock-design.md` | |
| ask-atlas | Ask Atlas: question to evidence on the map | One vertical slice: map sidebar → Cloudflare Worker → Graph-RAG API → LLM, and the evidence it raises on the map. | `src/atlas_map/src/ask/` `src/atlas_map/src/evidence/` `src/atlas_map/src/scene/EvidenceLayer.js` `src/atlas_map/src/scene/evidenceMath.js` `src/atlas_map/src/scene/evidenceMath.test.js` `src/atlas_map/src/scene/evidence.css` `src/atlas_map/src/test/fixtures/ask/` `src/atlas_map/e2e/ask.spec.js` `src/atlas_worker/` `src/atlas_ui/` `docs/superpowers/specs/2026-09-24-ask-atlas-evidence-design.md` | One vertical slice: map sidebar → Cloudflare Worker → Graph-RAG API → LLM. `src/atlas_ui/` is a standalone page that calls the same Worker. Skim: `src/atlas_ui/package-lock.json` `src/atlas_map/src/test/fixtures/ask/` `src/atlas_worker/test/fixtures/` |
| atlas-map-data | Atlas map data bundle | Builds the map's data bundle. | `src/atlas_map_data/` | Skim: `src/atlas_map_data/cable/rca_cable.geojson` `src/atlas_map_data/tests/fixtures/` |
| atlas-map-gateway | Atlas map gateway | Local live-lookup service behind the map. | `src/atlas_map_gateway/` | Skim: `src/atlas_map_gateway/tests/fixtures/` |
