from fastapi import APIRouter
from fastapi import Form

from infra.fastapi.dependables import TasksRepositoryDependable

tasks_api = APIRouter(tags=["Tasks"])


@tasks_api.get(
    "/tasks/{year}/{variant}",
    status_code=200,
)
def get_tasks(year: int, variant: int, tasks: TasksRepositoryDependable):
    return tasks.get_tasks(year, variant)


# ors imitom vtoveb, rom momavalshi anu sxvadasxva raodenobis taski tu igzavneba vicodet romelia sawiro da ise axla marto davlitac gvyofnis rviani.


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
    task7: list[str] = Form(...),
    task8: list[str] = Form(...),
    task9: list[str] = Form(...),
):
    # Here you can process the form data as needed
    all_tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9]

    task_dict = {}
    for task_num, task in enumerate(all_tasks):
        for task_value in task:
            if task_num in task_dict:
                task_dict[task_num].append(task_value)
            else:
                task_dict[task_num] = [task_value]

    request = {
        "language": subject,
        "year": year,
        "variant": variant,
        "tasks": task_dict,
    }
    return {
        "language": subject,
        "year": year,
        "variant": variant,
        "tasks": task_dict,
        "points": tasks.get_result_points(request),
    }


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
    task7: list[str] = Form(...),
    task8: list[str] = Form(...),
):
    # Here you can process the form data as needed
    all_tasks = [task1, task2, task3, task4, task5, task6, task7, task8]

    task_dict = {}
    for task_num, task in enumerate(all_tasks):
        for task_value in task:
            if task_num in task_dict:
                task_dict[task_num].append(task_value)
            else:
                task_dict[task_num] = [task_value]

    request = {
        "language": subject,
        "year": year,
        "variant": variant,
        "tasks": task_dict,
    }
    return {
        "language": subject,
        "year": year,
        "variant": variant,
        "tasks": task_dict,
        "points": tasks.get_result_points(request),
    }
