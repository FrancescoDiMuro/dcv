import sqlite3

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from os import getcwd
from typing import List
from backend.dto.dto import User, Customer, Job, Document, Revision

# Constants declaration and initialization
WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'
TEMPLATES_DIR = f'{WORKING_DIR}\\frontend\\static\\templates'


# Templates object to use templates in the app
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# App configuration

# Creazione dell'app con FastAPI
app = FastAPI()

# Endpoints configuration
# Root
@app.get('/', response_class=HTMLResponse)
def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('index.html', {'request': request})

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
            id, name, surname, email, password, created_at, updated_at, deleted_at, access_level_id  = d.values()
            user: User = User(id=id, 
                            name=name, 
                            surname=surname, 
                            email=email, 
                            password=password, 
                            created_at=created_at, 
                            updated_at=updated_at, 
                            deleted_at=deleted_at, 
                            access_level_id=access_level_id)

            # Append the User to the list of Users
            users.append(user)
    
        return users
    

# GET /customers
@app.get('/customers', description='Get list of configured Customers')
async def get_customers() -> List[Customer]:

    # Creating a dictionary to use it as a container for Customer data
    d: dict = {}

    # Initialize empty list of customers
    customers: List[Customer] = []

    query: str = '''SELECT * 
                    FROM Customers 
                    WHERE Customers.deleted_at IS NULL 
                    ORDER BY Customers.name'''

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
            id, name, created_at, updated_at, deleted_at = d.values()
            customer: Customer = Customer(id=id, 
                                      name=name,                             
                                      created_at=created_at, 
                                      updated_at=updated_at, 
                                      deleted_at=deleted_at)

            # Append the Customer to the list of Customers
            customers.append(customer)
    
        return customers
    

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
            id, name, description, created_at, updated_at, deleted_at, customer_id = d.values()
            job: Job = Job(id=id, 
                           name=name,
                           description=description,                         
                           created_at=created_at, 
                           updated_at=updated_at, 
                           deleted_at=deleted_at,
                           customer_id=customer_id)

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
            id, name, description, created_at, updated_at, deleted_at, job_id = d.values()
            document: Document = Document(id=id, 
                                          name=name,
                                          description=description,                         
                                          created_at=created_at, 
                                          updated_at=updated_at, 
                                          deleted_at=deleted_at,
                                          job_id=job_id)

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
            id, version, description, file_path, created_at, updated_at, deleted_at, user_id, document_id = d.values()
            revision: Revision = Revision(id=id, 
                                          version=version,
                                          description=description,
                                          file_path=file_path,                      
                                          created_at=created_at, 
                                          updated_at=updated_at, 
                                          deleted_at=deleted_at,
                                          user_id=user_id,
                                          document_id=document_id)

            # Append the Customer to the list of Documents
            revisions.append(revision)
    
        return revisions