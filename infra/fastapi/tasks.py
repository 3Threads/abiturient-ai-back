from fastapi import APIRouter
from pydantic import BaseModel

from core.task import TasksRepository
from infra.fastapi.dependables import TasksRepositoryDependable

tasks_api = APIRouter(tags=["Tasks"])


class TaskRequest(BaseModel):
    year: int
    variant: int


@tasks_api.get(
    "/tasks/{subject}/{year}/{variant}",
    status_code=200,
)
def get_tasks(year: int, variant: int, subject: str, tasks: TasksRepositoryDependable):
    print(tasks.get_tasks(year, variant, subject)[0].task_type.questions)
