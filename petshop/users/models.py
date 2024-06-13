from typing import Optional, TYPE_CHECKING, List
if TYPE_CHECKING:
    from petshop.pets.models import Pet
from sqlmodel import Field, SQLModel, Relationship


class UserBase(SQLModel):
    name: str
    email: str
    phone: str 
    address: str 

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str
    pets: List["Pet"] = Relationship(back_populates="owner")

class UserRead(UserBase):
    id: int

class UserCreate(UserBase):
    password: str
