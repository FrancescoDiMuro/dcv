import requests
import sqlite3
from typing import List
from os import getcwd, remove
from os.path import exists

# Directories
WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_FILE_NAME: str = f'{BACKEND_DIR}\\dcv.db'

# Endpoints
API_URL: str = 'http://127.0.0.1:8080'
USERS_ENDPOINT: str = f'{API_URL}/users'
CUSTOMERS_ENDPOINT: str = f'{API_URL}/customers'
JOBS_ENDPOINT: str = f'{API_URL}/jobs'
DOCUMENTS_ENDPOINT: str = f'{API_URL}/documents'
REVISIONS_ENDPOINT: str = f'{API_URL}/revisions'

TABLES_CREATE_STATEMENTS = \
[
    '''
    CREATE TABLE "Customers" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"created_at"	TEXT NOT NULL,
	"updated_at"	TEXT NOT NULL,
	"deleted_at"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
    ''',
    '''
    CREATE TABLE "Jobs" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"created_at"	TEXT NOT NULL,
	"updated_at"	TEXT NOT NULL,
	"deleted_at"	TEXT,
	"customer_id"	INTEGER NOT NULL,
	FOREIGN KEY("customer_id") REFERENCES "Customers"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
    );
    ''',
    '''
    CREATE TABLE "Documents" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"created_at"	TEXT NOT NULL,
	"updated_at"	TEXT NOT NULL,
	"deleted_at"	TEXT,
	"job_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("job_id") REFERENCES "Jobs"("id")
    )
    ''',
    '''
    CREATE TABLE "Revisions" (
	"id"	INTEGER NOT NULL UNIQUE,
	"version"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"file_path"	TEXT NOT NULL,
	"created_at"	TEXT NOT NULL,
	"updated_at"	TEXT NOT NULL,
	"deleted_at"	TEXT,
	"user_id"	INTEGER NOT NULL,
	"document_id"	INTEGER NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "Users"("id"),
	FOREIGN KEY("document_id") REFERENCES "Documents"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
    )
    ''',
    '''
    CREATE TABLE "Users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"created_at"	TEXT NOT NULL,
	"updated_at"	TEXT NOT NULL,
	"deleted_at"	TEXT,
	"access_level_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
    )
    '''
]

test_users: List[dict[str, int]] = \
[
    {
        'name': 'Mario',
        'surname': 'Rossi',
        'email': 'mario.rossi@somedomain.it',
        'password': 'somepassword',
        'access_level_id': 1
    },
    {
        'name': 'Giovanni',
        'surname': 'Verdi',
        'email': 'giovanni.verdi@somedomain.it',
        'password': 'somerandompassword',
        'access_level_id': 10
    },
    {
        'name': 'Alessandro',
        'surname': 'Bianchi',
        'email': 'alessandro.bianchi@somedomain.it',
        'password': 'anotherpassword',
        'access_level_id': 100
    }
]

test_customers: List[dict[str, int]] = \
[
    {'name': 'CUSTOMER001'},
    {'name': 'CUSTOMER002'},
    {'name': 'CUSTOMER003'},
]

test_jobs: List[dict[str, int]] = \
[
    {'name': 'JOB001',
     'description': 'This is the description of JOB001',
     'customer_id': 1
    },
    {'name': 'JOB002',
     'description': 'This is the description of JOB002',
     'customer_id': 1
    },
    {'name': 'JOB003',
     'description': 'This is the description of JOB003',
     'customer_id': 2
    },
    {'name': 'JOB004',
     'description': 'This is the description of JOB004',
     'customer_id': 3
    },
    {'name': 'JOB005',
     'description': 'This is the description of JOB005',
     'customer_id': 3
    },
    {'name': 'JOB006',
     'description': 'This is the description of JOB006',
     'customer_id': 3
    }
]

test_documents: List[dict[str, int]] = \
[
    {
        'name': 'DOCUMENT001',
        'description': 'Operator Manual',
        'job_id': 1
    },
    {
        'name': 'DOCUMENT002',
        'description': 'Alarms List',
        'job_id': 1
    },
    {
        'name': 'DOCUMENT003',
        'description': 'Signals List',
        'job_id': 1
    },
    {
        'name': 'DOCUMENT004',
        'description': 'Functional Design Specification',
        'job_id': 2
    },
    {
        'name': 'DOCUMENT005',
        'description': 'Wiring Diagram',
        'job_id': 3
    },
    {
        'name': 'DOCUMENT006',
        'description': 'Operator Manual',
        'job_id': 3
    },
    {
        'name': 'DOCUMENT007',
        'description': 'Software Design Specification',
        'job_id': 4
    },
    {
        'name': 'DOCUMENT008',
        'description': 'Installation and Operation Qualification',
        'job_id': 4
    },
    {
        'name': 'DOCUMENT009',
        'description': 'Risk Assessment',
        'job_id': 5
    },
    {
        'name': 'DOCUMENT010',
        'description': 'User Requirements',
        'job_id': 6
    }
]

test_revisions: List[dict[str, int]] = \
[
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\operator_manual.docx',
        'user_id': 1,
        'document_id': 1
    },
    {
        'version': 'B',
        'description': 'Updated images in page 10',
        'file_path': '\\\\someserver\\somepath\\fioperator_manualle.docx',
        'user_id': 2,
        'document_id': 1
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\alarms_list.xlsx',
        'user_id': 1,
        'document_id': 2
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\signal_list.xlsx',
        'user_id': 2,
        'document_id': 3
    },
    {
        'version': 'B',
        'description': 'Added new signals',
        'file_path': '\\\\someserver\\somepath\\signal_list.xlsx',
        'user_id': 1,
        'document_id': 3
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\fds.docx',
        'user_id': 1,
        'document_id': 4
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\wiring_diagram.dwg',
        'user_id': 2,
        'document_id': 5
    },
    {
        'version': 'B',
        'description': 'Updated signal at page 5',
        'file_path': '\\\\someserver\\somepath\\wiring_diagram.dwg',
        'user_id': 2,
        'document_id': 5
    },
    {
        'version': 'C',
        'description': 'Removed signal at page 12',
        'file_path': '\\\\someserver\\somepath\\wiring_diagram.dwg',
        'user_id': 3,
        'document_id': 5
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\operator_manual.docx',
        'user_id': 1,
        'document_id': 6
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\sds.docx',
        'user_id': 3,
        'document_id': 7
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\ioq.docx',
        'user_id': 1,
        'document_id': 8
    },
    {
        'version': 'B',
        'description': 'Added test #5 as per client request',
        'file_path': '\\\\someserver\\somepath\\ioq.docx',
        'user_id': 1,
        'document_id': 8
    },
    {
        'version': 'C',
        'description': 'Updated date/time format as per client request',
        'file_path': '\\\\someserver\\somepath\\ioq.docx',
        'user_id': 2,
        'document_id': 8
    },
    {
        'version': 'D',
        'description': 'Added test #6 as per client request',
        'file_path': '\\\\someserver\\somepath\\ioq.docx',
        'user_id': 2,
        'document_id': 8
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\ra.docx',
        'user_id': 3,
        'document_id': 9
    },
    {
        'version': 'B',
        'description': 'Added risk matrix as per client request',
        'file_path': '\\\\someserver\\somepath\\ra.docx',
        'user_id': 3,
        'document_id': 9
    },
    {
        'version': 'A',
        'description': 'First release',
        'file_path': '\\\\someserver\\somepath\\usr.docx',
        'user_id': 1,
        'document_id': 10
    },
    {
        'version': 'B',
        'description': 'Added comments',
        'file_path': '\\\\someserver\\somepath\\usr.docx',
        'user_id': 3,
        'document_id': 10
    },
    {
        'version': 'C',
        'description': 'Added section as per client request',
        'file_path': '\\\\someserver\\somepath\\usr.docx',
        'user_id': 2,
        'document_id': 10
    },
        {
        'version': 'D',
        'description': 'Added new feature',
        'file_path': '\\\\someserver\\somepath\\usr.docx',
        'user_id': 2,
        'document_id': 10
    }
]

# # Create the db
# if exists(DATABASE_FILE_NAME):
#     remove(DATABASE_FILE_NAME)

# with sqlite3.connect(DATABASE_FILE_NAME) as connection:
#     for query in TABLES_CREATE_STATEMENTS:
#         connection.execute(query)
#         connection.commit()        

# # Populating Users
# print(f'{"-" * 10} USERS {"-" * 10}')
# for user in test_users:
#     if requests.post(USERS_ENDPOINT, json=user).status_code == 200:
#         print(f'The user "{user["name"]}" has been inserted in the table')

# # Populating Customers
# print(f'{"-" * 10} CUSTOMERS {"-" * 10}')
# for customer in test_customers:
#     if requests.post(CUSTOMERS_ENDPOINT, json=customer).status_code == 200:
#         print(f'The customer "{customer["name"]}" has been inserted in the table')

# # Populating Jobs
# print(f'{"-" * 10} JOBS {"-" * 10}')
# for job in test_jobs:
#     if requests.post(JOBS_ENDPOINT, json=job).status_code == 200:
#         print(f'The job "{job["name"]}" has been inserted in the table')

# # Populating Documents
# print(f'{"-" * 10} DOCUMENTS {"-" * 10}')
# for document in test_documents:
#     if requests.post(DOCUMENTS_ENDPOINT, json=document).status_code == 200:
#         print(f'The document "{document["name"]}" has been inserted in the table')

# # Populating Revisions
# print(f'{"-" * 10} REVISIONS {"-" * 10}')
# for revision in test_revisions:
#     if requests.post(REVISIONS_ENDPOINT, json=revision).status_code == 200:
#         print(f'The revision "{revision["version"]}" of document_id {revision["document_id"]} has been inserted in the table')
    