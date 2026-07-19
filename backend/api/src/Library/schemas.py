from pydantic import BaseModel
from datetime import date

class LibraryBase(BaseModel):
    title: str
    url: str
    category: str
    sub_category: str
    summary: str
    date_created: date

class LibraryCreate(LibraryBase):
    pass

class LibraryResponse(LibraryBase):
    id: int

    class config:
        from_attribute = True

class LibraryUpdate(BaseModel):
    title: str 
    url: str 
    category: str 
    sub_category: str 
    summary: str 
    watched: bool 