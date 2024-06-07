from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    nome: str
    email: str

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str

class UserRead(UserBase):
    id: int

class UserCreate(UserBase):
    password: str
