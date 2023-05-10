from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import Session, sessionmaker


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

# Connection to the DB
with engine.connect() as connection:

        # Use of a sessionmaker (factory) to avoid to specify the engine for every session created
        Session = sessionmaker(engine)

        # Thanks to the sessionmaker, we are able to create a context manager that handles both the Session
        # and the BEGIN-COMMIT-ROLLBACK block (thanks to the .begin() function)
        with Session().begin() as session:                
                metadata_obj = MetaData()                
                users_table = Table('Users', 
                                     metadata_obj,
                                     Column('id', Integer, primary_key=True),
                                     Column('name', String(30)),
                                     Column('surname', String(50)),
                                     Column('email', String),
                                     Column('password', String),
                                     Column('access_level_id', Integer))
                
                metadata_obj.create_all(bind=connection)
                                
                # users_table.create(bind=connection)

                data = {'id': 1,
                        'name': 'Francesco',
                        'surname': 'Di Muro',
                        'email': 'dimurofrancesco@virgilio.it',
                        'password': 'somepassword',
                        'access_level_id': 100}

                # result = users_table.insert().values(data)
                ins = users_table.insert().values(id=1, name='a', surname='b', email='c', password='d', access_level_id=100)
                connection.execute(ins)
                connection.commit()
                
                
                
