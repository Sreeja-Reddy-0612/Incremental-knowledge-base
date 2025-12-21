from fastapi import APIRouter
from pydantic import BaseModel
from embeddings.embedder import embed_text
from vectorstore.chroma_store import query_similar

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_knowledge_base(request: QueryRequest):
    query_embedding = embed_text(request.question)

    results = query_similar(query_embedding)

    if not results["documents"]:
        return {"answer": "No relevant information found."}

    top_doc = results["documents"][0][0]

    return {
        "answer": top_doc
    }
