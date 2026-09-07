from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.actions.workflow import build_follow_up_actions
from app.retrieval.retriever import retrieve_contract_context
from app.risk_analysis.analyzer import analyze_contract_risks


router = APIRouter(prefix="/api", tags=["contracts"])


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1)
    contract_id: str | None = None


class QueryResponse(BaseModel):
    answer: str
    retrieved_context: list[str]
    risks: list[str]
    recommended_actions: list[str]


@router.post("/query", response_model=QueryResponse)
def query_contract(request: QueryRequest) -> QueryResponse:
    context = retrieve_contract_context(
        question=request.question,
        contract_id=request.contract_id,
    )
    risks = analyze_contract_risks(context)
    actions = build_follow_up_actions(risks)

    return QueryResponse(
        answer="This scaffold found relevant context and prepared review items.",
        retrieved_context=context,
        risks=risks,
        recommended_actions=actions,
    )
