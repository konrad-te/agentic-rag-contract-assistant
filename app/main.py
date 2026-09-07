from fastapi import FastAPI

from app.api.routes import router as api_router


app = FastAPI(
    title="Agentic RAG Contract Assistant",
    version="0.1.0",
    description="Contract ingestion, retrieval, risk analysis, and action orchestration API.",
)

app.include_router(api_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
