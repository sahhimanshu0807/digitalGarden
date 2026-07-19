from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, AnyHttpUrl
from datetime import date

app = FastAPI()

# library: list[dict] = [
#     {
#         "id": 1,
#         "url": "https://x.com/Freakycinefan/status/2078143484276711524?s=20",
#         "category": "Video",
#         "sub-category": "python",
#         "watched": "No",
#         "summary": "This is supposed to be ai generated if asked by the user.",
#         "date-posted": "2/10/2026",
#     },
#     {
#         "id": 2,
#         "url": "https://x.com/Freakycinefan/status/2078143484276711524?s=20",
#         "category": "Book",
#         "sub-category": "c++",
#         "watched": "No",
#         "summary": "This is supposed to be ai generated if asked by the user.",
#         "date-posted": "2/10/2027",
#     },
# ]

@app.get("/")
def home():
    return {"message" : "Hello, World!"}

# @app.get("/api/library")
# def get_library():
#     return library

# @app.get("/api/library/{item_id}")
# def get_item(item_id: int):
#     for items in library:
#         if(items.get("id") == item_id):
#             return items
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!")