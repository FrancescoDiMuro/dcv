from typing import List, Tuple, Union
from random import randint, sample
from operator import itemgetter
import requests

RANDOM_USER_API: str = 'https://randomuser.me/api/'
RANDOM_USERS_API: str = 'https://randomapi.com/api/6de6abfedb24f889e0b5f675edc50deb?fmt=raw&sole'

def get_random_user() -> str:  
    '''
        Function to obtain a random user's name

        Parameters:
            None

        Returns:
            random_user (str): returns a random user's name
    '''
    
    random_user = requests.get(RANDOM_USER_API).json()['results'][0]['name']['first']
    return random_user


def get_random_users(n: int = 5) -> List[Tuple[str]]:
    '''
        Function to obtain a list of random users' names

        Parameters:
            n (int): number of users to return (default = 5)

        Returns:
            random_users (List[Tuple[str]]): returns a list of tuples of n random users' names
    '''

    random_users = []

    random_users_info = requests.get(RANDOM_USERS_API).json()[0:n]
    for random_user_info in random_users_info:
        random_users.append(tuple([random_user_info['first']]))

    return random_users


def get_random_customers(n: int = 5) -> List[Tuple[str]]:
    '''
        Function to obtain a list of random customers

        Parameters:
            n (int): number of customers to return (default = 5)

        Returns:
            List[Tuple[str]]: returns a list of tuples of n random customers
    '''
    random_customers = []

    for random_customer in [f'Customer {i}' for i in range(1, n + 1)]:
        random_customers.append(tuple([random_customer]))
    
    return random_customers


def get_random_jobs(min_id: int, max_id: int, n: int = 5) -> List[Tuple[Union[str, int]]]:
    '''
        Function to obtain a list of random jobs

        Parameters:
            min_id (int): min id in Customers table
            max_id (int): max id in Customers table
            n (int): number of jobs to return (default = 5)

        Returns:
            List[Tuple[Union[str, int]]]: returns a list of tuples of n random jobs
    '''
    random_jobs = []

    for random_job in [f'Job {i}' for i in range(1, n + 1)]:
        random_jobs.append(tuple([random_job, f'Description of {random_job}', randint(min_id, max_id)]))
    
    return random_jobs


def get_random_documents(min_id: int, max_id: int) -> List[dict]:
    '''
        Function to obtain a list of random documents

        Parameters:
            min_id (int): min id in Jobs table
            max_id (int): max id in Jobs table
            n (int): number of documents to return (default = 5)

        Returns:
            List[Tuple[Union[str, int]]]: returns a list of tuples of n random documents
    '''

    # Collections of available documents
    DOCUMENTS = [{'name': 'MAN', 'description': 'Operator Manual'},
                 {'name': 'ELC', 'description': 'Signals List'},
                 {'name': 'ALL', 'description': 'Alarms List'},
                 {'name': 'FDS', 'description': 'Functional Design Specification'},
                 {'name': 'RA', 'description': 'Risk Assessment'}]

    random_documents: List[dict] = []

    # For every job in the Jobs table
    for i in range(min_id, max_id):

        # Obtaining a list of random indexes    
        random_indexes: List[int] = sample(range(len(DOCUMENTS)), randint(1, 5)) # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Why 1, 5?

        # If the length of random_indexes list is greater than 1,
        # then we can convert the returned tuple into a list;
        # while, if the condition is false, then a dictionary is returned,
        # so we can't use the list() function, and we need to wrap the dictionary
        # into a pair of square brackets, making it a list of a dictionary
        if len(random_indexes) > 1:
            random_documents_templates = list(itemgetter(*random_indexes)(DOCUMENTS))
        else:
            random_documents_templates = [itemgetter(*random_indexes)(DOCUMENTS)]
        
        # Obtaining a random job_id
        random_job_id = sample(range(min_id, max_id), 1)[0]
        
        # For each document in the random documents list
        for random_document_template in random_documents_templates:            
            
            # Adding the job_id
            random_document_template['job_id'] = random_job_id

            random_documents.append(random_document_template)
    
    return random_documents
