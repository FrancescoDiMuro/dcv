from typing import List
from backend.schemas.dto import Job
from backend.utils.utils import select_rows_from_table, select_row_from_table


def u_get_jobs() -> List[Job] | None:
    '''
        Summary:
            returns a list of Jobs if there are any, otherwise it returns None

        Parameters:
            None

        Return Value:
            List[Job] | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Jobs 
                    WHERE Jobs.deleted_at IS NULL 
                    ORDER BY Jobs.id'''
     
    # Obtaining the list of Jobs, unpacking the dictonaries in the data variable
    jobs_list = select_rows_from_table(query=query)

    # If there is some data
    if len(jobs_list) > 0:
        return [Job(**data) for data in jobs_list]
    
    return None
   

def u_get_job_by_id(job_id: int) -> Job | None:
    '''
        Summary:
            returns a Job if the job with "job_id" is found, otherwise it returns None

        Parameters:
            job_id (int): id of the job to look for

        Return Value:
            Job | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Jobs 
                    WHERE Jobs.deleted_at IS NULL AND 
                    Jobs.id = :job_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'job_id': job_id}

    job_data: dict = select_row_from_table(query=query, query_parameters=query_parameters)
    
    return Job(**job_data) if len(job_data.items()) > 0 else None
    