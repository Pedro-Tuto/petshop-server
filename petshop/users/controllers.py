from sqlmodel import Session
from petshop.users.models import *

def create_user(user_create: UserCreate, db: Session) -> User:

    user = User.model_validate(user_create)

    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

