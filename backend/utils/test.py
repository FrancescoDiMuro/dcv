from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import Session, sessionmaker


DATABASE_TYPE: str = 'sqlite'
DBAPI: str = 'pysqlite'
DATABASE_NAME: str = 'testdb.db'


# Create the engine to use as ORM
engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}:///{DATABASE_NAME}', echo=True)

with engine.connect() as connection:

        # Use of a sessionmaker (factory) to avoid to specify the engine for every session created
        Session = sessionmaker(engine)

        # Thanks to the sessionmaker, we are able to create a context manager that handles both the Session
        # and the BENIG-COMMIT-ROLLBACK block (thanks to the .begin() function)
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

                data = {'id': 1,
                        'name': 'Francesco',
                        'surname': 'Di Muro',
                        'email': 'dimurofrancesco@virgilio.it',
                        'password': 'somepassword',
                        'access_level_id': 100}

                result = users_table.insert().values(data)

                print(result.description)

        connection.commit()
