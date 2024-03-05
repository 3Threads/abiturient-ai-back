from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.task import (
    MatchParagraphsTask,
    ListeningTask,
    ReadingTask,
    FillTextTask,
    FillTextWithoutOptionsTask, Task, ConversationTask, EmailTask, EssayTask,
)
from infra.constants import DELIMITER, LISTENING, MATCHING, READING, FILLING, FILLING_WITHOUT_OPTIONS, CONVERSATION, \
    EMAIL, ESSAY


@dataclass
class TasksDatabase:
    con: Connection
    cur: Cursor

    # def get_questions_info(self, question_type: str, task_id: str):
    #     sql_script = (
    #             "SELECT * FROM " + question_type + " WHERE TASK_ID = " + str(task_id)
    #     )
    #     questions_info = self.cur.execute(sql_script).fetchall()
    #     return questions_info
    #
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
    def insert_into_tasks(self, task_number: int, task_title: str, task_point: int, task_type: str,
                          exam_id: int) -> int:
        self.cur.execute(
            "INSERT INTO Tasks(TASK_NUMBER, TASK_TITLE, TASK_POINT, TASK_TYPE, EXAM_ID) VALUES (?, ?, ?, ?, ?)",
            (task_number, task_title, task_point, task_type, exam_id),
        )
        last_row_id = self.cur.lastrowid
        self.con.commit()
        return last_row_id

    def insert_listening_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                              address_to_audio: str, text_num: int) -> int:
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        self.cur.execute(
            "INSERT INTO ListeningTask(TASK_ID, ADDRESS_TO_AUDIO, TEXT_NUM) VALUES (?, ?, ?)",
            (task_id, address_to_audio, text_num),
        )
        self.con.commit()
        return task_id

    def get_listening_task(self, task_id: int) -> ListeningTask:
        listening = self.cur.execute(
            "SELECT * FROM ListeningTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

        return ListeningTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            address_to_audio=listening[1],
            text_num=listening[2],
        )

    def insert_match_paragraphs_task(
            self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int, text_title: str,
            paragraphs: list[str]
    ) -> int:
        paragraph = paragraphs[0]
        for i in range(len(paragraphs)):
            if i != 0:
                paragraph = paragraph + f"{DELIMITER}{paragraphs[i]}"
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        self.cur.execute(
            "INSERT INTO MatchParagraphsTask(TASK_ID, TEXT_TITLE, PARAGRAPHS) VALUES (?, ?, ?)",
            (task_id, text_title, paragraph),
        )
        self.con.commit()
        return task_id

    def get_match_paragraphs_task(self, task_id: int) -> MatchParagraphsTask:
        matchParagraphs = self.cur.execute(
            "SELECT * FROM MatchParagraphsTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        return MatchParagraphsTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            text_title=matchParagraphs[1],
            paragraphs=matchParagraphs[2].split(DELIMITER),
        )

    def insert_reading_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                            text_title: str, text: str) -> int:
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        self.cur.execute(
            "INSERT INTO ReadingTask(TASK_ID, TEXT_TITLE, TEXT) VALUES (?, ?, ?)",
            (task_id, text_title, text),
        )
        self.con.commit()
        return task_id

    def get_reading_task(self, task_id: int) -> ReadingTask:
        reading = self.cur.execute(
            "SELECT * FROM ReadingTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        return ReadingTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            text_title=reading[1],
            text=reading[2],
        )

    def insert_fill_text_task(
            self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
            text_title: str, text: str, options: list[str]
    ) -> int:
        option = options[0]
        for i in range(len(options)):
            if i != 0:
                option = option + f"{DELIMITER}{options[i]}"
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        self.cur.execute(
            "INSERT INTO FillTextTask(TASK_ID, TEXT_TITLE, TEXT, OPTIONS) VALUES (?, ?, ?, ?)",
            (task_id, text_title, text, option),
        )
        self.con.commit()
        return task_id

    def get_fill_text_task(self, task_id: int) -> FillTextTask:
        fillText = self.cur.execute(
            "SELECT * FROM FillTextTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        return FillTextTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            text_title=fillText[1],
            text=fillText[2],
            options=fillText[3].split(DELIMITER),
        )

    def insert_fill_text_without_options_task(
            self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
            text_title: str, text: str
    ) -> int:
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        self.cur.execute(
            "INSERT INTO FillTextWithoutOptionsTask(TASK_ID, TEXT_TITLE, TEXT) VALUES (?, ?, ?)",
            (task_id, text_title, text),
        )
        self.con.commit()
        return task_id

    def get_fill_text_without_options_task(
            self, task_id: int
    ) -> FillTextWithoutOptionsTask:
        fillTextWithoutOptions = self.cur.execute(
            "SELECT * FROM FillTextWithoutOptionsTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        return FillTextWithoutOptionsTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            text_title=fillTextWithoutOptions[1],
            text=fillTextWithoutOptions[2],
        )

    def insert_conversation_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                                 text_title: str, text: str, dialogues: list[str]) -> int:
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        dialogue = dialogues[0]
        for i in range(len(dialogues)):
            if i != 0:
                dialogue = dialogue + f"{DELIMITER}{dialogues[i]}"
        self.cur.execute(
            "INSERT INTO ConversationTask(TASK_ID, TEXT_TITLE, TEXT, DIALOGUES) VALUES (?, ?, ?, ?)",
            (task_id, text_title, text, dialogue),
        )
        self.con.commit()
        return task_id

    def get_conversation_task(self, task_id: int) -> ConversationTask:
        conversation = self.cur.execute(
            "SELECT * FROM ConversationTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()

        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        return ConversationTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            text_title=conversation[1],
            text=conversation[2],
            dialogue=conversation[3].split(DELIMITER),
        )

    def insert_email_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                          text_title: str, text: str, asking_information: list[str]) -> int:
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        asking_info = asking_information[0]
        for i in range(len(asking_information)):
            if i != 0:
                asking_info = asking_info + f"{DELIMITER}{asking_information[i]}"
        self.cur.execute(
            "INSERT INTO EmailTask(TASK_ID, TEXT_TITLE, TEXT, ASKING_INFORMATION) VALUES (?, ?, ?, ?)",
            (task_id, text_title, text, asking_info),
        )
        self.con.commit()
        return task_id

    def get_email_task(self, task_id: int) -> EmailTask:
        email = self.cur.execute(
            "SELECT * FROM EmailTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        return EmailTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            text_title=email[1],
            text=email[2],
            asking_information=email[3].split(DELIMITER),
        )

    def insert_essay_task(self, task_number: int, task_title: str, task_point: int, task_type: str, exam_id: int,
                          essay_title: str) -> int:
        task_id = self.insert_into_tasks(task_number, task_title, task_point, task_type, exam_id)
        self.cur.execute(
            "INSERT INTO EssayTask(TASK_ID, ESSAY_TITLE) VALUES (?, ?)",
            (task_id, essay_title),
        )
        self.con.commit()
        return task_id

    def get_essay_task(self, task_id: int) -> EssayTask:
        essay = self.cur.execute(
            "SELECT * FROM EssayTask WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        task = self.cur.execute(
            "SELECT * FROM Tasks WHERE TASK_ID = ?", (task_id,)
        ).fetchone()
        return EssayTask(
            task_id=task[0],
            task_number=task[1],
            task_title=task[2],
            task_point=task[3],
            task_type=task[4],
            exam_id=task[5],
            questions=[],
            essay_title=essay[1],
        )

    def get_tasks(self, exam_id: int) -> list[Task]:
        fetched = self.cur.execute(
            "SELECT * FROM Tasks WHERE EXAM_ID = ?", (exam_id,)
        ).fetchall()
        tasks = []
        for task in fetched:
            task_id = task[0]
            task_type = task[4]
            if task_type == LISTENING:
                listening = self.get_listening_task(task_id)
                tasks.append(listening)
            elif task_type == MATCHING:
                matching = self.get_match_paragraphs_task(task_id)
                tasks.append(matching)
            elif task_type == READING:
                reading = self.get_reading_task(task_id)
                tasks.append(reading)
            elif task_type == FILLING:
                filling = self.get_fill_text_task(task_id)
                tasks.append(filling)
            elif task_type == FILLING_WITHOUT_OPTIONS:
                filling_without_options = self.get_fill_text_without_options_task(task_id)
                tasks.append(filling_without_options)
            elif task_type == CONVERSATION:
                conversation = self.get_conversation_task(task_id)
                tasks.append(conversation)
            elif task_type == EMAIL:
                email = self.get_email_task(task_id)
                tasks.append(email)
            elif task_type == ESSAY:
                essay = self.get_essay_task(task_id)
                tasks.append(essay)
        return tasks
