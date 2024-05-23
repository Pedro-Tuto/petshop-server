from fastapi import APIRouter, Depends
from sqlmodel import Session
from petshop.users.controllers import *
from petshop.database import get_session
from petshop.users.models import *

router = APIRouter()

@router.post('', response_model=UserRead)
def post_user(user_create: UserCreate, db: Session = Depends(get_session)):

    return create_user(user_create, db)


@router.get('/{id}', response_model=UserRead)
def get_user(id: int, db: Session = Depends(get_session)):

    return read_user(id, db) 

@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_session)):

    remove_user(id, db)
