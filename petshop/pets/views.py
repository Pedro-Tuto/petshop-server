from fastapi import APIRouter, Depends
from sqlmodel import Session
from petshop.pets.controllers import create_pet, read_pet, remove_pet
from petshop.database import get_session
from petshop.pets.models import PetCreate, PetRead

router = APIRouter()

@router.post("", response_model=PetRead)
def post_pet(pet_create: PetCreate, db: Session = Depends(get_session)):
    return create_pet(pet_create, db)

@router.get("/{id}", response_model=PetRead)
def get_pet(id: int, db: Session = Depends(get_session)):
    return read_pet(id, db)

@router.delete("/{id}")
def delete_pet(id: int, db: Session = Depends(get_session)):
    remove_pet(id, db)
