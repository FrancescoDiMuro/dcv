import sqlite3

from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from os import getcwd
from typing import List
from backend.schemas.dto import User, Customer, Job, Document, Revision
from datetime import datetime, timezone

from backend.utils.customers_utils import u_get_customers, u_get_customer_by_id
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
app.mount("/static", StaticFiles(directory="frontend/static/templates"), name="static")

# ----- Endpoints configuration -----
# Root
@app.get('/', response_class=HTMLResponse)
def root(request: Request) -> HTMLResponse:
    
    customers: List[Customer] = u_get_customers()

    return templates.TemplateResponse('index.html', {'request': request, 'customers': customers})
   

# GET /customers
@app.get('/customers', description='Get list of configured Customers')
async def get_customers() -> List[Customer]:
    customers: List[Customer] = u_get_customers()
    return customers


# GET /customers/{customer_id}
@app.get('/customers/{customer_id}', description='Get a specific Customers by its id')
async def get_customer_by_id(request: Request, customer_id: int) -> Customer:
    customer: Customer = u_get_customer_by_id(customer_id=customer_id)
    return templates.TemplateResponse('customer_info.html', {'request': request, 'customer': customer})


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


@app.patch('/customers/{customer_id}')
async def delete_customer(customer_id: int):
    with sqlite3.connect(DATABASE_DIR) as connection:
    
        customer: dict = u_get_customer_by_id(customer_id).dict(exclude_unset=True)

        # customer['deleted_at'] = datetime.now(timezone.utc)
        customer['deleted_at'] = ISO8601_now()

        return customer

        

# GET /jobs
@app.get('/jobs', description='Get list of configured Jobs')
async def get_jobs() -> List[Job]:

    # Creating a dictionary to use it as a container for Job data
    d: dict = {}

    # Initialize empty list of jobs
    jobs: List[Job] = []

    query: str = '''SELECT * 
                    FROM Jobs 
                    WHERE Jobs.deleted_at IS NULL
                    ORDER BY Jobs.name'''

    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Obtaining cursor from db
        cursor = connection.execute(query)

        # Obtaining records from table
        rows = cursor.fetchall()

        # Obtaining columns names from the cursor
        column_names = [c[0] for c in cursor.description]

        # For each row in the query result
        for r in rows:
            
            # zipping column name with the corresponding value
            r = list(zip(column_names, r))
            
            # For each zipped tuple (k, v), creating a dictionary with the association k:v
            for t in r:
                d[t[0]] = t[1]
            
            # Unpacking dictionary values            
            job: Job = Job(**d)

            # Append the Customer to the list of Jobs
            jobs.append(job)
    
        return jobs
    

# GET /documents
@app.get('/documents', description='Get list of configured Documents')
async def get_documents() -> List[Document]:

    # Creating a dictionary to use it as a container for Document data
    d: dict = {}

    # Initialize empty list of documents
    documents: List[Revision] = []

    query: str = '''SELECT * 
                    FROM Documents 
                    WHERE Documents.deleted_at IS NULL
                    ORDER BY Documents.name'''

    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Obtaining cursor from db
        cursor = connection.execute(query)

        # Obtaining records from table
        rows = cursor.fetchall()

        # Obtaining columns names from the cursor
        column_names = [c[0] for c in cursor.description]

        # For each row in the query result
        for r in rows:
            
            # zipping column name with the corresponding value
            r = list(zip(column_names, r))
            
            # For each zipped tuple (k, v), creating a dictionary with the association k:v
            for t in r:
                d[t[0]] = t[1]
            
            # Unpacking dictionary values            
            document: Document = Document(**d)

            # Append the Customer to the list of Documents
            documents.append(document)
    
        return documents
    

# GET /revisions
@app.get('/revisions', description='Get list of configured Revisions')
async def get_revisions() -> List[Revision]:

    # Creating a dictionary to use it as a container for Revision data
    d: dict = {}

    # Initialize empty list of revisions
    revisions: List[Revision] = []

    query: str = '''SELECT * 
                    FROM Revisions 
                    WHERE Revisions.deleted_at IS NULL
                    ORDER BY Revisions.id'''

    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Obtaining cursor from db
        cursor = connection.execute(query)

        # Obtaining records from table
        rows = cursor.fetchall()

        # Obtaining columns names from the cursor
        column_names = [c[0] for c in cursor.description]

        # For each row in the query result
        for r in rows:
            
            # zipping column name with the corresponding value
            r = list(zip(column_names, r))
            
            # For each zipped tuple (k, v), creating a dictionary with the association k:v
            for t in r:
                d[t[0]] = t[1]
            
            # Unpacking dictionary values            
            revision: Revision = Revision(**d)

            # Append the Customer to the list of Documents
            revisions.append(revision)
    
        return revisions
    

# GET /users
@app.get('/users', description='Get list of configured Users')
async def get_users() -> List[User]:

    # Creating a dictionary to use it as a container for User data
    d: dict = {}

    # Initialize empty list of users
    users: List[User] = []

    query: str = '''SELECT * 
                    FROM Users 
                    WHERE Users.deleted_at IS NULL 
                    ORDER BY Users.name'''

    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Obtaining cursor from db
        cursor = connection.execute(query)

        # Obtaining records from table
        rows = cursor.fetchall()

        # Obtaining columns names from the cursor
        column_names = [c[0] for c in cursor.description]

        # For each row in the query result
        for r in rows:
            
            # zipping column name with the corresponding value
            r = list(zip(column_names, r))
            
            # For each zipped tuple (k, v), creating a dictionary with the association k:v
            for t in r:
                d[t[0]] = t[1]
            
            # Unpacking dictionary values            
            user: User = User(**d)

            # Append the User to the list of Users
            users.append(user)
    
        return users