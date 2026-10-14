from fastapi import FastAPI

from app.models import Task
from app.schemas import TestTaskCreate, TaskResponse
from app.services.task_service import (
    create_task,
    delete_task,
    get_task,
    get_tasks,
)


# 创建 FastAPI 应用
app = FastAPI(
    title="AI Quality Platform",  # 项目名称，会显示在 Swagger 页面
    version="0.1.0",              # 当前项目版本
)


# 健康检查接口
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


# 创建测试任务
@app.post("/task", status_code=201)
def create_task_route(task_create: TestTaskCreate) -> TaskResponse:
    return create_task(task_create)


# 查询全部任务
@app.get("/tasks")
def get_tasks_route() -> list[Task]:
    return get_tasks()


# 根据任务 ID 查询单个任务
@app.get("/task/{task_id}")
def get_task_route(task_id: int) -> Task:
    return get_task(task_id)


# 根据任务 ID 删除任务
@app.delete("/task/{task_id}", status_code=204)
def delete_task_route(task_id: int) -> None:
    delete_task(task_id)