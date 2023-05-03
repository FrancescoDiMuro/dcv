import sqlite3
from typing import List
from backend.schemas.dto import Document
from backend.utils.utils import DATABASE_DIR


def u_get_documents() -> List[Document]:
    
    # Creating a dictionary to use it as a container for Document data
    d: dict = {}

    # Initialize empty list of documents
    documents: List[Document] = []

    query: str = '''SELECT * 
                    FROM Documents 
                    WHERE Documents.deleted_at IS NULL 
                    ORDER BY Documents.id'''

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

            # Append the Document to the list of Documents
            documents.append(document)
    
        return documents
    

def u_get_document_by_id(document_id: int):

    # Creating a dictionary to use it as a container for Document data
    d: dict = {}

    query: str = '''SELECT * 
                    FROM Documents 
                    WHERE Documents.deleted_at IS NULL AND 
                    Documents.id = :document_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'document_id': document_id}

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
        document: Document = Document(**d)
    
        return document
    