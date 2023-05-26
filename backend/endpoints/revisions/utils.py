from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from backend.db.models import Revision
from typing import List

def read_revisions(session: Session) -> List[dict] | None:
    revisions = [row.__dict__ for row in session.query(Revision).all()]

    return revisions if len(revisions) > 0 else None

def read_revision_by_id(session: Session, revision_id: int) -> dict | None:
    try:
        return session.query(Revision).filter(Revision.id == revision_id).one().__dict__
    except NoResultFound:
        return None
    
def create_revision(session: Session, revision_dto: dict) -> dict | None:
    
    revision = Revision(**revision_dto)
    session.add(revision)
    session.commit()
    response_body: dict = {'id': revision.id, **revision_dto}
    
    return response_body
