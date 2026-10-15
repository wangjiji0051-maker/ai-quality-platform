from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.models import TaskType, TaskStatus

class TaskCreate(BaseModel):
    mr_info: Optional[str] = None
    task_type: TaskType

class TaskOut(BaseModel):
    id: int
    mr_info: Optional[str]
    task_type: TaskType
    status: TaskStatus
    created_at: datetime
    finished_at: Optional[datetime]

    class Config:
        from_attributes = True


class TestResultOut(BaseModel):
    id: int
    task_id: int
    case_name: str
    status: str
    log_content: Optional[str]
    error_msg: Optional[str]
    ai_root_cause: Optional[str]
    ai_cause_type: Optional[str]

    class Config:
        from_attributes = True
