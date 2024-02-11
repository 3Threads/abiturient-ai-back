from fastapi import APIRouter
from fastapi import Form
from starlette.responses import JSONResponse

from core.errors import UserAlreadyExistError, UserNotFoundError
from infra.fastapi.dependables import UsersRepositoryDependable

sign_api = APIRouter(tags=["Login"])


@sign_api.get(
    "/login",
    status_code=200,
)
def sign_in(users_repository: UsersRepositoryDependable, email: str = Form(...), password: str = Form(...)):
    try:
        user = users_repository.try_authorization(email, password)
        return {"user": user}
    except UserNotFoundError as e:
        return e.get_error_json_response()


@sign_api.post(
    "/signup",
    status_code=200,
)
def sign_up(users_repository: UsersRepositoryDependable, username: str = Form(...), email: str = Form(...),
            password: str = Form(...)):
    print("aaaa")
    try:
        users_repository.create(username, email, password)
        return JSONResponse(
            status_code=200,
            content={"message": f"User created successfully"},
        )
    except UserAlreadyExistError as e:
        return e.get_error_json_response()
