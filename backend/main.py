import fastapi
import sqlite3
from os import getcwd
from dto import User


WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'

app = fastapi.FastAPI()

@app.get('/')
def root():
    return {'message': 'Home Page'}

@app.get('/users')
async def get_users():

    d: dict = {}

    with sqlite3.connect(DATABASE_DIR) as connection:
        # rows = connection.execute('SELECT * FROM Users WHERE Users.deleted_at IS NULL ORDER BY Users.name')
        cursor = connection.execute('SELECT * FROM Documents WHERE Documents.deleted_at IS NULL ORDER BY Documents.id')
        rows = cursor.fetchall()
        column_names = [c[0] for c in cursor.description]

        
        for i, r in enumerate(rows):
            r = list(zip(column_names, r))
            for t in r:
                d[t[0]] = t[1]
            
            rows[i] = d

        id, name = d.values()

        users = User(id=id, name=name)
    
        return users