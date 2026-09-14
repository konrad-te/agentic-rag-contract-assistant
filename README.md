# Agentic RAG Contract Assistant

Agentic RAG Contract Assistant is an AI-powered contract analysis assistant that helps users understand contracts faster. It is designed to make long, technical agreements easier to explore by combining document management, semantic search, question answering, and contract-risk analysis.

The application is not intended to replace a lawyer or make final legal decisions. Its purpose is to provide a useful first analysis, highlight clauses that deserve attention, and help users locate the original contract passages behind an answer.

## What It Does

A user uploads a contract, and the system should process it through several stages:

1. Read and process the uploaded document.
2. Divide the contract into smaller, meaningful sections.
3. Store the contract and its basic metadata.
4. Convert contract text into embeddings for semantic search.
5. Let users ask natural-language questions about the contract.
6. Identify potentially risky clauses and explain why they may matter.

Example questions include:

- What are the termination conditions?
- Is there an automatic renewal clause?
- What penalties can be charged?
- Who is responsible if something goes wrong?
- Are there unusual payment terms?

## Problem It Solves

Contracts are often long, technical, and time-consuming to review. Important obligations, deadlines, penalties, and risk terms can be hidden across many pages. This assistant helps users perform an initial review more quickly by finding relevant sections, explaining them in plain language, and pointing back to the source text.

## Intended Users

- Small businesses reviewing supplier or customer contracts
- Employees trying to understand employment agreements
- Project managers checking obligations and deadlines
- Legal teams performing an initial contract review
- Anyone comparing multiple agreements

## Example Scenario

A company uploads a 30-page supplier agreement. The assistant finds a clause allowing automatic renewal, identifies a large late-payment penalty, and shows the sections describing how the agreement can be terminated. The user can then examine those exact passages or take them to a lawyer.

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Docker Services

```bash
docker compose up --build
```

The compose file starts the API, Postgres, and Qdrant.