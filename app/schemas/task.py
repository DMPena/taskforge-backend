from pydantic import BaseModel
from typing import Optional

# --- Input schema (when creating a new task) ---
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False


# --- Output schema (what we return to clients) ---
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True  # Allows conversion from SQLAlchemy model to Pydantic model
