from fastapi import HTTPException, status
from app.v1.schema import task_chema, user_schema
from app.v1.model.task_model import Task as Task_Model
from app.v1.utils.db import Session

session = Session()

def create_task(task: task_chema.TaskCreate, user: user_schema.User):
    db_task = Task_Model(
        title = task.title,
        child_id = user.id 
    )
    session.add(db_task)
    session.commit()

    return task_chema.Task(
        id = db_task.id,
        title = db_task.title,
        is_done = db_task.is_done,
        create_at = db_task.create_at
    )

def get_tasks(user: user_schema.User, is_done: bool = None):
    if(is_done is None):
        tasks_by_user = session.query(Task_Model).filter(
            Task_Model.child_id == user.id
        ).order_by(Task_Model.create_at.desc())
    else:
        tasks_by_user = session.query(Task_Model).filter(
            (Task_Model.child_id == user.id) &
            (Task_Model.is_done == is_done)
        ).order_by(Task_Model.create_at.desc())
    
    list_tasks = []
    for task in tasks_by_user:
        list_tasks.append(
            task_chema.Task(
                id = task.id,
                title = task.title,
                is_done = task.is_done,
                create_at = task.create_at
            )
        )
    return list_tasks

def get_task(task_id: int, user: user_schema.User):
    task = session.query(Task_Model).filter(
        (Task_Model.id == task_id) &
        (Task_Model.child_id == user.id)
    ).first()

    if not task:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Task not found"
        )
    
    return task_chema.Task(
        id = task.id,
        title = task.title,
        is_done = task.is_done,
        create_at = task.create_at
    )