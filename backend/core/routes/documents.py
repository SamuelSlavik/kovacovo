from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session

from ..db.documents import db_get_all_documents, db_create_document, db_delete_document, db_get_document, \
    db_update_document
from ..db.databases import get_session
from ..db.models import *
from ..schemas.documents import Document, DocumentInDatabase

documents_route = APIRouter()


@documents_route.get("")
async def retrieve_all_documents(session: Session = Depends(get_session)):
    documents = db_get_all_documents(session)
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found")
    return documents


@documents_route.get("/{document_id}")
async def retrieve_all_documents(document_id: int, session: Session = Depends(get_session)):
    document = db_get_document(document_id, session)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@documents_route.post("/create")
async def create_document(
        title: str = Form(...),
        year: int = Form(...),
        document: UploadFile = File(...),
        session: Session = Depends(get_session)
):
    file_location = f"documents/{document.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(document.file.read())

    # Create the Document object
    new_document = DocumentORM(
        title=title,
        year=year,
        document=file_location
    )
    return db_create_document(new_document, session)


@documents_route.put("/update/{document_id}")
async def update_document(
    document_id: int,
    title: str = Form(...),
    year: int = Form(...),
    document: Optional[UploadFile] = File(None),
    session: Session = Depends(get_session)
):
    # Update document file if provided
    if document is not None:
        file_location = f"documents/{document.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(document.file.read())

    new_document = DocumentORM(
        title=title,
        year=year,
        document=file_location
    )
    return db_update_document(document_id, new_document, session)


@documents_route.delete("/delete/{document_id}")
async def delete_document(document_id: int, session: Session = Depends(get_session)):
    try:
        result = db_delete_document(document_id, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


