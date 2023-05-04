from typing import List
from backend.schemas.dto import Document
from backend.utils.utils import select_rows_from_table, select_row_from_table


def u_get_documents() -> List[Document] | None:
    '''
        Summary:
            returns a list of Documents if there are any, otherwise it returns None

        Parameters:
            None

        Return Value:
            List[Document] | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Documents 
                    WHERE Documents.deleted_at IS NULL 
                    ORDER BY Documents.id'''
     
    # Obtaining the list of Documents, unpacking the dictonaries in the data variable
    documents_list = select_rows_from_table(query=query)

    # If there is some data
    if len(documents_list) > 0:
        return [Document(**data) for data in documents_list]
    
    return None
   

def u_get_document_by_id(document_id: int) -> Document | None:
    '''
        Summary:
            returns a Document if the document with "document_id" is found, otherwise it returns None

        Parameters:
            document_id (int): id of the document to look for

        Return Value:
            Document | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Documents 
                    WHERE Documents.deleted_at IS NULL AND 
                    Documents.id = :document_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'document_id': document_id}

    document_id: dict = select_row_from_table(query=query, query_parameters=query_parameters)
    
    return Document(**document_id) if len(document_id.items()) > 0 else None
    