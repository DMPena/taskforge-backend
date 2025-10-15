from app.core.database import Base, engine
from app.models import task  # import all models

print("Creating tables in database...")
Base.metadata.create_all(bind=engine)
print("Done.")
