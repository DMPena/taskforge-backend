from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings


# --- Configuration class ---
class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # Tells Pydantic to load environment variables from .env file


# Load settings from .env
settings = Settings()

# --- Create the SQLAlchemy engine ---
# This is the actual connection to the PostgreSQL database.
engine = create_engine(settings.DATABASE_URL)

# --- Create a session factory ---
# Each request will use a new "session" to talk to the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Base class for our models ---
Base = declarative_base()


# --- Dependency to get a DB session ---
# This function will be used with FastAPI's Depends()
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provides a session to whatever function depends on it
    finally:
        db.close()  # Ensures the session closes after each request
