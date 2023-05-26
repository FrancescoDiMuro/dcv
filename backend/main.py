from fastapi import FastAPI, HTTPException
from os import getcwd
from typing import List

from backend.db.dto import Customer, Job, Document, Revision, User

from backend.utils.utils import ISO8601_now

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from backend.db.models import Base
from backend.endpoints.customers.utils import read_customers, read_customer_by_id, create_customer
from backend.endpoints.jobs.utils import read_jobs, read_job_by_id, create_job
from backend.endpoints.documents.utils import read_documents, read_document_by_id, create_document
from backend.endpoints.revisions.utils import read_revisions, read_revision_by_id, create_revision
from backend.endpoints.users.utils import read_users, read_user_by_id, create_user

# Constants declaration and initialization
WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\db\\dcv.db'
DATABASE_TYPE: str = 'sqlite'
DBAPI: str = 'pysqlite'

engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}:///{DATABASE_DIR}', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

with Session.begin() as session:

    # ----- FastAPI App -----

    # App creation
    app = FastAPI()

# ----- Endpoints configuration -----
# Root
@app.get('/')
async def root() -> dict:
    return {'message': 'Root'}
   

# GET /customers
@app.get('/customers', description='Get list of configured Customers')
async def get_customers() -> List[Customer] | object:
    customers = [Customer(**d) for d in read_customers(session=session)]
    return customers if customers is not None else HTTPException(204)

# GET /customers/{customer_id}
@app.get('/customers/{customer_id}', description='Get a Customer by its id')
async def get_customer_by_id(customer_id: int) -> Customer | object:
    customer = read_customer_by_id(session=session, customer_id=customer_id)    
    return customer if customer is not None else HTTPException(204)


# POST /customers
@app.post('/customers', description='Creates a new Customer', response_model=Customer)
async def post_customer(customer: Customer) -> Customer | object:    
    customer.created_at = ISO8601_now()
    customer.updated_at = ISO8601_now()
    customer_dto = customer.dict()
    customer_dto.pop('id')
    entity = Customer(**create_customer(session=session, customer_dto=customer_dto))
    return entity if isinstance(entity, Customer) else HTTPException(409)

       
# GET /jobs
@app.get('/jobs', description='Get list of configured Jobs')
async def get_jobs() -> List[Job] | object:
    jobs = [Job(**d) for d in read_jobs(session=session)]
    return jobs if jobs is not None else HTTPException(204)


# GET /jobs/{job_id}
@app.get('/jobs/{job_id}', description='Get a Job by its id')
async def get_job_by_id(job_id: int) -> Job | object:
    job = read_job_by_id(session=session, job_id=job_id)    
    return job if job is not None else HTTPException(204)


# POST /jobs
@app.post('/jobs', description='Creates a new Job', response_model=Job)
async def post_job(job: Job) -> Job | object:    
    job.created_at = ISO8601_now()
    job.updated_at = ISO8601_now()
    job_dto = job.dict()
    job_dto.pop('id')
    entity = Job(**create_job(session=session, job_dto=job_dto))
    return entity if isinstance(entity, Job) else HTTPException(409)
    

# GET /documents
@app.get('/documents', description='Get list of configured Documents')
async def get_documents() -> List[Document] | object:
    documents = [Document(**d) for d in read_documents(session=session)]
    return documents if documents is not None else HTTPException(204)


# GET /documents/{document_id}
@app.get('/documents/{document_id}', description='Get a Document by its id')
async def get_document_by_id(document_id: int) -> Document | object:
    document = read_document_by_id(session=session, document_id=document_id)    
    return document if document is not None else HTTPException(204)


# POST /documents
@app.post('/documents', description='Creates a new Document', response_model=Document)
async def post_document(document: Document) -> Document | object:    
    document.created_at = ISO8601_now()
    document.updated_at = ISO8601_now()
    document_dto = document.dict()
    document_dto.pop('id')
    entity = Document(**create_document(session=session, document_dto=document_dto))
    return entity if isinstance(entity, Document) else HTTPException(409)


# GET /revisions
@app.get('/revisions', description='Get list of configured Revisions')
async def get_revisions() -> List[Revision] | object:
    revisions = [Revision(**d) for d in read_revisions(session=session)]
    return revisions if revisions is not None else HTTPException(204)


# GET /revisions/{revision_id}
@app.get('/revisions/{revision_id}', description='Get a Revision by its id')
async def get_revision_by_id(revision_id: int) -> Revision | object:
    revision = read_revision_by_id(session=session, revision_id=revision_id)    
    return revision if revision is not None else HTTPException(204)


# POST /revisions
@app.post('/revisions', description='Creates a new Revision', response_model=Revision)
async def post_revision(revision: Revision) -> Revision | object:    
    revision.created_at = ISO8601_now()
    revision.updated_at = ISO8601_now()
    revision_dto = revision.dict()
    revision_dto.pop('id')
    entity = Revision(**create_revision(session=session, revision_dto=revision_dto))
    return entity if isinstance(entity, Revision) else HTTPException(409)
    

# GET /users
@app.get('/users', description='Get list of configured Users')
async def get_users() -> List[User] | object:
    users = [User(**d) for d in read_users(session=session)]
    return users if users is not None else HTTPException(204)


# GET /users/{user_id}
@app.get('/users/{user_id}', description='Get a User by its id')
async def get_user_by_id(user_id: int) -> User | object:
    user = read_user_by_id(session=session, user_id=user_id)    
    return user if user is not None else HTTPException(204)


# POST /users
@app.post('/users', description='Creates a new User', response_model=User)
async def post_user(user: User) -> User | object:    
    user.created_at = ISO8601_now()
    user.updated_at = ISO8601_now()
    user_dto = user.dict()
    user_dto.pop('id')
    entity = User(**create_user(session=session, user_dto=user_dto))
    return entity if isinstance(entity, User) else HTTPException(409)
    