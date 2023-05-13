from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from backend.db.models import User, Customer, Job, Document, Revision, Base
from backend.utils.test_data import test_users, test_customers, test_jobs, test_documents, test_revisions
from backend.utils.utils import ISO8601_now
from os import getcwd


WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\db\\dcv.db'
DATABASE_TYPE: str = 'sqlite'
DBAPI: str = 'pysqlite'


# Create the engine to use as ORM
# The creation of the engine estabilshes a lazy inizialization, since the connection is effectively
# estabilished when the method .connect() (or .execute()) is called
# URL passed to the engine can be a literal string with this format:
# dialect+driver://username:password@host:port/database
# dialect = rdbms name
# driver = driver used to communicate with dialect
# # or it can be a URL object, which is preferred since it escapes automatically special characters such as @
engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}:///{DATABASE_DIR}', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

with Session.begin() as session:
    
    for record in test_users:
        record['created_at'] = ISO8601_now()
        record['updated_at'] = ISO8601_now()    
    
    session.bulk_insert_mappings(mapper=User, mappings=test_users)

    for record in test_customers:
        record['created_at'] = ISO8601_now()
        record['updated_at'] = ISO8601_now()
    
    session.bulk_insert_mappings(mapper=Customer, mappings=test_customers)

    for record in test_jobs:
        record['created_at'] = ISO8601_now()
        record['updated_at'] = ISO8601_now()
    
    session.bulk_insert_mappings(mapper=Job, mappings=test_jobs)

    for record in test_documents:
        record['created_at'] = ISO8601_now()
        record['updated_at'] = ISO8601_now()

    session.bulk_insert_mappings(mapper=Document, mappings=test_documents)   

    for record in test_revisions:
        record['created_at'] = ISO8601_now()
        record['updated_at'] = ISO8601_now()
    
    session.bulk_insert_mappings(mapper=Revision, mappings=test_revisions)

    
    # result = session.query(User).all()
    # print(result)

    # result = session.query(User).filter(User.name.like('M%')).all()
    # print(result)

