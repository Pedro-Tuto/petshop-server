from sqlmodel import Field, SQLModel



class User(SQLModel, table=True):


    id: str=Field(default=None, primary_key=True)
    name: str
    email: str
