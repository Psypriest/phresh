# FastAPI

Following https://www.youtube.com/watch?v=0sOvCWFmrtA

## What is a path operation

```python
# pather operation in some langs its  also called routes.
# app is the fast api instance. get here is the http method. "/" is the path
@app.get("/")  # decorator. Its gonna perform a little magic. 
def root():
    # whatever return here is the data that gets sent back to the user.
    return {"message": "Welcome to my api!!!"}
```

## Why do we need schema?

- Its a pain to get all the values form the body.
- The client can send whatever data they want
- the data isn't getting validated
- We ultimately want to force the client to send data in a schema that we expect. 

## CRUD

- Always use plura. Request is post. Path is going to be /posts
- While updating you can put or patch. While using put you have to send all fields while using patch you can change just one specific field.
- Create: POST, /posts ```python @app.post("/posts")```
- Read: 
  - GET, /posts/:id ```python @app.get("/posts/{id}")```
  - GET, /posts  ```python @app.get("/posts")```
- Update  PUT/PATCH /posts ```python @app.put("posts/{id}")```
- Delete   DELETE /posts/:id ```python @app.delete("posts/{id}")```

## What is a Database?

- Collection of organized data that can be easily accessed and managed.
- Structured query language (SQL)  

## Postgres

- Each instance of postgres can be carved into multiple seperate databases.
- `pip install psycopg2-binary`

## ORM

- ORM is a layer of abstraction that sits between the database and us 
- We can perform all database operations through traditional python code. No more SQL!
- Benefits:
  - Queries can be made exclusively with python cod. No SQL necessary.
  - Instead of manually defining tables in postgres, we can define our tables as python modules.

## Authentication

- Two main ways:
  - Session: We store some thing in the backedn the confirm if the user is logged in.
  - JWT: This is stateless. Nothing in backend, api, or db. The token itself which we don't store, its in the frontend, keeps track. One of the simpler solutions.
    - What is a JWT Token?: JWT token is not encrypted.
    - Made of 3 individual comps:
      - Headers: has algorithm like HS256 and type which is JWT.
      - Payload: The payload of the token is up to us. You have to be careful with what you put in the payload. because its not ecrypted. So no secrets. We can include a role, any info like . The more info we putin the packet size is going to be bigger and its gonna take more time for auth.
      - Verify Signature:
        - Why signature? The signature ensure that the data integrity is still valid. That no one has changed anything in that payload.
    - Anybody can changed the data of the token they can see the data of the token they just can't generate a new signature because they don't have the password.
  - Hash is just a oneway ride. So when the user sends the plain text password the application will hash it and check it with the hashed password that is already saved in the db. When the hashes match that is when the passwords match. When it doesn't.