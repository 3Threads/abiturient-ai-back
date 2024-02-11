from dataclasses import field, dataclass
from typing import Protocol
from uuid import UUID, uuid4


@dataclass
class User:
    username: str
    email: str
    password: str
    subscribe_type: str
    subscribe_start_date: str
    subscribe_end_date: str
    id: UUID = field(default_factory=uuid4)


class UsersRepository(Protocol):
    def create(self, username: str, email: str, password: str) -> User:
        pass

    def try_authorization(self, username: str, password: str) -> User:
        pass