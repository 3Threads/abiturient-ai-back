import hashlib
from dataclasses import dataclass
from sqlite3 import Connection, Cursor, IntegrityError

from core.errors import UserAlreadyExistError, UserNotFoundError
from core.users import User
from infra.sqlite.subscribes import SubscribesDataBase


def hash_password(password):
    hash_object = hashlib.sha256()

    hash_object.update(password.encode("utf-8"))

    hashed_password = hash_object.hexdigest()

    return hashed_password


@dataclass
class UsersDatabase:
    con: Connection
    cur: Cursor
    subscribes_db: SubscribesDataBase

    def create(self, username: str, email: str, password: str) -> User:
        subscription = self.subscribes_db.get_subscribe_by_type("Free")
        user = User(username, email, "Free", "", "")

        try:
            self.cur.execute(
                "INSERT INTO USERS (USERNAME, EMAIL, PASSWORD, SUBSCRIBE_ID, START_SUBSCRIBE_DATE, END_SUBSCRIBE_DATE) VALUES ("
                "?, ?, ?, ?, NULL, NULL)",
                [
                    user.username,
                    user.email,
                    hash_password(password),
                    subscription.subscribe_id,
                ],
            )
        except IntegrityError:
            raise UserAlreadyExistError()

        self.con.commit()
        return user

    def try_authorization(self, email: str, password: str) -> User:
        user_db = self.cur.execute(
            "SELECT * FROM USERS WHERE EMAIL = ? AND PASSWORD = ?",
            [email, hash_password(password)],
        ).fetchone()
        if user_db is not None:
            subscription = self.subscribes_db.get_subscribe_by_id(user_db[4])
            user = User(user_db[1], user_db[2], subscription.subscribe_type, user_db[5], user_db[6])
            print(user)
            return user

        raise UserNotFoundError()
