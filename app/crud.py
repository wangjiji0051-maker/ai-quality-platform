from sqlalchemy.orm import Session
from app import models, schemas

# 创建测试任务
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.TestTask(
        mr_info=task.mr_info,
        task_type=task.task_type,
        status="pending"
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# 根据id查询任务
def get_task_by_id(db: Session, task_id: int):
    return db.query(models.TestTask).filter(models.TestTask.id == task_id).first()

# 更新任务状态
def update_task_status(db: Session, task_id:int, status:str):
    task = get_task_by_id(db, task_id)
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task

# 添加测试结果
def add_test_result(db: Session, task_id:int, case_name:str, status:str, log_content:str, error_msg:str):
    new_result = models.TestResult(
        task_id = task_id,
        case_name = case_name,
        status = status,
        log_content = log_content,
        error_msg = error_msg,
        ai_root_cause = "",
        ai_cause_type = ""
    )
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result

# 根据任务id查询所有测试结果
def get_results_by_task_id(db:Session, task_id:int):
    return db.query(models.TestResult).filter(models.TestResult.task_id == task_id).all()
