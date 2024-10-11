from pydantic import BaseModel ,UUID4

class Book(BaseModel):
    id: UUID4
    name: str
    autor: str
    count_page: int
    