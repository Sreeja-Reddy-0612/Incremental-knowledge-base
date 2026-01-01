import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(
        persist_directory="chroma",
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)

def add_chunks(chunk_ids, texts, embeddings, metadatas):
    collection.add(
        ids=chunk_ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

def query_similar(embedding, top_k: int = 3):
    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    if not results or not results.get("documents") or not results["documents"][0]:
        return None

    return results


def delete_by_doc_id(doc_id: str):
    collection.delete(where={"doc_id": doc_id})



def delete_document(doc_id: str):
    collection.delete(
        where={"doc_id": doc_id}
    )



def update_document(doc_id: str, chunks, embeddings, metadatas, chunk_ids):
    # 1️⃣ delete all old chunks
    collection.delete(where={"doc_id": doc_id})

    # 2️⃣ add updated chunks
    collection.add(
        ids=chunk_ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )
