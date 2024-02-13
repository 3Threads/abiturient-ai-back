from dataclasses import dataclass
from typing import Protocol


@dataclass
class User:
    id: int
    username: str
    email: str
    subscribe_type: str
    subscribe_start_date: str
    subscribe_end_date: str


class UsersRepository(Protocol):
    def create(self, username: str, email: str, password: str) -> User:
        pass

    def try_authorization(self, username: str, password: str) -> User:
        pass
