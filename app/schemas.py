from pydantic import BaseModel, Field
from typing import Literal

from app.models import Task


# ===========================
# 创建任务时，客户端提交的数据
# ===========================
class TestTaskCreate(BaseModel):
    # Git 仓库名称，例如：ai-quality-platform
    repository: str = Field(min_length=1)

    # Git 分支名称，例如：main、develop
    branch: str = Field(min_length=1)

    # Merge Request（合并请求）编号，必须大于 0
    merge_request_id: int = Field(gt=0)

    # 测试环境，只允许下面三个值
    environment: Literal["test", "staging", "production"]

    # 测试类型，只允许下面两个值
    test_type: Literal["smoke", "regression"]


# ===========================
# 创建任务接口返回的数据
# ===========================
class TaskResponse(BaseModel):

    # 返回给客户端的提示信息
    message: str

    # 创建完成后的任务对象
    task: Task

class TaskListResponse(BaseModel):
    tasks: list[Task]