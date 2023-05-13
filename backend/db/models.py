from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Identity, ForeignKey


# Creation of the declarative base, use to declare all other models
Base = declarative_base()

class User(Base):

    __tablename__ = 'Users'

    id = Column('id', Integer, Identity(), primary_key=True, nullable=False)
    name = Column('name', String, nullable=False)
    surname = Column('surname', String, nullable=False)
    email = Column('email', String, nullable=False)
    password = Column('password', String, nullable=False)
    created_at = Column('created_at', String, nullable=False)
    updated_at = Column('updated_at', String, nullable=False)
    deleted_at = Column('deleted_at', String, nullable=True, default=None)
    access_level_id = Column('access_level_id', String, nullable=False)

    def __init__(self, name: str, surname: str, email: str, password: str, 
                 created_at: str | None = None, updated_at: str | None = None, 
                 access_level_id: int | None = None):
        
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        self.access_level_id = access_level_id

    def __repr__(self):
        return f'User (id = {self.id}, name = {self.name}, surname = {self.surname})'


class Customer(Base):

    __tablename__ = 'Customers'

    id = Column('id', Integer, Identity(), primary_key=True, nullable=False)
    name = Column('name', String, nullable=False)    
    created_at = Column('created_at', String, nullable=False)
    updated_at = Column('updated_at', String, nullable=False)
    deleted_at = Column('deleted_at', String)

    def __init__(self, name: str, created_at: str | None = None, updated_at: str | None = None, deleted_at: str | None = None):
        
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return f'Customer (id = {self.id}, name = {self.name})'


class Job(Base):

    __tablename__ = 'Jobs'

    id = Column('id', Integer, Identity(), primary_key=True, nullable=False)
    name = Column('name', String, nullable=False)
    description = Column('description', String, nullable=False)
    created_at = Column('created_at', String, nullable=False)
    updated_at = Column('updated_at', String, nullable=False)
    deleted_at = Column('deleted_at', String)
    customer_id = Column(Integer, ForeignKey('Customers.id'), nullable=False) 

    def __init__(self, name: str, description: str, 
                 created_at: str | None = None, updated_at: str | None = None,
                 customer_id: int | None = None):
        
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.customer_id = customer_id

    def __repr__(self):
        return f'Job (id = {self.id}, name = {self.name})'
    

class Document(Base):

    __tablename__ = 'Documents'

    id = Column('id', Integer, Identity(), primary_key=True, nullable=False)
    name = Column('name', String, nullable=False)
    description = Column('description', String, nullable=False)
    created_at = Column('created_at', String, nullable=False)
    updated_at = Column('updated_at', String, nullable=False)
    deleted_at = Column('deleted_at', String)
    job_id = Column(Integer, ForeignKey('Jobs.id'), nullable=False)

    def __init__(self, name: str, description: str, 
                 created_at: str | None = None, updated_at: str | None = None,
                 job_id: int | None = None):
        
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.job_id = job_id

    def __repr__(self):
        return f'Document (id = {self.id}, name = {self.name})'
    

class Revision(Base):

    __tablename__ = 'Revisions'

    id = Column('id', Integer, Identity(), primary_key=True, nullable=False)
    version = Column('version', String, nullable=False)
    description = Column('description', String, nullable=False)
    file_path = Column('file_path', String, nullable=False)
    created_at = Column('created_at', String, nullable=False)
    updated_at = Column('updated_at', String, nullable=False)
    deleted_at = Column('deleted_at', String)
    user_id = Column('user_id', Integer, ForeignKey('Users.id'), nullable=False)
    document_id = Column(Integer, ForeignKey('Documents.id'), nullable=False)

    def __init__(self, version: str, description: str, file_path: str,
                 created_at: str | None = None, updated_at: str | None = None,
                 user_id: int | None = None, document_id: int | None = None):
        
        self.version = version
        self.description = description
        self.file_path = file_path
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id
        self.document_id = document_id

    def __repr__(self):
        return f'Revision (id = {self.id}, version = {self.version}, document_id = {self.document_id})'
