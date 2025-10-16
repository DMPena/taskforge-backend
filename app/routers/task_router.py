from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_db
from app.schemas.task import Task, TaskCreate
from app.services import task_service
from app.schemas.task import TaskUpdate

router = APIRouter(
    prefix="/tasks",  # URL prefix for all routes in this router
    tags=["Tasks"],   # Group name for Swagger UI
)

# --- GET /tasks ---
@router.get("/", response_model=List[Task])
def read_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)

# --- GET /tasks/{id} ---
@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# --- POST /tasks ---
@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task)

# --- DELETE /tasks/{id} ---
@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# --- PATCH /tasks/{id} ---

@router.patch("/{task_id}", response_model=Task)
def patch_task(task_id: int, changes: TaskUpdate, db: Session = Depends(get_db)):
    updated = task_service.update_task(db, task_id, changes)
    if not updated:
        raise HTTPException(404, "Task not found")
    return updated