from typing import List
from backend.schemas.dto import Revision
from backend.utils.utils import select_rows_from_table, select_row_from_table


def u_get_revisions() -> List[Revision] | None:
    '''
        Summary:
            returns a list of Revisions if there are any, otherwise it returns None

        Parameters:
            None

        Return Value:
            List[Revision] | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Revisions 
                    WHERE Revisions.deleted_at IS NULL 
                    ORDER BY Revisions.id'''
     
    # Obtaining the list of Revisions, unpacking the dictonaries in the data variable
    revisions_list = select_rows_from_table(query=query)

    # If there is some data
    if len(revisions_list) > 0:
        return [Revision(**data) for data in revisions_list]
    
    return None
   

def u_get_revision_by_id(revision_id: int) -> Revision | None:
    '''
        Summary:
            returns a Revision if the revision with "revision_id" is found, otherwise it returns None

        Parameters:
            revision_id (int): id of the revision to look for

        Return Value:
            Revision | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Revisions 
                    WHERE Revisions.deleted_at IS NULL AND 
                    Revisions.id = :revision_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'revision_id': revision_id}

    revision: dict = select_row_from_table(query=query, query_parameters=query_parameters)
    
    return Revision(**revision) if len(revision.items()) > 0 else None
    