from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import Session
from petshop.pets.models import Pet, PetCreate, PetRead
from petshop.pets.crud import PetCRUD
from petshop.database import get_session

router = APIRouter()
crud = PetCRUD()

@router.post("/", response_model=PetRead)
def create_pet(pet: PetCreate, db: Session = Depends(get_session)):
    return crud.create_pet(Pet(**pet.dict()))



@router.get("/{pet_id}", response_model=PetRead)
def read_pet(pet_id: int, db: Session = Depends(get_session)):
    pet = crud.read_pet(pet_id)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet com o id {id} não encontrado")
    return pet



@router.delete("/{pet_id}", response_model=bool)
def delete_pet(pet_id: int, db: Session = Depends(get_session)):
    success = crud.delete_pet(pet_id)
    if not success:
        raise HTTPException(status_code=404, detail="Pet com o id {id} não encontrado")
    return success
