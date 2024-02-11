import hashlib
from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from mypy.typeshed.stdlib.sqlite3.dbapi2 import IntegrityError

from core.errors import UserAlreadyExistError
from core.users import User


def hash_password(password):
    hash_object = hashlib.sha256()

    hash_object.update(password.encode('utf-8'))

    hashed_password = hash_object.hexdigest()

    return hashed_password


@dataclass
class UsersDatabase:
    con: Connection
    cur: Cursor

    def create(self, username: str, email: str, password: str) -> User:
        user = User(username, email, "", "", "")
        try:
            self.cur.execute(
                "INSERT INTO USERS (USERNAME, EMAIL, PASSWORD, HAVE_SUBSCRIBE, SUBSCRIBE_ID, START_SUBSCRIBE_DATE, END_SUBSCRIBE_DATE) VALUES ("
                "?, ?, ?, 0, NULL, NULL, NULL)", [user.username, user.email, hash_password(password)])
        except IntegrityError:
            raise UserAlreadyExistError()

        self.con.commit()
        return user

    def try_authorization(self, email: str, password: str) -> User:
        user_db = self.cur.execute("SELECT * FROM USERS WHERE EMAIL = ? AND PASSWORD = ?",
                                   [email, hash_password(password)]).fetchone()
        if user_db is not None:
            user = User(user_db[1], user_db[2], user_db[4], user_db[5], user_db[6])

            return user
        return None
