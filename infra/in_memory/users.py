from dataclasses import field
from uuid import UUID

from core.errors import UserAlreadyExistError, UserNotFoundError
from core.users import User
import hashlib


def hash_password(password):
    hash_object = hashlib.sha256()

    hash_object.update(password.encode('utf-8'))

    hashed_password = hash_object.hexdigest()

    return hashed_password


class UsersInMemory:
    users: dict[UUID, User] = {}

    def create(self, username: str, email: str, password: str) -> None:
        for user in self.users.values():
            if user.email == email or user.username == username:
                raise UserAlreadyExistError
        new_user = User(username, email, hash_password(password), "", "", "")
        self.users[new_user.id] = new_user

    def try_authorization(self, email: str, password: str) -> UUID:
        for user in self.users.values():
            if user.email == email and hash_password(password) == password:
                return user.id
        raise UserNotFoundError
