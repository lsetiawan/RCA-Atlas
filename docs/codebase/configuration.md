# Configuration and secrets

Every environment variable and secret that RCA Atlas code reads: which component reads it, what it is for,
where its value is set, and its default. Values are never recorded here. Code constants and command-line
flags are not configuration in this sense; each chapter's **Configuration and secrets** section lists them.
Back to the [knowledge base README](README.md).

As of `1047fc8`. Citations are repository paths; a `path:line` is where the value is read.

## Where values are set

| Place | Who reads it | Notes |
|---|---|---|
| `.env` at the repository root, copied from `.env.example` | The Atlas map gateway reads it directly (`src/atlas_map_gateway/config.py:37-38`); process environment wins over the file. The graphrag README tells operators to create it there (`src/graphrag_runtime/README.md:25-32`). | Gitignored (`.gitignore:12-14`). Compose may not read this file: see the first known issue below. |
| Docker Compose variable substitution in `src/graphrag_runtime/compose.yaml` | The `db`, `api` and `loader` services | `${VAR:?message}` makes a variable required; `${VAR:-default}` supplies a default (`compose.yaml:7-8`, `21-25`, `33-34`). |
| `src/graphrag_runtime/Dockerfile` | The API image | Sets `GRAPHRAG_EMBEDDING_OFFLINE` and `GRAPHRAG_MODEL_CACHE` (`Dockerfile:10`). |
| `src/atlas_worker/wrangler.toml` `[vars]` | The Cloudflare Worker | Public values only (`wrangler.toml:5-12`). |
| `wrangler secret put <NAME>` | The deployed Worker | The secret list is a comment in `wrangler.toml:14-22`. |
| `src/atlas_worker/.dev.vars` | `wrangler dev` (local Worker) | Named in `src/atlas_map/README.md:26-27`. **Not gitignored**: `git check-ignore` matches no rule for it. |
| A Vite env file in `src/atlas_map/`, or the shell | `npm run dev` | `loadEnv("development", process.cwd(), "VITE_ATLAS_ASK")` (`src/atlas_map/vite.config.js:7`). |
| The environment of the MCP client that launches a `run_mcp.sh` | MCP servers | Each launcher fills defaults with `: "${VAR:=…}"` before `exec` (for example `src/agentic_qaqc/run_mcp.sh:7-10`). No MCP client configuration is tracked in the repository. |
| The operator's shell | Release, restore and build scripts | For example `GITHUB_REPOSITORY` (`scripts/bootstrap_machine.sh:5`). |

## Graph-RAG runtime: database, loader and API ([graphrag-runtime](chapters/graphrag-runtime.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `POSTGRES_PASSWORD` | `src/graphrag_runtime/compose.yaml:7`, `:33-34` | Password of the owner role `graphrag_owner`, used by the `db` container and the loader's connection string. | Compose `.env` | Required (`:?`). | Yes |
| `GRAPHRAG_API_DATABASE_PASSWORD` | `compose.yaml:8`, `:21`; `migrations/002_local_api_role.sql:3-7` (`\getenv` at first database start) | Password of the read-only API role `graphrag_api_role`. | Compose `.env` | Required (`:?`). | Yes |
| `GRAPHRAG_API_KEY_SHA256` | `src/graphrag_runtime/app/config.py:20`; `compose.yaml:22` | Comma-separated SHA-256 digests of the client keys the API accepts. Only digests are stored server-side. | Compose `.env` | Required (`:?`). | Treat as sensitive |
| `GRAPHRAG_API_KEY` | Not read by the API. Read by the gateway as a fallback (`src/atlas_map_gateway/config.py:42`). | The plain client key whose digest is in `GRAPHRAG_API_KEY_SHA256`; entered on the evidence page (`src/graphrag_runtime/README.md:12`). | Root `.env` | Optional. | Yes |
| `DATABASE_URL` | `app/config.py:25-27` | Connection string of the API role. | `compose.yaml:21` (api); also set for the loader at `:33`, whose code takes `--dsn` instead. | Required by the API. | Yes (embeds a password) |
| `GEMINI_API_KEY` | `app/config.py:33`; `compose.yaml:23` | Gemini key for `POST /v1/answer`. | Compose `.env` | Optional; `/v1/answer` needs it. | Yes |
| `GRAPHRAG_ANSWER_MODEL` | `app/config.py:34`; `compose.yaml:24` | Gemini model for `/v1/answer`. | Compose `.env` | `gemini-2.5-flash`. | No |
| `GRAPHRAG_API_PORT` | `compose.yaml` `ports` (`127.0.0.1:${GRAPHRAG_API_PORT:-8000}:8000`); gateway `config.py:39` | Host port of the API. | `.env` | `8000`. A blank value breaks the gateway's default URL (see known issues). | No |
| `GRAPHRAG_STATEMENT_TIMEOUT_MS` | `app/config.py:28`; `app/repository.py:57-58` | Per-transaction statement timeout. | `compose.yaml:25` sets `4000`. | `4000`, clamped to 250-15000. | No |
| `GRAPHRAG_POOL_MIN`, `GRAPHRAG_POOL_MAX` | `app/config.py:29-30` | Connection-pool bounds per Gunicorn worker. | Environment | `1` and `10`, clamped. | No |
| `GRAPHRAG_EMBEDDING_MODEL` | `app/config.py:32`; `app/repository.py:84` | Query-embedding model; also filters `hybrid_search` to vectors from that model. | Environment | `BAAI/bge-small-en-v1.5`. | No |
| `GRAPHRAG_EMBEDDING_OFFLINE` | `app/embeddings.py:29` | When `1`, `true` or `yes`, FastEmbed uses local model files only. | `Dockerfile:10` sets `true`. | Unset outside the image. | No |
| `GRAPHRAG_MODEL_CACHE` | `app/embeddings.py:28` | FastEmbed model cache directory. | `Dockerfile:10` sets `/models`. | FastEmbed's default outside the image. | No |
| `HF_HUB_OFFLINE` | `build_embeddings.py:193` sets it to `1`; `prefetch_model.py:28` removes it | Hugging Face hub offline switch: the embedding build runs offline, the prefetch must reach the network. | Set by the scripts. | n/a | No |
| `OWNER_DATABASE_URL` | Not read by code; a shell placeholder in `src/graphrag_runtime/README.md:60` | Owner connection string passed to `load_postgres.py --dsn`. | Operator's shell | Operator supplied. | Yes |

## Ask Atlas: Cloudflare Worker and map ([ask-atlas](chapters/ask-atlas.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `ALLOWED_ORIGIN` | `src/atlas_worker/src/index.js:13`, `:36` | The one browser origin allowed to call `/v1/answer`. | `wrangler.toml:8` | `https://coszo.org`. | No |
| `ANSWER_MODEL` | `index.js:318` | Gemini model for `auto` and for unknown model names. | `wrangler.toml:9` | `gemini-2.5-flash`. | No |
| `ATLAS_API_ORIGIN` | `index.js:414`, `:417` | Base URL of the private Graph-RAG API, an HTTPS Cloudflare Tunnel (`src/atlas_worker/README.md:23`). | `wrangler secret put` (`wrangler.toml:20`); the comment at `wrangler.toml:5-6` calls it a public value. | Required for corpus questions. | Listed as a secret |
| `ATLAS_API_KEY` | `index.js:414`, `:420` | Plain Graph-RAG client key, sent as `x-api-key` to `/v1/context`; its digest must be in `GRAPHRAG_API_KEY_SHA256`. | `wrangler secret put`; `.dev.vars` locally | Required for corpus questions. | Yes |
| `ATLAS_MAP_GATEWAY_ORIGIN` | `index.js:42`, `:48` | Base URL of the live-data gateway for the `/v1/live/*` proxy. | Not in `wrangler.toml`; `.dev.vars` locally (`src/atlas_map/README.md:26-27`). How production sets it is an open question. | Without it, `/v1/live/*` returns 503. | Treat as sensitive |
| `GEMINI_API_KEY` | `index.js:319` | Gemini completions. The key travels as a URL query parameter. | `wrangler secret put`; `.dev.vars` | Needed for Gemini models and `auto`. | Yes |
| `GROQ_API_KEY` | `index.js:256` | Groq completions (`groq-*` models and the `auto` fallback). | `wrangler secret put` | Optional. | Yes |
| `OPENAI_API_KEY` | `index.js:282` | OpenAI completions (`gpt-*` models; local `auto` fallback). | `wrangler secret put`; `.dev.vars` | Optional. | Yes |
| `AUTO_FALLBACK_OPENAI_MODEL` | `index.js:355-357` | Lets `auto` finish on an OpenAI model. | `.dev.vars` only, by design (`index.js:353-354`). | Unset when deployed. | No |
| `OPENROUTER_API_KEY`, `OPENROUTER_FREE_MODEL` | `index.js:268-269`, in a function nothing calls since `14868d7` | Former OpenRouter fallback. | `wrangler.toml:12` (model); secret list (key) | Dead configuration. | Key: yes |
| `TURNSTILE_SECRET` | No code reads it | Planned bot protection (`wrangler.toml:21-22`). | n/a | Unused. | Yes |
| `VITE_ATLAS_ASK` | `src/atlas_map/vite.config.js:7` | Development target of `/api/ask`; `http://127.0.0.1:8788` points it at `wrangler dev` (`vite.config.js:4-5`). | Vite env file in `src/atlas_map/` or the shell | The deployed Worker, `https://rca-atlas.quakehunt.workers.dev`. In development, questions therefore reach the production Worker unless this is set. | No |
| `import.meta.env.PROD` | `src/atlas_map/src/api/gateway.js:5`; `src/atlas_map/src/ask/askApi.js:5` | Production builds call the Worker; development calls the Vite proxy (`/api`, `/api/ask`). | Set by Vite. | n/a | No |
| `ATLAS_WORKER` (constant) | `src/atlas_map/src/api/gateway.js:2` | Production Worker URL. | Hard-coded. | Not configurable. | No |

## Atlas map gateway ([atlas-map-gateway](chapters/atlas-map-gateway.md))

The gateway merges the root `.env` with the process environment (`src/atlas_map_gateway/config.py:37-38`). Its
upstream limits are constants, not environment variables (`config.py:16-21`).

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `ATLAS_BUNDLE_DIR` | `config.py:43` | Folder holding the bundle's `sensors.json`, the allowlist of ids. | Root `.env` or environment | `src/atlas_map/public/atlas`. | No |
| `ATLAS_API_URL` | `config.py:41` | Graph-RAG API base URL; used only by `POST /chat`, which nothing in the repo calls. | Root `.env` | `http://127.0.0.1:<GRAPHRAG_API_PORT>`. | No |
| `ATLAS_API_KEY` | `config.py:42` | Graph-RAG client key for `POST /chat`. | Root `.env` | Falls back to `GRAPHRAG_API_KEY`. | Yes |
| `GRAPHRAG_API_PORT` | `config.py:39` | Port in the default `ATLAS_API_URL`. | Root `.env` | `8000`. | No |
| `EARTHSCOPE_RUNTIME_ROOT` | `src/atlas_map_gateway/toolkits.py:29` | Overwritten with a fresh temporary folder at each start, so waveform downloads stay out of `runtime_data/`. | Set by the gateway. | n/a | No |
| `EARTHSCOPE_TIMEOUT_SECONDS`, `PI_PORTAL_TIMEOUT_SECONDS`, `PI_PORTAL_MAX_RETRIES` | `toolkits.py:22-25` | Shorter timeouts and retries for map requests. | Set by the gateway only when absent. | 8 s, 8 s and 1 retry. | No |

## MCP servers and their toolkits

### QA/QC ([agentic-qaqc](chapters/agentic-qaqc.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `QAQC_DASHBOARD_URL` | `src/agentic_qaqc/mcp_server.py:30` | Dashboard base URL. | MCP client environment | `https://ec2.qaqc.ooi-rca.net`. | No |
| `QAQC_INSTRUMENT_ROOT` | `mcp_server.py:32` | Folder with `instruments.jsonl`. | `run_mcp.sh:7` | `<repo>/data/Instruments`. | No |
| `QAQC_HITL_SNAPSHOT` | `mcp_server.py:33` | Offline fallback for human-in-the-loop notes. | `run_mcp.sh:8` | `<repo>/data/QAQC/graphrag/hitl_snapshot.jsonl`. | No |
| `QAQC_INDEX_CACHE` | `mcp_server.py:31` | Cached plot-index JSON. | `run_mcp.sh:9` | `${TMPDIR:-/tmp}/rcn-agent-qaqc-index.json`. | No |
| `QAQC_PYTHON` | `run_mcp.sh:10` | Interpreter for the server. | MCP client environment | `python3`. | No |
| `QAQC_AGENT_ALLOW_PIPELINE` | `src/agentic_qaqc/qaqc_agent_tools.py:366` | `1` enables running the vendored plot pipeline; with `s3_sync` and no `prefix` that writes to the live bucket. | Root `.env.example:17` lists it empty | Unset: execution disabled. | No |
| `GH_PAT`, `AWS_KEY`, `AWS_SECRET` | Vendored backend: `src/agentic_qaqc/vendor/rca_data_tools/qaqc/scheduler.py:18`, `qaqc/utils.py:37-38` | Credentials of the upstream pipeline; the toolkit's plan names Prefect and AWS credentials for cloud or sync runs (`qaqc_agent_tools.py:362`). | Environment of the pipeline run | Needed only for cloud or S3 runs. | Yes |

### Axial earthquakes ([axial](chapters/axial.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `AXIAL_BASE_URL` | `src/axial_earthquakes/mcp_server.py:25` | Base URL of the UW catalog. | MCP client environment | `http://axial.ocean.washington.edu`. | No |
| `AXIAL_DB_PATH` | `mcp_server.py:26` | SQLite event store for the snapshot fallback. | `run_mcp.sh:5` | `<repo>/runtime_data/AxialEarthquakes/graphrag/events.sqlite`. | No |
| `AXIAL_CACHE_DIR` | `mcp_server.py:27` | HTTP response cache. | MCP client environment | `<OS temp>/rcn-agent-axial-cache`. | No |

The OSU monitoring server (`src/axial_monitoring_website/mcp_server.py`) reads no environment variables.

### Nereus ([corpus-instruments-ops](chapters/corpus-instruments-ops.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `NEREUS_BASE_URL` | `src/nereus_pipeline/mcp_server.py:16` | Nereus origin. | MCP client environment | `https://nereus.ooirsn.uw.edu`. | No |
| `NEREUS_QUERY_DIR` | `mcp_server.py:16` | The allowlisted `.graphql` operations. | `run_mcp.sh:5` | `src/nereus_pipeline/queries`. | No |
| `NEREUS_SNAPSHOT_DIR` | `mcp_server.py:16` | Offline fallback snapshots. | `run_mcp.sh:6` | `<repo>/data/Nereus/graphrag/snapshots`. | No |
| `NEREUS_CACHE_DIR` | `mcp_server.py:16` | Disk cache for live responses. | `run_mcp.sh:7` | `${TMPDIR:-/tmp}/rcn-agent-nereus-cache`. | No |
| `NEREUS_PYTHON` | `run_mcp.sh:8` | Interpreter for the server. | MCP client environment | `python3`. | No |

### COSZO Hub ([coszo-hub-core](chapters/coszo-hub-core.md), [coszo-hub-sources](chapters/coszo-hub-sources.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `COSZO_HUB_REPOSITORY_ROOT` | `src/coszo_hub_tools/mcp_server.py:27` | Directory of the `coszo-hub` repository checkouts. | MCP client environment | `<repo>/source_material/repositories/coszo-hub`. | No |
| `COSZO_HUB_INDEX_PATH` | `mcp_server.py:28` | SQLite output index. | MCP client environment | `<repo>/runtime_data/COSZOHub/output_index.sqlite`. | No |
| `COSZO_HUB_CACHE_DIR` | `mcp_server.py:29` | Cache for rendered Dive Index pages. | MCP client environment | `<repo>/runtime_data/COSZOHub/cache`. | No |
| `COSZO_PRESSURE_OUTPUT_ROOT`, `COSZO_VELOCITY_OUTPUT_ROOT`, `COSZO_CHRONFIX_OUTPUT_ROOT`, `COSZO_DIVE_OUTPUT_ROOT` | `coszo_hub_agent_tools.py:49-75`, `:240` | Live output trees of the PREST, VEL3D, Chronfix and Dive Index pipelines. When the Chronfix root is set, no `git pull` runs (`:490`). | `.env.example:13-16`; production paths in `src/coszo_hub_tools/README.md` | Checkouts under the repository root. | No |
| `COSZO_CHRONFIX_REFRESH_TTL_SECONDS` | `coszo_hub_agent_tools.py:231` | Minimum seconds between Chronfix pulls. | MCP client environment | `300`. | No |
| `COSZO_PYTHON` | `run_mcp.sh:4-5` | Interpreter for the server. If unset, a hard-coded interpreter on the author's machine is tried before `python3` (`run_mcp.sh:6-9`). | MCP client environment | `python3`. | No |
| `OOI_USERNAME`, `OOI_TOKEN` | `src/coszo_hub_tools/ooi_m2m_agent_tools.py`; presence check `coszo_hub_agent_tools.py:795-796` | OOI machine-to-machine (M2M) API credentials for live inventory, deployment, stream and request calls. Never returned by tools. | `.env.example:11-12`; MCP client environment | Required only for live M2M calls. | Yes |
| `OOI_INSTRUMENT_INVENTORY` | `ooi_m2m_agent_tools.py:99` | Local inventory for instrument search. | MCP client environment | `<repo>/data/Instruments/instruments.jsonl`. | No |
| `OOI_M2M_RUNTIME_ROOT`, `OOI_M2M_MAX_REQUEST_DAYS`, `OOI_M2M_MAX_DOWNLOAD_BYTES`, `OOI_M2M_TIMEOUT_SECONDS` | `ooi_m2m_agent_tools.py:98-104` | Download folder and request bounds. | MCP client environment | `runtime_data/OOIM2M`, 31 days, 2 GiB, 30 s. | No |
| `PI_PORTAL_RUNTIME_ROOT`, `PI_PORTAL_MAX_INDEX_BYTES`, `PI_PORTAL_MAX_DOWNLOAD_BYTES`, `PI_PORTAL_MAX_DOWNLOAD_FILES`, `PI_PORTAL_TIMEOUT_SECONDS`, `PI_PORTAL_MAX_RETRIES`, `PI_PORTAL_RETRY_BACKOFF_SECONDS` | `src/coszo_hub_tools/pi_portal_agent_tools.py:304-310` | Download folder and bounds for the PI portal. | MCP client environment; the gateway overrides two | `runtime_data/PIPortal`, 10 MiB, 512 MiB, 10 files, 60 s, 2 retries, 0.5 s. | No |
| `EARTHSCOPE_RUNTIME_ROOT`, `EARTHSCOPE_MAX_REQUEST_HOURS`, `EARTHSCOPE_MAX_DOWNLOAD_BYTES`, `EARTHSCOPE_TIMEOUT_SECONDS` | `src/coszo_hub_tools/earthscope_fdsn_agent_tools.py:77-80` | Download folder and bounds for EarthScope FDSN waveforms. | MCP client environment; the gateway overrides two | `runtime_data/EarthScope`, 24 h, 512 MiB, 120 s. | No |
| `RCN_INSTRUMENT_CORPUS` | `src/coszo_hub_tools/build_pi_portal_graph.py:181` | Instruments file that enriches the PI-portal corpus build. | Builder's shell | `<repo>/data/Instruments/instruments.jsonl`. | No |

### Literature full text ([literature-fulltext](chapters/literature-fulltext.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `LITERATURE_CORPUS_PATH` | `src/literature_fulltext/mcp_server.py:22` | Canonical literature catalog. | `run_mcp.sh:5` | `<repo>/data/Literature/literature.jsonl`. | No |
| `LITERATURE_FULL_TEXT_CACHE_DIR` | `mcp_server.py:23` | Full-text cache root. | `run_mcp.sh:6` | `<repo>/runtime_data/Literature/full_text_cache`. | No |
| `LITERATURE_FULL_TEXT_TIMEOUT` | `mcp_server.py:24` | Socket and `pdftotext` timeout in seconds. | MCP client environment | `35`. | No |
| `LITERATURE_FULL_TEXT_MAX_BYTES` | `mcp_server.py:25` | Byte cap per network response. | MCP client environment | 50 MiB, clamped. | No |
| `LITERATURE_FULL_TEXT_PYTHON` | `run_mcp.sh:7` | Interpreter for the server. | MCP client environment | `python3`. | No |
| `UNPAYWALL_EMAIL` | `mcp_server.py:26`; `literature_fulltext_tools.py:221` | Enables the Unpaywall DOI resolver, which requires a contact email. The value is written into tool `attempts` and acquisition reports (`literature_fulltext_tools.py:506-507`). | MCP client environment; not in `.env.example` | Optional. | Personal data |

## Model Lab ([eval-experiments](chapters/eval-experiments.md))

Keys are looked up by the `api_key_env` field of `src/model_eval/config/providers.json` and
`src/model_eval/config/embedding_indexes.json`, then read with `os.environ.get` (`src/model_eval/providers.py:84`, `:116`,
`:141`, `:174`; `src/model_eval/embeddings.py:42-44`). All are listed in `.env.example:1-10`.

| Name | Purpose | Default or required | Secret |
|---|---|---|---|
| `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `MOONSHOT_API_KEY` | Answer-model providers. | Required for that provider's models (Moonshot sends no header when unset). | Yes |
| `OPENAI_COMPATIBLE_API_KEY` | vLLM, SGLang, Ollama or another OpenAI-compatible server. | Optional. | Yes |
| `OPENAI_COMPATIBLE_BASE_URL` | Would set that server's URL, but no code reads it; the URL is in `providers.json`. | Unused. | No |
| `VOYAGE_API_KEY`, `JINA_API_KEY`, `COHERE_API_KEY` | Candidate embedding indexes. | Required only when that index is embedded. | Yes |

## Release and restore scripts ([repo-ops-data](chapters/repo-ops-data.md))

| Name | Read at | Purpose | Set in | Default or required | Secret |
|---|---|---|---|---|---|
| `GITHUB_REPOSITORY` | `scripts/bootstrap_machine.sh:5` | Repository whose releases to restore; `--repo` overrides it. | Operator's shell | The `origin` remote. | No |
| GitHub CLI login | `gh release download` in `bootstrap_machine.sh` | Access to the private release assets. | `gh auth login` | Required. | Yes (held by `gh`) |

## Known issues

- **Compose may not see the root `.env`.** The graphrag README creates `.env` at the repository root
  (`src/graphrag_runtime/README.md:32`) and runs `docker compose` from `src/graphrag_runtime/`. Docker's
  documentation says Compose reads `.env` from the project directory, which defaults to the Compose file's directory.
  If so, the required `POSTGRES_PASSWORD` and `GRAPHRAG_API_DATABASE_PASSWORD` substitutions fail unless the
  variables are exported or `--env-file ../../.env` is passed. This was not run here: the host has no Compose plugin.
  See [restore-and-run](flows/restore-and-run.md).
- **`src/atlas_worker/.dev.vars` is not gitignored**, although it holds Worker keys and the map README says it is not
  committed (`src/atlas_map/README.md:26`).
- **Historical credentials.** From `833c343` through `c9267e0`, `src/graphrag_runtime/compose.yaml` held a literal
  password for `graphrag_api_role` and a literal API-key digest; `e91311a` replaced them with required variables.
  Rotate them if they were ever used outside local development.
- **A blank `GRAPHRAG_API_PORT`** (as copied from `.env.example`) is not treated as unset by the gateway
  (`config.py:39`), so its default `ATLAS_API_URL` becomes `http://127.0.0.1:`. Compose uses `:-8000` and is unaffected.
- **Keys in URLs and reports.** Both the Worker (`src/atlas_worker/src/index.js:319`) and the Graph-RAG API's answer
  path (`src/graphrag_runtime/app/answering.py:50`) send `GEMINI_API_KEY` as a URL query parameter, where proxies and
  error messages can capture it. The full-text tools write the `UNPAYWALL_EMAIL` value into their attempt logs.
- **The owner password sits in the loader's command line.** `compose.yaml:34` builds the owner connection string from
  `POSTGRES_PASSWORD` into the `loader` command, so container inspection shows it (inferred from Compose behaviour).
- **Dead or unused names**: `OPENAI_COMPATIBLE_BASE_URL`, `TURNSTILE_SECRET`, `OPENROUTER_API_KEY`,
  `OPENROUTER_FREE_MODEL`, and `OWNER_DATABASE_URL` (a README placeholder).
