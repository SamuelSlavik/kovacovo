import os

from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import DocumentORM
from ..config import config
from ..schemas.documents import Document, DocumentInDatabase


def db_get_all_documents(db: Session):
    return db.query(DocumentORM).all()


def db_get_document(document_id, db: Session):
    return db.query(DocumentORM).filter(DocumentORM.id == document_id).first()


def db_create_document(document: DocumentORM, db: Session):
    new_document = DocumentORM(
        title=document.title,
        year=document.year,
        document=document.document
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return DocumentInDatabase(
        id=new_document.id,
        title=new_document.title,
        year=new_document.year,
        document=new_document.document
    )


def db_delete_document(id: int, db: Session):
    document = db.query(DocumentORM).filter(DocumentORM.id == id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

        # Delete file from the directory
    file_path = document.document  # Assuming document_path stores the file path
    if os.path.exists(file_path):
        os.remove(file_path)

    db.delete(document)
    db.commit()
    return {"message": "Document deleted successfully"}


def db_update_document(document_id, document, session: Session):
    # Check if the document exists in the database
    existing_document = session.query(DocumentORM).filter(DocumentORM.id == document_id).first()
    if not existing_document:
        raise HTTPException(status_code=404, detail="Document not found")

    # Update document attributes if provided
    if document.title:
        existing_document.title = document.title
    if document.year:
        existing_document.year = document.year
    if document.document:
        existing_document.document = document.document

    # Commit changes to the database
    session.commit()

    return {"message": "Document updated successfully", "document_id": document_id}