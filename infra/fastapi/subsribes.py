from fastapi import APIRouter
from pydantic import BaseModel

from core.errors import UserAlreadyExistError, UserNotFoundError
from infra.fastapi.dependables import UsersRepositoryDependable, SubscribesRepositoryDependable

subscribe_api = APIRouter(tags=["Subscribe"])


class AddSubscribeRequest(BaseModel):
    subscribe_type: str
    user_id: int


class AddNewSubscribeRequest(BaseModel):
    subscribe_type: str
    subscribe_price: float
    subscribe_trial: int


class SubscribeItem(BaseModel):
    subscribe_id: int
    subscribe_type: str
    subscribe_price: float
    subscribe_trial: int


class SubscribeItemEnvelope(BaseModel):
    subscribe: SubscribeItem


class SubscribeListEnvelope(BaseModel):
    subscribes: list[SubscribeItem]


@subscribe_api.get(
    "/subscribes",
    status_code=200,
    response_model=SubscribeListEnvelope
)
def get_subscribes(subscribe_repository: SubscribesRepositoryDependable):
    return {"subscribes": subscribe_repository.get_subscribes()}


@subscribe_api.post(
    "/subscribes",
    status_code=200,
)
def add_subscribe(request: AddNewSubscribeRequest, subscribe_repository: SubscribesRepositoryDependable):
    subscribe_repository.add_subscribe(request.subscribe_type, request.subscribe_price, request.subscribe_trial)


@subscribe_api.post(
    "/subscribe",
    status_code=201,
)
def add_subscribe_to_user(
        request: AddSubscribeRequest,
        subscribe_repository: SubscribesRepositoryDependable,
):
    print(request)
    subscribe_id = subscribe_repository.get_subscribe_by_type(request.subscribe_type).subscribe_id
    subscribe_repository.add_subscribe_to_user(subscribe_id, request.user_id)
