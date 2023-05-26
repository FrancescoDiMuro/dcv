from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from backend.db.models import Document
from typing import List

def read_documents(session: Session) -> List[dict] | None:
    documents = [row.__dict__ for row in session.query(Document).all()]

    return documents if len(documents) > 0 else None

def read_document_by_id(session: Session, document_id: int) -> dict | None:
    try:
        return session.query(Document).filter(Document.id == document_id).one().__dict__
    except NoResultFound:
        return None
    
def create_document(session: Session, document_dto: dict) -> dict | None:
    
    document = Document(**document_dto)
    session.add(document)
    session.commit()
    response_body: dict = {'id': document.id, **document_dto}
    
    return response_body
