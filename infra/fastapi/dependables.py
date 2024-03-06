from typing import Annotated

from fastapi import Depends
from fastapi.requests import Request

from core.exam import ExamsRepository
from core.subscribes import SubscribesRepository
from core.task import TasksRepository
from core.users import UsersRepository


def get_exams_repository(request: Request) -> ExamsRepository:
    return request.app.state.exams  # type: ignore


ExamsRepositoryDependable = Annotated[ExamsRepository, Depends(get_exams_repository)]


def get_tasks_repository(request: Request) -> TasksRepository:
    return request.app.state.tasks  # type: ignore


TasksRepositoryDependable = Annotated[TasksRepository, Depends(get_tasks_repository)]


def get_users_repository(request: Request) -> UsersRepository:
    return request.app.state.users  # type: ignore


UsersRepositoryDependable = Annotated[UsersRepository, Depends(get_users_repository)]


def get_subscribes_repository(request: Request) -> SubscribesRepository:
    return request.app.state.subscribes  # type: ignore


SubscribesRepositoryDependable = Annotated[
    SubscribesRepository, Depends(get_subscribes_repository)
]
