from app.database import SessionLocal
from app import crud

def run_test_task(task_id: int, task_type: str):
    # 在子线程单独创建会话，解决线程不安全问题
    db = SessionLocal()
    try:
        # 修改任务状态为running
        crud.update_task_status(db, task_id, "running")

        if task_type == "smoke":
            case_name = "冒烟测试"
            status = "pass"
            log_content = "冒烟测试全部执行通过"
            error_msg = ""
        else:
            case_name = "回归测试"
            status = "fail"
            log_content = "断言失败：预期结果2，实际结果3"
            error_msg = "AssertionError: 2 != 3"

        # 写入测试结果记录
        crud.add_test_result(db, task_id, case_name, status, log_content, error_msg)
        # 更新任务最终状态
        final_status = "success" if status == "pass" else "failed"
        crud.update_task_status(db, task_id, final_status)
    finally:
        db.close()
