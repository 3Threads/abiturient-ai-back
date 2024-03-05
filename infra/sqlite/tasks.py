from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.task import (
    MatchParagraphsTask,
    ListeningTask,
    ReadingTask,
    FillTextTask,
    FillTextWithoutOptionsTask,
)


@dataclass
class TasksDatabase:
    con: Connection
    cur: Cursor

    # def get_tasks(self, subject: str, year: int, variant: int) -> list[Task]:
    #     global task_1
    #     tasks_info = self.cur.execute(
    #         "SELECT * FROM TASKS WHERE SUBJECT = ? AND VARIANT = ? AND YEAR = ?",
    #         [subject, variant, year],
    #     ).fetchall()
    #     tasks = []
    #     for (
    #             id,
    #             task_num,
    #             task_title,
    #             task_text,
    #             task_options,
    #             point,
    #             task_type,
    #             year,
    #             variant,
    #             subject,
    #     ) in tasks_info:
    #         questions = []
    #         match task_type:
    #             case "titling":
    #                 questions_info = self.get_questions_info("TitlingQuestion", id)
    #                 for id, t_id, paragraph, correct_answers in questions_info:
    #                     question = OpenQuestion(paragraph, correct_answers)
    #                     questions.append(question)
    #                 task_1 = MatchParagraphsTask(questions, task_text.split("#"))
    #             case "reading":
    #                 questions_info = self.get_questions_info(
    #                     "MultipleChoiceQuestion", id
    #                 )
    #                 for (
    #                         id,
    #                         t_id,
    #                         question_text,
    #                         question_options,
    #                         question_answer,
    #                 ) in questions_info:
    #                     question = MultipleChoiceQuestion(
    #                         question_text, question_options.split("#"), question_answer
    #                     )
    #                     questions.append(question)
    #                 task_1 = ReadingTask(questions, task_text)
    #             case "filling":
    #                 questions_info = self.get_questions_info("FillTextQuestion", id)
    #                 for id, t_id, question_answer in questions_info:
    #                     question = FillTextQuestion(question_answer)
    #                     questions.append(question)
    #                 task_1 = FillTextTask(questions, task_text, task_options.split("#"))
    #             case "articles":
    #                 questions_info = self.get_questions_info(
    #                     "FillWithArticlesQuestion", id
    #                 )
    #                 for id, t_id, question_answer in questions_info:
    #                     question = FillWithArticlesQuestion(question_answer.split("#"))
    #                     questions.append(question)
    #                 task_1 = FillTextWithoutOptionsTask(questions, task_text)
    #             case "email":
    #                 email_question = EmailQuestion()
    #                 task_1 = EmailTask([email_question], task_text)
    #             case "essay":
    #                 essey_question = EssayQuestion()
    #                 task_1 = EssayTask([essey_question], task_text)
    #             case "listening":
    #                 questions_info = self.get_questions_info(
    #                     "MultipleChoiceQuestion", id
    #                 )
    #                 for (
    #                         id,
    #                         t_id,
    #                         question_text,
    #                         question_options,
    #                         question_answer,
    #                 ) in questions_info:
    #                     question = MultipleChoiceQuestion(
    #                         question_text, question_options.split("#"), question_answer
    #                     )
    #                     questions.append(question)
    #                 task_1 = ListeningTask(questions)
    #         task = Task(task_num, task_title, point, task_type, task_1)
    #         tasks.append(task)
    #     return tasks
    #
    # def get_questions_info(self, question_type: str, task_id: str):
    #     sql_script = (
    #             "SELECT * FROM " + question_type + " WHERE TASK_ID = " + str(task_id)
    #     )
    #     questions_info = self.cur.execute(sql_script).fetchall()
    #     return questions_info
    #
    # def insert_task(
    #         self,
    #         task_num: int,
    #         task_title: str,
    #         task_text: str,
    #         task_options: str,
    #         point: int,
    #         task_type: str,
    #         year: int,
    #         variant: int,
    #         subject: str,
    # ):
    #     self.cur.execute(
    #         "INSERT INTO TASKS(TASK_NUM, TASK_TITLE, TASK_TEXT, TASK_OPTIONS, POINT, TASK_TYPE, YEAR, VARIANT, SUBJECT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #         (
    #             task_num,
    #             task_title,
    #             task_text,
    #             task_options,
    #             point,
    #             task_type,
    #             year,
    #             variant,
    #             subject,
    #         ),
    #     )
    #     self.con.commit()

    # def get_result_points(
    #         self, request: dict
    # ) -> list[tuple[int, list[tuple[int, str]]]]:
    #     subject = request["subject"]
    #     year = request["year"]
    #     variant = request["variant"]
    #     tasks = self.get_tasks(subject, year, variant)
    #     answers = request["answers"]
    #
    #     results = []
    #     for task in tasks:
    #         results.append(task.task.get_result_points(answers[task.task_number - 1]))
    #
    #     return results

    # - - - - - - - - - - - - - - - - - - -
    def insert_listening_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                              task_id: int, address_to_audio: str, text_num: int):
        self.cur.execute(
            "INSERT INTO ListeningTask(TASK_ID, ADDRESS_TO_AUDIO, TEXT_NUM) VALUES (?, ?, ?)",
            (task_id, address_to_audio, text_num),
        )

        self.con.commit()

    def get_listening_task(self, task_id: int) -> ListeningTask:
        return self.cur.execute(
            "SELECT * FROM ListeningTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

    def insert_match_paragraphs_task(
            self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int, task_id: int,
            text_title: str, paragraphs: list[str]
    ):
        paragraph = paragraphs[0]
        for i in range(len(paragraphs)):
            if i != 0:
                paragraph = paragraph + f"#{paragraphs[i]}"
        self.cur.execute(
            "INSERT INTO MatchParagraphsTask(TASK_ID, TEXT_TITLE, PARAGRAPHS) VALUES (?, ?, ?)",
            (task_id, text_title, paragraph),
        )
        self.con.commit()

    def get_match_paragraphs_task(self, task_id: int) -> MatchParagraphsTask:
        return self.cur.execute(
            "SELECT * FROM MatchParagraphsTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

    def insert_reading_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                            task_id: int, text_title: str, text: str):
        self.cur.execute(
            "INSERT INTO ReadingTask(TASK_ID, TEXT_TITLE, TEXT) VALUES (?, ?, ?)",
            (task_id, text_title, text),
        )
        self.con.commit()

    def get_reading_task(self, task_id: int) -> ReadingTask:
        return self.cur.execute(
            "SELECT * FROM ReadingTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

    def insert_fill_text_task(
            self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
            task_id: int, text_title: str, text: str, options: list[str]
    ):
        option = options[0]
        for i in range(len(options)):
            if i != 0:
                option = option + f"#{options[i]}"
        self.cur.execute(
            "INSERT INTO FillTextTask(TASK_ID, TEXT_TITLE, TEXT, OPTIONS) VALUES (?, ?, ?, ?)",
            (task_id, text_title, text, option),
        )
        self.con.commit()

    def get_fill_text_task(self, task_id: int) -> FillTextTask:
        return self.cur.execute(
            "SELECT * FROM FillTextTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

    def insert_fill_text_without_options_task(
            self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
            task_id: int, text_title: str, text: str
    ):
        self.cur.execute(
            "INSERT INTO FillTextWithoutOptionsTask(TASK_ID, TEXT_TITLE, TEXT) VALUES (?, ?, ?)",
            (task_id, text_title, text),
        )
        self.con.commit()

    def get_fill_text_without_options_task(
            self, task_id: int
    ) -> FillTextWithoutOptionsTask:
        return self.cur.execute(
            "SELECT * FROM FillTextWithoutOptionsTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

    def insert_conversation_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                                 task_id: int, text_title: str, text: str, dialogues: str):
        self.cur.execute(
            "INSERT INTO ConversationTask(TASK_ID, TEXT_TITLE, TEXT, DIALOGUES) VALUES (?, ?, ?, ?)",
            (task_id, text_title, text, dialogues),
        )
        self.con.commit()

    def get_conversation_task(self, task_id: int) -> str:
        return self.cur.execute(
            "SELECT * FROM ConversationTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

    def insert_email_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                          task_id: int, text_title: str, text: str, asking_information: str):
        self.cur.execute(
            "INSERT INTO EmailTask(TASK_ID, TEXT_TITLE, TEXT, ASKING_INFORMATION) VALUES (?, ?, ?, ?)",
            (task_id, text_title, text, asking_information),
        )
        self.con.commit()

    def get_email_task(self, task_id: int) -> str:
        return self.cur.execute(
            "SELECT * FROM EmailTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

    def insert_essay_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                          task_id: int, essay_title: str):
        self.cur.execute(
            "INSERT INTO EssayTask(TASK_ID, ESSAY_TITLE) VALUES (?, ?)",
            (task_id, essay_title),
        )
        self.con.commit()

    def get_essay_task(self, task_id: int) -> str:
        return self.cur.execute(
            "SELECT * FROM EssayTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
