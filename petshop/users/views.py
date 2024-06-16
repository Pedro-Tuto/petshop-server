from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from petshop.users.controllers import create_user, read_user, remove_user, list_users, update_user
from petshop.database import get_session
from petshop.users.models import User, UserCreate, UserRead, UserUpdate
from typing import List

router = APIRouter()

@router.post("", response_model=UserRead)
def post_user(user_create: UserCreate, db: Session = Depends(get_session)):
    return create_user(user_create, db)

@router.get("/{id}", response_model=UserRead)
def get_user(id: int, db: Session = Depends(get_session)):
    return read_user(id, db)

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_session)):
    remove_user(id, db)

@router.get("/", response_model=List[UserRead])
def list_users(db: Session = Depends(get_session)):
    users = db.exec(select(User)).all()
    return users

@router.patch("/{id}", response_model=UserRead)
def patch_user(id: int, user_update: UserUpdate, db: Session = Depends(get_session)):
    return update_user(id, user_update, db)
