from pydantic import BaseModel, Field
from typing import Literal


# ===========================
# 系统内部真正保存的任务对象
# ===========================
class Task(BaseModel):

    # Git 仓库名称
    repository: str = Field(min_length=1)

    # Git 分支名称
    branch: str = Field(min_length=1)

    # Merge Request 编号
    merge_request_id: int = Field(gt=0)

    # 测试环境
    environment: Literal["test", "staging", "production"]

    # 测试类型
    test_type: Literal["smoke", "regression"]

    # 系统生成的任务 ID
    task_id: int

    # 当前任务状态
    # pending：等待中
    # running：执行中
    # success：成功
    # failed：失败
    status: Literal["pending", "running", "success", "failed"]

class Report(BaseModel):
    id: int
    task_id: int
    summary: str
    ai_analysis: str
    status: str
