from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from app.models import Book
from app.scheemas import BookCreate
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
import uuid


router = APIRouter()
books = []

@router.post("/books/")
def book_create(book_form: BookCreate):
    id = uuid.uuid4()
    book = Book(id=id, name=book_form.name, autor=book_form.autor, count_page=book_form.count_page)
    books.append(book)
    return {"book": book.name, "message": "Book was added to list successfully"}

@router.put("/books/{book_id}")
def book_refresh(book_id:int , book_refrash : BookCreate):
    new_book = Book(id = book_id, name=book_refrash.name, autor=book_refrash.autor, count_page=book_refrash.count_page)
    if book in books :
        book = new_book
        return {"book": book.name,"all books count":len(books), "message": "Book was added to list successfully"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@router.get("/books")
def get_books(request: Request):
    return books

@router.get("/books/{book_id}")
async def get_book(book_id: int, request: Request):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

@router.post("/books/{book_id}")
async def delete_boock(book_id: int):
    global books
    books = [book for book in books if book.id != book_id]
    return {"message": "Book deleted"}

@router.get("/books/{book_id}/show")
async def show_book(book_id: int):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

