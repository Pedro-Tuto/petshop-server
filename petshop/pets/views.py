import select
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from petshop.pets.controllers import create_pet, read_pet, remove_pet, list_pets
from petshop.database import get_session
from petshop.pets.models import Pet, PetCreate, PetRead
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

@router.get("/", response_model=list[PetRead])
def get_pets(db: Session = Depends(get_session)):
    return list_pets(db)
