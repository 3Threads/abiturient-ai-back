import os

import pytest

from infra.constants import SQL_FILE_TEST
from infra.sqlite.database_connect import Database
from infra.sqlite.exams import ExamsDatabase


@pytest.fixture
def db() -> Database:
    db = Database(":memory:", os.path.abspath(SQL_FILE_TEST))
    db.initial()
    return db


def test_create_new_exam_and_get(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam = exams_db.get_exam(1)
    assert exam.subject == "english"
    assert exam.year == 2021
    assert exam.variant == 1
    db.close_database()


def test_get_exam_id(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    assert exam_id == 1
    db.close_database()


def test_get_exams(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exams_db.create_new_exam("english", 2021, 2)
    exams = exams_db.get_exams()
    assert len(exams) == 2
    assert exams[0].subject == "english"
    assert exams[0].year == 2021
    assert exams[0].variant == 1
    assert exams[1].subject == "english"
    assert exams[1].year == 2021
    assert exams[1].variant == 2
    db.close_database()


def test_get_exams_by_subject(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exams_db.create_new_exam("german", 2021, 2)
    exams = exams_db.get_exams_by_subject("english")
    assert len(exams) == 1
    assert exams[0].subject == "english"
    assert exams[0].year == 2021
    assert exams[0].variant == 1
    db.close_database()
