

from sqlite3 import IntegrityError
from time import sleep
import typing
from fastapi import Depends, FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas, utils
from .database import SessionLocal, engine, get_db
import json
from .routers import post, user, auth
models.Base.metadata.create_all(bind=engine)

app = FastAPI()



absolute_path = '/Users/saurav/Developer/repos/phresh/secrets/config.json'
relative_path = '../secrets/config.json'
with open(absolute_path,'r') as f:
    config = json.load(f)

while True:
    try:
        conn = psycopg2.connect(
            host=config['host'], 
            database=config['database'], 
            user=config['user'], 
            password=config['password'],
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        sleep(2)
        print("Connecting to database failed")
        print("Error ",error)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/") 
def root():
    return {"message": "Hello world!"}

# getting all posts


# deleting a post


