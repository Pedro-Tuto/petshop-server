from sqlmodel import Field, SQLModel
from datetime import date

class PetBase(SQLModel):
    name: str
    date_of_birth: date
    breed: str

class Pet(PetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PetRead(PetBase):
    id: int

class PetCreate(PetBase):
    pass
