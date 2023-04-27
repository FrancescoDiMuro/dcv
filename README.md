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
- id (integer, unique, not null, auto-increment)
- name (text, not null)

<u>#### Client Relationships</u>
A Client is unique, and for every client there can be more than one Job(s), so the relation between Client and Jobs is 1 -> N.

#### Table Structure
Considering what explained above, the table will have the following structure:

```console
CREATE TABLE "Customers" (
"id"	INTEGER NOT NULL UNIQUE,
"name"	TEXT NOT NULL,
PRIMARY KEY("id" AUTOINCREMENT)
)
```

