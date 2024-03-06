import os

import pytest

from core.question import MultipleChoiceQuestion
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


def test_insert_and_get_listening_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_listening_task(
        1, "title", 1, LISTENING, exam_id, "address", 5
    )

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_multiple_choice_question(
        task_id, "question1", ["option1", "option2"], "option1"
    )

    task = task_db.get_listening_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 1
    assert task.task_title == "title"
    assert task.task_point == 1
    assert task.task_type == LISTENING
    assert task.exam_id == exam_id
    assert task.address_to_audio == "address"
    assert task.text_num == 5
    assert len(task.questions) == 1

    db.close_database()


def test_insert_and_get_match_paragraphs_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_match_paragraphs_task(
        2, "title", 2, MATCHING, exam_id, "text_title", ["paragraph1", "paragraph2"]
    )

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_open_question(task_id, "question1", ["option1", "option2"])
    questions_db.insert_open_question(task_id, "question2", ["option1", "option2"])

    task = task_db.get_match_paragraphs_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 2
    assert task.task_title == "title"
    assert task.task_point == 2
    assert task.task_type == MATCHING
    assert task.exam_id == exam_id
    assert task.text_title == "text_title"
    assert task.paragraphs == ["paragraph1", "paragraph2"]
    assert len(task.questions) == 2

    db.close_database()


def test_insert_and_get_reading_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_reading_task(
        3, "title", 3, READING, exam_id, "text_title", "text"
    )

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_multiple_choice_question(
        task_id, "question1", ["option1", "option2"], "option1"
    )
    questions_db.insert_multiple_choice_question(
        task_id, "question2", ["option1", "option2"], "option2"
    )
    questions_db.insert_multiple_choice_question(
        task_id, "question3", ["option1", "option2"], "option1"
    )

    task = task_db.get_reading_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 3
    assert task.task_title == "title"
    assert task.task_point == 3
    assert task.task_type == READING
    assert task.exam_id == exam_id
    assert task.text_title == "text_title"
    assert task.text == "text"
    assert len(task.questions) == 3

    db.close_database()


def test_insert_and_get_fill_text_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_fill_text_task(
        4, "title", 4, FILLING, exam_id, "text_title", "text", ["option1", "option2"]
    )

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_open_question(task_id, "", ["option1"])
    questions_db.insert_open_question(task_id, "", ["option2"])
    questions_db.insert_open_question(task_id, "", ["option3"])
    questions_db.insert_open_question(task_id, "", ["option4"])

    task = task_db.get_fill_text_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 4
    assert task.task_title == "title"
    assert task.task_point == 4
    assert task.task_type == FILLING
    assert task.exam_id == exam_id
    assert task.text_title == "text_title"
    assert task.text == "text"
    assert task.options == ["option1", "option2"]
    assert len(task.questions) == 4

    db.close_database()


def test_insert_and_get_fill_text_without_options_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_fill_text_without_options_task(
        5, "title", 5, FILLING_WITHOUT_OPTIONS, exam_id, "text_title", "text"
    )

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_open_question(task_id, "", ["option1, option2"])
    questions_db.insert_open_question(task_id, "", ["option1, option2"])
    questions_db.insert_open_question(task_id, "", ["option1, option2"])
    questions_db.insert_open_question(task_id, "", ["option1, option2"])
    questions_db.insert_open_question(task_id, "", ["option1, option2"])

    task = task_db.get_fill_text_without_options_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 5
    assert task.task_title == "title"
    assert task.task_point == 5
    assert task.task_type == FILLING_WITHOUT_OPTIONS
    assert task.exam_id == exam_id
    assert task.text_title == "text_title"
    assert task.text == "text"
    assert len(task.questions) == 5

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
        CONVERSATION,
        exam_id,
        "text_title",
        "text",
        ["dialog1", "dialog2", "dialog3"],
    )

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_open_question(task_id, "question1", ["option1, option2"])
    questions_db.insert_open_question(task_id, "question2", ["option1, option2"])
    questions_db.insert_open_question(task_id, "question3", ["option1, option2"])
    questions_db.insert_open_question(task_id, "question4", ["option1, option2"])
    questions_db.insert_open_question(task_id, "question5", ["option1, option2"])
    questions_db.insert_open_question(task_id, "question6", ["option1, option2"])

    task = task_db.get_conversation_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 6
    assert task.task_title == "title"
    assert task.task_point == 6
    assert task.task_type == CONVERSATION
    assert task.exam_id == exam_id
    assert task.text_title == "text_title"
    assert task.text == "text"
    assert task.dialogue == ["dialog1", "dialog2", "dialog3"]
    assert len(task.questions) == 6

    db.close_database()


def test_insert_and_get_email_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_email_task(7, "title", 7, EMAIL, exam_id)

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_email_question(
        task_id, "text_title", "text", ["where", "by whom", "when"]
    )

    task = task_db.get_email_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 7
    assert task.task_title == "title"
    assert task.task_point == 7
    assert task.task_type == EMAIL
    assert task.exam_id == exam_id
    assert len(task.questions) == 1

    db.close_database()


def test_insert_and_get_essay_task(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_id = task_db.insert_essay_task(8, "title", 8, ESSAY, exam_id)

    questions_db = QuestionsDatabase(db.get_connection(), db.get_cursor())
    questions_db.insert_essay_question(task_id, "essay_title")

    task = task_db.get_essay_task(task_id)

    assert task.task_id == task_id
    assert task.task_number == 8
    assert task.task_title == "title"
    assert task.task_point == 8
    assert task.task_type == ESSAY
    assert task.exam_id == exam_id
    assert len(task.questions) == 1

    db.close_database()


def test_get_tasks(db: Database) -> None:
    exams_db = ExamsDatabase(db.get_connection(), db.get_cursor())
    exams_db.create_new_exam("english", 2021, 1)
    exam_id = exams_db.get_exam_id("english", 2021, 1)
    task_db = TasksDatabase(db.get_connection(), db.get_cursor())
    task_db.insert_listening_task(1, "title", 1, LISTENING, exam_id, "address", 5)
    task_db.insert_match_paragraphs_task(
        2, "title", 2, MATCHING, exam_id, "text_title", ["paragraph1", "paragraph2"]
    )
    task_db.insert_reading_task(3, "title", 3, READING, exam_id, "text_title", "text")
    task_db.insert_fill_text_task(
        4, "title", 4, FILLING, exam_id, "text_title", "text", ["option1", "option2"]
    )
    task_db.insert_fill_text_without_options_task(
        5, "title", 5, FILLING_WITHOUT_OPTIONS, exam_id, "text_title", "text"
    )
    task_db.insert_conversation_task(
        6,
        "title",
        6,
        CONVERSATION,
        exam_id,
        "text_title",
        "text",
        ["dialog1", "dialog2", "dialog3"],
    )
    task_db.insert_email_task(7, "title", 7, EMAIL, exam_id)
    task_db.insert_essay_task(8, "title", 8, ESSAY, exam_id)
    tasks = task_db.get_tasks(exam_id)

    assert len(tasks) == 8
    assert tasks[0].task_type == LISTENING
    assert tasks[1].task_type == MATCHING
    assert tasks[2].task_type == READING
    assert tasks[3].task_type == FILLING
    assert tasks[4].task_type == FILLING_WITHOUT_OPTIONS
    assert tasks[5].task_type == CONVERSATION
    assert tasks[6].task_type == EMAIL
    assert tasks[7].task_type == ESSAY
    for i in range(8):
        assert tasks[i].task_number == i + 1
    for i in range(8):
        assert tasks[i].task_point == i + 1
    for i in range(8):
        assert tasks[i].task_title == "title"
    for i in range(8):
        assert tasks[i].exam_id == exam_id
    for i in range(8):
        assert tasks[i].questions == []

    db.close_database()
