import sqlite3
from os import getcwd
from typing import List
from backend.schemas.dto import Revision
from backend.utils.utils import DATABASE_DIR


def u_get_revisions() -> List[Revision]:
    
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

            # Append the Revision to the list of Revisions
            revisions.append(revision)
    
        return revisions
    

def u_get_revision_by_id(user_id: int):

    # Creating a dictionary to use it as a container for Revision data
    d: dict = {}

    query: str = '''SELECT * 
                    FROM Revisions 
                    WHERE Revisions.deleted_at IS NULL AND 
                    Revisions.id = :revision_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'revision_id': user_id}

    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Obtaining cursor from db
        cursor = connection.execute(query, query_parameters)

        # Obtaining records from table
        r = cursor.fetchone()

        # Obtaining columns names from the cursor
        column_names = [c[0] for c in cursor.description]

        # zipping column name with the corresponding value
        r = list(zip(column_names, r))
            
        # For each zipped tuple (k, v), creating a dictionary with the association k:v
        for t in r:
            d[t[0]] = t[1]
        
        # Unpacking dictionary values
        revision: Revision = Revision(**d)
    
        return revision
    