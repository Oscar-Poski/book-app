# backend/app/main.py
from fastapi import FastAPI
from app.api.routes.books import router as books_router

app = FastAPI(
    title="My WebApp API",
    description="Backend REST API with FastAPI",
    version="0.1.0",
)

@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

app.include_router(books_router)
