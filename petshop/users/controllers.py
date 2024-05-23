from fastapi import Depends, HTTPException, status
from sqlmodel import Session
from petshop.users.models import *


def create_user(user_create: UserCreate, db: Session) -> User:

    user = User.model_validate(user_create)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def read_user(id: int, db: Session) -> User:

    user = db.get(User, id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User com id {id} não encontrado.",
        )

    return user

def remove_user(id: int, db: Session):

    user_to_delete = read_user(id, db)
    db.delete(user_to_delete)
    db.commit()
