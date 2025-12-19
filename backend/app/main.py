from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.ingest import router as ingest_router
from app.query import router as query_router

# Create FastAPI app
app = FastAPI(title="Incremental Knowledge Base Backend")
app.include_router(ingest_router)
app.include_router(query_router)

# Allow frontend (Vite runs on 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
