from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.question import FillTextQuestion, MultipleChoiceQuestion


@dataclass
class MultipleChoiceQuestionDataBase:
    con: Connection
    cur: Cursor

    def insert_multiple_choice_question(self, task_id: int, question: str, options: list[str], answer: str):
        question_options = options[0]
        for i in range(len(options)):
            if i != 0:
                question_options = question_options + f"#{options[i]}"
        self.cur.execute("INSERT INTO MultipleChoiceQuestion(TASK_ID, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER) VALUES (?, ?, ?, ?)", (task_id, question, question_options, answer))
        self.con.commit()

    def get_multiple_choice_questions(self, task_id: int) -> list[MultipleChoiceQuestion]:
        return self.cur.execute("SELECT * FROM MultipleChoiceQuestion WHERE TASK_ID = ?", (task_id,)).fetchall()

@dataclass
class FillWithArticlesQuestionDataBase:
    con: Connection
    cur: Cursor

    def insert_fill_with_articles_question(self, task_id: int, answers: list[str]):
        answer = answers[0]
        for i in range(len(answers)):
            if i != 0:
                answer = answer + f"#{answers[i]}"
        self.cur.execute("INSERT INTO FillWithArticlesQuestion(TASK_ID, CORRECT_ANSWER) VALUES (?, ?)", (task_id, answer))
        self.con.commit()


@dataclass
class TitlingQuestionDataBase:
    con: Connection
    cur: Cursor

    def insert_titling_question(self, task_id: int, paragraph: str, answers: list[str]):
        answer = answers[0]
        for i in range(len(answers)):
            if i != 0:
                answer = answer + f"#{answers[i]}"
        self.cur.execute("INSERT INTO TitlingQuestion(TASK_ID, PARAGRAPH, CORRECT_ANSWERS) VALUES (?, ?, ?)", (task_id, paragraph, answer))
        self.con.commit()


@dataclass
class FillTextQuestionDataBase:
    con: Connection
    cur: Cursor

    def insert_fill_text_question(self, task_id: int, question_id: int, answer: str):
        self.cur.execute("INSERT INTO FillTextQuestion(TASK_ID, QUESTION_ID, CORRECT_ANSWER) VALUES (?, ?, ?)", (task_id, question_id, answer))
        self.con.commit()

    def get_fill_text_questions(self, task_id: int) -> list[FillTextQuestion]:
        return self.cur.execute("SELECT * FROM FillTextQuestion WHERE TASK_ID = ?", (task_id,)).fetchall()

    # def insert_essay_question(self, question: str, answer: str):
    #     pass
    #
    # def insert_email_question(self, question: str, answer: str):
    #     pass



