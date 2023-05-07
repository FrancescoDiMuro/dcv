# Project DCV
This is a personal project for building a DCV (Document Control Version).

## Database structure
To make the project easier to build, I created a local SQLite3 db in which store data.
The entities in the db are:
- Customer
- Job
- Document
- Revision
- User

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
