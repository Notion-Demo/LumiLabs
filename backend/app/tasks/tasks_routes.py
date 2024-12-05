from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Task
from database import get_db

router = APIRouter()

@router.get("/")
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.post("/")
def create_task(title: str, description: str, assigned_to: int, db: Session = Depends(get_db)):
    task = Task(title=title, description=description, assigned_to=assigned_to)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
