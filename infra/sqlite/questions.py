from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.question import MultipleChoiceQuestion, OpenQuestion


@dataclass
class QuestionDataBase:
    con: Connection
    cur: Cursor

    def insert_into_questions(self, task_id: int) -> int:
        self.cur.execute("INSERT INTO Questions(TASK_ID) VALUES (?)", (task_id,))
        last_row_id = self.cur.lastrowid
        self.con.commit()
        return last_row_id

    # def get_questions(self, task_id: int) -> list[Question]:
    #     questions = self.cur.execute("SELECT * FROM Questions WHERE TASK_ID = ?", (task_id,)).fetchall()
    #     questions_list = []
    #     for question in questions:
    #         if question[1] == MULTIPLE_CHOICE_QUESTION:
    #             yield self.get_multiple_choice_questions(task_id, question[0])
    #         elif question[1] == FILL_WITH_ARTICLES_QUESTION:
    #             yield self.get_fill_with_articles_questions(task_id, question[0])
    #         elif question[1] == TITLING_QUESTION:
    #             yield self.get_titling_questions(task_id, question[0])

    def insert_multiple_choice_question(self, question_text: str, question_options: list[str], question_answer: str,
                                        task_id: int) -> int:
        question_id = self.insert_into_questions(task_id)
        self.cur.execute(
            "INSERT INTO MultipleChoiceQuestion(QUESTION_ID, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER) VALUES (?, ?, ?, ?)",
            (question_id, question_text, question_options, question_answer),
        )
        self.con.commit()
        return question_id

    def get_multiple_choice_questions(
            self, question_id: int
    ) -> list[MultipleChoiceQuestion]:
        multiple_choice_questions = self.cur.execute(
            "SELECT * FROM MultipleChoiceQuestion WHERE QUESTION_ID = ?",
            (question_id,),
        ).fetchall()
        questions = []
        for question in multiple_choice_questions:
            questions.append(MultipleChoiceQuestion(
                question[1], question[2], question[3]
            ))

        return questions

