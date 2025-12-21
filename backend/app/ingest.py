from fastapi import APIRouter
from pydantic import BaseModel
from embeddings.embedder import embed_text
from vectorstore.chroma_store import add_document
import uuid

router = APIRouter()

class IngestRequest(BaseModel):
    text: str

@router.post("/ingest")
def ingest_document(request: IngestRequest):
    if not request.text.strip():
        return {"status": "error", "message": "Empty document"}

    embedding = embed_text(request.text)
    doc_id = str(uuid.uuid4())

    add_document(doc_id, request.text, embedding)

    return {
        "status": "success",
        "doc_id": doc_id,
        "embedding_dim": len(embedding)
    }
