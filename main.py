from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.get("/blog")
def index(limit = 10, published: bool = True, sort:Optional[str] = None):
    if published:
        return {'data' : f"{limit} published blogs from db"}
    else:
        return {"data" : f"{limit} blogs from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data" : "All unpublished blogs"}

@app.get("/blog/{id}/comments")
def comments(id, limit = 10):
    return {"data" :  {'1', '2'}}

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post("/blog")
def create_blog(blog : Blog):
    return {"data" : f"Blog is created with title as {blog.title}"}