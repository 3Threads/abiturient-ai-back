from typing import Annotated

from fastapi import Depends
from fastapi.requests import Request

from core.task import TasksRepository
from core.users import UsersRepository


def get_tasks_repository(request: Request) -> TasksRepository:
    return request.app.state.tasks  # type: ignore


TasksRepositoryDependable = Annotated[TasksRepository, Depends(get_tasks_repository)]


def get_users_repository(request: Request) -> UsersRepository:
    return request.app.state.users  # type: ignore


UsersRepositoryDependable = Annotated[UsersRepository, Depends(get_users_repository)]
