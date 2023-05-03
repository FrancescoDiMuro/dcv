from typing import List
from backend.schemas.dto import User
from backend.utils.utils import select_rows_from_table, select_row_from_table


def u_get_users() -> List[User] | None:
    '''
        Summary:
            returns a list of Users if there are any, otherwise it returns None

        Parameters:
            None

        Return Value:
            List[User] | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Users 
                    WHERE Users.deleted_at IS NULL 
                    ORDER BY Users.id'''
     
    # Obtaining the list of Users, unpacking the dictonaries in the data variable
    users_list = select_rows_from_table(query=query)

    # If there is some data
    if len(users_list) > 0:
        return [User(**data) for data in users_list]
    
    return None
   

def u_get_user_by_id(user_id: int) -> User | None:
    '''
        Summary:
            returns a User if the user with "user_id" is found, otherwise it returns None

        Parameters:
            user_id (int): id of the user to look for

        Return Value:
            User | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Users 
                    WHERE Users.deleted_at IS NULL AND 
                    Users.id = :user_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'user_id': user_id}

    user_data: dict = select_row_from_table(query=query, query_parameters=query_parameters)
    
    return User(**user_data) if len(user_data.items()) > 0 else None
    