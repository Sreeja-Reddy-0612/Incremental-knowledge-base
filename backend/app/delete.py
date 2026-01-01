from fastapi import APIRouter
from pydantic import BaseModel
from vectorstore.chroma_store import delete_by_doc_id

router = APIRouter()

class DeleteRequest(BaseModel):
    doc_id: str

@router.post("/delete")
def delete_doc(req: DeleteRequest):
    delete_by_doc_id(req.doc_id)
    return {"status": "deleted"}
