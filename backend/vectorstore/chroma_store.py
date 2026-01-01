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
    return collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )
