from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, AnyHttpUrl
from datetime import date

app = FastAPI()

class LibraryItem(BaseModel):
    id: str
    url: AnyHttpUrl
    category: str
    sub_category: str
    watched: bool
    summary: str
    date_created: date


library: list[dict] = [
    {
        "id": 1,
        "url": "https://x.com/Freakycinefan/status/2078143484276711524?s=20",
        "category": "Video",
        "sub-category": "python",
        "watched": "No",
        "summary": "This is supposed to be ai generated if asked by the user.",
        "date-posted": "2/10/2026",
    },
    {
        "id": 2,
        "url": "https://x.com/Freakycinefan/status/2078143484276711524?s=20",
        "category": "Book",
        "sub-category": "c++",
        "watched": "No",
        "summary": "This is supposed to be ai generated if asked by the user.",
        "date-posted": "2/10/2027",
    },
]

@app.get("/")
def home():
    return {"message" : "Hello, World!"}

@app.get("/api/library")
def get_library():
    return library