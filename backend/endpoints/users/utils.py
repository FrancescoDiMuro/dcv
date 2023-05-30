from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from backend.db.models import User
from typing import List

def read_users(session: User) -> List[dict] | None:
    users = [row.__dict__ for row in session.query(User).all()]

    return users if len(users) > 0 else None

def read_user_by_id(session: Session, user_id: int) -> dict | None:
    try:
        return session.query(User).filter(User.id == user_id).one().__dict__
    except NoResultFound:
        return None
    
def create_user(session: Session, user_dto: dict) -> dict | None:
    
    print(user_dto['username'])

    user = User(**user_dto)
    session.add(user)
    session.commit()
    response_body: dict = {'id': user.id, **user_dto}
    
    return response_body
