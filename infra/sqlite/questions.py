from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.question import (
    MultipleChoiceQuestion,
    OpenQuestion,
    EmailQuestion,
    Question,
    EssayQuestion,
)
from infra.constants import (
    MULTIPLE_CHOICE_QUESTION,
    DELIMITER,
    OPEN_QUESTION,
    EMAIL_QUESTION,
    ESSAY_QUESTION,
)


@dataclass
class QuestionsDatabase:
    con: Connection
    cur: Cursor

    def insert_into_questions(self, task_id: int) -> int:
        self.cur.execute("INSERT INTO Questions(TASK_ID) VALUES (?)", (task_id,))
        last_row_id = self.cur.lastrowid
        self.con.commit()
        return last_row_id

    def get_questions(self, task_id: int) -> list[Question]:
        questions = self.cur.execute(
            "SELECT * FROM Questions WHERE TASK_ID = ?", (task_id,)
        ).fetchall()
        questions_list = []
        for question in questions:
            if question[1] == MULTIPLE_CHOICE_QUESTION:
                multiple_choice_question = self.get_multiple_choice_question(
                    question[0]
                )
                questions_list.append(multiple_choice_question)
            elif question[1] == OPEN_QUESTION:
                open_question = self.get_open_question(question[0])
                questions_list.append(open_question)
            elif question[1] == EMAIL_QUESTION:
                email_question = self.get_email_question(question[0])
                questions_list.append(email_question)
            elif question[1] == ESSAY_QUESTION:
                essay_question = self.get_essay_question(question[0])
                questions_list.append(essay_question)
        return questions_list

    def insert_multiple_choice_question(
        self,
        task_id: int,
        question_text: str,
        question_options: list[str],
        question_answer: str,
    ) -> int:
        question_id = self.insert_into_questions(task_id)
        options = question_options[0]
        for option in question_options:
            if option != question_options[0]:
                options += DELIMITER + option

        self.cur.execute(
            "INSERT INTO MultipleChoiceQuestion(QUESTION_ID, QUESTION_OPTIONS, QUESTION_ANSWER, QUESTION_TEXT) VALUES (?, ?, ?, ?)",
            (question_id, options, question_answer, question_text),
        )
        self.con.commit()
        return question_id

    def get_multiple_choice_question(self, question_id: int) -> MultipleChoiceQuestion:
        multiple_choice_question = self.cur.execute(
            "SELECT * FROM MultipleChoiceQuestion WHERE QUESTION_ID = ?",
            (question_id,),
        ).fetchone()
        options = multiple_choice_question[1].split(DELIMITER)
        return MultipleChoiceQuestion(
            options, multiple_choice_question[2], multiple_choice_question[3]
        )

    def insert_open_question(
        self, task_id: int, question: str, correct_answers: list[str]
    ) -> int:
        question_id = self.insert_into_questions(task_id)
        answers = correct_answers[0]
        for answer in correct_answers:
            if answer != correct_answers[0]:
                answers += DELIMITER + answer

        self.cur.execute(
            "INSERT INTO OpenQuestion(QUESTION_ID, CORRECT_ANSWERS, QUESTION) VALUES (?, ?, ?)",
            (question_id, answers, question),
        )
        self.con.commit()
        return question_id

    def get_open_question(self, question_id: int) -> OpenQuestion:
        open_question = self.cur.execute(
            "SELECT * FROM OpenQuestion WHERE QUESTION_ID = ?",
            (question_id,),
        ).fetchone()
        answers = open_question[1].split(DELIMITER)
        return OpenQuestion(answers, open_question[2])

    def insert_email_question(
        self, task_id: int, text_title: str, text: str, asking_information: list[str]
    ) -> int:
        question_id = self.insert_into_questions(task_id)
        asking_info = asking_information[0]
        for info in asking_information:
            if info != asking_information[0]:
                asking_info += DELIMITER + info

        self.cur.execute(
            "INSERT INTO EmailQuestion(QUESTION_ID, TEXT_TITLE, TEXT, ASKING_INFORMATION) VALUES (?, ?, ?, ?)",
            (question_id, text_title, text, asking_info),
        )
        self.con.commit()
        return question_id

    def get_email_question(self, question_id: int) -> EmailQuestion:
        email_question = self.cur.execute(
            "SELECT * FROM EmailQuestion WHERE QUESTION_ID = ?",
            (question_id,),
        ).fetchone()
        asking_information = email_question[3].split(DELIMITER)
        return EmailQuestion(email_question[1], email_question[2], asking_information)

    def insert_essay_question(self, task_id: int, essay_title: str) -> int:
        question_id = self.insert_into_questions(task_id)
        self.cur.execute(
            "INSERT INTO EssayQuestion(QUESTION_ID, ESSAY_TITLE) VALUES (?, ?)",
            (question_id, essay_title),
        )
        self.con.commit()
        return question_id

    def get_essay_question(self, question_id: int) -> EssayQuestion:
        essay_question = self.cur.execute(
            "SELECT * FROM EssayQuestion WHERE QUESTION_ID = ?",
            (question_id,),
        ).fetchone()
        return EssayQuestion(essay_question[1])
