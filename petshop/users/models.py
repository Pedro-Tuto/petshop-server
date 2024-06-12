from petshop.pets.models import Pet
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class UserBase(SQLModel):
    name: str
    email: str
    phone: str  # Novo atributo
    address: str  # Novo atributo

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str
    pets: List["Pet"] = Relationship(back_populates="owner")  # Relacionamento com Pet

class UserRead(UserBase):
    id: int

class UserCreate(UserBase):
    password: str
