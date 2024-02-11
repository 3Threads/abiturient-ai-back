from uuid import UUID

from core.errors import UserAlreadyExistError, UserNotFoundError, IncorrectPasswordError
from core.users import User
import hashlib


def hash_password(password):
    hash_object = hashlib.sha256()

    hash_object.update(password.encode('utf-8'))

    hashed_password = hash_object.hexdigest()

    return hashed_password


class UsersInMemory:
    users: dict[str, User] = {}

    def create(self, username: str, email: str, password: str) -> None:
        if not self.users.keys().__contains__(email):
            new_user = User(username, email, hash_password(password), "", "", "")
            self.users[email] = new_user
        else:
            raise UserAlreadyExistError

    def try_authorization(self, email: str, password: str) -> User:
        try:
            user = self.users[email]
            if hash_password(password) == user.password:
                return user
            else:
                raise IncorrectPasswordError
        except:
            raise UserNotFoundError
