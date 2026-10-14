from app.models import Task

tasks: list[Task] = []

def save(task: Task):
    tasks.append(task)

# def save1(Task):
#     tasks.append(Task)

def find_all():
    return tasks

def find_by_id(task_id):
    for task in tasks:
        if task.task_id == task_id:
            return task
    return None

def delete(task_id):
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            return