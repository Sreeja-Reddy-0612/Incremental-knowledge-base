from fastapi import APIRouter
from pydantic import BaseModel
from embeddings.embedder import embed_text
from vectorstore.chroma_store import add_chunks
from utils.chunker import chunk_text
import uuid

router = APIRouter()

class IngestRequest(BaseModel):
    text: str

@router.post("/ingest")
def ingest_document(request: IngestRequest):
    if not request.text.strip():
        return {"status": "error", "message": "Empty document"}

    doc_id = str(uuid.uuid4())

    chunks = chunk_text(request.text)

    chunk_ids = []
    chunk_texts = []
    embeddings = []
    metadatas = []

    for idx, chunk in enumerate(chunks):
        chunk_id = f"{doc_id}_chunk_{idx}"

        chunk_ids.append(chunk_id)
        chunk_texts.append(chunk)
        embeddings.append(embed_text(chunk))
        metadatas.append({
            "doc_id": doc_id,
            "chunk_index": idx
        })

    add_chunks(chunk_ids, chunk_texts, embeddings, metadatas)

    return {
        "status": "success",
        "doc_id": doc_id,
        "chunks_ingested": len(chunks)
    }
