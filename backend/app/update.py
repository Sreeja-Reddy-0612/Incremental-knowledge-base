from fastapi import APIRouter
from pydantic import BaseModel
from embeddings.embedder import embed_text
from utils.chunker import chunk_text
from vectorstore.chroma_store import update_document

router = APIRouter()

class UpdateRequest(BaseModel):
    doc_id: str
    text: str

@router.post("/update")
def update_doc(req: UpdateRequest):
    chunks = chunk_text(req.text)
    embeddings = [embed_text(c) for c in chunks]

    metadatas = [
        {"doc_id": req.doc_id, "chunk_index": i}
        for i in range(len(chunks))
    ]

    chunk_ids = [f"{req.doc_id}_{i}" for i in range(len(chunks))]

    update_document(req.doc_id, chunks, embeddings, metadatas, chunk_ids)

    return {"status": "updated"}
