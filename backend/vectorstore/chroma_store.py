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

def add_document(doc_id: str, text: str, embedding: list):
    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )

def query_similar(embedding: list, top_k: int = 3):
    return collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )
