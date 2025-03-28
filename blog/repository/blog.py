from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(blog: schemas.Blog, db:Session):
    new_blog = models.Blog(title = blog.title, body = blog.body, user_id = 1    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destry(id, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(id, request:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    blog.update(request.model_dump())
    db.commit()
    return "updated"

def show(id, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not available.")
        # response.status_code = status.HTTP_404_NOT_FOUND    
        # return {'detail': f"Blog with {id} is not available."}
    return blog