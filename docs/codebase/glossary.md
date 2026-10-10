# Glossary

Every term the chapters define, merged, deduplicated and alphabetized. Where several chapters define a term,
the definition comes from the chapter that uses it most, listed first under **Chapters**; the chapters hold
the citations behind each definition. Back to the [knowledge base README](README.md).

| Term | Meaning | Chapters |
|---|---|---|
| A-0-A (A0ABPA301) | A calibrated pressure instrument at Central Caldera. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Abstract | A paper's formal summary, taken from the publisher, Crossref or PubMed. The generated README states that descriptions are not promoted to abstracts, but the code stores any Zotero `abstractNote` as the abstract. See Open questions. | [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md) |
| Active build | The single build queries read, named in `graphrag.active_corpus`. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| ADS | NASA Astrophysics Data System, an index of astronomy, physics and planetary science literature. | [literature-batches](chapters/literature-batches.md) |
| Advisory lock | Application-level PostgreSQL lock used to serialise loads and activation. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| AGU | American Geophysical Union, which publishes the meeting abstracts that some records cite. | [literature-batches](chapters/literature-batches.md) |
| AI | Artificial intelligence. Here, the agents that call the MCP tools. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| AMC | Axial magma chamber, the magma body under Axial Seamount. The build draws the top of its reflector. | [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md) |
| Analogs, dPo, dLoc | Historical events used as analogs, and the polarity-distance and location-distance values from the focal workflow | [axial](chapters/axial.md) |
| Answer model | An LLM that writes the answer from evidence. The Model Lab compares several. | [eval-experiments](chapters/eval-experiments.md) |
| APG | Absolute pressure gauge. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| API | Application programming interface. "The Graph-RAG API" is the FastAPI service in graphrag-runtime; the map's live-data service is the gateway. | [graphrag-runtime](chapters/graphrag-runtime.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [eval-experiments](chapters/eval-experiments.md), [literature-batches](chapters/literature-batches.md), [literature-corpus](chapters/literature-corpus.md) |
| Apparent time | A timestamp as the instrument clock wrote it, before correction. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| ARCADA | The upstream repository `mhemmett/arcada`. Its collection is labelled RCA Information. | [corpus-docs-web](chapters/corpus-docs-web.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-data](chapters/atlas-map-data.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [graphrag-runtime](chapters/graphrag-runtime.md), [repo-ops-data](chapters/repo-ops-data.md) |
| Archive prefix | S3 key prefix such as `archives/internal/<slug>` under which staged output is written. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| ASHES | The hydrothermal vent field at Axial | [axial](chapters/axial.md) |
| Ask Atlas | The question-answering feature on the map. | [ask-atlas](chapters/ask-atlas.md) |
| Async results | The output folder that OOI fills for a submitted request, with `status.txt` and `status.json`. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Atlas | This browser map in `src/atlas_map`, titled "Cascadia Offshore Sensor Atlas". | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Atlas bundle | The folder of JSON and binary files that this package writes to `src/atlas_map/public/atlas/`. | [atlas-map-data](chapters/atlas-map-data.md) |
| Atlas chunk ID | Stable ID of one passage in the normalized corpus. | [eval-experiments](chapters/eval-experiments.md) |
| Auto | The default model choice: Gemini, then Groq, then OpenAI only in local development. | [ask-atlas](chapters/ask-atlas.md) |
| AUV | Autonomous underwater vehicle. The MBARI 1 m summit survey was made by one. | [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| Auxiliary input | Catalogued JSONL that is neither embedded nor node-linked. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| AWS | Amazon Web Services. Amazon S3 is one of its services. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Axial Seamount | Active submarine volcano on the Juan de Fuca Ridge, off Oregon, instrumented by the RCA. | [axial](chapters/axial.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-scene](chapters/atlas-map-scene.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [repo-ops-data](chapters/repo-ops-data.md), [ask-atlas](chapters/ask-atlas.md), [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md) |
| BAAI bge-small-en-v1.5 | A 384-dimension text-embedding model from the Beijing Academy of Artificial Intelligence (BAAI). It is the production retrieval index. | [eval-experiments](chapters/eval-experiments.md) |
| Baseline | A directed acoustic range between two FETCH stations. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Base release | The stable corpus release that bootstrap restores first. | [repo-ops-data](chapters/repo-ops-data.md) |
| Beachball | The diagram of a focal mechanism | [axial](chapters/axial.md) |
| BGE | BAAI's `bge-small-en-v1.5` English embedding model. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| BM25 | Okapi BM25, a term-weighting formula for ranking text. `_search` uses it. | [literature-fulltext](chapters/literature-fulltext.md) |
| BOTPT | Bottom Pressure and Tilt instrument package; stream names look like `BOTPT-A301-MJ03F` | [axial](chapters/axial.md) |
| BPR | Bottom pressure recorder, a seafloor pressure sensor. The captured inflation answer uses the term. | [ask-atlas](chapters/ask-atlas.md), [axial](chapters/axial.md) |
| Budget | Per-request limits on tokens, cost, tool calls and time. | [eval-experiments](chapters/eval-experiments.md) |
| Build fingerprint | SHA-256 over every collection's manifest hash and input hashes. The first 12 characters name the archives. | [repo-ops-data](chapters/repo-ops-data.md) |
| Build ID, fingerprint | SHA-256 over all catalog inputs, used as the build's identity. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Bundle | The static JSON and binary files under `public/atlas/`, which the page loads at startup. | [atlas-map-scene](chapters/atlas-map-scene.md), [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Bundle fingerprint | SHA-256 over the three bundle files' hashes, identifying the exact model used. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| Cable | The RCA cable route on the seafloor. | [atlas-map-scene](chapters/atlas-map-scene.md), [ask-atlas](chapters/ask-atlas.md) |
| Cable route | A cable segment, marked charted, approximate or mapped. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| Cached input tokens | Prompt tokens a provider serves from its cache, billed at a lower rate. | [eval-experiments](chapters/eval-experiments.md) |
| Cache (validated) | An entry under `runtime_data/Literature/full_text_cache/<work_id>/` whose stored hashes still match. | [literature-fulltext](chapters/literature-fulltext.md) |
| Caldera | The sunken summit of a volcano. Axial's central caldera sites sit in it. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Candidate | An entity, relation or report that GraphRAG proposes and no one has reviewed yet. | [eval-experiments](chapters/eval-experiments.md) |
| Candidate graph | The reviewable paper-to-instrument and paper-to-site graph built from cached passages. It is not canonical. | [literature-fulltext](chapters/literature-fulltext.md) |
| Canonical ID | The stable key of an inventory record. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Canonical record | One row per distinct work. Occurrences point to it through `canonical_id`. | [literature-batches](chapters/literature-batches.md) |
| Canonical URL and alias | The URL kept for a set of identical pages, and the other URLs listed under `aliases`. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Canonical work | One row in `literature.jsonl`, identified by `id` and `canonical_id`. | [literature-corpus](chapters/literature-corpus.md) |
| Canonical work ID | The catalog `id` of a work, such as `COSZO-REF-064`. | [literature-fulltext](chapters/literature-fulltext.md) |
| Catalog | `src/graphrag_runtime/discover_corpora.py`, which finds every manifest under `data/` and lists its inputs. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| CAWCR | Centre for Australian Weather and Climate Research (expansion from general knowledge, not in the repository). Its wave and wind hindcast is the Dive Index source. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| CDOM | Colored dissolved organic matter, a water-chemistry variable measured by a fluorometer. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| CE | Coastal Endurance Array, another OOI array outside RCA scope. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Champion / challenger | The model in use, and the models tested against it. | [eval-experiments](chapters/eval-experiments.md) |
| Channel | One position along a DAS cable, at 2 m spacing for the OptaSense geometry. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Channel codes | Seismic channel names such as HHZ and EHZ (vertical seismometer channels) and HDH (a hydrophone channel). | [atlas-map-panels](chapters/atlas-map-panels.md) |
| Charted, mapped, approximate, surveyed | Accuracy labels on cable features: from the Marine Cadastre (charted), from `ooi_cables.csv` (mapped), straight or proxy (approximate), and from OOI asset-management positions (surveyed). | [atlas-map-data](chapters/atlas-map-data.md) |
| Chronfix | The clock-correction package and its correction bundle. | [coszo-hub-core](chapters/coszo-hub-core.md), [eval-experiments](chapters/eval-experiments.md) |
| Chunk | A bounded piece of text that is embedded and cited. Stored in `chunks.jsonl`. | [corpus-docs-web](chapters/corpus-docs-web.md), [axial](chapters/axial.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| Chunk, entity, capability, relationship | Record types in the graph layer. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Citation occurrence ID | An alias for a canonical work, used when a work is cited from another source. For example, `COSZO-REF-066` resolves to `COSZO-REF-064`. | [literature-fulltext](chapters/literature-fulltext.md) |
| CLI | Command-line interface: a program run from a shell with flags and subcommands, such as `qaqc_agent_tools.py health`. | [agentic-qaqc](chapters/agentic-qaqc.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Coastal Endurance Array | An OOI array off the US Pacific Northwest coast (domain background; the code does not describe it). Its Zotero collection key is `E5UH7L89`. | [literature-corpus](chapters/literature-corpus.md) |
| COBSO | COBSO broadband seismometer and strong-motion package. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| Collection | One named input set under `data/`, such as `Websites` or `Literature`. | [repo-ops-data](chapters/repo-ops-data.md), [coszo-hub-core](chapters/coszo-hub-core.md), [eval-experiments](chapters/eval-experiments.md) |
| Composite packet | A multi-part PDF split into logical sections. `COSZO Project DataMSRI.pdf` is one. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Concept | One OKF Markdown file with frontmatter that records a decision, fact, requirement, bug or architecture note. | [repo-ops-data](chapters/repo-ops-data.md) |
| conda-forge | A community package channel. The repository uses a prefix.dev mirror of it. | [repo-ops-data](chapters/repo-ops-data.md) |
| Constant-time compare | `hmac.compare_digest`, which compares digests without leaking timing. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Content-addressed | Named by a prefix of its own SHA-256 hash. The payload is `document-<sha16>`. | [literature-fulltext](chapters/literature-fulltext.md) |
| Corpus-first routing | The rule that availability questions are answered from the static corpus before any live call. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Corrections | Reviewed fixes to a sensor's position, each with a reason. | [atlas-map-data](chapters/atlas-map-data.md) |
| CORS | Cross-origin resource sharing: the response headers that let a browser read a response from another origin. | [ask-atlas](chapters/ask-atlas.md), [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Cosine distance | Angle-based distance, written `<=>` in SQL. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| COSZO | Cascadia Offshore Subduction Zone Observatory, the second project in scope. Its instrument suites sit at RCA's Oregon sites, and its PDFs, website and COSZO Hub outputs are collections in the corpus. | [corpus-docs-web](chapters/corpus-docs-web.md), [agentic-qaqc](chapters/agentic-qaqc.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-batches](chapters/literature-batches.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| COSZO-ADD-### | ID of a citation occurrence that was not in the seed. | [literature-batches](chapters/literature-batches.md) |
| COSZO Hub | The public `coszo-hub` GitHub organization of computational repositories. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| COSZO-PRODB-### | Working IDs for the eight works in retrieval_b. | [literature-batches](chapters/literature-batches.md) |
| COSZO-REF-### | Canonical ID of a seed or pass-2 work (001 to 133 seed; 134 onward new). | [literature-batches](chapters/literature-batches.md), [literature-corpus](chapters/literature-corpus.md) |
| Coverage mask | A texture that records which finer tiles are shown. A coarser tile sinks beneath them. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Cover sheet | The cover sheet and site table of a proposal, not the full proposal. Marked `retrieved_proposal_cover_sheet_only`. | [literature-fulltext](chapters/literature-fulltext.md) |
| COVIS | Cabled Observatory Vent Imaging Sonar. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| CREW | Cascadia Region Earthquake Workgroup, whose scenario report is record 021. | [literature-batches](chapters/literature-batches.md) |
| Crossref | Public registry of DOI metadata. | [literature-batches](chapters/literature-batches.md), [literature-corpus](chapters/literature-corpus.md) |
| Crosswalk | A file that joins Nereus reference designators to the local instrument graph. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| CSV | Comma-separated values, a plain-text table format. HITL notes are published as CSV. | [agentic-qaqc](chapters/agentic-qaqc.md), [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| CSV, HTTP | Comma-separated values; Hypertext Transfer Protocol | [axial](chapters/axial.md) |
| CTD | Conductivity, temperature and depth seafloor sensor | [axial](chapters/axial.md), [atlas-map-panels](chapters/atlas-map-panels.md) |
| CTD-DO | Conductivity, temperature and depth with a dissolved-oxygen sensor. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| CZMID, CZOFF, CZOSH, CZSHF | COSZO station codes for the Mid Slope, Offshore, Outer Shelf and Shelf sites. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| DAS | Distributed acoustic sensing: a fiber-optic cable read as a line of channels at fixed spacing. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md), [corpus-docs-web](chapters/corpus-docs-web.md), [coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-corpus](chapters/literature-corpus.md) |
| DAS24 | The repository's name for the 2024 multiplexed RCA DAS experiment, an OptoDAS configuration. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| DAS25 | The DAS preprint about the 2025-2026 RCA deployment, added in commit `2ea6c00`. Its work ID is `OOI-DAS-2026-001`. Its publication year is open (see Open questions). | [literature-corpus](chapters/literature-corpus.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| DataCite | DOI registration agency for datasets and reports. | [literature-batches](chapters/literature-batches.md) |
| DataMSRI | The name in `COSZO Project DataMSRI.pdf`, the composite packet. The repo does not expand it. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Data range | Value range of a plot: `full`, `standard` or `local`. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Datum | The reference level for depths, 1.5 km. | [ask-atlas](chapters/ask-atlas.md), [atlas-map-data](chapters/atlas-map-data.md) |
| delta_t | Clock error in seconds. True UTC is apparent time minus delta_t. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| DEMS | Diffuse Effluent Measurement System, a 2014 camera and temperature campaign system at ASHES. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Deployment | An OOI installation period for an instrument, numbered. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Dive Index | A COSZO hindcast index for ROV dive conditions (ROV is expanded as remotely operated vehicle from general knowledge): significant wave height times 10 m wind speed in knots. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| DNS | Domain Name System. The SSRF guard resolves host names through it. | [literature-fulltext](chapters/literature-fulltext.md) |
| Dock | The row of three 30 px icon buttons at the top right. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| DOI | Digital object identifier, a persistent ID for a publication, dataset or report. | [literature-batches](chapters/literature-batches.md), [corpus-docs-web](chapters/corpus-docs-web.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md) |
| DOI, IEDA | Digital object identifier; the Interdisciplinary Earth Data Alliance, which hosts the catalog citation | [axial](chapters/axial.md) |
| DOM | The browser's page-element tree. The evidence numbers, halos and chips are DOM elements placed over the canvas. | [ask-atlas](chapters/ask-atlas.md) |
| DPG | Deep-sea differential pressure gauge. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| DPI | Dots per inch: the resolution of a rendered page image. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| DP, SF, PC | Deep profiler, shallow profiler and 200 m platform: OOI moorings whose node prefixes set depth ranges. | [atlas-map-data](chapters/atlas-map-data.md) |
| Dry run | A cost estimate that makes no provider calls. | [eval-experiments](chapters/eval-experiments.md) |
| DSN | Data source name, the connection string passed to `--dsn`. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| DTS | Distributed temperature sensing, the same fiber technique applied to temperature. Domain background, not in the repository. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| EarthScope | The seismic data service that runs the FDSN endpoints at `service.earthscope.org`. | [coszo-hub-sources](chapters/coszo-hub-sources.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md) |
| EarthScope, FDSN | EarthScope is a seismic data archive. FDSN is the web-service standard its station service follows. | [atlas-map-data](chapters/atlas-map-data.md) |
| EarthScope station id | A seismic station id such as `station_OO_AXCC1`, mapped to `EARTHSCOPE-OO-AXCC1`. | [ask-atlas](chapters/ask-atlas.md) |
| Edge chip | A marker clamped to the edge of the free area, for evidence that is off screen. | [ask-atlas](chapters/ask-atlas.md) |
| Edge fact | Unique `(collection, source, predicate, target)` row used for traversal. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| EEW | Earthquake early warning. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| EEZ | Exclusive economic zone. The US EEZ limit is where the Marine Cadastre geometry ends. | [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md) |
| Embedding | A list of floats that represents a text's meaning; here 384 of them. | [graphrag-runtime](chapters/graphrag-runtime.md), [eval-experiments](chapters/eval-experiments.md), [repo-ops-data](chapters/repo-ops-data.md) |
| endpointId | The bundle's id for one PI portal folder, `PI-PORTAL-ENDPOINT-…`. The toolkit has its own ids such as `covis-raw`. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Endurance | Filename prefix for the Coastal Endurance Array outputs. | [literature-corpus](chapters/literature-corpus.md) |
| Entity | A graph node: author, resource type, topic, place, project, glossary term, web resource, Zotero collection or proposal section. | [literature-corpus](chapters/literature-corpus.md) |
| epochMs | Milliseconds since 1970-01-01 UTC, the time format of series and waveform points. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| ERDDAP | Environmental Research Division's Data Access Program: the public data server OOI uses. | [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md) |
| ESS Open Archive | The preprint server that hosts the DAS25 record. | [literature-corpus](chapters/literature-corpus.md) |
| Europe PMC | Europe PubMed Central, a biomedical literature index. | [literature-batches](chapters/literature-batches.md) |
| evidenceMode | The `/status` field saying whether the answer is live or from a snapshot. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| evidence_mode | The provenance label on a live result: `live`, `live_cache` or `snapshot_fallback`. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Evidence package | The frozen hits and relationships given to the answer model. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| EvidencePackage | The frozen set of evidence items, with corpus and graph versions, that every answer model receives. | [eval-experiments](chapters/eval-experiments.md) |
| EXIF | Image metadata that can hold an orientation flag. Pillow's `exif_transpose` applies it. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Family | One of six sensor families, each with its own colour and glyph. | [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| FastAPI | Python web framework used for the gateway. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| FastAPI, Gunicorn, Uvicorn, pydantic | The Python web framework, process manager, ASGI server and data-validation library. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| FastEmbed | Python library that runs ONNX embedding models. | [graphrag-runtime](chapters/graphrag-runtime.md), [repo-ops-data](chapters/repo-ops-data.md) |
| Fast-forward pull | `git pull --ff-only`, which fails rather than merging. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| FDSN | International Federation of Digital Seismograph Networks. The standard web services for seismic station and waveform data. | [coszo-hub-sources](chapters/coszo-hub-sources.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md), [corpus-docs-web](chapters/corpus-docs-web.md), [coszo-hub-core](chapters/coszo-hub-core.md), [graphrag-runtime](chapters/graphrag-runtime.md) |
| Feather | Easing the summit heights into GMRT across the survey's outer 0.5 km. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| FETCH | The Axial Seamount network of three acoustic ranging stations (transponders) that measure distances between one another. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [atlas-map-data](chapters/atlas-map-data.md), [graphrag-runtime](chapters/graphrag-runtime.md), [repo-ops-data](chapters/repo-ops-data.md) |
| Flight | An eased camera move with a fixed duration. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Focal mechanism | The fault orientation (strike, dip, rake) that best explains an earthquake. Fault classes are N (normal), R (reverse), S (strike-slip) and U (unclassified) | [axial](chapters/axial.md) |
| Free area | The map between the side panels and the top row. | [ask-atlas](chapters/ask-atlas.md) |
| Full-text link | A direct PDF or HTML link to the work, kept after a live check in most stages (see Decisions). | [literature-batches](chapters/literature-batches.md) |
| Full-text search | PostgreSQL lexical ranking with `tsvector` and `websearch_to_tsquery`. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Gateway | The local FastAPI service for live lookups, on port 8787. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Gemini | Google's LLM family; the default model is `gemini-2.5-flash`. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| GET | The HTTP method that reads a resource. Every outbound call here is a GET. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| GIN | Generalized inverted index, used here for full-text and JSONB search. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Glass | The subsurface view: the seafloor turns translucent so the layers beneath show. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Gleaning | In Microsoft GraphRAG, a second extraction pass that asks the model for entities it missed. | [eval-experiments](chapters/eval-experiments.md) |
| Glossary term | One of eight definitions extracted from `Glossary.pdf`. | [literature-corpus](chapters/literature-corpus.md) |
| GMRT | Global Multi-Resolution Topography (general knowledge; the repo does not spell the name out), the seafloor grid the terrain comes from. | [atlas-map-scene](chapters/atlas-map-scene.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Gold row / reference answer | A hand-checked expected answer with the sources it must use. | [eval-experiments](chapters/eval-experiments.md) |
| Governance | An OKF frontmatter field: `hold`, `constraint` or `context`. `search --for-path` surfaces it. | [repo-ops-data](chapters/repo-ops-data.md) |
| GPT | OpenAI's model family. The Model Lab prices three of its models. | [eval-experiments](chapters/eval-experiments.md) |
| Graph expansion | Adding neighbors of seed nodes, up to a hop limit. | [eval-experiments](chapters/eval-experiments.md) |
| GraphQL | A query language. Nereus exposes only allowlisted operations. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Graph-RAG | Retrieval-augmented generation over a graph: a large language model answers from retrieved text chunks plus the entities and typed edges linked to them, so each claim can cite its source. In RCA Atlas the Graph-RAG API returns text hits, graph neighbours and tool hints. | [ask-atlas](chapters/ask-atlas.md), [agentic-qaqc](chapters/agentic-qaqc.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [axial](chapters/axial.md), [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| GraphRAG (Microsoft) | Microsoft's open-source pipeline. It uses an LLM to extract entities, relations, claims and community reports from text. | [eval-experiments](chapters/eval-experiments.md) |
| GSSM | Geodetic and Seismic Sensor Module, a COSZO package. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| h5dump | The HDF5 command-line tool used to read datasets. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| HASH | Program that estimates focal mechanisms from polarities | [axial](chapters/axial.md) |
| Hasura | The GraphQL engine that serves Nereus, as the path `/hasura/v1/graphql` suggests. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| HDF5 | Hierarchical Data Format version 5, the file format of the DAS files this extractor reads. | [coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| HDH | A hydrophone (pressure) channel code. The bundle builder gives it to the seismic station on the same node. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| HHZ | A SEED (Standard for the Exchange of Earthquake Data) channel code: the vertical component of a high-rate seismometer. The bundle default. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| HITL | Human-in-the-loop: status notes written by people and published as CSV. | [agentic-qaqc](chapters/agentic-qaqc.md), [graphrag-runtime](chapters/graphrag-runtime.md) |
| HNSW | Approximate nearest-neighbour index type in pgvector. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Homebrew QARTOD | Staged, proposed QARTOD test tables, published only to an archive prefix. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Host limiter | Per-source semaphore (`HostLimiter`) allowing 4 requests in flight. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| HTML | HyperText Markup Language. The OOI site inventories are archived as HTML. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [corpus-docs-web](chapters/corpus-docs-web.md), [literature-corpus](chapters/literature-corpus.md) |
| HTTP | Hypertext Transfer Protocol. | [atlas-map-gateway](chapters/atlas-map-gateway.md), [agentic-qaqc](chapters/agentic-qaqc.md), [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md) |
| HTTP 410 | "Gone". Here, the availability service's response during the 2026 transition. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| HTTP status codes | 200 and 206 are success (206 is partial content); 403 is refused; 405 is method not allowed; 429 is too many requests. | [literature-batches](chapters/literature-batches.md) |
| httpx | HTTP client library the gateway uses for upstream calls. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| HUD | Heads-up display: here, the top row of title card, region list and dock, laid over the map. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| HYDLF | Low-frequency hydrophone. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| hypo71 | The University of Washington's daily earthquake catalog format. | [ask-atlas](chapters/ask-atlas.md), [axial](chapters/axial.md) |
| Hypocenter | An earthquake's location in latitude, longitude and depth | [axial](chapters/axial.md) |
| Hypocentre | The point where an earthquake starts, given by latitude, longitude and depth. | [ask-atlas](chapters/ask-atlas.md) |
| HYS14 | The OOI Hydrate Ridge ocean-bottom seismometer station whose clock the Chronfix model corrects. | [coszo-hub-core](chapters/coszo-hub-core.md), [eval-experiments](chapters/eval-experiments.md) |
| IANA time zone | A zone name such as `America/Los_Angeles`, sent as `tz`. | [ask-atlas](chapters/ask-atlas.md) |
| ICD | Interface control document: a specification for how two hardware parts connect. Several COSZO sections are ICDs. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| ID | Identifier. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| IEDA | Interdisciplinary Earth Data Alliance, which issues the `10.26022/IEDA/...` DOIs used for two datasets. | [literature-batches](chapters/literature-batches.md) |
| Insets | The pixels that panels cover on each side. The camera centres in what is left. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| INSTRUMENT-<hash> | An instrument id. The resolver reads its first 18 hex digits. | [ask-atlas](chapters/ask-atlas.md) |
| Instrument key | The PI portal's key for an instrument, such as `PI-COVIS`. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Int16 | A 16-bit signed integer. Terrain and AUV tiles are stored this way. | [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| Inverted index | OpenAlex's abstract format. Rebuilt into text by sorting word positions. | [literature-batches](chapters/literature-batches.md) |
| IODP | Integrated Ocean Drilling Program, named in a citation at `coszo_products/a/build_extraction.py:43`. | [literature-batches](chapters/literature-batches.md) |
| IPv4 | Internet Protocol version 4 address. The adapter redacts private, loopback, link-local and reserved literals. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| ISO 8601 | The date-time text format used in query strings, such as `2026-09-20T00:00:00Z`. | [atlas-map-gateway](chapters/atlas-map-gateway.md), [axial](chapters/axial.md) |
| Jaccard similarity | The size of the overlap of two sets divided by the size of their union. Used with five-word shingles to flag near-duplicate abstracts. | [literature-corpus](chapters/literature-corpus.md) |
| JATS | Journal Article Tag Suite, the XML markup that Crossref abstracts use. Stripped with a regex. | [literature-batches](chapters/literature-batches.md), [literature-corpus](chapters/literature-corpus.md) |
| Jitter | Scatter of sample times around the fitted clock. The anomaly detector flags a fractional residual above 0.4. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| JSON | JavaScript Object Notation, the text format of every `.json` and `.jsonl` file in this chapter. | [corpus-docs-web](chapters/corpus-docs-web.md), [agentic-qaqc](chapters/agentic-qaqc.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| JSON, JSONL | JSON is a text data format. JSONL (JSON Lines) holds one JSON object per line. | [literature-batches](chapters/literature-batches.md) |
| JSONL | JSON Lines: one JSON object per line. | [corpus-docs-web](chapters/corpus-docs-web.md), [agentic-qaqc](chapters/agentic-qaqc.md), [axial](chapters/axial.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md) |
| JSON-LD | JSON used as linked data inside a web page; some publisher pages carry article metadata this way. | [literature-batches](chapters/literature-batches.md) |
| JSON-RPC | A JSON request and response protocol. MCP is built on it. | [agentic-qaqc](chapters/agentic-qaqc.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| JSON-RPC 2.0 | The request and response format under MCP. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| JSON-RPC, stdio | JSON-RPC 2.0 messages, one per line on standard input and output | [axial](chapters/axial.md) |
| Junction box (MJ, LJ) | Node-name codes for cable junction boxes, as used in the cable notes. The repo does not define them (inferred: OOI naming). | [atlas-map-data](chapters/atlas-map-data.md) |
| Legacy and anomaly detectors | The two PREST gap algorithms. Legacy uses a median interval and an adaptive threshold. Anomaly fits a sample clock and reconstructs integer steps. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| Level and stride | Level 0, 1 or 2 of the summit tiles, with strides of 16, 4 and 1 finest cells. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Level of detail (LOD) | Tiles at several resolutions, with the finest loaded nearest the camera. | [atlas-map-data](chapters/atlas-map-data.md) |
| lifespan | FastAPI's startup and shutdown hook; the gateway's temp-root cleanup runs there. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| LILY | The publisher's tilt product prefix | [axial](chapters/axial.md) |
| LLM | Large language model. Gemini, Groq-hosted open models and OpenAI models write the answers. | [ask-atlas](chapters/ask-atlas.md), [axial](chapters/axial.md), [eval-experiments](chapters/eval-experiments.md) |
| Located | A sensor with a recorded position. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| Located, documents, events, count | The four outputs of `resolveEvidence`: map items, further reading, quake events and the Axial day count. | [ask-atlas](chapters/ask-atlas.md) |
| Locator | The `page N` or `section X` label that tells a reader where a passage came from. | [literature-fulltext](chapters/literature-fulltext.md) |
| LOD | Level of detail: coarse tiles everywhere, finer tiles near the camera. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Logical node | One entity per `(collection_id, local_id)` after deduplication. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| M2M | Machine-to-machine. The OOI data API. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| Magma chamber (AMC) | The axial magma chamber. Its top is the `amc` surface. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Manifest | `manifest.json`: counts, input files and status for a collection, read by the catalog. | [corpus-docs-web](chapters/corpus-docs-web.md), [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Marine Cadastre | The public cable-area dataset of NOAA (US National Oceanic and Atmospheric Administration) and BOEM (Bureau of Ocean Energy Management), the source of the charted route. | [atlas-map-data](chapters/atlas-map-data.md) |
| MARUM | The research group whose sonars, camera and CTD appear in the PI registry. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| MBARI | Monterey Bay Aquarium Research Institute, which surveyed the Axial summit at 1 m. | [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| MCP | Model Context Protocol: a JSON-RPC tool interface that AI agent clients use to call servers. | [agentic-qaqc](chapters/agentic-qaqc.md), [axial](chapters/axial.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [eval-experiments](chapters/eval-experiments.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| Method and stream | OOI delivery route (for example `telemetered`, `recovered_inst`) and the named data stream within it. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| MHZ | The 8 Hz vertical seismic channel on HYS14 used to derive and validate the Chronfix model. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| MiB | Mebibyte, 2^20 bytes. The MultiDAS header reader stops after 1 MiB. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [agentic-qaqc](chapters/agentic-qaqc.md) |
| MiniSEED | A binary format for seismic waveform records. | [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md), [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| MiniSEED, StationXML, NetCDF | Waveform, station-metadata and array data formats named in the artifact schemas. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| MIT | The MIT License, a permissive open-source license. It is ARCADA's repository license. | [corpus-docs-web](chapters/corpus-docs-web.md), [agentic-qaqc](chapters/agentic-qaqc.md) |
| MJ03B, MJ03D, MJ03E, MJ03F | OOI platform codes for the ASHES, International District, Eastern Caldera and Central Caldera sites | [axial](chapters/axial.md) |
| Mock transport | A test double that replaces the HTTP call. | [eval-experiments](chapters/eval-experiments.md) |
| Mooring | A site's vertical instrument line, drawn as a dashed line from the seafloor to the surface. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| MPO | Multi-Picture Format, a camera format that stores several JPEG images in one file (general background, not stated in the repo). Some JPEG-labelled figures in the corpus are really MPO. | [repo-ops-data](chapters/repo-ops-data.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| msgpack | A binary serialization format used for MultiDAS headers. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| MultiDAS | The Nokia multi-span DAS system of the 2025-26 deployment. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| MultiDAS, OptoDAS, OptaSense | DAS products named in the overlays. MultiDAS is the 2025–2026 unmasked spans, OptoDAS the south first span, and OptaSense the 2021 conventional channel geometry. | [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md) |
| MVCC | PostgreSQL's multi-version concurrency control, which gives readers a consistent snapshot. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Mw | Moment magnitude, the catalog's `magnitude_mw` | [axial](chapters/axial.md) |
| NaN | Not a number: ERDDAP's missing-value marker, which the gateway skips. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Native text | The text layer already inside a PDF, read without OCR. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| NCBI | National Center for Biotechnology Information, which runs PubMed and PubMed Central. | [literature-batches](chapters/literature-batches.md) |
| `[n]` citation | A bracketed number in the answer that points at entry n of `answer_citations`. | [ask-atlas](chapters/ask-atlas.md) |
| nDCG, MRR, recall at k | Ranking metrics: normalized discounted cumulative gain, mean reciprocal rank, and the share of relevant items in the top k. | [eval-experiments](chapters/eval-experiments.md) |
| Negative cache | Keeping a failed fetch for a set time. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Nereus | RCA's operational web system, hosted at `nereus.ooirsn.uw.edu`, with a public GraphQL API. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md), [eval-experiments](chapters/eval-experiments.md) |
| NetCDF | Network Common Data Form, the self-describing scientific file format that OOI requests return. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| NET.STA | A seismic network and station code pair, such as `OO.AXCC1`. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| NET, STA, LOC, CHA | Network, station, location and channel codes in an FDSN selection. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| News & Views | A Nature commentary article type. Its text is a standfirst. | [literature-corpus](chapters/literature-corpus.md) |
| NOAA | National Oceanic and Atmospheric Administration. | [literature-batches](chapters/literature-batches.md) |
| Node and edge | A record in an entity or document table is a node. A row of `relationships.jsonl` is an edge with a predicate. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Node controller | The COSZO Node Controller Computer, the system role in the node-controller requirements document. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| NSF | National Science Foundation. Its Award API returns grant records. | [literature-batches](chapters/literature-batches.md) |
| OA | Open access: a publicly readable copy. It is the only kind of copy this tool fetches. | [literature-fulltext](chapters/literature-fulltext.md) |
| OBS | Ocean-bottom seismometer. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| Occurrence | One place a citation appears in the PDF, with its page and section. | [literature-batches](chapters/literature-batches.md) |
| Ocean Observatories Initiative (OOI) | The programme that runs RCA. | [atlas-map-data](chapters/atlas-map-data.md) |
| Ocelot | VersaLogic Ocelot VL-EPMs-21, the current node controller. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| OCR | Optical character recognition: reading text from page images. | [corpus-docs-web](chapters/corpus-docs-web.md), [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| OFDR | The leading tag of MultiDAS files, the magic string `OFDR1MAGIC`. The acronym is domain background (optical frequency-domain reflectometry); the repository does not expand it. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| OKF | The bundle format (v0.2) used by `knowledge/`, defined by the okf-agent-memory project. The repository does not expand the acronym (Open question 11). | [repo-ops-data](chapters/repo-ops-data.md) |
| OLS | Ordinary least squares, the linear fit that the anomaly detector uses to estimate the sample period. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| ONNX | Open model file format; the pinned file is `model_optimized.onnx`. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| OOI | Ocean Observatories Initiative, the ocean observing program whose cabled seafloor part is the RCA. Its data services used here include the M2M API, ERDDAP and THREDDS catalogs. | [coszo-hub-sources](chapters/coszo-hub-sources.md), [agentic-qaqc](chapters/agentic-qaqc.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md), [axial](chapters/axial.md), [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-batches](chapters/literature-batches.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| ooi-harvester | An open-source OOI data harvester (MIT), used only as a design reference. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| OOI M2M | The OOI machine-to-machine data API at `ooinet.oceanobservatories.org/api/m2m`. | [coszo-hub-sources](chapters/coszo-hub-sources.md), [axial](chapters/axial.md) |
| OOINet | An open-source OOI client project (GPL-3.0), used only as a design reference. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| `OOI-ZOT-###` | Work IDs for new works from the Zotero exports, numbered in first-seen order. | [literature-corpus](chapters/literature-corpus.md) |
| OpenAI-compatible server | A server that speaks OpenAI's chat-completions API, such as vLLM, SGLang or Ollama. | [eval-experiments](chapters/eval-experiments.md) |
| OpenAlex | Open scholarly index. Stores abstracts as an inverted index: word to positions. | [literature-batches](chapters/literature-batches.md) |
| OpenAlex, Crossref, Unpaywall | Public scholarly metadata services. The tool asks them for copy links. | [literature-fulltext](chapters/literature-fulltext.md) |
| OpenAlex, Europe PMC, Semantic Scholar | Public scholarly metadata services queried for missing abstracts. | [literature-corpus](chapters/literature-corpus.md) |
| OPeNDAP | A protocol for remote access to gridded scientific data. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| OptaSense, Silixa | Makers of DAS interrogators, the instruments that read the fiber. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| OptoDAS | The DAS interrogator family whose HDF5 layout the extractor is written for. | [coszo-hub-core](chapters/coszo-hub-core.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| OptoDAS, MultiDAS, OptaSense, Silixa | Vendor interrogator products or data formats named in the PI registry. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Origin | The HTTP header that names the page that made a request. The Worker accepts only `https://coszo.org`. | [ask-atlas](chapters/ask-atlas.md) |
| OS | Operating system; the default cache lives in its temp directory | [axial](chapters/axial.md) |
| OSU CEOAS | Oregon State University College of Earth, Ocean, and Atmospheric Sciences, which publishes the monitoring pages | [axial](chapters/axial.md) |
| Other arrays | Other OOI arrays, such as Pioneer, Endurance, Irminger, Station Papa and NEPTUNE/Endeavour. Excluded from the website corpus. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Output root | A directory that a pipeline writes to, configured per repository. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| Overlay | Extra layer named in a plot file name: `none`, `anno`, `clim`, `flag`, `near`, `time`. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Overlay release | A supplemental runtime archive restored after a base release. | [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| Override | A reviewed correction for one Zotero key, stored in an override file and applied at assembly. | [literature-corpus](chapters/literature-corpus.md) |
| Owner | The person whose product list an occurrence sits under in the PDF. Inferred where the page does not print it. | [literature-batches](chapters/literature-batches.md) |
| Package | The assembled folder `package/` produced by `assemble_zotero.py` and installed by `install.py`. | [literature-corpus](chapters/literature-corpus.md) |
| Packet page | The printed page number of the PDF's personnel packet. Separate from the one-based PDF page. | [literature-batches](chapters/literature-batches.md) |
| P and S picks | Arrival times of compressional (P) and shear (S) seismic waves at a station | [axial](chapters/axial.md) |
| Pass 1, pass 2 | Abstract batches for the seed (pass 1) and retrieval for new works from the Products sections (pass 2). | [literature-batches](chapters/literature-batches.md) |
| Passage | A returned excerpt with its locator, score and chunk ID. | [literature-fulltext](chapters/literature-fulltext.md) |
| Paywall | An access control that needs payment or a login. The tool does not pass one. | [literature-fulltext](chapters/literature-fulltext.md) |
| PCB | Printed circuit board. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| PDF | Portable document format. The COSZO project file is a PDF with a personnel packet. | [literature-batches](chapters/literature-batches.md), [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [literature-fulltext](chapters/literature-fulltext.md) |
| pdftoppm | A Poppler command that renders PDF pages to PNG. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| PEP | Python Enhancement Proposal. PEP 701 is the f-string change behind the Python 3.12 floor (external reference; inferred). | [corpus-docs-web](chapters/corpus-docs-web.md) |
| pgvector | PostgreSQL extension that stores vectors and ranks them. | [graphrag-runtime](chapters/graphrag-runtime.md), [repo-ops-data](chapters/repo-ops-data.md) |
| ph2dt | The UW daily phase-pick file format: station P and S picks per event | [axial](chapters/axial.md) |
| Physical record | One raw JSONL row, kept in `node_records` or `edge_records`. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| PI | Principal Investigator. Here, the research teams whose datasets sit on the UW portal. | [coszo-hub-sources](chapters/coszo-hub-sources.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md) |
| Pin | A fixed version, revision or hash that a build must match. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| PI portal | The principal investigators' data portal at `piweb.ooirsn.uw.edu`, with one or more folder trees (endpoints) per instrument, four for COVIS. | [atlas-map-gateway](chapters/atlas-map-gateway.md), [agentic-qaqc](chapters/agentic-qaqc.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-panels](chapters/atlas-map-panels.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-fulltext](chapters/literature-fulltext.md) |
| pixi | An environment manager that reads `pixi.toml` and `pixi.lock`. | [repo-ops-data](chapters/repo-ops-data.md) |
| Placeholder row | An ARCADA source row whose text contains "undefined" and that duplicates another row's ID. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| PMC BioC | NCBI's XML format for PubMed Central articles. | [literature-batches](chapters/literature-batches.md) |
| PNG | Portable Network Graphics, a raster image format. Plot files are PNG or SVG. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Polite pool | External API policy: faster access that OpenAlex and Crossref say they give clients who give a contact address. Not checked here (see Open questions). | [literature-batches](chapters/literature-batches.md) |
| Popover | A panel that opens under the dock, from Terrain controls, Legend or Help. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| Poppler | The PDF command-line tools `pdfinfo`, `pdftotext` and `pdftoppm`. | [literature-fulltext](chapters/literature-fulltext.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| Poppler, pdftotext | Command-line PDF tools. `pdftotext -layout` extracts the glossary text. | [literature-corpus](chapters/literature-corpus.md) |
| POSIX | Portable Operating System Interface, the Unix standard for portable shell scripts. `run_mcp.sh` runs under `/bin/sh`. | [agentic-qaqc](chapters/agentic-qaqc.md), [axial](chapters/axial.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| PostgreSQL | The relational database that holds the authoritative graph. | [eval-experiments](chapters/eval-experiments.md) |
| Predicate | The typed relation on an edge, for example `OBSERVES`. The source field may be `relationship_type`; the API field is `predicate`. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Prefect | Workflow orchestrator that the vendored pipeline runs on. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Pre-QA | Published before quality-assurance review | [axial](chapters/axial.md) |
| PREST | The absolute seafloor pressure instrument family and its collection pipeline. | [coszo-hub-core](chapters/coszo-hub-core.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [eval-experiments](chapters/eval-experiments.md) |
| Primary node (PN) | A hub on the cable, identified by a code such as PN5A. | [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-scene](chapters/atlas-map-scene.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| Private network address | An address in a private, loopback, link-local or reserved range. The sanitizer redacts these. | [repo-ops-data](chapters/repo-ops-data.md) |
| Products sections | Two lists in the PDF: "Products Most Closely Related to the Proposed Project" and "Other Significant Products". | [literature-batches](chapters/literature-batches.md) |
| Profiler | A moving instrument on a mooring, such as the shallow or deep profiler. | [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| psycopg, psycopg-pool | PostgreSQL driver and its connection pool. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| PubMed, PMID, PMCID | PubMed is the NCBI biomedical index; PMID is a PubMed record number; PMCID is a PubMed Central article number. | [literature-batches](chapters/literature-batches.md) |
| PubMed, PubMed Central (PMC) | The US National Library of Medicine's biomedical literature index and its full-text archive. Source of some abstracts. | [literature-corpus](chapters/literature-corpus.md) |
| Pydantic | Data-validation library that FastAPI uses for request bodies. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| pymseed | Python package that decodes MiniSEED files. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| pypdf | Python library that reads PDF text, bookmarks and metadata. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| QA/QC | Quality assurance and quality control. The RCA QA/QC site serves pre-rendered plots. | [atlas-map-data](chapters/atlas-map-data.md), [agentic-qaqc](chapters/agentic-qaqc.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md), [eval-experiments](chapters/eval-experiments.md) |
| QAQC | Quality assurance and quality control. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| QARTOD | Quality Assurance/Quality Control of Real-Time Oceanographic Data, the standard set of automated QC tests. Upstream's `flag` overlay draws QC flags, and uses QARTOD runs when `homebrew_qartod` is set. Definition from general knowledge, not from this repo. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Quick answer | An answer built from graph evidence with no language model. | [ask-atlas](chapters/ask-atlas.md) |
| Ranged GET | An HTTP request for only the first bytes of a file (the `Range` header), used to test a link without downloading it. | [literature-batches](chapters/literature-batches.md) |
| RCA | Regional Cabled Array, the cabled seafloor part of OOI off Oregon, reaching Southern Hydrate Ridge and Axial Seamount; the main scope of this project. | [agentic-qaqc](chapters/agentic-qaqc.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-scene](chapters/atlas-map-scene.md), [axial](chapters/axial.md), [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md), [repo-ops-data](chapters/repo-ops-data.md) |
| RCA Information | The display name of the `arcada` collection. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| `record_key` | Synthetic row key from the raw catalog line | [axial](chapters/axial.md) |
| record_status | The inventory label for what kind of record a row is. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Recursive CTE | `WITH RECURSIVE`, the SQL form used for graph walks. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Reduced motion | The OS setting `prefers-reduced-motion`, which makes flights instant. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Reference designator (refdes) | OOI's instrument identifier, made of site, node and instrument code, for example `RS03AXPS-PC03A-4A-CTDPFA303`. | [atlas-map-data](chapters/atlas-map-data.md), [agentic-qaqc](chapters/agentic-qaqc.md), [atlas-map-scene](chapters/atlas-map-scene.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-panels](chapters/atlas-map-panels.md) |
| Region | One of four map regions: Axial Seamount, Oregon Slope Base, Hydrate Ridge and Oregon Shelf. | [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-data](chapters/atlas-map-data.md) |
| Relationship (edge) | A typed link between two nodes, such as `HAS_CHUNK`, `CITES`, `LISTED_IN` or `AUTHORED_BY`. | [literature-corpus](chapters/literature-corpus.md) |
| Release asset | A file attached to a GitHub release. The corpus archives are private assets. | [repo-ops-data](chapters/repo-ops-data.md) |
| Release gate | A check that must pass before a release is published. Here the audit's zero-finding requirement. | [repo-ops-data](chapters/repo-ops-data.md) |
| Release manifest | JSON listing each asset's name, byte count and SHA-256. | [repo-ops-data](chapters/repo-ops-data.md) |
| Resolver | A service that maps a DOI to candidate copy URLs. | [literature-fulltext](chapters/literature-fulltext.md) |
| Retrieval reason | The required routing label `abstract_relevant_but_insufficient`. | [literature-fulltext](chapters/literature-fulltext.md) |
| Ring | A site's marker: one arc per sensor, coloured by family. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| RMT | Filename prefix for the Regional Cabled Array outputs. The code does not expand it (inferred). | [literature-corpus](chapters/literature-corpus.md) |
| robots.txt | A site file that states crawler rules. Saved here, not applied. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| RRF | Reciprocal rank fusion: merges ranked lists by summing 1/(k + rank). | [eval-experiments](chapters/eval-experiments.md), [graphrag-runtime](chapters/graphrag-runtime.md) |
| RS | Reference-designator prefix for RCA instruments. The toolkit's scope filter. | [agentic-qaqc](chapters/agentic-qaqc.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| RSAM | Real-time seismic-amplitude measurement: one-minute median absolute vertical amplitude in the 1-2 Hz and 2-4 Hz bands | [axial](chapters/axial.md) |
| RSN | Regional Scale Nodes, a name that the ARCADA builder matches as another name for RCA. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Runtime folder | `data/Literature/` after `prepare_runtime.py`: the canonical JSONL and the glossary PDF only. | [literature-corpus](chapters/literature-corpus.md) |
| S3 | Amazon Simple Storage Service, where plots and HITL notes are published. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Safety box (KCE, VAA) | Avoidance areas on OOI safety flyers. The cable build puts PN1B, PN1D, PN5A and PN3B at their box centres. PN1C sits at a COSZO ROV site instead, and PN3A at the MJ03A junction box. | [atlas-map-data](chapters/atlas-map-data.md) |
| SandCat | VersaLogic SandCat VL-EPM-39, a candidate node-controller replacement. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Saved interval | A distance range along a cable that a masked MultiDAS file stored. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| SBE 54 | Sea-Bird SBE 54 tsunameter, a pressure sensor used in earlier RCA work. | [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Science junction box | Infrastructure that carries science cables. Kept out of instrument counts. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| SCPR | Self-calibrating pressure recorder. | [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| SECURITY DEFINER | A function that runs with its owner's privileges rather than the caller's. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Seed | The main bibliography, `coszo_citations.jsonl`, with one row per citation occurrence. | [literature-batches](chapters/literature-batches.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| SEED channel code | A three-character channel name such as BHZ or HHZ. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| SeedLink | The streaming protocol for continuous real-time seismic data, which these tools do not use. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Seismic channel codes (HHZ, EHZ, BHZ, SHZ, HDH) | Three-letter SEED-style codes. Z is the vertical component. HDH is the hydrophone channel. | [atlas-map-data](chapters/atlas-map-data.md) |
| Semantic Scholar | Public scholarly graph API, queried by DOI. | [literature-batches](chapters/literature-batches.md) |
| semaphore | A counter that caps concurrent use; `HostLimiter` keeps one per source. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Sensitive finding | An audit hit: a private address, MAC address, internal hostname, credential-bearing URL or secret-like value. | [repo-ops-data](chapters/repo-ops-data.md) |
| Sensor | A catalogued instrument with a position, type, family, status and access routes. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| SHA-256 | A cryptographic hash used to check that a file is intact. | [repo-ops-data](chapters/repo-ops-data.md), [agentic-qaqc](chapters/agentic-qaqc.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [axial](chapters/axial.md), [corpus-docs-web](chapters/corpus-docs-web.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [graphrag-runtime](chapters/graphrag-runtime.md), [literature-batches](chapters/literature-batches.md), [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md) |
| Shared instrument ID | An `INSTRUMENT-…` identifier from the shared Instruments corpus, reused so PI records join the same instrument. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| Shingle | A run of consecutive words, here five tokens, used to compare texts. | [literature-corpus](chapters/literature-corpus.md) |
| Sidebar | An unlabelled text box on a publisher page. Not an abstract. | [literature-batches](chapters/literature-batches.md) |
| Side panel | The 440 px panel at the right for a site or the unplaced list. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| SIGTERM | The stop signal a process manager sends to a server. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Site | One physical location, grouping every sensor within 150 m of another. | [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| Sitemap | An XML list of a site's URLs. The crawler reads `wp-sitemap.xml` and `sitemap-posts-` files. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Skill | An instruction file that agents load. Here, `.agents/skills/okf-memory/SKILL.md`. | [repo-ops-data](chapters/repo-ops-data.md) |
| Skirt | A ring of extra vertices around a tile, dropped 25 m, which hides cracks between tiles. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Snapshot | A dated copy of live data, used when the live source is down. | [agentic-qaqc](chapters/agentic-qaqc.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Snapshot, live, fallback | `snapshot` reads `events.sqlite`; `live` reads the UW site; `snapshot_fallback` is used when the live fetch fails | [axial](chapters/axial.md) |
| Source description | Text that is not an abstract: report descriptions, dataset descriptions, standfirsts. Stored separately. | [literature-batches](chapters/literature-batches.md) |
| Source-material checkout | A local git clone of a COSZO Hub repository under `source_material/`, which the repository ignores. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| Source occurrence (citation occurrence) | One place where a work is cited, such as a proposal section or a Zotero collection. There are 398 in total, each with an `occurrence_id`. | [literature-corpus](chapters/literature-corpus.md) |
| Span | Time window of a plot: `day`, `week`, `month`, `year` or `deploy`. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Spatial mask | A file-specific restriction on which cable distances were saved. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Spike | A glowing beam that rises from the seafloor at a located point. | [ask-atlas](chapters/ask-atlas.md) |
| SQL | Structured Query Language, used by the migrations and the four `graphrag_api` functions. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| SQLite | An embedded file database; the store is `events.sqlite` | [axial](chapters/axial.md), [coszo-hub-core](chapters/coszo-hub-core.md) |
| SSA | Seismological Society of America. | [literature-batches](chapters/literature-batches.md) |
| SSRF | Server-side request forgery: a fetch that is steered to internal hosts. Guarded at `:426-453`. | [literature-fulltext](chapters/literature-fulltext.md) |
| Stable ID | An identifier that does not change between builds, such as `chunk:...` or a figure ID. | [eval-experiments](chapters/eval-experiments.md) |
| Stack | The terrain grids, finest first, that answer elevation queries. | [atlas-map-data](chapters/atlas-map-data.md) |
| Standfirst | A short publisher summary or teaser that is not a formal abstract. | [literature-corpus](chapters/literature-corpus.md), [literature-batches](chapters/literature-batches.md) |
| Station, dataselect, availability | The three FDSN services used here: station metadata, waveform selection and coverage. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| StationXML | An XML format for seismic station metadata, used by the OOI station records. | [repo-ops-data](chapters/repo-ops-data.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-sources](chapters/coszo-hub-sources.md), [graphrag-runtime](chapters/graphrag-runtime.md) |
| Status group | `operating`, `offline`, `planned` or `unknown`, derived from the status. | [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| statusGroup | Groups the status words into operating, offline, planned and unknown. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| stdio | Standard input and output, the transport the MCP server uses. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [agentic-qaqc](chapters/agentic-qaqc.md), [coszo-hub-core](chapters/coszo-hub-core.md) |
| Structured record | Exact-match sidecar row kept as JSONB and not embedded. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Subsurface | The earthquakes, magma-chamber top and caldera-wall faults beneath Axial. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| SVG | Scalable Vector Graphics, an XML image format. The power plot is SVG. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [agentic-qaqc](chapters/agentic-qaqc.md) |
| SVG, PNG, JPEG | Image formats returned by the tools | [axial](chapters/axial.md) |
| SZ4D | Subduction Zones in 4D, a research initiative with a report in the parent overrides. | [literature-batches](chapters/literature-batches.md) |
| TDM | Text and data mining. A common term in license strings that the scripts treat as not an article license. | [literature-batches](chapters/literature-batches.md) |
| TDS EEW | Trident Data Services early-warning software. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Tesseract | The open-source OCR engine, run as the `tesseract` command. Its page segmentation mode (PSM) sets the layout assumption. | [corpus-docs-web](chapters/corpus-docs-web.md), [literature-fulltext](chapters/literature-fulltext.md) |
| TestClient | FastAPI's in-process test client, which the gateway's tests use. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Thinning | Reducing a long series to at most 2,000 points by keeping each bucket's min and max. | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| THREDDS | A data-server catalog format. The adapter reads its XML to list files. | [coszo-hub-sources](chapters/coszo-hub-sources.md) |
| three.js | The WebGL library the scene is built on. OrbitControls is its camera controller. | [atlas-map-scene](chapters/atlas-map-scene.md), [ask-atlas](chapters/ask-atlas.md) |
| Title similarity | Ratio from 0 to 1 given by Python's `difflib.SequenceMatcher` on normalized titles. Batch 2's resolver takes the higher of this and token similarity. | [literature-batches](chapters/literature-batches.md) |
| Token similarity | Share of words two titles have in common (Jaccard), used by the DOI recovery pass in batch 2. | [literature-batches](chapters/literature-batches.md) |
| Tool definition | Metadata for a live tool that is routed but never executed here. | [graphrag-runtime](chapters/graphrag-runtime.md) |
| Tool expectation | Whether a question must, or must not, call a live tool (`tool_expectation` in the gold file). | [eval-experiments](chapters/eval-experiments.md) |
| Toolkit | A class in another folder that calls one upstream and returns `{ok,...}` dictionaries (`NereusToolkit`, `QAQCToolkit`, `PIPortalToolkit`, `EarthScopeFDSNToolkit`). | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Tour | Stepping through the evidence in order with ← and →. | [ask-atlas](chapters/ask-atlas.md) |
| Transponder | In this context, a seafloor acoustic ranging station. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Trigger period | An interval of clock discontinuity. Query times inside it get NaN; Decision 7 gives the limit of that guarantee. | [coszo-hub-core](chapters/coszo-hub-core.md) |
| TS-7800 | Technologic Systems TS-7800-V2, an embedded computer and candidate node-controller replacement. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| TSV | Tab-separated values: the `tsv` output format of Tesseract, which the OCR helper parses. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| TTL | Time to live: how long a cached answer may be reused. | [atlas-map-gateway](chapters/atlas-map-gateway.md), [agentic-qaqc](chapters/agentic-qaqc.md), [axial](chapters/axial.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Typed-in | Text hand-entered into a script. Not produced by any automated step. | [literature-batches](chapters/literature-batches.md) |
| Unlocated, unplaced | Unlocated means a null lat or lon. Unplaced means unlocated and not attached to a site. | [atlas-map-data](chapters/atlas-map-data.md) |
| Unplaced | A sensor with no usable position and no catalogued site. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| Untrusted data | Text from outside the project, flagged in records and responses (`source_is_untrusted_data`). | [literature-fulltext](chapters/literature-fulltext.md), [corpus-docs-web](chapters/corpus-docs-web.md) |
| uPlot | The charting library behind `Chart`. | [atlas-map-panels](chapters/atlas-map-panels.md) |
| URL | Uniform Resource Locator: a web address. The crawler normalizes URLs before using them as keys. | [corpus-docs-web](chapters/corpus-docs-web.md), [agentic-qaqc](chapters/agentic-qaqc.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [axial](chapters/axial.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| USGS | U.S. Geological Survey. Its Publications Warehouse API returns catalog text. | [literature-batches](chapters/literature-batches.md) |
| UTC | Coordinated Universal Time. The MCP tools use it for every day boundary; Ask Atlas can use the asker's zone (Gotcha 5) | [axial](chapters/axial.md), [ask-atlas](chapters/ask-atlas.md), [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| uvicorn | Server that runs the gateway, speaking ASGI (Asynchronous Server Gateway Interface). | [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| UW | University of Washington, which publishes the Axial earthquake catalog | [axial](chapters/axial.md), [atlas-map-data](chapters/atlas-map-data.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md), [coszo-hub-core](chapters/coszo-hub-core.md) |
| VEL3D | The sea-water velocity (current-meter) instrument family and its collection pipeline. | [coszo-hub-core](chapters/coszo-hub-core.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Version of record | The published, citable version of a work, as opposed to a preprint or a conference paper. | [literature-batches](chapters/literature-batches.md) |
| Vertical exaggeration | A height multiplier from 1× to 12× in the HUD slider. The scene applies it at `AtlasScene.js:176`. | [atlas-map-scene](chapters/atlas-map-scene.md) |
| Vite | The dev server and bundler for the site. | [atlas-map-scene](chapters/atlas-map-scene.md), [atlas-map-gateway](chapters/atlas-map-gateway.md) |
| Vite proxy | The development-server rule that forwards `/api/ask` and adds the Origin header. | [ask-atlas](chapters/ask-atlas.md) |
| WARN | A three-component accelerometer processing method named in the datasheet metadata. The repo gives no expansion. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Water column | The vertical line from a mooring up to the sea surface, with labels for the depths where sensors sample. | [atlas-map-panels](chapters/atlas-map-panels.md), [atlas-map-data](chapters/atlas-map-data.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| WGS84 | World Geodetic System 1984, the coordinate reference for latitude and longitude. | [coszo-hub-core](chapters/coszo-hub-core.md), [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| WordPress | The site software whose `wp-json/wp/v2` endpoints the crawler reads for two of the three sites. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| WordPress REST API | The `wp-json/wp/v2` endpoints that serve site content as JSON. | [corpus-docs-web](chapters/corpus-docs-web.md) |
| Workbook | The COSZO deployment spreadsheets, cited as evidence and not read by the code. | [corpus-instruments-ops](chapters/corpus-instruments-ops.md) |
| Worker | A Cloudflare Worker: JavaScript run at Cloudflare's edge. Here it is the public boundary. | [ask-atlas](chapters/ask-atlas.md), [atlas-map-gateway](chapters/atlas-map-gateway.md), [atlas-map-scene](chapters/atlas-map-scene.md) |
| Wrangler | Cloudflare's command-line tool for running and deploying Workers. | [ask-atlas](chapters/ask-atlas.md) |
| YAML | YAML Ain't Markup Language, a text configuration format. Some vendored parameter tables use it. | [agentic-qaqc](chapters/agentic-qaqc.md) |
| Zotero | Reference manager. Its group libraries hold the public bibliographies used here. | [literature-corpus](chapters/literature-corpus.md), [literature-fulltext](chapters/literature-fulltext.md) |
| zstd | Zstandard, a compression format and tool. | [repo-ops-data](chapters/repo-ops-data.md) |
