from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from typing import Annotated
from sqlalchemy import select


router = APIRouter(tags=["task"])

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).filter(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).filter(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    task_data = Task(**task.model_dump(), user_id=user_id)
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalar(select(Task).filter(Task.id == task_id))
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(existing_task, key, value)
    db.commit()
    db.refresh(existing_task)
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}


@router.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).filter(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task deletion is successful!"}
