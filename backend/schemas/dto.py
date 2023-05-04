from datetime import datetime
from pydantic import BaseModel
from backend.utils.utils import ISO8601_now

class Customer(BaseModel):
    id: int | None = None
    name: str
    created_at: datetime = ISO8601_now
    updated_at: datetime = ISO8601_now
    deleted_at: datetime | None = None

class Job(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    customer_id: int

class Document(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    job_id: int

class Revision(BaseModel):
    id: int
    version: str
    description: str    
    file_path: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    user_id: int
    document_id: int    

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    access_level_id: int