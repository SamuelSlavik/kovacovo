from fastapi import UploadFile
from pydantic import BaseModel


class Document(BaseModel):
    title: str
    year: int
    document: str


class DocumentInDatabase(Document):
    id: int
