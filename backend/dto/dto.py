from datetime import datetime
from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name: str

class Job(BaseModel):
    id: int
    name: str
    description: str
    customer_id: int

class Document(BaseModel):
    id: int
    name: str
    description: str
    job_id: int

class User(BaseModel):
    id: int
    name: str

class Revision(BaseModel):
    id: int
    version: int
    description: str
    timestamp: datetime
    file_path: str
    user_id: int
    document_id: int