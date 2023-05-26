import sqlite3
import sqlalchemy
from typing import List
from datetime import datetime, timezone
from os import getcwd


WORKING_DIR: str = getcwd()
BACKEND_DIR = f'{WORKING_DIR}\\backend'
DATABASE_DIR: str = f'{BACKEND_DIR}\\dcv.db'

def ISO8601_now():    
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')
