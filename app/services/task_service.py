from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate
from app.schemas.task import TaskUpdate

# --- READ ALL TASKS ---
def get_tasks(db: Session):
    return db.query(Task).all()

# --- READ ONE TASK ---
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# --- CREATE TASK ---
def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())  # Converts schema -> SQLAlchemy model
    db.add(db_task)
    db.commit()
    db.refresh(db_task)  # Refresh to get generated ID
    return db_task

# --- DELETE TASK ---
def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task

# --- UPDATE TASK ---
def update_task(db: Session, task_id: int, changes: TaskUpdate):
    task = get_task(db, task_id)
    if not task:
        return None
    for key, value in changes.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task