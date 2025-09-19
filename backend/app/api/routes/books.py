# backend/app/api/routes/books.py
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session

from app.schemas.book import Book, BookCreate, BookUpdate
from app.db.deps import get_db
from app.db.models.book import BookORM

router = APIRouter(prefix="/api/v1/books", tags=["books"])

@router.get("/", response_model=List[Book])
def list_books(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)) -> List[Book]:
    rows = db.query(BookORM).limit(limit).offset(offset).all()
    # Mapea ORM -> schema
    return [Book(
        id=row.id,
        title=row.title,
        author=row.author,
        pages=row.pages,
        rating=row.rating,
        notes=row.notes
    ) for row in rows]

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate, db: Session = Depends(get_db)) -> Book:
    row = BookORM(
        title=payload.title,
        author=payload.author,
        pages=payload.pages,
        rating=payload.rating,
        notes=payload.notes,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return Book(
        id=row.id,
        title=row.title,
        author=row.author,
        pages=row.pages,
        rating=row.rating,
        notes=row.notes
    )

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: UUID, db: Session = Depends(get_db)) -> Book:
    row = db.get(BookORM, book_id)
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    return Book(
        id=row.id,
        title=row.title,
        author=row.author,
        pages=row.pages,
        rating=row.rating,
        notes=row.notes
    )

@router.put("/{book_id}", response_model=Book)
def replace_book(book_id: UUID, payload: BookCreate, db: Session = Depends(get_db)) -> Book:
    row = db.get(BookORM, book_id)
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    row.title = payload.title
    row.author = payload.author
    row.pages = payload.pages
    row.rating = payload.rating
    row.notes = payload.notes
    db.commit()
    db.refresh(row)
    return Book(
        id=row.id, title=row.title, author=row.author,
        pages=row.pages, rating=row.rating, notes=row.notes
    )

@router.patch("/{book_id}", response_model=Book)
def update_book(book_id: UUID, payload: BookUpdate, db: Session = Depends(get_db)) -> Book:
    row = db.get(BookORM, book_id)
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(row, k, v)
    db.commit()
    db.refresh(row)
    return Book(
        id=row.id, title=row.title, author=row.author,
        pages=row.pages, rating=row.rating, notes=row.notes
    )

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: UUID, db: Session = Depends(get_db)) -> None:
    row = db.get(BookORM, book_id)
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(row)
    db.commit()
    return None
