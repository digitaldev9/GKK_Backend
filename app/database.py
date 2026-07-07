import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# PostgreSQL connection URL loaded from .env
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/gkk_backend",
)

# Engine: the actual connection to the DB
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory: creates new DB sessions on demand
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class that our models will inherit from
Base = declarative_base()

# Dependency for FastAPI routes to get a DB session
async def get_db():
    async with SessionLocal() as session:
        yield session