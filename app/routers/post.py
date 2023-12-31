
from click import get_current_context
from app import oauth2
from .. import models, schemas, oauth2

from fastapi import status, Depends, HTTPException, Response, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
import typing 

router = APIRouter(
    prefix="/posts",
    tags = ['Posts']
)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Post with id {id} doesn\'t exist'
        )
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update post
@router.put("/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id: {id} doesn\'t exist')
    post_query.update(updated_post.dict(), synchronize_session = False)
    db.commit()
    return post_query.first()
    
    

@router.get("/", status_code=status.HTTP_200_OK, response_model=typing.List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    posts = db.query(models.Post).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with Id {id} not found.")
    return post
    
    
