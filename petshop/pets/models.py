from sqlmodel import Field, SQLModel, Relationship
from datetime import date
from typing import Optional, List

class PetBase(SQLModel):
    name: str
    date_of_birth: date
    breed: str
    color: str  # Novo atributo
    weight: Optional [float] = None # Novo atributo

class Pet(PetBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    owner: Optional["User"] = Relationship(back_populates="pets") # Relacionamento com User

class PetRead(PetBase):
    id: int
    owner_id: Optional[int]  # Adicione o owner_id

class PetCreate(PetBase):
    owner_id: Optional[int] = None  # Adicione o owner_id