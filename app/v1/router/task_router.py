from fastapi import APIRouter, Depends, Body, status, Query, Path
from app.v1.schema import task_chema
from app.v1.service import task_service
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user
from app.v1.utils.db import Session
from typing import List, Optional

task_route = APIRouter(
    prefix="/api/v1",
    tags=["task"])

@task_route.post(
    '/task',
    status_code=status.HTTP_201_CREATED,
    response_model=task_chema.Task)
def create_task(task: task_chema.TaskCreate = Body(...), current_user: User = Depends(get_current_user)):
    return task_service.create_task(task, current_user)

@task_route.get(
    '/task',
    status_code = status.HTTP_200_OK,
    response_model = List[task_chema.Task])
def get_tasks(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return task_service.get_tasks(current_user, is_done)

@task_route.get(
    '/task/{task_id}',
    status_code = status.HTTP_200_OK,
    response_model = task_chema.Task)
def get_task(
    task_id: int = Path(
        ...,
        gt = 0
    ),
    current_user: User = Depends(get_current_user)
):
    return task_service.get_task(task_id, current_user)