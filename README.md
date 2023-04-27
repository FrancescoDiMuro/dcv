# Project DCV
This is a personal project for building a DCV (Document Control Version).

## Database structure
To make the project easier to build, I created a local SQLite3 db in which store data.
The entities in the db are:
- Client
- Job
- Document
- Revision
- User

### Client Entity
Each Client has the following attributes:
- id
- name

#### Client Relationships
A Client is unique, and for every Client there can be more than one Job(s), so the relation between Client and Jobs is 1 → N.

#### Table Structure
Considering what explained above, the data table will have the following structure:

```console
CREATE TABLE "Customers" (
    "id"	INTEGER NOT NULL UNIQUE,
    "name"	TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
)
```

### Job Entity
Each Job has the following attributes:
- id
- name
- description
- customer_id (foreign key)

#### Job Relationships
A Job is unique, and for every Job there can be more than one Documents(s), so the relation between Jobs and Documents is 1 → N.

#### Table Structure
Considering what explained above, the data table will have the following structure:

```console
CREATE TABLE "Jobs" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"customer_id"	INTEGER NOT NULL,
	FOREIGN KEY("customer_id") REFERENCES "Customers"("id") ON DELETE CASCADE,
	PRIMARY KEY("id" AUTOINCREMENT)
)
```

#### Table Integrity Checks
If a Customer is deleted from the corresponding table, all the Jobs will have an id which is no longer referencing to any Customer,
causing to have invalid data.
To avoid this behaviour, an integrity check **ON DELETE CASCADE** has been added to the foreign key customer_id, so if a Customer is deleted,
all the Job(s) referred to it will be deleted as well.

### Document Entity
Each Document has the following attributes:
- id
- name
- description
- job_id (foreign key)

#### Document Relationships
A Document is unique, and for every Document there can be more than one Revision(s), so the relation between Documents and Revisions is 1 → N.

#### Table Structure
Considering what explained above, the data table will have the following structure:

```console
CREATE TABLE "Documents" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"job_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("job_id") REFERENCES "Jobs"("id") ON DELETE CASCADE
)
```

#### Table Integrity Checks
If a Job is deleted from the corresponding table, all the Documents will have an id which is no longer referencing to any Job,
causing to have invalid data.
To avoid this behaviour, an integrity check **ON DELETE CASCADE** has been added to the foreign key job_id, so if a Job is deleted,
all the Document(s) referred to it will be deleted as well.