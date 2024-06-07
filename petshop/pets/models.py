from sqlmodel import Field, SQLModel

class PetBase(SQLModel):
    nome: str
    idade: int
    raça: str

class Pet(PetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PetRead(PetBase):
    id: int

class PetCreate(PetBase):
    pass
