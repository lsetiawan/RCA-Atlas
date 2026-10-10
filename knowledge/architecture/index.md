# Architecture
* [Data and release lifecycle](data-release-lifecycle.md) - Versioned corpus data stays out of Git and moves between machines as private GitHub Release assets that scripts/bootstrap_machine.sh verifies and restores.
* [Data maintenance scripts](data-maintenance.md) - Three scripts keep data/ to Markdown, JSON, JSONL and images, strip private network details from the corpus, and audit it before a release.
* [Graph-RAG runtime](graphrag-runtime.md) - Turns the corpus collections into one immutable PostgreSQL + pgvector build and serves bounded hybrid search, graph neighbours and tool hints behind an API key.
* [COSZO PDF pipeline](coszo-pdf-pipeline.md) - Converts the COSZO project PDFs into a page-bounded Graph-RAG collection with native text, OCR, rendered pages and entity links.
* [Figures and datasheets pipelines](figures-datasheets-pipeline.md) - Builds the curated figures and instrument-datasheets collections, linking each image or datasheet page to sites, products and inventory instruments.
* [Website crawler](website-pipeline.md) - Crawls coszo.org, oceanobservatories.org and Interactive Oceans into the websites collection in three stages: discover, build and package.
* [ARCADA pipeline](arcada-pipeline.md) - Converts the pinned upstream ARCADA repository's chunks and catalogs into the arcada collection, which users see as RCA Information.
* [Instrument inventory](instrument-inventory.md) - Compiles data/Instruments, the instrument-level inventory of RCA and COSZO instruments that nearly every other component joins on.
* [Nereus integration](nereus-pipeline.md) - Builds the Nereus operational snapshot and serves ten live MCP tools that use only Nereus's public, allowlisted GraphQL operations.
* [FETCH transponders](fetch-transponders.md) - Builds the FETCH collection: the three acoustic ranging transponders on Axial Seamount, with no depth or manufacturer claimed.
* [OOI DAS geometry](ooi-das-geometry.md) - Publishes the channel geometry of the RCA fibre-optic DAS cables and reads the saved-interval masks in MultiDAS file headers.
* [Literature pipeline](literature-pipeline.md) - Reconciles the COSZO bibliography and two OOI Zotero collections into one canonical literature catalog and the graph files the runtime loads.
* [Literature full-text tools](literature-fulltext.md) - MCP tools that fetch bounded, cached open full-text passages for a work only when its abstract is relevant but insufficient.
* [COSZO Hub tools](coszo-hub-tools.md) - The COSZO Hub snapshot builder and MCP server, plus live adapters for the PI portal, OOI M2M and EarthScope FDSN that the same server exposes.
* [Agentic QA/QC tools](agentic-qaqc.md) - MCP tools that join instrument identity from the inventory with the live RCA QA/QC dashboard's plot index and human-in-the-loop notes, plus an opt-in vendored plot pipeline.
* [Axial earthquake tools](axial-earthquakes.md) - Builds an exact Axial Seamount earthquake store and Graph-RAG corpus from the UW catalog and serves 13 live MCP tools for counts, searches and figures.
* [Axial monitoring website tools](axial-monitoring-website.md) - Archives the OSU Axial monitoring pages as the axial_monitoring collection and serves three live MCP tools for their plots.
* [Model Lab](model-eval.md) - A library and CLI for comparing answer and embedding models on one frozen evidence package; its answer-comparison path has no caller yet.
* [Microsoft GraphRAG candidate layer](microsoft-graphrag-layer.md) - Exports normalized Atlas chunks as input for an external Microsoft GraphRAG pilot whose output stays a reviewed candidate layer.
* [Atlas map website](atlas-map.md) - The React and three.js website that draws the seafloor off Oregon in 3D with every located sensor, live panels and the Ask Atlas sidebar.
* [Atlas map data bundle](atlas-map-data.md) - Builds the map's static data bundle in src/atlas_map/public/atlas from the restored corpus, GMRT terrain and the committed cable route.
* [Atlas map gateway](atlas-map-gateway.md) - A local FastAPI service on 127.0.0.1:8787 that answers the map's live lookups only for ids listed in the bundle, with TTL caches, per-source limits and one error shape.
* [RCA Atlas Worker](atlas-worker.md) - The Cloudflare Worker that is RCA Atlas's public boundary: it answers Ask Atlas questions from Graph-RAG evidence and an LLM, and proxies allowlisted live-data paths.
* [Standalone Ask Atlas page](atlas-ui.md) - A standalone page that sends questions to the same Worker, strips citation markers, lists sources and draws its own 2D evidence graph.
