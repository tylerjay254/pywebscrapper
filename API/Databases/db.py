from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


print('booting database ...')

#USING SQLITE
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


#USING POSTGRESQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:PASSWORD@localhost/DATABASE"



# start db engine

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Dependency


def get_db():
    print("contacting database...")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()