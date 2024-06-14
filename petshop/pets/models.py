from sqlmodel import Field, SQLModel, Relationship
from datetime import date
from typing import Optional, List


class PetBase(SQLModel):
    name: str
    date_of_birth: date
    breed: str
    color: str  
    weight: Optional[float] = None  

class Pet(PetBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    owner: Optional["User"] = Relationship(back_populates="pets")   

class PetRead(PetBase):
    id: int
    owner_id: Optional[int] 

class PetCreate(PetBase):
    owner_id: Optional[int] = None  

class PetUpdate(SQLModel):
    name: Optional[str] 
    date_of_birth: Optional[date] 
    breed: Optional[str] 
    color: Optional[str] 
    weight: Optional[float]
    owner_id: Optional[int] 
