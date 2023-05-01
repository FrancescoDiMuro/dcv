import sqlite3
from os import getcwd
from typing import List
from backend.schemas.dto import Customer
from typing import Any


WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'

def query_table(table_name: str, 
                columns: List[str] | str, 
                where_condition: str = '1=1',
                order_by: str = '1',
                asc: bool = True,  
                return_type: object = None) -> Any:

    if type(columns) == List[str]:
        columns = ','.join(columns)
    else:
        columns = columns[0]

    sql_query: str = f'''SELECT {columns} 
                         FROM {table_name}
                         WHERE {where_condition}
                         ORDER BY {order_by} {"" if asc else "DESC"}'''
    
    print(sql_query)


def u_get_customers() -> List[Customer]:
    
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
            customer: Customer = Customer(**d)

            # Append the Customer to the list of Customers
            customers.append(customer)
    
        return customers
    

def u_get_customer_by_id(customer_id: int):

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
        customer: Customer = Customer(**d)
    
        return customer
    

query_table('Customers', ['name', 'created_at'])