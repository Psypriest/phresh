from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

from app.database import Base


# extending the base model
# defines the structure of a request and response

    
class PostBase(BaseModel):
    title: str 
    content: str 
    published: bool = True 
    
class PostCreate(PostBase):
    pass 

class Post(PostBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str 

class UserOut(BaseModel):
    id: int 
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

    
class UserLogin(BaseModel):
    email: EmailStr
    password: str 
    

class Token(BaseModel):
    access_token: str 
    token_type: str 
    
class TokenData(BaseModel):
    id: Optional[str] = None 
    created_at = datetime
    
    class Config: 
        orm_mode = True
    


    


