from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import engine, Base, get_db
from app.schemas import UserCreate, UserResponse
from app.models import User
from app.auth import get_current_user
from app import crud

app = FastAPI(title="GKK_Backend - Auth PoC")


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_username = await crud.get_user_by_username(db, user_data.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    existing_email = await crud.get_user_by_email(db, user_data.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = await crud.create_user(db, user_data)
    return new_user


@app.get("/login")
async def login(current_user: User = Depends(get_current_user)):
    return {"message": f"Login successful. Welcome, {current_user.username}!"}


@app.get("/me", response_model=UserResponse)
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user