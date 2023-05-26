from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from backend.db.models import Customer
from typing import List

def read_customers(session: Session) -> List[dict] | None:
    customers = [row.__dict__ for row in session.query(Customer).all()]

    return customers if len(customers) > 0 else None

def read_customer_by_id(session: Session, customer_id: int) -> dict | None:
    try:
        return session.query(Customer).filter(Customer.id == customer_id).one().__dict__
    except NoResultFound:
        return None
    
def create_customer(session: Session, customer_dto: dict) -> dict | None:
    
    customer = Customer(**customer_dto)
    session.add(customer)
    session.commit()
    response_body: dict = {'id': customer.id, **customer_dto}
    
    return response_body
