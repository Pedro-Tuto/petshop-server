from fastapi import APIRouter, Depends
from sqlmodel import Session
from petshop.users.controllers import create_user
from petshop.database import get_session
from petshop.users.models import User

router = APIRouter()

@router.post('', response_model=User)
def post_user(user: User, db: Session = Depends(get_session)):

    return create_user(user, db)

