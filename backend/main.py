import sqlite3

from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from os import getcwd
from typing import List

from backend.schemas.dto import Customer, Job, Document, Revision, User

from backend.utils.customers_utils import u_get_customers, u_get_customer_by_id
from backend.utils.jobs_utils import u_get_jobs, u_get_job_by_id
from backend.utils.documents_utils import u_get_documents, u_get_document_by_id
from backend.utils.revisions_utils import u_get_revisions, u_get_revision_by_id
from backend.utils.users_utils import u_get_users, u_get_user_by_id

from backend.utils.utils import ISO8601_now

# Constants declaration and initialization
WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'
TEMPLATES_DIR = f'{WORKING_DIR}\\frontend\\static\\templates'


# Templates object to use templates in the app
templates = Jinja2Templates(directory=TEMPLATES_DIR)

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
async def post_customer(customer_name: str = Form(...)) -> Customer:
    
    # Settings created_at and updated_at timestamps
    created_at = updated_at = ISO8601_now()
    
    # Creation of Customer
    customer = Customer(name=customer_name,
                        created_at=created_at,
                        updated_at=updated_at)
    
    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
    
        sql_query = '''INSERT INTO Customers (name, created_at, updated_at)
                        VALUES (:name, :created_at, :updated_at)'''
        
        # Execution of the INSERT query
        connection.execute(sql_query, customer.dict())

    return customer


# PATCH /customers
@app.patch('/customers/{customer_id}')
async def delete_customer(customer_id: int):
    with sqlite3.connect(DATABASE_DIR) as connection:
    
        customer: dict = u_get_customer_by_id(customer_id).dict(exclude_unset=True)

        customer['deleted_at'] = ISO8601_now()

        return customer

        
# GET /jobs
@app.get('/jobs', description='Get list of configured Jobs')
async def get_jobs() -> List[Job]:
    jobs = u_get_jobs()
    return jobs


# GET /jobs/{job_id}
@app.get('/jobs/{job_id}', description='Get a Job by its id')
async def get_job_by_id(job_id: int) -> Job:
    job = u_get_job_by_id(job_id=job_id)
    return job
    

# GET /documents
@app.get('/documents', description='Get list of configured Documents')
async def get_documents() -> List[Document]:
    documents = u_get_documents()
    return documents


# GET /documents/{document_id}
@app.get('/documents/{document_id}', description='Get a Document by its id')
async def get_document_by_id(document_id: int) -> Document:
    document = u_get_document_by_id(document_id=document_id)
    return document
    

# GET /revisions
@app.get('/revisions', description='Get list of configured Revisions')
async def get_revisions() -> List[Revision]:
    revisions = u_get_revisions()
    return revisions


# GET /revisions/{revision_id}
@app.get('/revisions/{revision_id}', description='Get a Revision by its id')
async def get_revision_by_id(revision_id: int) -> Revision:
    revision = u_get_revision_by_id(revision_id=revision_id)
    return revision
    

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
    