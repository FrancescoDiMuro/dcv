from typing import List
from backend.schemas.dto import Customer
from backend.utils.utils import (select_rows_from_table, 
                                 select_row_from_table, 
                                 insert_rows_into_table)


def u_get_customers() -> List[Customer] | None:
    '''
        Summary:
            returns a list of Customers if there are any, otherwise it returns None

        Parameters:
            None

        Return Value:
            List[Customer] | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Customers 
                    WHERE Customers.deleted_at IS NULL 
                    ORDER BY Customers.id'''
     
    # Obtaining the list of Customers, unpacking the dictonaries in the data variable
    customers_list = select_rows_from_table(query=query)

    # If there is some data
    if len(customers_list) > 0:
        return [Customer(**data) for data in customers_list]
    
    return None
   

def u_get_customer_by_id(customer_id: int) -> Customer | None:
    '''
        Summary:
            returns a Customer if the customer with "customer_id" is found, otherwise it returns None

        Parameters:
            customer_id (int): id of the customer to look for

        Return Value:
            Customer | None
    '''
    
    # Defining the query to execute
    query: str = '''SELECT * 
                    FROM Customers 
                    WHERE Customers.deleted_at IS NULL AND 
                    Customers.id = :customer_id
                    LIMIT 1'''
    
    # Defining and assigning query parameters
    query_parameters = {'customer_id': customer_id}

    customer_data: dict = select_row_from_table(query=query, query_parameters=query_parameters)
    
    return Customer(**customer_data) if len(customer_data.items()) > 0 else None


def u_create_customer(dto_dict: dict) -> Customer | None:

    query = '''INSERT INTO Customers (name, created_at, updated_at)
               VALUES (:name, :created_at, :updated_at)'''
    
    if insert_rows_into_table(query=query, dto_dict=dto_dict):        
        return Customer(**dto_dict)
    
    return None
    