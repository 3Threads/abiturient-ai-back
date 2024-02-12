import os

import pytest

from core.question import FillTextQuestion
from infra.constants import SQL_FILE_TEST
from infra.sqlite.database_connect import Database
from infra.sqlite.questions import MultipleChoiceQuestionDataBase, FillWithArticlesQuestionDataBase, \
    TitlingQuestionDataBase, FillTextQuestionDataBase
from infra.sqlite.tasks import TasksDatabase


@pytest.fixture
def db() -> Database:
    db = Database(":memory:", os.path.abspath(SQL_FILE_TEST))
    db.initial()
    return db


def test_insert_multiple_choice_question(db: Database) -> None:
    task = TasksDatabase(db.get_connection(), db.get_cursor())
    task.insert_task(1, "title", "", "", 10, "listening", 2021, 1, "english")
    mcq = MultipleChoiceQuestionDataBase(db.get_connection(), db.get_cursor())
    mcq.insert_multiple_choice_question(1, "question", ["option1", "option2", "option3"], "option1")
    mcq.insert_multiple_choice_question(1, "q", ["1", "2", "3"], "2")
    questions = mcq.get_multiple_choice_questions(1)
    assert len(questions) == 2
    assert questions[0][2] == "question"
    assert questions[0][3] == "option1#option2#option3"
    assert questions[0][4] == "option1"
    assert questions[1][2] == "q"
    assert questions[1][3] == "1#2#3"
    assert questions[1][4] == "2"
    db.close_database()


def test_insert_fill_with_articles_question(db: Database) -> None:
    task = TasksDatabase(db.get_connection(), db.get_cursor())
    task.insert_task(1, "title", "", "", 10, "listening", 2021, 1, "english")
    fill_article = FillWithArticlesQuestionDataBase(db.get_connection(), db.get_cursor())
    fill_article.insert_fill_with_articles_question(1, ["a", "an", "the"])
    questions = fill_article.get_fill_with_articles_questions(1, 1)
    assert len(questions) == 1
    assert questions[0][2] == "a#an#the"
    assert questions[0][1] == 1
    assert questions[0][0] == 1
    db.close_database()

def test_titling_question(db: Database) -> None:
    task = TasksDatabase(db.get_connection(), db.get_cursor())
    task.insert_task(1, "title", "", "", 10, "listening", 2021, 1, "english")
    titling_question = TitlingQuestionDataBase(db.get_connection(), db.get_cursor())
    titling_question.insert_titling_question(1, "paragraph", ["A", "B"])
    question = titling_question.get_titling_questions(1, 1)
    assert len(question) == 1
    assert question[0][2] == "paragraph"
    assert question[0][3] == "A#B"
    assert question[0][1] == 1
    db.close_database()

def test_fill_text_question(db: Database) -> None:
    task = TasksDatabase(db.get_connection(), db.get_cursor())
    task.insert_task(1, "title", "", "", 10, "listening", 2021, 1, "english")
    fill_text = FillTextQuestionDataBase(db.get_connection(), db.get_cursor())
    fill_text.insert_fill_text_question(1, 1, "answer")
    question = fill_text.get_fill_text_questions(1, 1)
    assert len(question) == 1
    assert question[0][2] == "answer"
    assert question[0][1] == 1
    assert question[0][0] == 1
