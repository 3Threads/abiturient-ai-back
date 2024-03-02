from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.question import (
    MultipleChoiceQuestion,
    OpenQuestion,
    FillTextQuestion,
    FillWithArticlesQuestion,
    EmailQuestion,
    EssayQuestion,
)
from core.task import Task, MatchParagraphsTask, ListeningTask, ReadingTask, FillTextTask, EssayTask, EmailTask, \
    FillTextWithoutOptionsTask


@dataclass
class TasksDatabase:
    con: Connection
    cur: Cursor

    def get_tasks(self, subject: str, year: int, variant: int) -> list[Task]:
        global task_1
        tasks_info = self.cur.execute(
            "SELECT * FROM TASKS WHERE SUBJECT = ? AND VARIANT = ? AND YEAR = ?",
            [subject, variant, year],
        ).fetchall()
        tasks = []
        for (
                id,
                task_num,
                task_title,
                task_text,
                task_options,
                point,
                task_type,
                year,
                variant,
                subject
        ) in tasks_info:
            questions = []
            match task_type:
                case "titling":
                    questions_info = self.get_questions_info("TitlingQuestion", id)
                    for id, t_id, paragraph, correct_answers in questions_info:
                        question = OpenQuestion(paragraph, correct_answers)
                        questions.append(question)
                    task_1 = MatchParagraphsTask(questions, task_text.split('#'))
                case "reading":
                    questions_info = self.get_questions_info("MultipleChoiceQuestion", id)
                    for id, t_id, question_text, question_options, question_answer in questions_info:
                        question = MultipleChoiceQuestion(question_text, question_options.split('#'),
                                                          question_answer)
                        questions.append(question)
                    task_1 = ReadingTask(questions, task_text)
                case "filling":
                    questions_info = self.get_questions_info("FillTextQuestion", id)
                    for id,t_id,  question_answer in questions_info:
                        question = FillTextQuestion(question_answer)
                        questions.append(question)
                    task_1 = FillTextTask(questions, task_text, task_options.split('#'))
                case "articles":
                    questions_info = self.get_questions_info("FillWithArticlesQuestion", id)
                    for id, t_id, question_answer in questions_info:
                        question = FillWithArticlesQuestion(question_answer.split('#'))
                        questions.append(question)
                    task_1 = FillTextWithoutOptionsTask(questions, task_text)
                case "email":
                    email_question = EmailQuestion()
                    task_1 = EmailTask([email_question], task_text)
                case "essay":
                    essey_question = EssayQuestion()
                    task_1 = EssayTask([essey_question], task_text)
                case "listening":
                    questions_info = self.get_questions_info("MultipleChoiceQuestion", id)
                    for id, t_id, question_text, question_options, question_answer in questions_info:
                        question = MultipleChoiceQuestion(question_text, question_options.split('#'),
                                                          question_answer)
                        questions.append(question)
                    task_1 = ListeningTask(questions)
            task = Task(task_num, task_title, point, task_type, task_1)
            tasks.append(task)
        return tasks

    def get_questions_info(self, question_type: str, task_id: str):
        sql_script = "SELECT * FROM " + question_type + " WHERE TASK_ID = " + str(task_id)
        questions_info = self.cur.execute(sql_script).fetchall()
        return questions_info

    def insert_task(self, task_num: int, task_title: str, task_text: str, task_options: str, point: int, task_type: str,
                    year: int, variant: int, subject: str):
        self.cur.execute(
            "INSERT INTO TASKS(TASK_NUM, TASK_TITLE, TASK_TEXT, TASK_OPTIONS, POINT, TASK_TYPE, YEAR, VARIANT, SUBJECT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (task_num, task_title, task_text, task_options, point, task_type, year, variant, subject))
        self.con.commit()

    def get_result_points(self, request: dict) -> list[tuple[int, list[tuple[int, str]]]]:
        subject = request["subject"]
        year = request["year"]
        variant = request["variant"]
        tasks = self.get_tasks(subject, year, variant)
        answers = request["answers"]

        results = []
        for task in tasks:
            results.append(task.task.get_result_points(answers[task.task_number-1]))

        return results