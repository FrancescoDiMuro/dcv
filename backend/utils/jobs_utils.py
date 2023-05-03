import sqlite3
from os import getcwd
from typing import List
from backend.schemas.dto import Job
from backend.utils.utils import DATABASE_DIR


def u_get_jobs() -> List[Job]:
    
    # Creating a dictionary to use it as a container for Job data
    d: dict = {}

    # Initialize empty list of jobs
    jobs: List[Job] = []

    query: str = '''SELECT * 
                    FROM Jobs 
                    WHERE Jobs.deleted_at IS NULL 
                    ORDER BY Jobs.id'''

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

            # Append the Job to the list of Jobs
            jobs.append(job)
    
        return jobs
    

def u_get_job_by_id(job_id: int):

    # Creating a dictionary to use it as a container for Job data
    d: dict = {}

    query: str = '''SELECT * 
                    FROM Jobs 
                    WHERE Jobs.deleted_at IS NULL AND 
                    Jobs.id = :job_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'job_id': job_id}

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
        job: Job = Job(**d)
    
        return job
    