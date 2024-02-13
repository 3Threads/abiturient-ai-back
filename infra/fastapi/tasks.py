from fastapi import APIRouter
from fastapi import Form
from fastapi.responses import JSONResponse

from infra.fastapi.dependables import TasksRepositoryDependable

tasks_api = APIRouter(tags=["Tasks"])


@tasks_api.get(
    "/tasks/{subject}/{year}/{variant}",
    status_code=200,
)
def get_tasks(subject: str, year: int, variant: int, tasks: TasksRepositoryDependable):
    result_tasks = tasks.get_tasks(subject, year, variant)
    if len(result_tasks):
        return {"tasks": result_tasks}
    return JSONResponse(status_code=404, content={"message": "Tasks not found. will be added soon."})


@tasks_api.post("/tasks", status_code=201)
def process_test_data(
    tasks: TasksRepositoryDependable,
    subject: str = Form(...),
    year: int = Form(...),
    variant: str = Form(...),
    task1: list[str] = Form(...),
    task2: list[str] = Form(...),
    task3: list[str] = Form(...),
    task4: list[str] = Form(...),
    task5: list[str] = Form(...),
    task6: list[str] = Form(...),
    # task7: list[str] = Form(...),
    # task8: list[str] = Form(...),
):
    answers = [task1, task2, task3, task4, task5, task6]

    answers_dict = {}
    for task_num, task in enumerate(answers):
        for task_value in task:
            if task_num in answers_dict:
                answers_dict[task_num].append(task_value)
            else:
                answers_dict[task_num] = [task_value]

    request = {
        "subject": subject,
        "year": year,
        "variant": variant,
        "answers": answers_dict,
    }
    return {
        "subject": subject,
        "year": year,
        "variant": variant,
        "answers": answers_dict,
        "points": tasks.get_result_points(request),
    }
