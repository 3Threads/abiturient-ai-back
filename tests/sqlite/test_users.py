# import os
#
# import pytest
#
# from infra.constants import SQL_FILE_TEST
# from infra.sqlite.database_connect import Database
# from infra.sqlite.users import UsersDatabase, hash_password
#
#
# @pytest.fixture
# def db() -> Database:
#     db = Database(":memory:", os.path.abspath(SQL_FILE_TEST))
#     db.initial()
#     return db
#
#
# def test_insert_user(db: Database) -> None:
#     users = UsersDatabase(db.get_connection(), db.get_cursor())
#     users.create("meloti kaci", "meloti@gmail.com", "123456")
#     user = users.try_authorization("meloti@gmail.com", "123456")
#     assert user.email == "meloti@gmail.com"
#     assert user.username == "meloti kaci"
#     assert user.password == hash_password("123456")
#     db.close_database()
