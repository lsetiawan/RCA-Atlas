## 2026-10-09
* **Update**: Linked `requirements/llm-keys-server-side.md` to `architecture/atlas-worker.md` (The Worker holds its keys as secrets.).
* **Update**: Linked `requirements/llm-keys-server-side.md` to `architecture/graphrag-runtime.md` (The API container holds the Gemini key.).
* **Update**: Linked `decisions/model-champions-from-rca-evaluation.md` to `architecture/model-eval.md` (Sets how the Model Lab may pick champions.).
* **Update**: Linked `requirements/candidate-graphs-need-review.md` to `architecture/literature-fulltext.md` (Keeps the full-text candidate graph out of the canonical graph.).
* **Update**: Linked `requirements/candidate-graphs-need-review.md` to `architecture/microsoft-graphrag-layer.md` (Keeps the pilot's output a candidate layer.).
* **Update**: Linked `decisions/arcada-display-name.md` to `architecture/graphrag-runtime.md` (The runtime maps the arcada id to its display name.).
* **Update**: Linked `decisions/arcada-display-name.md` to `architecture/arcada-pipeline.md` (Names the collection this pipeline builds.).
* **Update**: Linked `decisions/gateway-reuses-toolkits.md` to `architecture/atlas-map-gateway.md` (Sets how the gateway reaches its upstream sources.).
* **Update**: Linked `decisions/hys14-clock-correction-scope.md` to `architecture/coszo-hub-tools.md` (Scopes the Chronfix correction that the COSZO Hub tools apply.).
* **Update**: Linked `decisions/live-first-operational-data.md` to `architecture/axial-earthquakes.md` (Current-day counts come from the live catalog, with the store as fallback.).
* **Update**: Linked `decisions/live-first-operational-data.md` to `architecture/nereus-pipeline.md` (Nereus status is queried live with a labelled snapshot fallback.).
* **Update**: Linked `decisions/authors-from-structured-metadata.md` to `architecture/literature-pipeline.md` (Governs the literature graph's author and citation edges.).
* **Update**: Linked `decisions/abstracts-source-text-only.md` to `architecture/literature-pipeline.md` (Governs what the catalog's abstract field may hold.).
* **Update**: Linked `requirements/literature-abstract-first.md` to `architecture/literature-fulltext.md` (Governs when the full-text tool may run.).
* **Update**: Linked `decisions/worker-auto-free-routes.md` to `architecture/atlas-worker.md` (Sets the deployed Worker's model fallback chain.).
* **Update**: Linked `requirements/worker-deploys-by-maintainers.md` to `architecture/atlas-worker.md` (Governs who deploys the Worker.).
* **Update**: Linked `requirements/staged-qartod-archive-prefix.md` to `architecture/agentic-qaqc.md` (Constrains the vendored plot pipeline's syncs.).
* **Update**: Linked `requirements/nereus-network-redaction.md` to `architecture/nereus-pipeline.md` (Constrains every Nereus result, cache and snapshot.).
* **Update**: Linked `requirements/release-audit-gate.md` to `architecture/data-release-lifecycle.md` (Gates every corpus release.).
* **Update**: Linked `requirements/release-audit-gate.md` to `architecture/data-maintenance.md` (The audit script is this gate's check.).
* **Update**: Linked `architecture/atlas-ui.md` to `architecture/atlas-worker.md` (Posts questions to the Worker's /v1/answer.).
* **Update**: Linked `architecture/atlas-worker.md` to `architecture/axial-earthquakes.md` (Reimplements the daily earthquake count, for the asker's local day instead of UTC.).
* **Update**: Linked `architecture/atlas-worker.md` to `architecture/atlas-map-gateway.md` (Proxies allowlisted /v1/live paths to the gateway.).
* **Update**: Linked `architecture/atlas-worker.md` to `architecture/graphrag-runtime.md` (Calls POST /v1/context for evidence.).
* **Update**: Linked `architecture/atlas-map-gateway.md` to `architecture/coszo-hub-tools.md` (Imports the PI portal and EarthScope toolkits for /files and /waveform.).
* **Update**: Linked `architecture/atlas-map-gateway.md` to `architecture/agentic-qaqc.md` (Imports QAQCToolkit for /plots.).
* **Update**: Linked `architecture/atlas-map-gateway.md` to `architecture/nereus-pipeline.md` (Imports NereusToolkit for /status.).
* **Update**: Linked `architecture/atlas-map-gateway.md` to `architecture/atlas-map-data.md` (Builds its id allowlist from the bundle's sensors.json.).
* **Update**: Linked `architecture/atlas-map-data.md` to `architecture/instrument-inventory.md` (Builds sensor records from data/Instruments.).
* **Update**: Linked `architecture/atlas-map.md` to `architecture/atlas-worker.md` (Sends Ask Atlas questions and production live-data requests through the Worker.).
* **Update**: Linked `architecture/atlas-map.md` to `architecture/atlas-map-data.md` (Loads the static bundle at startup.).
* **Update**: Linked `architecture/microsoft-graphrag-layer.md` to `architecture/graphrag-runtime.md` (Exports the runtime's normalized chunks to the pilot.).
* **Update**: Linked `architecture/model-eval.md` to `architecture/graphrag-runtime.md` (Records the runtime's pinned BGE model as its retrieval champion.).
* **Update**: Linked `architecture/axial-monitoring-website.md` to `architecture/graphrag-runtime.md` (Writes the axial_monitoring collection that the runtime loads.).
* **Update**: Linked `architecture/axial-earthquakes.md` to `architecture/graphrag-runtime.md` (Writes the axial_earthquakes collection and its tool manifest.).
* **Update**: Linked `architecture/agentic-qaqc.md` to `architecture/instrument-inventory.md` (Resolves instruments through data/Instruments.).
* **Update**: Linked `architecture/coszo-hub-tools.md` to `architecture/graphrag-runtime.md` (Writes the coszo_hub and pi_portal collections that the runtime loads.).
* **Update**: Linked `architecture/literature-fulltext.md` to `architecture/literature-pipeline.md` (Resolves works against the canonical literature catalog.).
* **Update**: Linked `architecture/literature-pipeline.md` to `architecture/graphrag-runtime.md` (Writes the literature collection's graph files that the runtime loads.).
* **Update**: Linked `architecture/ooi-das-geometry.md` to `architecture/graphrag-runtime.md` (Writes the ooi_das_geometry collection that the runtime loads.).
* **Update**: Linked `architecture/fetch-transponders.md` to `architecture/graphrag-runtime.md` (Writes the fetch collection that the runtime loads.).
* **Update**: Linked `architecture/nereus-pipeline.md` to `architecture/instrument-inventory.md` (Its crosswalk joins Nereus reference designators to inventory instruments.).
* **Update**: Linked `architecture/instrument-inventory.md` to `architecture/graphrag-runtime.md` (Writes the instruments collection that the runtime loads.).
* **Update**: Linked `architecture/instrument-inventory.md` to `architecture/arcada-pipeline.md` (Reads the ARCADA documents and chunks to build instrument records.).
* **Update**: Linked `architecture/arcada-pipeline.md` to `architecture/graphrag-runtime.md` (Writes the arcada collection that the runtime serves as RCA Information.).
* **Update**: Linked `architecture/website-pipeline.md` to `architecture/graphrag-runtime.md` (Its package becomes the websites collection that the runtime serves.).
* **Update**: Linked `architecture/figures-datasheets-pipeline.md` to `architecture/graphrag-runtime.md` (Writes the figures and datasheets collections that the runtime loads.).
* **Update**: Linked `architecture/coszo-pdf-pipeline.md` to `architecture/graphrag-runtime.md` (Writes the coszo_documents collection that the runtime discovers and loads.).
* **Update**: Linked `architecture/data-maintenance.md` to `architecture/data-release-lifecycle.md` (Cleans and audits data/ before the release scripts pack it.).
* **Update**: Linked `architecture/data-release-lifecycle.md` to `architecture/graphrag-runtime.md` (Release archives are named by the runtime's catalog fingerprint, and the restored runtime_data feeds its loader.).
* **Creation**: Documented concept `requirements/llm-keys-server-side.md` (Model and Graph-RAG keys never reach the browser).
* **Creation**: Documented concept `decisions/model-champions-from-rca-evaluation.md` (Model champions come only from RCA Atlas results).
* **Creation**: Documented concept `requirements/candidate-graphs-need-review.md` (Candidate graphs never write to the authoritative graph).
* **Creation**: Documented concept `decisions/arcada-display-name.md` (ARCADA is shown as RCA Information, with its internal id kept).
* **Creation**: Documented concept `decisions/gateway-reuses-toolkits.md` (The map gateway reuses the agent toolkits).
* **Creation**: Documented concept `decisions/hys14-clock-correction-scope.md` (The Chronfix correction applies only to the HYS14 OBS clock).
* **Creation**: Documented concept `decisions/live-first-operational-data.md` (Operational values come from live tools).
* **Creation**: Documented concept `decisions/authors-from-structured-metadata.md` (Author and citation edges only from structured metadata).
* **Creation**: Documented concept `decisions/abstracts-source-text-only.md` (Abstracts are source text, never generated).
* **Creation**: Documented concept `requirements/literature-abstract-first.md` (Literature answers start from abstracts).
* **Creation**: Documented concept `decisions/worker-auto-free-routes.md` (Deployed Auto mode stays on free routes).
* **Creation**: Documented concept `requirements/worker-deploys-by-maintainers.md` (Only the maintainers deploy the Worker).
* **Creation**: Documented concept `requirements/staged-qartod-archive-prefix.md` (Staged QARTOD output never syncs to the live dashboard).
* **Creation**: Documented concept `requirements/nereus-network-redaction.md` (No private network details leave the Nereus adapter).
* **Creation**: Documented concept `requirements/release-audit-gate.md` (Corpus releases need a clean network audit).
* **Creation**: Documented concept `architecture/atlas-ui.md` (Standalone Ask Atlas page).
* **Creation**: Documented concept `architecture/atlas-worker.md` (RCA Atlas Worker).
* **Creation**: Documented concept `architecture/atlas-map-gateway.md` (Atlas map gateway).
* **Creation**: Documented concept `architecture/atlas-map-data.md` (Atlas map data bundle).
* **Creation**: Documented concept `architecture/atlas-map.md` (Atlas map website).
* **Creation**: Documented concept `architecture/microsoft-graphrag-layer.md` (Microsoft GraphRAG candidate layer).
* **Creation**: Documented concept `architecture/model-eval.md` (Model Lab).
* **Creation**: Documented concept `architecture/axial-monitoring-website.md` (Axial monitoring website tools).
* **Creation**: Documented concept `architecture/axial-earthquakes.md` (Axial earthquake tools).
* **Creation**: Documented concept `architecture/agentic-qaqc.md` (Agentic QA/QC tools).
* **Creation**: Documented concept `architecture/coszo-hub-tools.md` (COSZO Hub tools).
* **Creation**: Documented concept `architecture/literature-fulltext.md` (Literature full-text tools).
* **Creation**: Documented concept `architecture/literature-pipeline.md` (Literature pipeline).
* **Creation**: Documented concept `architecture/ooi-das-geometry.md` (OOI DAS geometry).
* **Creation**: Documented concept `architecture/fetch-transponders.md` (FETCH transponders).
* **Creation**: Documented concept `architecture/nereus-pipeline.md` (Nereus integration).
* **Creation**: Documented concept `architecture/instrument-inventory.md` (Instrument inventory).
* **Creation**: Documented concept `architecture/arcada-pipeline.md` (ARCADA pipeline).
* **Creation**: Documented concept `architecture/website-pipeline.md` (Website crawler).
* **Creation**: Documented concept `architecture/figures-datasheets-pipeline.md` (Figures and datasheets pipelines).
* **Creation**: Documented concept `architecture/coszo-pdf-pipeline.md` (COSZO PDF pipeline).
* **Creation**: Documented concept `architecture/graphrag-runtime.md` (Graph-RAG runtime).
* **Creation**: Documented concept `architecture/data-maintenance.md` (Data maintenance scripts).
* **Creation**: Documented concept `architecture/data-release-lifecycle.md` (Data and release lifecycle).
* **Creation**: Initialized OKF v0.2 knowledge bundle.
