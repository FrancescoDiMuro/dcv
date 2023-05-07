# Project DCV

## Introduction
This is a personal project for building a DCV (Document Control Version) application.
The main goal of the project is to develop a web application using REST APIs developed
with FastAPI, and integrate some Front End programming language(s) in order to create a UI for the users.
I'm developing this project to learn how to design, create, test and maintain a web application,
since my current goal is to become a back-end developer.
I choose Python and FastAPI among all the other programming languages and web-app frameworks because I have
some familiarity with Python, and thanks to its easy syntax, I thought it would be a good language
to practice the concepts of back-end development.

## Database structure
To make the project easier to build, I created a local SQLite3 db in which store data.
The entities in the db are:
- Customer
- Job
- Document
- Revision
- User

## Installation
The project has been entirely developed using Python 3.11.3.
To install it, you can use git clone or you can manually download and move all the files and folders in this repository in the local project folder.
The project uses a Virtual Environment in order to keep all packages and modules to avoid conflicts, so a "requirements.txt" file is provided in the root folder.
To install the "requirements.txt" file, navigate to the "Scripts" folder (env) and use:
```
pip install -r requirements.txt
```

## Running the API server
This project uses Uvicorn as a web server to manage the APIs.
In order to test the application, you have to use the executable "uvicorn.exe" in the Virtual Environment, 
running the server with the command:
```
uvicorn.exe backend.main:app --reload
```

The parameter "--reload" is used to reload the server everytime some changes are detected in the project files.
On Windows, it may be that the default port used by uvicorn is already in use, so if this is the case, you can use the parameter "--port" in order
to change the port used by the web server, so:
```
uvicorn.exe backend.main:app --reload --port 8080
```

## Tables schemas
In this section, you can find more details about tables schemas used in the database.

<details>
	<summary>Tables schemas</summary>

### Customer Entity
Each Client has the following attributes:
class Customer(BaseModel):
- id
- name
- created_at
- updated_at
- deleted_at

#### Customer Relationships
For every Customer there can be more than one Job(s), so the relation between Customer and Jobs is 1 → N.

#### Table Structure
Considering what explained above, the data table will have the following structure:

```sql
CREATE TABLE "Customers" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"created_at"	TEXT NOT NULL,
	"updated_at"	TEXT NOT NULL,
	"deleted_at"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

### Job Entity
Each Job has the following attributes:
- id
- name
- description
- created_at
- updated_at
- deleted_at
- customer_id (foreign key)

#### Job Relationships
For every Job there can be more than one Documents(s), so the relation between Jobs and Documents is 1 → N.

#### Table Structure
Considering what explained above, the data table will have the following structure:

```sql
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
)
```

### Document Entity
Each Document has the following attributes:
- id
- name
- description
- created_at
- updated_at
- deleted_at
- job_id (foreign key)

#### Document Relationships
For every Document there can be more than one Revisions, so the relation between Documents and Revisions is 1 → N.

#### Table Structure
Considering what explained above, the data table will have the following structure:

```sql
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
```

### Revision Entity
Each Revision has the following attributes:
- id
- version
- description  
- file_path
- created_at
- updated_at
- deleted_at
- user_id
- document_id

#### Table Structure
Considering what explained above, the data table will have the following structure:

```sql
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
```

### User Entity
Each User has the following attributes:
- id
- name
- surname
- email
- password
- created_at
- updated_at
- deleted_at
- access_level_id (foreign key) # for future use

#### Table Structure
Considering what explained above, the data table will have the following structure:

```sql
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
```

</details>

## Endpoints
In this section, you can find more details about the available endpoints provided by the REST APIs server.

<details>
	<summary>Endpoints</summary>

The available endpoints are:
- /customers
- /jobs
- /documents
- /revisions
- /users

For each endpoint, there is a GET metod without any parameters (query all data), and a GET method with the id path parameter, like:
```
/customers/customer_id
```
where customer_id is a positive integer greater than 0.

As well as the GET method, for each endpoint there is a POST method to create a resource in the database.

</details>

## Test data
The project provides a file named "test_data.py" in the folder "backend\utils\" which is responsible to fill the database with some test data.

## Application features
After creating the functions to fullfill the basic GET and POST methods in order to get and create some resources,  
the web application should be able to:
1. show a list of customers with a summary of how many jobs are associated to it
- once clicking on a customer, the user should access a web page with the info of the customer and the jobs associated to it, with the total number of documents for each job;
- in this page, the user should be able to edit the customer's info, as well as delete it;
2. clicking on a job, the user should access to a web page with the info of the job, the documents associated to it, with the total number of revisions, the last version, the last update timestamp and the last actor for each document;
- in this page, the user should be able to edit the job's info, as well as delete it;
3. clicking on a document, the user should access to a web page with the info of the document, and the revisions associated to it;
- in this page, the user should be able to edit the document's info, as well as delete it.

# SQL queries to fullfill application features
1. Show a list of customers with a summary of how many jobs are associated to it:
```sql
SELECT Customers.name AS 'customer_name',
	   COUNT(Jobs.id) AS 'total_jobs'
FROM Customers
LEFT JOIN Jobs
ON Jobs.customer_id = Customers.id
WHERE Customers.deleted_at IS NULL
GROUP BY Customers.id
ORDER BY Customers.name
```
- once clicking on a customer, the user should access a web page with the info of the customer and the jobs associated to it, with the total number of documents for each job;
```sql
SELECT Jobs.name AS 'job_name',
Jobs.description AS 'job_description',
COUNT(Documents.id) AS 'total_documents'
FROM Customers
LEFT JOIN Jobs
ON Jobs.customer_id = Customers.id
LEFT JOIN Documents
ON Documents.job_id = Jobs.id
WHERE Customers.id = 1 AND
Jobs.deleted_at IS NULL 
GROUP BY Jobs.id
ORDER BY Jobs.name
```

2. clicking on a job, the user should access to a web page with the info of the job, the documents associated to it, with the total number of revisions, the last version, the last update timestamp and the last actor for each document:
```sql
SELECT Documents.name AS 'document_name',
	   Documents.description AS 'document_description',
	   COUNT(Revisions.id) AS 'total_revisions',
	   MAX(Revisions.version) AS 'last_revision',
	   Revisions.updated_at AS 'last_update',
	   Users.name || ' ' || Users.surname AS 'actor'
FROM Jobs
LEFT JOIN Documents
ON Documents.job_id = Jobs.id
LEFT JOIN Revisions
ON Revisions.document_id = Documents.id
LEFT JOIN Users
ON Revisions.user_id = Users.id
WHERE Jobs.id = 3 AND
Documents.deleted_at IS NULL 
GROUP BY Documents.id
ORDER BY Documents.id
```

3. clicking on a document, the user should access to a web page with the info of the document, and the revisions associated to it;
- in this page, the user should be able to edit the document's info, as well as delete it;
```sql
SELECT Revisions.version AS 'document_version',
	   Revisions.updated_at 'document_last_update',
	   Users.name || ' ' || Users.surname AS 'revision_actor'
FROM Documents
LEFT JOIN Revisions
ON Revisions.document_id = Documents.id
LEFT JOIN Users
ON Revisions.user_id = Users.id
WHERE Documents.id = 10
ORDER BY Revisions.version
```