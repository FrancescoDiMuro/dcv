from pydantic import BaseModel

class Customer(BaseModel):
    id: int | None = None
    name: str
    created_at: str | None = None
    updated_at: str | None = None
    deleted_at: str | None = None

class Job(BaseModel):
    id: int | None = None
    name: str
    description: str
    created_at: str | None = None
    updated_at: str | None = None
    deleted_at: str | None = None
    customer_id: int

class Document(BaseModel):
    id: int | None = None
    name: str
    description: str
    created_at: str | None = None
    updated_at: str | None = None
    deleted_at: str | None = None
    job_id: int

class Revision(BaseModel):
    id: int | None = None
    version: str
    description: str    
    file_path: str
    created_at: str | None = None
    updated_at: str | None = None
    deleted_at: str | None = None
    user_id: int
    document_id: int    

class User(BaseModel):
    id: int | None = None
    name: str
    surname: str
    email: str
    password: str
    created_at: str | None = None
    updated_at: str | None = None
    deleted_at: str | None = None
    access_level_id: int | None = None