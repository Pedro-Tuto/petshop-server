from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from petshop.pets.models import Pet, PetCreate, PetUpdate
from typing import List
from petshop.users.models import User

def create_pet(pet_create: PetCreate, db: Session) -> Pet:
    pet = Pet.from_orm(pet_create)
    if pet_create.owner_id:
        owner = db.get(User, pet_create.owner_id)
        if owner is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found")
        pet.owner = owner
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

def read_pet(id: int, db: Session) -> Pet:
    pet = db.get(Pet, id)
    if pet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pet with id {id} not found.",
        )
    return pet

def remove_pet(id: int, db: Session):
    pet_to_delete = read_pet(id, db)
    db.delete(pet_to_delete)
    db.commit()

def list_pets(db: Session) -> List[Pet]:
    pets = db.exec(select(Pet)).all()
    return pets

def update_pet(id: int, pet_update: PetUpdate, db: Session) -> Pet:
    pet = read_pet(id, db)
    pet_data = pet_update.dict(exclude_unset=True)

    if "owner_id" in pet_data and pet_data["owner_id"] is not None:
        owner = db.get(User, pet_data["owner_id"])
        if owner is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found")

    for key, value in pet_data.items():
        setattr(pet, key, value)
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet
