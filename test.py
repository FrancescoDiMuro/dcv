from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from backend.schemas.models import User, Base
from backend.utils.test_data import test_users
from backend.utils.utils import ISO8601_now


DATABASE_TYPE: str = 'sqlite'
DBAPI: str = 'pysqlite'
DATABASE_NAME: str = 'testdb.db'


# Create the engine to use as ORM
# The creation of the engine estabilshes a lazy inizialization, since the connection is effectively
# estabilished when the method .connect() (or .execute()) is called
# URL passed to the engine can be a literal string with this format:
# dialect+driver://username:password@host:port/database
# dialect = rdbms name
# driver = driver used to communicate with dialect
# # or it can be a URL object, which is preferred since it escapes automatically special characters such as @

engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}:///{DATABASE_NAME}', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

with Session.begin() as session:
    
    # for test_user in test_users:
    #     test_user['created_at'] = ISO8601_now()
    #     test_user['updated_at'] = ISO8601_now()
    #     session.add(User(**test_user))

    result = session.query(User).all()
    print(result)