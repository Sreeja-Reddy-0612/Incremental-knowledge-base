from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_knowledge_base(request: QueryRequest):
    return {
        "answer": "This is a dummy answer. Semantic search will be added next."
    }
