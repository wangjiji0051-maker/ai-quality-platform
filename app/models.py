from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import datetime

class TaskType(str, enum.Enum):
    SMOKE = "smoke"
    REGRESSION = "regression"

class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

class TestTask(Base):
    __tablename__ = "test_tasks"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    mr_info = Column(String, nullable=True)
    task_type = Column(Enum(TaskType))
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    # 关联测试结果
    test_results = relationship("TestResult", back_populates="task")

class TestResult(Base):
    __tablename__ = "test_results"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("test_tasks.id"))
    case_name = Column(String)
    status = Column(String) # passed / failed / skipped
    log_content = Column(Text, nullable=True)
    error_msg = Column(Text, nullable=True)
    ai_root_cause = Column(Text, nullable=True) # 留给AI分析输出
    ai_cause_type = Column(String, nullable=True) # 代码问题 / 脚本问题 / 环境问题 / 其他

    task = relationship("TestTask", back_populates="test_results")
