from app.core.database import SessionLocal
from sqlalchemy.orm import Session

# Dependency that provides a database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
