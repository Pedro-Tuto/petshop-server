from fastapi import Depends, HTTPException, status
from sqlmodel import Session
from petshop.pets.models import Pet, PetCreate

def create_pet(pet_create: PetCreate, db: Session) -> Pet:
    pet = Pet.model_validate(pet_create)
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

def read_pet(id: int, db: Session) -> Pet:
    pet = db.get(Pet, id)
    if pet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"pet com id {id} não encontrado.",
        )
    return pet

def remove_pet(id: int, db: Session):
    pet_to_delete = read_pet(id, db)
    db.delete(pet_to_delete)
    db.commit()
