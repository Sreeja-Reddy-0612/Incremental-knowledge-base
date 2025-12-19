from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Simple in-memory store (temporary)
DOCUMENT_STORE = []

class IngestRequest(BaseModel):
    text: str

@router.post("/ingest")
def ingest_document(request: IngestRequest):
    if not request.text.strip():
        return {"status": "error", "message": "Empty document"}

    DOCUMENT_STORE.append(request.text)

    return {
        "status": "success",
        "documents_ingested": len(DOCUMENT_STORE)
    }
