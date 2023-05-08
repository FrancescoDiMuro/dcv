import sqlite3
import sqlalchemy
from typing import List
from datetime import datetime, timezone
from os import getcwd


WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'

def ISO8601_now():    
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')


def select_rows_from_table(query: str, query_parameters: dict = {}) -> List[dict]:
    
    # Creating a dictionary to use it as a container for the data
    d: dict = {}

    # Initialize empty list
    data: list = []

    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Obtaining cursor from db
        cursor = connection.execute(query, query_parameters)      

        # Obtaining records from table
        rows = cursor.fetchall()

        # If the query returned some data
        if len(rows) > 0:

            # Obtaining columns names from the cursor
            column_names = [c[0] for c in cursor.description]

            # For each row in the query result
            for r in rows:
                
                # zipping column name with the corresponding value
                r = list(zip(column_names, r))
                
                # For each zipped tuple (k, v), creating a dictionary with the association k:v
                for t in r:
                    d[t[0]] = t[1]
            
                # Append data to the list of dictionaries
                data.append(d)

                # Re-create the dictionary
                d = {}

    # Clean-up
    cursor.close()
            
    return data


def select_row_from_table(query: str, query_parameters: dict = {}) -> dict:
    
    # Creating a dictionary to use it as a container for the data
    d: dict = {}

    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
        
        # Obtaining cursor from db
        cursor = connection.execute(query, query_parameters)

        # Obtaining one row from table
        row = cursor.fetchone()

        if row is not None:

            # Obtaining columns names from the cursor
            column_names = [c[0] for c in cursor.description]

            # zipping column name with the corresponding value
            row = list(zip(column_names, row))
                
            # For each zipped tuple (k, v), creating a dictionary with the association k:v
            for t in row:
                d[t[0]] = t[1]
            
        # Clean-up
        cursor.close()
        
        return d
        
def insert_rows_into_table(query: str, dto_dict: dict) -> bool:
    
    ret_val: bool = False
    
    # Inizialize SQLite db connection
    with sqlite3.connect(DATABASE_DIR) as connection:
                  
        # INSERT query execution
        cursor = connection.execute(query, dto_dict)
        ret_val = True if cursor.rowcount > 0 else False
        connection.commit()
        cursor.close()

    return ret_val
