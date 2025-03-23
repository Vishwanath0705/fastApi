from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, models, schemas, hashing
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

get_db = database.get_db

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated = "auto")

@router.post("/", response_model=schemas.ShowUser)
def create_user(request : schemas.User, db:Session = Depends(get_db)):
    return user.createUser(request, db)

@router.get("/{id}", response_model = schemas.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get_user(id, db)