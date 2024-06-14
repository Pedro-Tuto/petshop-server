import select
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from petshop.pets.controllers import create_pet, read_pet, remove_pet, list_pets, update_pet
from petshop.database import get_session
from petshop.pets.models import Pet, PetCreate, PetRead, PetUpdate
from typing import List

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

@router.get("/", response_model=List[PetRead])
def get_pets(db: Session = Depends(get_session)):
    return list_pets(db)

@router.patch("/{id}", response_model=PetRead)
def patch_pet(id: int, pet_update: PetUpdate, db: Session = Depends(get_session)):
    return update_pet(id, pet_update, db)
