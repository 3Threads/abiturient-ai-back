import os

import pytest

from infra.constants import SQL_FILE_TEST
from infra.sqlite.database_connect import Database
from infra.sqlite.questions import MultipleChoiceQuestionDataBase
from infra.sqlite.tasks import TasksDatabase


@pytest.fixture
def db() -> Database:
    db = Database(":memory:", os.path.abspath(SQL_FILE_TEST))
    db.initial()
    return db


def test_insert_multiple_choice_question(db: Database) -> None:
    task = TasksDatabase(db.get_connection(), db.get_cursor())
    task.insert_task(1, "title", "", "", 10, "listening", 2021, 1, "english")
    print(task.get_tasks("english", 2021, 1))
    mcq = MultipleChoiceQuestionDataBase(db.get_connection(), db.get_cursor())
    mcq.insert_multiple_choice_question(1, "question", ["option1", "option2", "option3"], "option1")
    questions = mcq.get_multiple_choice_questions(1)
    assert len(questions) == 1
    print(questions)
    print(questions[0][0])
    assert questions[0][2] == "question"
    assert questions[0][3] == "option1#option2#option3"
    assert questions[0][4] == "option1"
    db.close_database()
