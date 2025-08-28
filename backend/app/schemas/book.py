# backend/app/schemas/book.py
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=200)
    pages: Optional[int] = Field(None, ge=1)
    rating: Optional[float] = Field(None, ge=0, le=5)
    notes: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=200)
    pages: Optional[int] = Field(None, ge=1)
    rating: Optional[float] = Field(None, ge=0, le=5)
    notes: Optional[str] = None

class Book(BookBase):
    id: UUID = Field(default_factory=uuid4)
