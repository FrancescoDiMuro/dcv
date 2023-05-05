import sqlite3

from fastapi import FastAPI, HTTPException
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from os import getcwd
from typing import List

from backend.schemas.dto import Customer, Job, Document, Revision, User

from backend.utils.customers_utils import (u_get_customers, 
                                           u_get_customer_by_id, 
                                           u_create_customer)

from backend.utils.jobs_utils import (u_get_jobs, 
                                      u_get_job_by_id, 
                                      u_create_job)

from backend.utils.documents_utils import (u_get_documents, 
                                           u_get_document_by_id, 
                                           u_create_document)

from backend.utils.revisions_utils import (u_get_revisions, 
                                           u_get_revision_by_id, 
                                           u_create_revision)

from backend.utils.users_utils import (u_get_users, 
                                       u_get_user_by_id,
                                       u_create_user)

from backend.utils.utils import ISO8601_now

# Constants declaration and initialization
WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'
TEMPLATES_DIR = f'{WORKING_DIR}\\frontend\\static\\templates'


# Templates object to use templates in the app
# templates = Jinja2Templates(directory=TEMPLATES_DIR)

# ----- FastAPI App -----

# App creation
app = FastAPI()

# Mounting static files directory in order to link web pages to each other
# app.mount("/static", StaticFiles(directory="frontend/static/templates"), name="static")

# ----- Endpoints configuration -----
# Root
@app.get('/')
async def root() -> dict:
    return {'message': 'Root'}
   

# GET /customers
@app.get('/customers', description='Get list of configured Customers')
async def get_customers() -> List[Customer] | object:
    customers = u_get_customers()
    return customers if customers is not None else HTTPException(204)


# GET /customers/{customer_id}
@app.get('/customers/{customer_id}', description='Get a Customer by its id')
async def get_customer_by_id(customer_id: int) -> Customer | object:
    customer = u_get_customer_by_id(customer_id=customer_id)    
    return customer if customer is not None else HTTPException(204)


# POST /customers
@app.post('/customers', description='Creates a new Customer', response_model=Customer)
async def post_customer(customer: Customer) -> Customer | object:    
    customer.created_at = ISO8601_now()
    customer.updated_at = ISO8601_now()
    customer_dict = customer.dict()
    entity = u_create_customer(customer_dict)
    return entity if isinstance(entity, Customer) else HTTPException(409)


# PATCH /customers
@app.patch('/customers/{customer_id}')
async def delete_customer(customer_id: int):
    with sqlite3.connect(DATABASE_DIR) as connection:
    
        customer: dict = u_get_customer_by_id(customer_id).dict(exclude_unset=True)

        customer['deleted_at'] = ISO8601_now()

        return customer

        
# GET /jobs
@app.get('/jobs', description='Get list of configured Jobs')
async def get_jobs() -> List[Job] | object:
    jobs = u_get_jobs()
    return jobs if jobs is not None else HTTPException(204)


# GET /jobs/{job_id}
@app.get('/jobs/{job_id}', description='Get a Job by its id')
async def get_job_by_id(job_id: int) -> Job | object:
    job = u_get_job_by_id(job_id=job_id)    
    return job if job is not None else HTTPException(204)


# POST /jobs
@app.post('/jobs', description='Creates a new Job', response_model=Job)
async def post_job(job: Job) -> Job | object:    
    job.created_at = ISO8601_now()
    job.updated_at = ISO8601_now()
    job_dict = job.dict() 
    entity = u_create_job(job_dict)
    return entity if isinstance(entity, Job) else HTTPException(409)
    

# GET /documents
@app.get('/documents', description='Get list of configured Documents')
async def get_documents() -> List[Document] | object:
    documents = u_get_documents()
    return documents if documents is not None else HTTPException(204)


# GET /documents/{document_id}
@app.get('/documents/{document_id}', description='Get a Document by its id')
async def get_document_by_id(document_id: int) -> Document | object:
    document = u_get_document_by_id(document_id=document_id)
    return document if document is not None else HTTPException(204)


# POST /documents
@app.post('/documents', description='Creates a new Document', response_model=Document)
async def post_document(document: Document) -> Document | object:    
    document.created_at = ISO8601_now()
    document.updated_at = ISO8601_now()
    document_dict = document.dict() 
    entity = u_create_document(document_dict)
    return entity if isinstance(entity, Document) else HTTPException(409)
    

# GET /revisions
@app.get('/revisions', description='Get list of configured Revisions')
async def get_revisions() -> List[Revision] | object:
    revisions = u_get_revisions()
    return revisions if revisions is not None else HTTPException(204)


# GET /revisions/{revision_id}
@app.get('/revisions/{revision_id}', description='Get a Revision by its id')
async def get_revision_by_id(revision_id: int) -> Revision | object:
    revision = u_get_revision_by_id(revision_id=revision_id)
    return revision if revision is not None else HTTPException(204)


# POST /revisions
@app.post('/revisions', description='Creates a new Revision', response_model=Revision)
async def post_revision(revision: Revision) -> Revision | object:    
    revision.created_at = ISO8601_now()
    revision.updated_at = ISO8601_now()
    revision_dict = revision.dict() 
    entity = u_create_revision(revision_dict)
    return entity if isinstance(entity, Revision) else HTTPException(409)
    

# GET /users
@app.get('/users', description='Get list of configured Users')
async def get_users() -> List[User] | object:
    users = u_get_users()
    return users if users is not None else HTTPException(204)


# GET /users/{user_id}
@app.get('/users/{user_id}', description='Get a User by its id')
async def get_user_by_id(user_id: int) -> User | object:
    user = u_get_user_by_id(user_id=user_id)
    
    return user if user is not None else HTTPException(204)


# POST /users
@app.post('/users', description='Creates a new User', response_model=User)
async def post_user(user: User) -> User | object:    
    user.created_at = ISO8601_now()
    user.updated_at = ISO8601_now()
    user.access_level_id = 1  # For future use
    user_dict = user.dict()
    entity = u_create_user(user_dict)
    return entity if isinstance(entity, User) else HTTPException(409)
    