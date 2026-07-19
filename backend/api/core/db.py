from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from api.core.config import settings

# Create engine
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create declarative base for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=engine)