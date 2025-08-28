# backend/app/api/routes/books.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID

from app.schemas.book import Book, BookCreate, BookUpdate

router = APIRouter(prefix="/api/v1/books", tags=["books"])

# Simple in-memory "DB"
BOOKS: dict[UUID, Book] = {}

@router.get("/", response_model=List[Book])
def list_books() -> List[Book]:
    return list(BOOKS.values())

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate) -> Book:
    book = Book(**payload.dict())
    BOOKS[book.id] = book
    return book

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: UUID) -> Book:
    book = BOOKS.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book)
def replace_book(book_id: UUID, payload: BookCreate) -> Book:
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="Book not found")
    new_book = Book(id=book_id, **payload.dict())
    BOOKS[book_id] = new_book
    return new_book

@router.patch("/{book_id}", response_model=Book)
def update_book(book_id: UUID, payload: BookUpdate) -> Book:
    book = BOOKS.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    updated = book.copy(update=payload.dict(exclude_unset=True))
    BOOKS[book_id] = updated
    return updated

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: UUID) -> None:
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="Book not found")
    del BOOKS[book_id]
    return None
