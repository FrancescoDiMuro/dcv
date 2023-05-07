# Project DCV
This is a personal project for building a DCV (Document Control Version) application.

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
	FOREIGN KEY("job_id") REFERENCES "Jobs"("id") ON DELETE CASCADE
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

<details>
	<summary>Endpoints</summary>

The available endpoints are:
- /customers
- /jobs
- /documents
- /revisions
- /users

For each endpoint, there is a GET metod without any parameters (query all data), and a GET method with the id path parameter, like: 
/customers/customer_id

As well as the GET method, for each endpoint there is a POST parameter to create a resource
in the database.

</details>