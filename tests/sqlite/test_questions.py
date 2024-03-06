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
    CONVERSATION,
    ESSAY,
)
from infra.sqlite.database_connect import Database
from infra.sqlite.exams import ExamsDatabase
from infra.sqlite.questions import QuestionsDatabase
from infra.sqlite.tasks import TasksDatabase


@pytest.fixture
def db() -> Database:
    db = Database(":memory:", os.path.abspath(SQL_FILE_TEST))
    db.initial()
    return db


def test_insert_and_get_multiple_choice_question(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_listening_task(
        1, "title", 1, LISTENING, exam_id, "address", 1
    )

    question_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    question_id = question_db.insert_multiple_choice_question(
        task_id, "question1", ["option1", "option2"], "option1"
    )
    question = question_db.get_multiple_choice_question(question_id)

    assert question.question_text == "question1"
    assert question.question_options == ["option1", "option2"]
    assert question.question_answer == "option1"

    db.close_database()


def test_insert_and_get_open_question(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_reading_task(
        1, "title", 1, READING, exam_id, "text_title", "text"
    )

    question_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    question_id = question_db.insert_open_question(
        task_id, "question1", ["option1", "option2"]
    )
    question = question_db.get_open_question(question_id)

    assert question.question_text == "question1"
    assert question.correct_answers == ["option1", "option2"]

    db.close_database()


def test_insert_and_get_email_question(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_email_task(1, "title", 1, EMAIL, exam_id)

    question_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    question_id = question_db.insert_email_question(
        task_id, "text_title", "text", ["where", "by whom", "when"]
    )
    question = question_db.get_email_question(question_id)

    assert question.text_title == "text_title"
    assert question.text == "text"
    assert question.asking_information == ["where", "by whom", "when"]

    db.close_database()


def test_insert_and_get_essay_question(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_essay_task(1, "title", 1, ESSAY, exam_id)

    question_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    question_id = question_db.insert_essay_question(task_id, "essay_title")
    question = question_db.get_essay_question(question_id)

    assert question.essay_title == "essay_title"

    db.close_database()
