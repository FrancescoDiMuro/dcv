import sqlite3
from os import getcwd
from typing import List
from backend.dto.dto import Customer


WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'


def get_customers_list() -> List[Customer]:
    
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
    

def get_customer(customer_id: int):

    # Creating a dictionary to use it as a container for Customer data
    d: dict = {}

    query: str = '''SELECT * 
                    FROM Customers 
                    WHERE Customers.deleted_at IS NULL AND 
                    Customers.id = :customer_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'customer_id': customer_id}

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
        id, name, created_at, updated_at, deleted_at = d.values()
        customer: Customer = Customer(id=id, 
                                      name=name,                             
                                      created_at=created_at, 
                                      updated_at=updated_at, 
                                      deleted_at=deleted_at)

    
        return customer