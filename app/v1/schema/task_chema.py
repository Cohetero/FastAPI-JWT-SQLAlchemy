from datetime import datetime
from pydantic import BaseModel
from pydantic import Field

class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        min_length = 1,
        max_length = 60,
        example = "My first task"  
    )

class Task(TaskCreate):
    id: int = Field(...)
    is_done: bool = Field(default=False)
    create_at: datetime = Field(default=datetime.now())