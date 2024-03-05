import os

import pytest

from infra.constants import (
    SQL_FILE_TEST,
    LISTENING,
    MATCHING,
    READING,
    FILLING,
    FILLING_WITHOUT_OPTIONS,
    EMAIL,
)
from infra.sqlite.database_connect import Database
from infra.sqlite.exams import ExamsDatabase
from infra.sqlite.tasks import TasksDatabase


@pytest.fixture
def db() -> Database:
    db = Database(":memory:", os.path.abspath(SQL_FILE_TEST))
    db.initial()
    return db


def test_insert_and_get_listening_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_listening_task(
        1, "title", 1, LISTENING, exam_id, "address", 5
    )
    task = task_db.get_listening_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 1
    assert task.task_title == "title"
    assert task.task_point == 1
    assert task.task_type == LISTENING
    assert task.exam_id == exam_id
    assert task.questions == []
    assert task.address_to_audio == "address"
    assert task.text_num == 5

    db.close_database()


def test_insert_and_get_match_paragraphs_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_match_paragraphs_task(
        2, "title", 2, MATCHING, exam_id, "text_title", ["paragraph1", "paragraph2"]
    )
    task = task_db.get_match_paragraphs_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 2
    assert task.task_title == "title"
    assert task.task_point == 2
    assert task.task_type == MATCHING
    assert task.exam_id == exam_id
    assert task.questions == []
    assert task.text_title == "text_title"
    assert task.paragraphs == ["paragraph1", "paragraph2"]

    db.close_database()


def test_insert_and_get_reading_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_reading_task(
        3, "title", 3, READING, exam_id, "text_title", "text"
    )
    task = task_db.get_reading_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 3
    assert task.task_title == "title"
    assert task.task_point == 3
    assert task.task_type == READING
    assert task.exam_id == exam_id
    assert task.questions == []
    assert task.text_title == "text_title"
    assert task.text == "text"

    db.close_database()


def test_insert_and_get_fill_text_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_fill_text_task(
        4, "title", 4, FILLING, exam_id, "text_title", "text", ["option1", "option2"]
    )
    task = task_db.get_fill_text_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 4
    assert task.task_title == "title"
    assert task.task_point == 4
    assert task.task_type == FILLING
    assert task.exam_id == exam_id
    assert task.questions == []
    assert task.text_title == "text_title"
    assert task.text == "text"
    assert task.options == ["option1", "option2"]

    db.close_database()


def test_insert_and_get_fill_text_without_options_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_fill_text_without_options_task(
        5, "title", 5, FILLING_WITHOUT_OPTIONS, exam_id, "text_title", "text"
    )
    task = task_db.get_fill_text_without_options_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 5
    assert task.task_title == "title"
    assert task.task_point == 5
    assert task.task_type == FILLING_WITHOUT_OPTIONS
    assert task.exam_id == exam_id
    assert task.questions == []
    assert task.text_title == "text_title"
    assert task.text == "text"

    db.close_database()


def test_insert_and_get_conversation_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_conversation_task(
        6,
        "title",
        6,
        "conversation",
        exam_id,
        "text_title",
        "text",
        ["dialog1", "dialog2", "dialog3"],
    )
    task = task_db.get_conversation_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 6
    assert task.task_title == "title"
    assert task.task_point == 6
    assert task.task_type == "conversation"
    assert task.exam_id == exam_id
    assert task.questions == []
    assert task.text_title == "text_title"
    assert task.text == "text"
    assert task.dialogue == ["dialog1", "dialog2", "dialog3"]

    db.close_database()


def test_insert_and_get_email_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_email_task(
        7, "title", 7, EMAIL, exam_id, "text_title", "text", ["where?", "when?", "why?"]
    )
    task = task_db.get_email_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 7
    assert task.task_title == "title"
    assert task.task_point == 7
    assert task.task_type == EMAIL
    assert task.exam_id == exam_id
    assert task.questions == []
    assert task.text_title == "text_title"
    assert task.text == "text"
    assert task.asking_information == ["where?", "when?", "why?"]

    db.close_database()


def test_insert_and_get_essay_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_essay_task(8, "title", 8, "essay", exam_id, "essay_title")
    task = task_db.get_essay_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 8
    assert task.task_title == "title"
    assert task.task_point == 8
    assert task.task_type == "essay"
    assert task.exam_id == exam_id
    assert task.questions == []

    db.close_database()
