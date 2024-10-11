from pydantic import BaseModel
from fastapi import FastAPI, Query

class BookCreate(BaseModel):
    name: str
    autor: str = Query(min_length=3, max_length=30,)
    count_page: int = Query(ge = 10)
    