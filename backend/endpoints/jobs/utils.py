from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from backend.db.models import Job
from typing import List

def read_jobs(session: Session) -> List[dict] | None:
    jobs = [row.__dict__ for row in session.query(Job).all()]

    return jobs if len(jobs) > 0 else None

def read_job_by_id(session: Session, job_id: int) -> dict | None:
    try:
        return session.query(Job).filter(Job.id == job_id).one().__dict__
    except NoResultFound:
        return None
    
def create_job(session: Session, job_dto: dict) -> dict | None:
    
    job = Job(**job_dto)
    session.add(job)
    session.commit()
    response_body: dict = {'id': job.id, **job_dto}
    
    return response_body
