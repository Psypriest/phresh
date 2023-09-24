from sqlite3 import DatabaseError
from pydantic import BaseModel
from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

path = '/Users/saurav/Developer/repos/phresh/secrets/config.json'

with open(path,'r') as f:
    config = json.load(f)


user_name = config['user']
password = config['password']
database = config['database']
hostname = config['host']
port = config['port']

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address>/<hostname>/<database-name>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{user_name}:{password}@localhost/{database}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()