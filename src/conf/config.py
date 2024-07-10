class Config:
    DB_URL = "postgresql+asyncpg://postgres:150209@localhost:5432/contacts"

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///database.db"

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_sessionmaker = sessionmaker(class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False)

config = Config

import os

CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
