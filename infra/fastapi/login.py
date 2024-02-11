from fastapi import APIRouter
from pydantic import BaseModel

from core.errors import UserAlreadyExistError, UserNotFoundError
from infra.fastapi.dependables import UsersRepositoryDependable

sign_api = APIRouter(tags=["Login"])


@sign_api.get(
    "/login/{email}/{password}",
    status_code=200
)
def sign_in(email: str, password: str, users_repository: UsersRepositoryDependable):
    print(email, password)
    try:
        user = users_repository.try_authorization(email, password)
        return {"user": user}
    except UserNotFoundError as e:
        return e.get_error_json_response()


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


@sign_api.post(
    "/signup",
    status_code=201,
)
def sign_up(
    request: RegisterRequest,
    users_repository: UsersRepositoryDependable,
):
    username = request.username
    email = request.email
    password = request.password
    try:
        user = users_repository.create(username, email, password)
        return {"user": user}
    except UserAlreadyExistError as e:
        return e.get_error_json_response()
