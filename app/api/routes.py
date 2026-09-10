from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel, Field

from app.actions.workflow import build_follow_up_actions
from app.ingestion.uploads import MAX_UPLOAD_BYTES, validate_contract_upload
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


class UploadContractResponse(BaseModel):
    filename: str
    file_type: str
    content_type: str | None
    size_bytes: int
    max_size_bytes: int
    status: str


@router.post("/contracts/upload", response_model=UploadContractResponse)
async def upload_contract(file: UploadFile = File(...)) -> UploadContractResponse:
    upload = await validate_contract_upload(file)

    return UploadContractResponse(
        filename=upload.filename,
        file_type=upload.file_type,
        content_type=upload.content_type,
        size_bytes=upload.size_bytes,
        max_size_bytes=MAX_UPLOAD_BYTES,
        status="accepted",
    )


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
