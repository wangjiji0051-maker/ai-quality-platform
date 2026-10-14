
from fastapi import HTTPException

from app.models import Task
from app.repository.task_repository import tasks, save, find_all, find_by_id
from app.schemas import TestTaskCreate, TaskResponse

next_task_id = 1
def create_task(task_create: TestTaskCreate) -> TaskResponse:
    """
创建一个新的测试任务。

参数：
    task_create：用户提交的任务信息。

返回：
    TaskResponse：创建成功后的响应。
"""
    global next_task_id
    # 根据用户提交的数据，创建系统内部的 Task 对象
    task = Task(
        task_id=next_task_id,
        # 模拟数据库生成的任务 ID
        repository=task_create.repository,             # 仓库名称
        branch=task_create.branch,                     # 分支名称
        merge_request_id=task_create.merge_request_id, # Merge Request 编号
        environment=task_create.environment,           # 测试环境
        test_type=task_create.test_type,               # 测试类型
        status="pending",                       # 新任务默认状态
    )
    save(task)
    next_task_id+=1
    # 返回创建结果
    return TaskResponse(
        message="Task created",  # 提示信息
        task=task                # 创建好的任务对象
    )

def get_tasks() -> list[Task]:
    return find_all()

def get_task(task_id: int) -> Task:
    task = find_by_id(task_id)

    if task is None:
        raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

    return task

def delete_task(task_id: int):
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            return
    raise HTTPException(
            status_code=404,
            detail="Task not found"
        )