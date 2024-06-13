from sqlmodel import Session, SQLModel, create_engine
from petshop.config import settings
from petshop.users.models import User
from petshop.pets.models import Pet
from sqlalchemy import text

connect_args = {"check_same_thread": False}
engine = create_engine(settings.DATABASE_URI, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.execute(text("PRAGMA foreign_keys = ON;"))

def get_session():
    with Session(engine) as session:
        yield session
