from dataclasses import dataclass, field
from typing import Protocol
from uuid import UUID, uuid4


@dataclass
class Subscribe:
    subscribe_id: int
    subscribe_type: str
    subscribe_price: float
    subscribe_trial: int


class SubscribesRepository(Protocol):
    def add_subscribe(self, subscribe_title: str, subscribe_trial: int):
        pass

    def get_subscribes(self) -> list[Subscribe]:
        pass

    def add_subscribe_to_user(self, subscribe_id: int, user_id: int):
        pass