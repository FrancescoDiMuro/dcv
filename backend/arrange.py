from os import getcwd
from utils import get_random_users, get_random_customers, get_random_jobs, get_random_documents
import sqlite3


WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'

def reset_sql_sequence() -> None:
    with sqlite3.connect(DATABASE_DIR) as connection:
        connection.execute('UPDATE sqlite_sequence SET seq = 0')

def populate_customers() -> None:
    
    with sqlite3.connect(DATABASE_DIR) as connection:

        connection.execute('DELETE FROM Customers')

        # Getting a list of random customers
        random_customers = get_random_customers()

        # INSERT query
        sql_query = 'INSERT INTO Customers (name)' + \
                    f'VALUES (?)'
        
        # Execution of the INSERT query
        connection.executemany(sql_query, random_customers)

        # SELECT query
        sql_query = 'SELECT * FROM Customers'

        # Obtaining the result as a list of tuples
        result = connection.execute(sql_query).fetchall()

        # print(result)


def populate_jobs() -> None:
    
    with sqlite3.connect(DATABASE_DIR) as connection: 

        connection.execute('DELETE FROM Jobs')       

        # SELECT query
        sql_query = 'SELECT MIN(id), MAX(id) FROM Customers'

        # Obtaining MIN and MAX ids of Customers
        min_customers_id, max_customers_id = connection.execute(sql_query).fetchall()[0]

        # Getting a list of random jobs
        random_jobs = get_random_jobs(min_customers_id, max_customers_id, n=10)

        # INSERT query
        sql_query = 'INSERT INTO Jobs (name, description, customer_id)' + \
                    f'VALUES (?, ?, ?)'
        
        # Execution of the INSERT query
        connection.executemany(sql_query, random_jobs)

        # SELECT query
        sql_query = 'SELECT * FROM Jobs'

        # Obtaining the result as a list of tuples
        result = connection.execute(sql_query).fetchall()

        # print(result)


def populate_documents() -> None:
    
    with sqlite3.connect(DATABASE_DIR) as connection: 

        connection.execute('DELETE FROM Documents')       

        # SELECT query
        sql_query = 'SELECT MIN(id), MAX(id) FROM Jobs'

        # Obtaining MIN and MAX ids of Jobs
        min_jobs_id, max_jobs_id = connection.execute(sql_query).fetchall()[0]

        # Getting a list of random documents
        random_documents = get_random_documents(min_jobs_id, max_jobs_id)

        # INSERT query
        sql_query = 'INSERT INTO Documents (name, description, job_id)' + \
                    f'VALUES (:name, :description, :job_id)'
        
        for i, v in enumerate(random_documents):
            print(i, v)
        
        # Execution of the INSERT query
        connection.executemany(sql_query, random_documents)      

        # SELECT query
        sql_query = 'SELECT * FROM Documents'

        # Obtaining the result as a list of tuples
        result = connection.execute(sql_query).fetchall()

        # print(result)


def populate_users() -> None:
    
    with sqlite3.connect(DATABASE_DIR) as connection:

        connection.execute('DELETE FROM Users')

        # Getting a list of random users
        random_users = get_random_users()

        # INSERT query
        sql_query = 'INSERT INTO Users (name)' + \
                    f'VALUES (?)'
        
        # Execution of the INSERT query
        connection.executemany(sql_query, random_users)

        # SELECT query
        sql_query = 'SELECT * FROM Users'

        # Obtaining the result as a list of tuples
        result = connection.execute(sql_query).fetchall()

        # print(result)


reset_sql_sequence()
populate_customers()
populate_jobs()
populate_users()
populate_documents()