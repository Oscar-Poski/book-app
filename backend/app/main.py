# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.books import router as books_router
from app.db.session import engine
from app.db.base import Base

app = FastAPI(
    title="My WebApp API",
    description="Backend REST API with FastAPI",
    version="0.2.0",
)

@app.on_event("startup")
def on_startup():
    # Solo dev; en prod usa Alembic
    Base.metadata.create_all(bind=engine)

@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

app.include_router(books_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)