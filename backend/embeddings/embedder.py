from sentence_transformers import SentenceTransformer

# Load once (important for performance)
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str):
    """
    Convert text into a vector embedding.
    """
    return _model.encode(text).tolist()
