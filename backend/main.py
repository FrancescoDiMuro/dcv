import sqlite3

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from os import getcwd
from typing import List
from backend.dto.dto import User

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

    # Creazione di un dizionario per trasformare la lista di liste in una lista di dizionari    
    d: dict = {}

    # Lista di utenti
    users: List[User] = []

    # Query di SELECT
    query: str = '''SELECT * 
                    FROM Users 
                    WHERE Users.deleted_at IS NULL 
                    ORDER BY Users.name'''

    # Inizializzazione della connessione con il DB SQLite
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Ottenimento del cursore SQLite3
        cursor = connection.execute(query)

        # Ottenimento dei records
        rows = cursor.fetchall()

        # Ottenimento dei nomi delle colonne del risultato della query
        column_names = [c[0] for c in cursor.description]

        # Per ogni riga nel risultato della query
        for r in rows:
            
            # zip dei nomi delle colonne con i valori delle stesse
            r = list(zip(column_names, r))
            
            # Per ogni tupla zippata (k, v), creazione del dizionario con l'associazione k = v
            for t in r:
                d[t[0]] = t[1]
            
            # Unpacking dei valori del dizionario
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

            users.append(user)
    
        return users