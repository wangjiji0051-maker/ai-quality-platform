from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database, test_runner
import threading

app = FastAPI(title="AI测试质量平台")

# 把建表放到app启动事件，只执行一次
@app.on_event("startup")
async def startup():
    database.Base.metadata.create_all(bind=database.engine)

# 创建测试任务
@app.post("/api/task/create", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db:Session=Depends(database.get_db)):
    db_task = crud.create_task(db, task)
    # 只传任务id 和任务类型，不传递db对象
    def background_run():
        test_runner.run_test_task(db_task.id, task.task_type)
    t = threading.Thread(target=background_run)
    t.start()
    return db_task


# 查询任务详情
@app.get("/api/task/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id:int, db:Session=Depends(database.get_db)):
    return crud.get_task_by_id(db, task_id)

# 获取任务所有测试结果
@app.get("/api/task/{task_id}/result", response_model=List[schemas.TestResultOut])
def get_task_result(task_id:int, db:Session=Depends(database.get_db)):
    return crud.get_results_by_task_id(db, task_id)

# 【留给你AI Coding】AI分析接口，你在这里写AI根因判断
@app.post("/api/ai/analyze/{result_id}")
def ai_analyze_result(result_id:int, db:Session=Depends(database.get_db)):
    # 这里由你来实现：读取error_msg，调用LLM，填写ai_root_cause、ai_cause_type
    pass
