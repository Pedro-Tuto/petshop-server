from sqlmodel import Session
from petshop.users.models import User


def create_user(user: User, db: Session) -> User:

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

