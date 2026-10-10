# Open questions

Every open question raised by the 17 chapters (178) and the 7 flows (73). Duplicates are merged, so this page has
fewer items than that. Each item says what would answer it and links the documents that raised it; "Q3" means the
third item in that document's Open questions section. Each group names who could answer it, from
`git shortlog -sn HEAD -- <paths>` at `1047fc8`. Back to the [knowledge base README](README.md).

## The ten to answer first

1. **Where must `.env` live for Docker Compose?** The README creates it at the repository root, but Compose reads `.env`
   from `src/graphrag_runtime/`. Answer: on a host with the Compose v2 plugin, run `docker compose config --quiet`, then
   fix the README. ([restore-and-run Q1](flows/restore-and-run.md#open-questions), [repo-ops-data Q2](chapters/repo-ops-data.md#open-questions))
2. **What is actually deployed?** Answer these together:
   - Which collection set is current: 13, 15 or 16?
   - Has the PostgreSQL load ever run? `deployment_status.json` says `not_run` as of 2026-09-20.
   - Does the runtime release archive carry the normalized build and embeddings that the quickstart needs?

   Answer: run discovery and the loader on the latest release.
   ([graphrag-runtime Q1](chapters/graphrag-runtime.md#open-questions), [corpus-to-index Q1, Q5, Q9](flows/corpus-to-index.md#open-questions))
3. **Who owns the gate before a build goes live?**
   - Nothing runs `validate_loaded_build.sql`.
   - Activation does not require embeddings.
   - The loader never checks that the embeddings belong to the build's catalog and model.

   Answer: the release owner decides the gate and its order.
   ([corpus-to-index Q2-Q4](flows/corpus-to-index.md#open-questions), [graphrag-runtime Q7](chapters/graphrag-runtime.md#open-questions), [restore-and-run Q4, Q6](flows/restore-and-run.md#open-questions))
4. **How is the deployed Worker configured?** Which version is live? Are `ATLAS_MAP_GATEWAY_ORIGIN` and `GEMINI_API_KEY`
   set? Are the rate-limit rule and Turnstile in place? Where does the gateway run? Answer: the deployers, with
   `npx wrangler secret list` and the Cloudflare dashboard. ([ask-atlas Q3, Q4, Q15, Q16](chapters/ask-atlas.md#open-questions), [ask-atlas flow Q2, Q6](flows/ask-atlas.md#open-questions), [atlas-map-gateway Q6, Q9](chapters/atlas-map-gateway.md#open-questions), [live-panel Q1](flows/live-panel.md#open-questions))
5. **How do agents start the MCP servers, and which tool metadata do they trust?** No client configuration is tracked.
   The database copy of each tool manifest is frozen at the last build, while `tools/list` comes from the running
   process. Answer: the team's agent setup. Whoever launches the full-text server must also decide whether to set `UNPAYWALL_EMAIL`, and the OSU monitoring server has no launcher at all. ([agent-tool-call Q1-Q3](flows/agent-tool-call.md#open-questions), [agentic-qaqc Q1](chapters/agentic-qaqc.md#open-questions), [axial Q3](chapters/axial.md#open-questions), [coszo-hub-core Q3](chapters/coszo-hub-core.md#open-questions), [literature-fulltext Q1](chapters/literature-fulltext.md#open-questions))
6. **Is "yesterday" the UTC day or the asker's day?** Ask Atlas uses the asker's zone (commit `8457b94`), and the Axial
   MCP tool uses UTC. Answer: a product decision, then one shared fixture. ([axial Q2](chapters/axial.md#open-questions))
7. **Are the secrets clean?** Answer these together:
   - Were the literal credentials in `compose.yaml` (commits `833c343` to `c9267e0`) ever used outside local development?
   - Do the release archives carry `*.pem`, `*.key` or virtual environments?
   - Does the privacy policy cover the raw `source_material/` that ships unsanitized?

   Answer: the maintainers, then list each archive with `tar -tf`. ([security group](#8-security-and-privacy))
8. **Should the QA/QC plot index refresh inside a running process?** Today the MCP server and the map gateway keep it
   until restart. Answer: the toolkit's owner. ([agent-tool-call Q6](flows/agent-tool-call.md#open-questions), [live-panel Q4](flows/live-panel.md#open-questions))
9. **Which method document is canonical, and is the audit release gate run?** `data/CORPUS_METHOD.md` has drifted from
   `src/DATA_CORPUS_METHOD.md`, and no script enforces zero audit findings. ([repo-ops-data Q1, Q3](chapters/repo-ops-data.md#open-questions))
10. **How do the website and its bundle reach production?** No CI or deployment configuration is tracked, and the
    production gateway's `sensors.json` must come from the same build as the page's. ([atlas-bundle Q1, Q2](flows/atlas-bundle.md#open-questions))

## Answered or narrowed during synthesis

- **What does COSZO stand for?** Cascadia Offshore Subduction Zone Observatory. The corpus builders attach that alias to
  the COSZO entity (`src/coszo_pdf_pipeline/build_coszo_pdf_graph.py:43`; `src/literature_pipeline/code/build_graph_corpus.py:56`).
  ([coszo-hub-core Q12](chapters/coszo-hub-core.md#open-questions), [graphrag-runtime Q10](chapters/graphrag-runtime.md#open-questions))
- **Is `src/atlas_worker/.dev.vars` kept out of Git?** No. `git check-ignore` finds no rule for it, although the map
  README says it is not committed (`src/atlas_map/README.md:26`). Add an ignore rule. ([ask-atlas Q6](chapters/ask-atlas.md#open-questions))
- **Does Compose read the root `.env`?** Not by default: Docker's documentation places `.env` in the project directory,
  `src/graphrag_runtime/`. Still to confirm on a host with Compose (first item above).
- **Does macOS have `sha256sum`?** This macOS 27 host has `/sbin/sha256sum`. Older releases and a stock install are
  unverified, and the README does not list it. ([repo-ops-data Q10](chapters/repo-ops-data.md#open-questions), [restore-and-run Q2](flows/restore-and-run.md#open-questions), [transfer-release Q10](flows/transfer-release.md#open-questions))

## 1. Releases, restore and the runtime environment

Who could answer: Maleen Kidiwela (all 4 commits to `scripts/`; 8 of 13 to the top-level files). Derek Yao and Don
Setiawan also changed top-level files. Don Setiawan wrote the okf tooling (`.agents/`, `knowledge/`, `pixi.toml`).

- **Is the host-side manual load meant to work?** The README loads from the host, but `db` publishes no port. Decide
  where manual loads run, then fix the README. ([restore-and-run Q3](flows/restore-and-run.md#open-questions))
- **What happens after a database password change?** The init scripts run once per volume. Test on a scratch volume and
  document an `ALTER ROLE` step. ([restore-and-run Q9](flows/restore-and-run.md#open-questions))
- **Are passwords with `@`, `:` or `/` supported?** They are placed unencoded into connection URLs. ([restore-and-run Q10](flows/restore-and-run.md#open-questions))
- **Should the restore pin a tag instead of `latest`?** `latest` is resolved again for each asset. ([restore-and-run Q11](flows/restore-and-run.md#open-questions))
- **Do the restored parts belong to one build? Should the restore compare the release manifest's fingerprint with the
  catalog?** ([restore-and-run Q7](flows/restore-and-run.md#open-questions), [transfer-release Q2](flows/transfer-release.md#open-questions))
- **Where is the overlay release's upload procedure written down?** The README covers only `transfer_dist/*`, and both
  builders write the same manifest path. ([transfer-release Q1](flows/transfer-release.md#open-questions))
- **Should the release build rerun discovery before packing?** It trusts the catalog on disk. ([transfer-release Q4](flows/transfer-release.md#open-questions))
- **Should the restore honour `restore_root`, change directory, and clear the target first?** Today it extracts over
  whatever is in the current directory. ([transfer-release Q6, Q7](flows/transfer-release.md#open-questions))
- **Is the repository private, and are any assets near GitHub's per-file size limit?** ([transfer-release Q8, Q9](flows/transfer-release.md#open-questions))
- **Who maintains `deployment_status.json`, and does any published release match it?** ([repo-ops-data Q8](chapters/repo-ops-data.md#open-questions), [transfer-release Q5](flows/transfer-release.md#open-questions))
- **What produced `data/StationMetadata/`?** ([repo-ops-data Q4](chapters/repo-ops-data.md#open-questions))
- **Is FETCH in any built corpus?** ([repo-ops-data Q5](chapters/repo-ops-data.md#open-questions))
- **Where is `source_material/inbox/` created?** ([repo-ops-data Q7](chapters/repo-ops-data.md#open-questions))
- **Is `OPENAI_COMPATIBLE_BASE_URL` meant to override `providers.json`?** No code reads it. ([repo-ops-data Q9](chapters/repo-ops-data.md#open-questions))
- **What does OKF stand for?** Answer: the okf-agent-memory documentation. ([repo-ops-data Q11](chapters/repo-ops-data.md#open-questions))

## 2. Graph-RAG build, load and API

Who could answer: Maleen Kidiwela (all 10 commits to `src/graphrag_runtime/`).

- **Is the HNSW index intended, and which pgvector version runs?** The image tag pins no pgvector version. ([graphrag-runtime Q2](chapters/graphrag-runtime.md#open-questions), [corpus-to-index Q11](flows/corpus-to-index.md#open-questions))
- **Which normalization rules are real: `FIELD_MAP.md` or the code?** ([graphrag-runtime Q3](chapters/graphrag-runtime.md#open-questions))
- **Does the query side embed like the passage side?** The API uses `query_embed` and the builder `passage_embed`, and
  the image downloads the model without the builder's hash pin. ([graphrag-runtime Q5](chapters/graphrag-runtime.md#open-questions), [corpus-to-index Q8](flows/corpus-to-index.md#open-questions), [restore-and-run Q8](flows/restore-and-run.md#open-questions), [ask-atlas flow Q7](flows/ask-atlas.md#open-questions))
- **Is `graphrag_owner` a superuser, and must the production owner be?** ([graphrag-runtime Q6](chapters/graphrag-runtime.md#open-questions), [restore-and-run Q12](flows/restore-and-run.md#open-questions))
- **Is migration `002` for production?** The README says both "local only" and "apply both in production". ([graphrag-runtime Q12](chapters/graphrag-runtime.md#open-questions))
- **Is the connection budget intended?** Two workers times ten connections equals the role limit of 20. ([graphrag-runtime Q9](chapters/graphrag-runtime.md#open-questions))
- **Which statement timeout applies inside the SQL functions?** ([graphrag-runtime Q11](chapters/graphrag-runtime.md#open-questions), [agent-tool-call Q10](flows/agent-tool-call.md#open-questions))
- **Should an empty or inactive build be an error?** Search returns HTTP 200 with empty lists, while `/health` returns 503. ([corpus-to-index Q6](flows/corpus-to-index.md#open-questions), [restore-and-run Q5](flows/restore-and-run.md#open-questions))
- **Should a re-load replace stored vectors?** `ON CONFLICT DO NOTHING` keeps the old ones. ([corpus-to-index Q7](flows/corpus-to-index.md#open-questions))

## 3. Collection builders and data provenance

Who could answer: Maleen Kidiwela, who wrote every builder (corpus-instruments-ops 11 commits, axial 4, literature-corpus
3, coszo-hub 2 and 2, corpus-docs-web, literature-batches and agentic-qaqc 1 each).

- **Which Python environment runs the builders, and how is `msgpack` provisioned?** The datasheets builder needs
  Python 3.12 or later, and `pixi.toml` declares only okf. ([corpus-docs-web Q1](chapters/corpus-docs-web.md#open-questions), [corpus-instruments-ops Q8](chapters/corpus-instruments-ops.md#open-questions), [literature-corpus Q7](chapters/literature-corpus.md#open-questions))
- **What copies `src/website_pipeline/package/` into `data/Websites`?** ([corpus-docs-web Q2](chapters/corpus-docs-web.md#open-questions))
- **Was the timed-out Interactive Oceans listing recovered, and can the 98 recovered records be reproduced?** ([corpus-docs-web Q3, Q4](chapters/corpus-docs-web.md#open-questions))
- **Which folder holds the COSZO PDFs, and does the DataMSRI packet still have 524 pages?** ([corpus-docs-web Q5, Q8](chapters/corpus-docs-web.md#open-questions))
- **Are the hard-coded evidence IDs still valid?** These are the website figure IDs, the nine website page IDs in the
  inventory, and the PI and COSZO evidence IDs. ([corpus-docs-web Q6](chapters/corpus-docs-web.md#open-questions), [corpus-instruments-ops Q7](chapters/corpus-instruments-ops.md#open-questions))
- **Was a perceptual hash computed for the figure matches?** ([corpus-docs-web Q7](chapters/corpus-docs-web.md#open-questions))
- **Which edge name is right in the datasheets builder?** ([corpus-docs-web Q9](chapters/corpus-docs-web.md#open-questions))
- **Who writes `multidas_unmasked_coverage.jsonl`, from which URLs?** ([corpus-instruments-ops Q1](chapters/corpus-instruments-ops.md#open-questions), [atlas-map-data Q4](chapters/atlas-map-data.md#open-questions))
- **Where do the FETCH serial numbers and baselines come from?** ([corpus-instruments-ops Q5](chapters/corpus-instruments-ops.md#open-questions))
- **Are the COSZO Oregon Shelf APG and current-meter units deployed?** ([corpus-instruments-ops Q6](chapters/corpus-instruments-ops.md#open-questions))
- **Who captured the archived OOI site-inventory HTML, and when?** ([corpus-instruments-ops Q10](chapters/corpus-instruments-ops.md#open-questions))
- **Is the DAS25 work in the release's canonical literature file, and what is its publication year?** ([literature-corpus Q1, Q8](chapters/literature-corpus.md#open-questions))
- **What wrote the Zotero exports, and where are they?** The scripts disagree on the folder. ([literature-corpus Q2, Q3](chapters/literature-corpus.md#open-questions), [literature-batches Q10](chapters/literature-batches.md#open-questions))
- **Which manifest is `runtime_manifest.json`?** ([literature-corpus Q4](chapters/literature-corpus.md#open-questions))
- **Why is Zotero collection `PU7BMBHB` mapped by hand?** ([literature-corpus Q5](chapters/literature-corpus.md#open-questions))
- **Should the graph build write the source-material paths itself?** ([literature-corpus Q6](chapters/literature-corpus.md#open-questions))
- **Are all Zotero `abstractNote` values formal abstracts?** ([literature-corpus Q9](chapters/literature-corpus.md#open-questions))
- **Who wrote `src/literature_pipeline/README.md`?** ([literature-corpus Q10](chapters/literature-corpus.md#open-questions))
- **Where does the seed bibliography `coszo_citations.jsonl` come from?** ([literature-batches Q1](chapters/literature-batches.md#open-questions))
- **What were the extra works (IDs 168 to 175), and can the missing `retrieval_extra` stage be recovered?** ([literature-batches Q2](chapters/literature-batches.md#open-questions))
- **Which step wrote `*_crossref_direct.json`?** A clean run fails without it. ([literature-batches Q3](chapters/literature-batches.md#open-questions))
- **How were the typed-in raw sources fetched, and are the transcriptions correct?** ([literature-batches Q4, Q7](chapters/literature-batches.md#open-questions))
- **Why does `retrieval_a` skip exactly 13 IDs?** ([literature-batches Q5](chapters/literature-batches.md#open-questions))
- **What does "parent" mean in the products tree?** ([literature-batches Q6](chapters/literature-batches.md#open-questions))
- **Was the first abstracts package installed by this code, and should `before_expansion/` be tracked?** ([literature-batches Q8, Q9](chapters/literature-batches.md#open-questions))
- **Do Crossref and OpenAlex treat the placeholder contact address as an identified client?** ([literature-batches Q11](chapters/literature-batches.md#open-questions))
- **Which date switches focal mechanisms to the live CSV, and is there a coverage gap?** ([axial Q1, Q12](chapters/axial.md#open-questions))
- **Why does the monitoring corpus list eight streams when four are live, and is it mapped by normalization?** ([axial Q4, Q8](chapters/axial.md#open-questions))
- **Is `snapshot_figures.py` part of the refresh, and does the cleanup rule match what the builder writes?** ([axial Q5, Q6](chapters/axial.md#open-questions))
- **Are the Axial visual chunks embedding input or auxiliary?** The builder writes them to both files. ([axial Q7](chapters/axial.md#open-questions))
- **Where do the annual focal counts come from?** ([axial Q11](chapters/axial.md#open-questions))
- **Which command and data produced `data/QAQC/graphrag/`, and does its node count match Graph-RAG's?** ([agentic-qaqc Q2, Q10](chapters/agentic-qaqc.md#open-questions))
- **Is the QA/QC HITL snapshot meant to load as structured records?** ([agent-tool-call Q9](flows/agent-tool-call.md#open-questions))
- **Does the catalog pick up the DAS metadata file?** ([coszo-hub-core Q11](chapters/coszo-hub-core.md#open-questions))
- **Does the PI graph test pass without the private instrument corpus?** ([coszo-hub-sources Q6](chapters/coszo-hub-sources.md#open-questions))
- **Is `INSTRUMENT-e49ff2e8088de867de` retired in favour of `INSTRUMENT-981a1c15a947d3b1a1`, and does any consumer resolve sites by alias?** ([coszo-hub-sources Q7, Q10](chapters/coszo-hub-sources.md#open-questions))
- **Is a root `tools.jsonl` meant to be a graph node in every collection?** ([agent-tool-call Q4](flows/agent-tool-call.md#open-questions))

## 4. Live agent tools and MCP servers

Who could answer: Maleen Kidiwela, who wrote every MCP server and toolkit.

- **Do full-question queries return tool hints at all?** The tool search matches every word of the question. ([agent-tool-call Q5](flows/agent-tool-call.md#open-questions))
- **Is `axial_count_events` in the deployed tool catalog, and is the literature tool manifest current?** ([ask-atlas flow Q1](flows/ask-atlas.md#open-questions), [agent-tool-call Q8](flows/agent-tool-call.md#open-questions))
- **QA/QC:** Does a HITL CSV's first column always hold the refdes? Is the vendored tree identical to commit `03358ff`?
  Does it import under the pinned Prefect? Does `--site` accept site codes? Where do keys land with `--prefix /`? What
  load does the RCA team accept? ([agentic-qaqc Q3-Q6, Q8, Q11](chapters/agentic-qaqc.md#open-questions))
- **Should live QA/QC text carry the untrusted-data flag?** ([agentic-qaqc Q9](chapters/agentic-qaqc.md#open-questions))
- **Should an Axial auto-mode outage on a day with no stored rows be an error, not a zero?** ([agent-tool-call Q7](flows/agent-tool-call.md#open-questions))
- **Is the OSU monitoring tools' hard-coded `"ok": true` intended?** ([axial Q10](chapters/axial.md#open-questions))
- **COSZO Hub core:**
  - Is `chronfix_model.py` meant to be used?
  - Which deployment sets the four `COSZO_*_OUTPUT_ROOT` variables?
  - Does the first README test line run as written? Is numpy meant to come from the host Python?
  - Are the substring keyword matches `obs` and `wave` intended? They can apply the HYS14 clock correction to the wrong timestamps.
  - What is "RCA Series B"?
  - Is re-statting every file on every call intended?
  - Does the per-channel Chronfix claim hold? Are the hours inside a trigger window non-finite in the bundle?

  ([coszo-hub-core Q1, Q2, Q4-Q9, Q13](chapters/coszo-hub-core.md#open-questions))
- **COSZO Hub sources:**
  - Should one oversize OOI file abort the whole download?
  - Why does `list_streams` skip method names containing "bad"?
  - Is `service.iris.edu` meant to be allowed?
  - Should PI retries skip size-limit errors?
  - Do the README test commands run from the repo root?
  - When does EarthScope's availability service leave its 2026 transition?

  ([coszo-hub-sources Q1-Q5, Q9](chapters/coszo-hub-sources.md#open-questions))
- **Literature full text:**
  - What is the "bundled PDF-capable Python runtime"?
  - Who consumes the candidate graph, and what is "graph validation"?
  - Should a cache entry serve a larger `max_pages`?
  - Should the response report `truncated` and `pages_processed`?
  - What is the test command?

  ([literature-fulltext Q2-Q5, Q7](chapters/literature-fulltext.md#open-questions))
- **Nereus and DAS:** Does an MCP client render the SVG from `nereus_plot_power_history`? Is any agent served the DAS
  lookup tools? ([corpus-instruments-ops Q2, Q9](chapters/corpus-instruments-ops.md#open-questions))

## 5. Ask Atlas and the Worker

Who could answer: Maleen Kidiwela (32 commits) and Derek Yao (24) on the ask-atlas paths; Maleen Kidiwela wrote 21 of
the Worker's 27 commits. The spec names Derek and Maleen as the Worker's deployers
(`docs/superpowers/specs/2026-09-24-ask-atlas-evidence-design.md:152`) and Derek as its approver (`:3`).

- **Should a question with no retrieved evidence get an answer instead of a 503?** ([ask-atlas Q9](chapters/ask-atlas.md#open-questions), [ask-atlas flow Q9](flows/ask-atlas.md#open-questions))
- **Should Retry abort another pending question, and should `resolveEvidence` errors be caught and shown with Retry?**
  Either case can leave the composer locked. ([ask-atlas Q7](chapters/ask-atlas.md#open-questions), [ask-atlas flow Q10](flows/ask-atlas.md#open-questions))
- **Was dropping `sensor.location` from site matching intended?** ([ask-atlas Q10](chapters/ask-atlas.md#open-questions), [ask-atlas flow Q11](flows/ask-atlas.md#open-questions))
- **Should `/v1/live` check the Origin or be rate-limited like `/v1/answer`?** ([ask-atlas Q8](chapters/ask-atlas.md#open-questions), [live-panel Q6](flows/live-panel.md#open-questions))
- **Should the gateway's `POST /chat` and the Graph-RAG API's `POST /v1/answer` stay?** Nothing in the repository calls `/chat`. ([ask-atlas Q13](chapters/ask-atlas.md#open-questions), [atlas-map-gateway Q1](chapters/atlas-map-gateway.md#open-questions), [ask-atlas flow Q8](flows/ask-atlas.md#open-questions))
- **Is OpenRouter support meant to return?** Its code has no caller. ([ask-atlas Q2](chapters/ask-atlas.md#open-questions), [ask-atlas flow Q3](flows/ask-atlas.md#open-questions))
- **Is `answer_mode: "quick"` still wanted?** No client sends it. ([ask-atlas Q14](chapters/ask-atlas.md#open-questions))
- **Standalone page:** Should `src/atlas_ui` keep its 2D evidence map? Are `react-force-graph-3d` and `three` still
  needed? Where is the page hosted? It works only from `https://coszo.org`. ([ask-atlas Q1, Q11](chapters/ask-atlas.md#open-questions), [ask-atlas flow Q5](flows/ask-atlas.md#open-questions))
- **Is the plain-HTTP Axial catalog origin intended?** ([ask-atlas flow Q4](flows/ask-atlas.md#open-questions))
- **Is `error-503.json` meant for a test?** ([ask-atlas Q12](chapters/ask-atlas.md#open-questions))
- **Does the halo rest under reduced motion in a real browser?** ([ask-atlas Q5](chapters/ask-atlas.md#open-questions))

## 6. The map, its bundle and the gateway

Who could answer: Derek Yao (atlas-map-scene 49 commits, atlas-map-panels 26, atlas-map-data 17, atlas-map-gateway 11,
and all 14 spec commits) and Maleen Kidiwela (9, 4, 4 and 2).

- **Bundle build:**
  - What total should the counts check use? Today it compares the record list with itself.
  - Should a disallowed host fail the build?
  - Should `--refresh-external` fail rather than warn?
  - Should writes go to a staging folder?

  ([atlas-map-data Q1, Q5](chapters/atlas-map-data.md#open-questions), [atlas-bundle Q4-Q6](flows/atlas-bundle.md#open-questions))
- **Which vertical-channel order and which MultiDAS path are intended?** ([atlas-map-data Q2, Q3](chapters/atlas-map-data.md#open-questions))
- **Are the optional builders' sources pinned?** These are the `axial_visuals` commit behind `subsurface.json` and the
  MBARI grid behind the tiles. Do the committed 1 m tiles still match the reviewed sensor positions? ([atlas-map-data Q6](chapters/atlas-map-data.md#open-questions), [atlas-bundle Q7, Q8](flows/atlas-bundle.md#open-questions))
- **Is there a runbook for the cable pipeline, and what is the column order of `axial_calderaRim.m`?** ([atlas-map-data Q7, Q8](chapters/atlas-map-data.md#open-questions))
- **Should the gateway reload `sensors.json` after a rebuild?** ([atlas-bundle Q3](flows/atlas-bundle.md#open-questions))
- **What is the bundle's source for QA/QC coverage?** The spec lists `data/QAQC/graphrag/catalog_summary.json` as an input, but the build reads the live plot index (with `--refresh-external`) and no code reads that file. ([agentic-qaqc Q7](chapters/agentic-qaqc.md#open-questions))
- **Is it intended that Nereus snapshots never reach the gateway?** It builds the toolkit without `snapshot_dir`. ([live-panel Q3](flows/live-panel.md#open-questions))
- **Should timeouts be 504 rather than 502, and is the 500 from `/waveform/{station}/health` on bad input intended?** ([live-panel Q5](flows/live-panel.md#open-questions), [atlas-map-gateway Q2](chapters/atlas-map-gateway.md#open-questions))
- **Why does the waveform window end two minutes before the current minute, and is matching on "no waveform data" a
  contract with the toolkit?** ([atlas-map-gateway Q3](chapters/atlas-map-gateway.md#open-questions), [live-panel Q9](flows/live-panel.md#open-questions))
- **Which CDOM variable-name length is right, and does the spec or the code win where they differ?** ([atlas-map-gateway Q4, Q5](chapters/atlas-map-gateway.md#open-questions))
- **Which Python environment runs the gateway, and do the Worker's and the gateway's `ATLAS_API_KEY` match?** ([atlas-map-gateway Q7, Q10](chapters/atlas-map-gateway.md#open-questions))
- **What does the Vite dev proxy return when the gateway is down, and is `npm run preview` meant to reach the Worker?** ([atlas-map-gateway Q8](chapters/atlas-map-gateway.md#open-questions), [atlas-bundle Q9](flows/atlas-bundle.md#open-questions), [live-panel Q2, Q7](flows/live-panel.md#open-questions))
- **Do all bundle refdes match the Worker's path pattern, and can a PI listing exceed 10 MiB?** ([live-panel Q8, Q10](flows/live-panel.md#open-questions))
- **Panels:**
  - Do any sites have 24 or more sensors? Their depth-section targets would overlap.
  - Is the dock spec's Testing section stale?
  - Do long site labels overlap?
  - Should the cable node's `source` come from the build?
  - Should a sensor with EarthScope and QA/QC routes but no ERDDAP route show its plots?
  - Should the legend's "Not deployed / retired" cover every status in its group?
  - Should `Chart` follow the window size?
  - Should "Copied" wait for the clipboard write?

  ([atlas-map-panels Q1-Q8](chapters/atlas-map-panels.md#open-questions))
- **Scene:**
  - Is the 1 m summit grid meant to be square? Today it is 1.01 m east-west by 1.43 m north-south.
  - Was a 1 km seam blend intended?
  - Should `window.__atlas` ship to production?
  - Which plans do the code comments mean?
  - Should `dispose()` free GPU resources?
  - Which browsers are supported?
  - Should `mapped` cable lines be dashed?

  ([atlas-map-scene Q1-Q7](chapters/atlas-map-scene.md#open-questions))

## 7. Evaluation

Who could answer: Maleen Kidiwela (all commits to `src/model_eval/` and `src/microsoft_graphrag_layer/`).

- **Who runs the answer comparison, and are the registries meant to be read?** No command runs the answer path yet. ([eval-experiments Q1, Q2](chapters/eval-experiments.md#open-questions))
- **Are the expected tool names stale?** Nine of 30 match nothing, including Nereus, Axial and COSZO Hub names, and the
  `chronfix-001` expectation disagrees between files. ([eval-experiments Q4, Q5](chapters/eval-experiments.md#open-questions), [corpus-instruments-ops Q3](chapters/corpus-instruments-ops.md#open-questions), [axial Q9](chapters/axial.md#open-questions), [coszo-hub-core Q10](chapters/coszo-hub-core.md#open-questions))
- **Which Gemini models are the challengers, and how does Anthropic count cached tokens?** ([eval-experiments Q3, Q6](chapters/eval-experiments.md#open-questions))
- **What was the identifier branch in `route_query` for?** ([eval-experiments Q7](chapters/eval-experiments.md#open-questions))
- **Who reviews GraphRAG candidate merges, and which Microsoft GraphRAG release is pinned?** The README's pilot example
  names `figures_datasheets`, which matches no collection. ([eval-experiments Q8, Q9](chapters/eval-experiments.md#open-questions), [corpus-docs-web Q10](chapters/corpus-docs-web.md#open-questions))
- **Who wrote the question set and gold answers, and how were they checked?** ([eval-experiments Q10](chapters/eval-experiments.md#open-questions))

## 8. Security and privacy

Who could answer: the maintainers above. The credential history is in Maleen Kidiwela's commits to `compose.yaml`.

- **Were the historical `compose.yaml` credentials ever used outside local development?** From `833c343` through
  `c9267e0` the file held a literal password for `graphrag_api_role` and a literal API-key digest. Rotate them if so.
  ([graphrag-runtime](chapters/graphrag-runtime.md), Gotchas)
- **Do the release archives carry secrets or virtual environments?** The excludes cover only `.env` files. ([transfer-release Q3](flows/transfer-release.md#open-questions))
- **Does the privacy policy cover raw sources?** The sanitizer never touches `source_material/`, which ships in a release. ([repo-ops-data Q6](chapters/repo-ops-data.md#open-questions))
- **Is the release audit gate run?** ([repo-ops-data Q3](chapters/repo-ops-data.md#open-questions))
- **Does the live Nereus adapter strip MAC addresses and internal hostnames?** ([corpus-instruments-ops Q4](chapters/corpus-instruments-ops.md#open-questions))
- **Should the `UNPAYWALL_EMAIL` value be redacted from attempt logs and reports?** ([literature-fulltext Q6](chapters/literature-fulltext.md#open-questions))
- **Does the Gemini key appear in logs?** Both callers put it in the URL. ([graphrag-runtime Q8](chapters/graphrag-runtime.md#open-questions))
- **Is the owner password visible in the loader container's command?** ([corpus-to-index Q10](flows/corpus-to-index.md#open-questions))
- **Should synthesis see the untrusted-data marker on corpus text?** ([graphrag-runtime Q4](chapters/graphrag-runtime.md#open-questions))
- **Should the THREDDS XML parser be hardened, and is the PI portal still plain HTTP?** ([coszo-hub-sources Q8, Q11](chapters/coszo-hub-sources.md#open-questions))
- **Should the crawler honour robots.txt?** ([corpus-docs-web Q11](chapters/corpus-docs-web.md#open-questions))
