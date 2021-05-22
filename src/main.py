from fastapi import FastAPI
from pydantic import BaseModel
from models import document

app = FastAPI()

class User(BaseModel):
    microsoft_id: str

class Document(BaseModel):
    id: int
    title: str
    agenda: str
    content: str
    preview_img: str  # base64 image data
    stakeholders: List[User]



@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/document/{id}")
async def get_document(id: int):
    doc = document.get_document(id)
    del doc['_id']
    return doc

@app.post("/document/{id}")
async def post_document(id: int, doc: Document):
    document.set_document(id, doc.dict())
    return {"status": 200}
