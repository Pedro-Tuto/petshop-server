from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from petshop.users.models import User, UserCreate, UserUpdate
from typing import List

def create_user(user_create: UserCreate, db: Session) -> User:
    user = User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def read_user(id: int, db: Session) -> User:
    user = db.get(User, id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found.",
        )
    return user

def remove_user(id: int, db: Session):
    user_to_delete = read_user(id, db)
    db.delete(user_to_delete)
    db.commit()

def list_users(db: Session) -> List[User]:
    users = db.exec(select(User)).all()
    return users


def update_user(id: int, user_update: UserUpdate, db: Session) -> User:
    user = read_user(id, db)
    print(user)
    user_data = user_update.model_dump(exclude_unset=True)
    print(user_data)
    user.sqlmodel_update(user_data)
    print(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user