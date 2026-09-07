# Agentic RAG Contract Assistant

Agentic RAG Contract Assistant is a Python service scaffold for ingesting contracts, retrieving relevant clauses, analyzing legal and commercial risk, and preparing follow-up actions for human review.

## Project Structure

```text
agentic-rag-contract-assistant/
├── app/
│   ├── api/
│   ├── ingestion/
│   ├── retrieval/
│   ├── risk_analysis/
│   ├── actions/
│   ├── database/
│   └── main.py
├── data/
│   └── sample_contracts/
├── tests/
├── docs/
├── .env.example
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Local Setup

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Docker Services

```powershell
docker compose up --build
```

The compose file starts the API, Postgres, and Qdrant.

## Initial Endpoints

- `GET /health` returns service status.
- `POST /api/query` accepts a contract question and returns placeholder retrieval, risk, and action outputs.

## Next Implementation Steps

1. Add document parsing and chunking in `app/ingestion`.
2. Persist contract metadata in `app/database`.
3. Store embeddings in Qdrant through `app/retrieval`.
4. Replace deterministic risk checks in `app/risk_analysis` with model-backed analysis.
5. Wire `app/actions` to review queues, email, ticketing, or workflow automation.
