# 🦊 GitLab Knowledge Assistant

### Hybrid RAG over the GitLab Handbook

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![Qdrant](https://img.shields.io/badge/Vector_Database-Qdrant-DC244C)
![Langfuse](https://img.shields.io/badge/Observability-Langfuse-000000)

Ask questions about GitLab policies, processes, and internal documentation through a retrieval-augmented generation (RAG) API. The assistant combines semantic search, BM25 keyword search, and cross-encoder reranking to supply relevant handbook content to an OpenAI model, then returns an answer with source markers and retrieval diagnostics.

[Overview](#overview) · [Features](#-key-features) · [Architecture](#-system-architecture) · [Setup](#-installation--setup) · [API](#-api-usage) · [Syncing](#-keeping-the-knowledge-base-current)

---

## Overview

The GitLab Handbook contains documentation spread across Markdown pages, YAML files, PDFs, and spreadsheets. This project turns selected parts of that repository into a searchable knowledge base and exposes question answering through FastAPI.

The retrieval pipeline searches for both meaning and exact terms, merges the results using Reciprocal Rank Fusion (RRF), and reranks the candidates before generating an answer. Responses include the retrieved chunks and their metadata so the supporting material can be inspected.

Example questions:

- What is GitLab's parental leave policy, and who is eligible?
- How does GitLab run asynchronous meetings?
- What are the steps in the employee onboarding process?

## ✨ Key Features

### 🔍 Hybrid retrieval and answer generation

- **Semantic search:** OpenAI `text-embedding-3-small` embeddings with cosine similarity in Qdrant.
- **Keyword search:** Local `Qdrant/bm25` sparse embeddings with Qdrant's IDF modifier.
- **Rank fusion:** RRF combines semantic and keyword results while retaining each method's scores and ranks.
- **Cross-encoder reranking:** `Xenova/ms-marco-TinyBERT-L-2-v2` scores the fused candidates against the question.
- **Answers with source markers:** The generation prompt includes retrieved content and metadata and requests citations such as `[S1]` and `[S2]`.

### 📚 Document ingestion and synchronization

- **Multiple formats:** Markdown, YAML, PDF, and Excel ingestion with format-specific processing.
- **Source metadata:** Preserves Markdown frontmatter, PDF page numbers, and spreadsheet sheet names and row ranges.
- **Incremental updates:** Uses Git diffs to identify additions, modifications, and deletions.
- **Resumable runs:** Persists pending work and checkpoints to resume an interrupted ingestion.
- **Verified writes:** Checks source-level chunk counts before acknowledging successful additions or deletions.
- **Stable chunk IDs:** Derives UUIDs from the source, content, location, and repeated-chunk occurrence.
- **Webhook integration:** Accepted GitLab push events schedule synchronization as a background task.

### 📊 Observability

- Langfuse traces for retrieval, reranking, generation, Git synchronization, and ingestion.
- Separate timings for semantic search, BM25, fusion, reranking, and total retrieval.
- Answer request IDs and structured logs containing timings and returned chunk IDs.
- JSON ingestion reports with commit references, file outcomes, chunk counts, and embedding input-token usage.

## 🏗️ System Architecture

```mermaid
flowchart TD
    subgraph Ingestion[Document ingestion]
        A[GitLab Handbook checkout] --> B[Initial scan or Git diff]
        B --> C[Filter supported paths and formats]
        C --> D[Parse documents and preserve metadata]
        D --> E[Create chunks and stable IDs]
        E --> F[OpenAI dense embeddings + local BM25 vectors]
    end

    F --> Q[(Qdrant: gitlab_docs_v1)]

    subgraph Answering[Question answering]
        U[User question] --> API[FastAPI]
        API --> H[Semantic + BM25 search]
        H --> R[Reciprocal Rank Fusion]
        R --> X[TinyBERT cross-encoder reranking]
        X --> P[Context with source markers]
        P --> L[OpenAI answer generation]
        L --> O[Answer + chunks + retrieval timings]
    end

    Q --> H
```

### Retrieval flow

With the default settings, each question follows this sequence:

1. Embed the query and retrieve up to **16 semantic matches** from Qdrant.
2. Generate a local BM25 query vector and retrieve up to **16 keyword matches**.
3. Fuse both ranked lists using RRF and retain up to **8 candidates**.
4. Rerank the candidates with the cross-encoder and select up to **5 chunks**.
5. Pass the question, selected chunks, and metadata to the answer model.
6. Return the generated text, supporting chunks, and retrieval timings.

## 🛠️ Tech Stack

| Component | Technology |
| --- | --- |
| Language | Python 3.10+ |
| API | FastAPI, Pydantic, Uvicorn |
| Answer generation | OpenAI Responses API; `gpt-5.5` configured in the source |
| Dense embeddings | OpenAI `text-embedding-3-small`, 1,536 dimensions |
| Sparse embeddings | FastEmbed `Qdrant/bm25` |
| Vector storage | Qdrant with named `dense` and `bm25` vectors |
| Reranking | FastEmbed `TextCrossEncoder` with TinyBERT |
| Loading and splitting | LangChain document loaders and text splitters |
| Document parsing | Docling, python-frontmatter, PyYAML, openpyxl |
| Tracing | Langfuse |
| Change detection | Git diffs, persisted checkpoints, GitLab webhooks |

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10+ and Git.
- macOS or Linux. Ingestion uses the Unix `fcntl` module; use WSL on Windows.
- Docker for the local Qdrant instance, or an existing Qdrant service at `http://localhost:6333`.
- An OpenAI API key with access to the embedding and answer models configured in the source.
- Langfuse project credentials to collect traces.

Run the following commands from the project root unless stated otherwise.

### 1. Clone the project

```bash
git clone https://github.com/ParamSachdeva07/GitLab-Knowledge-Assistant.git
cd GitLab-Knowledge-Assistant
```

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install \
  fastapi "uvicorn[standard]" openai "qdrant-client==1.19.1" \
  python-dotenv langchain-community langchain-core langchain-text-splitters \
  python-frontmatter "langfuse==4.17.0" openpyxl pyyaml docling
```

`pyproject.toml` currently declares FastEmbed as the core dependency. The second installation command supplies the other runtime libraries imported by the application; the `migration` extra is not a complete application dependency set.

### 3. Configure environment variables

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key

LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

Use the base URL for your Langfuse region or self-hosted instance. See the [Langfuse SDK setup documentation](https://langfuse.com/docs/observability/sdk/overview). The repository already excludes `.env` from Git.

### 4. Start Qdrant

```bash
docker run -d \
  --name gitlab-knowledge-qdrant \
  -p 127.0.0.1:6333:6333 \
  -v gitlab-knowledge-qdrant:/qdrant/storage \
  qdrant/qdrant
```

The named volume persists the index across container restarts. For later sessions, start the existing container with `docker start gitlab-knowledge-qdrant`.

The application creates `gitlab_docs_v1` if it does not exist. Qdrant must be running before ingestion or API startup because the database client connects during module import. See the [Qdrant local quickstart](https://qdrant.tech/documentation/quickstart/) for additional deployment options.

### 5. Clone the GitLab Handbook

```bash
mkdir -p data
git clone --branch main \
  https://gitlab.com/gitlab-com/content-sites/handbook.git \
  data/handbook
```

The ingestion pipeline expects a clean Git checkout at `data/handbook` and synchronizes against `origin/main`.

### 6. Build the initial index

```bash
python - <<'PY'
import json
from langfuse import get_client
from src.chunking.incremental_loader import sync_changes

try:
    report = sync_changes(full_rebuild=True)
    print(json.dumps(report, indent=2))
finally:
    get_client().flush()
PY
```

This scans supported tracked files at the current checkout and establishes the indexed-commit checkpoint. The first index can take time and consumes OpenAI embedding tokens. FastEmbed and Docling may download model assets on first use.

Use `full_rebuild=True` to bootstrap a new collection: an ordinary sync on a fresh checkout only considers changes between that checkout and upstream. A pending run is resumed before a new scan begins.

### 7. Start the API

```bash
python -m uvicorn src.api:app --reload
```

Open the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## 💬 API Usage

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `POST` | `/answer` | Generate an answer and return supporting chunks and retrieval timings. |
| `POST` | `/retrieve_chunks` | Inspect retrieval results without generating an answer. |
| `POST` | `/webhooks/gitlab` | Schedule a sync for an accepted GitLab push event. |

### Ask a question

```bash
curl -X POST http://127.0.0.1:8000/answer \
  -H 'Content-Type: application/json' \
  -d '{"query": "What is GitLab parental leave policy, and who is eligible?", "k": 5}'
```

The answer response contains:

| Field | Contents |
| --- | --- |
| `request_id` | UUID used to correlate the request with application logs. |
| `results.response` | Generated answer text, prompted to include source markers. |
| `results.chunks` | Reranked chunks with IDs, content, source metadata, and retrieval scores. |
| `results.timings_ms` | `semantic`, `bm25`, `rrf`, `reranking`, and `retrieval_total` durations. |

Retrieval timings cover the search pipeline; they do not include answer generation. Chunk order corresponds to the source numbers supplied in the generation context.

### Inspect retrieved chunks

```bash
curl -X POST http://127.0.0.1:8000/retrieve_chunks \
  -H 'Content-Type: application/json' \
  -d '{"query": "employee onboarding checklist", "k": 5}'
```

This returns `results.chunks` and `results.timings_ms`. Both query endpoints accept a nonempty `query` and an optional `k` from `1` to `20`, defaulting to `5`. The retrieval candidate pool currently defaults to `8`, so requests with a larger `k` still return at most eight chunks.

## 🔄 Keeping the Knowledge Base Current

### Manual incremental sync

```bash
python -m src.chunking.incremental_loader
```

The sync fetches `origin/main`, fast-forwards the handbook checkout, and compares the last indexed commit with the target commit. Added files are indexed, modified files have their old chunks replaced, and deleted files have their chunks removed.

The pipeline records pending work before moving the checkout, verifies database changes, and advances the checkpoint after all pending items have been acknowledged. An OS file lock prevents concurrent ingestion runs from proceeding.

### GitLab webhook

Set `PROJECT_ID` in [src/api.py](src/api.py) to the GitLab project ID associated with the handbook checkout; its current value, `123456`, is a placeholder. Configure that project's push webhook to send requests to `/webhooks/gitlab` on your running API.

The handler accepts events when:

- `X-Gitlab-Event` is `Push Hook`.
- The payload's `project.id` matches `PROJECT_ID`.
- The pushed ref is `refs/heads/main`.

An accepted event returns `{"status": "accepted"}` and schedules synchronization using FastAPI background tasks. Completion or failure is recorded separately in logs and ingestion reports. The current handler checks event, project, and branch fields; webhook secret-token validation and API authentication are future improvements.

### Supported sources

Files must be inside `content/`, `data/`, `static/pdfs/`, or `static/files/legal/` in the handbook checkout. Hidden paths and temporary Excel files are excluded.

| Format | Processing | Additional metadata |
| --- | --- | --- |
| `.md` | Extract YAML frontmatter and split Markdown. | Frontmatter fields. |
| `.yaml`, `.yml` | Load as text and split recursively. | Format. |
| `.pdf` | Convert with Docling and split page-level Markdown. | Format and page number. |
| `.xlsx` | Group whole rows with repeated first-row headers. | Format, sheet, start row, end row. |

Every chunk also retains its source path. PDF conversion failures are recorded as skipped files so other files can continue; other preparation errors fail the run and leave pending work for a subsequent attempt.

## 📁 Project Structure

```text
GitLab-Knowledge-Assistant/
├── src/
│   ├── api.py                      # FastAPI endpoints and GitLab webhook
│   ├── db/
│   │   └── client.py                # Qdrant client and collection setup
│   ├── ingestion/
│   │   ├── filter.py                # Supported paths and file types
│   │   └── sync.py                  # Git diffs, fast-forward sync, pending reports
│   ├── chunking/
│   │   ├── loader.py                # Stable chunk IDs, embeddings, Qdrant upserts
│   │   └── incremental_loader.py    # Format parsing and resumable ingestion
│   └── retrieval/
│       ├── top_k_chunks.py          # Semantic search, BM25, RRF, reranking
│       └── response.py              # Generation context and OpenAI response
├── data/
│   ├── handbook/                   # Local handbook checkout; ignored by Git
│   └── ingestion_state/            # Generated checkpoints and run reports; ignored
│       ├── checkpoint.json
│       ├── pending.json            # Present while an ingestion run is pending
│       ├── sync.lock
│       └── runs/
├── .env                            # Local API credentials; ignored by Git
├── .gitignore
├── pyproject.toml
└── README.md
```

## ⚙️ Configuration Reference

These values are currently defined in source files:

| Setting | Default | Location |
| --- | --- | --- |
| Qdrant URL | `http://localhost:6333` | [src/db/client.py](src/db/client.py) |
| Collection | `gitlab_docs_v1` | [src/db/client.py](src/db/client.py) |
| Dense embedding model | `text-embedding-3-small` | [loader.py](src/chunking/loader.py), [top_k_chunks.py](src/retrieval/top_k_chunks.py) |
| Answer model | `gpt-5.5` with reasoning effort `none` | [src/retrieval/response.py](src/retrieval/response.py) |
| Fused candidate count | `8` | [src/retrieval/top_k_chunks.py](src/retrieval/top_k_chunks.py) |
| RRF constant | `60` | [src/retrieval/top_k_chunks.py](src/retrieval/top_k_chunks.py) |
| Embedding batch size | `100` chunks | [src/chunking/loader.py](src/chunking/loader.py) |
| Webhook project ID | `123456` placeholder | [src/api.py](src/api.py) |

The configured answer model must be available to your OpenAI account. If changing the dense embedding model, update both indexing and retrieval and use a collection with the matching vector dimensions.

## 🧭 Future Improvements

- Consolidate runtime dependencies and configuration into the project metadata and environment settings.
- Add retrieval and answer-quality evaluation against a curated handbook question set.
- Add webhook secret validation, API authentication, and a durable ingestion job queue.
- Add automated tests and a CI workflow.
- Add a chat interface with clickable source references.
- Track end-to-end latency and expose generation token usage alongside retrieval diagnostics.

## Author

[Param Sachdeva](https://github.com/ParamSachdeva07)

Built around the public [GitLab Handbook](https://gitlab.com/gitlab-com/content-sites/handbook). This is an independent project and is not an official GitLab product.
