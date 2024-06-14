from contextlib import asynccontextmanager
from fastapi import FastAPI
from petshop.users.views import router as user_router
from petshop.pets.views import router as pet_router
from petshop.config import Settings, settings
from petshop.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
        lifespan=lifespan,
    )
    app.include_router(user_router, prefix="/users")
    app.include_router(pet_router, prefix="/pets")
    return app

app = create_app(settings)
