from fastapi import APIRouter
from pydantic import BaseModel
from embeddings.embedder import embed_text

router = APIRouter()

DOCUMENT_STORE = []

class IngestRequest(BaseModel):
    text: str

@router.post("/ingest")
def ingest_document(request: IngestRequest):
    if not request.text.strip():
        return {"status": "error", "message": "Empty document"}

    embedding = embed_text(request.text)

    DOCUMENT_STORE.append({
        "text": request.text,
        "embedding": embedding
    })

    return {
        "status": "success",
        "embedding_dim": len(embedding),
        "documents_ingested": len(DOCUMENT_STORE)
    }
