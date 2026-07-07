from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite DB file will be created in project root as gkk_backend.db
DATABASE_URL = "sqlite+aiosqlite:///./gkk_backend.db"

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