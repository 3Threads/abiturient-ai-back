from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.question import (
    QuestionType,
    MultipleChoiceQuestion,
    TitlingQuestion,
    FillTextQuestion,
    FillWithArticlesQuestion,
    EmailQuestion,
    EssayQuestion,
)
from core.task import Task, TitlingTask, ListeningTask, ReadAndWriteTask, FillTextTask, EssayTask, EmailTask, \
    FillWithArticlesTask


@dataclass
class TasksDatabase:
    con: Connection
    cur: Cursor

    def get_tasks(self, subject: str, year: int, variant: int) -> list[Task]:
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
                subject,
                questions_id,
        ) in tasks_info:
            questions = []
            match task_type:
                case "TitlingTask":
                    questions_info = self.get_questions_info("TitlingQuestion", questions_id)
                    print(questions_info)
                    for id, paragraph, correct_answers in questions_info:
                        question = TitlingQuestion(paragraph, correct_answers.split('#'))
                        questions.append(question)
                    task_type = TitlingTask(questions, task_text.split('#'))
                case "ReadAndWriteTask":
                    questions_info = self.get_questions_info("MultipleChoiceQuestion", questions_id)
                    for id, question_text, question_options, question_answer in questions_info:
                        question = MultipleChoiceQuestion(question_text, question_options.split('#'),
                                                          question_answer.split('#'))
                        questions.append(question)
                    task_type = ReadAndWriteTask(questions, task_text)
                case "FillTextTask":
                    questions_info = self.get_questions_info("FillTextQuestion", questions_id)
                    for id, question_answer in questions_info:
                        question = FillTextQuestion(question_answer)
                        questions.append(question)
                    task_type = FillTextTask(questions, task_text, task_options.splite('#'))
                case "FillWithArticlesTask":
                    questions_info = self.get_questions_info("FillWithArticlesQuestion", questions_id)
                    for id, question_answer in questions_info:
                        question = FillWithArticlesQuestion(question_answer.split('#'))
                        questions.append(question)
                    task_type = FillWithArticlesTask(questions, task_text)
                case "EmailTask":
                    email_question = EmailQuestion()
                    task_type = EmailTask([email_question], task_text)
                case "EssayTask":
                    essey_question = EssayQuestion()
                    task_type = EssayTask([essey_question], task_text)
                case "ListeningTask":
                    questions_info = self.get_questions_info("MultipleChoiceQuestion", questions_id)
                    for id, question_text, question_options, question_answer in questions_info:
                        question = MultipleChoiceQuestion(question_text, question_options.split('#'),
                                                          question_answer.split('#'))
                        questions.append(question)
                    task_type = ListeningTask(questions)
            task = Task(task_num, task_title, point, task_type, task_type)
            tasks.append(task)
        return tasks

    def get_questions_info(self, question_type: str, question_ids: str):
        st = ""
        list_of_questions_id = str(question_ids).split("#")
        for id in list_of_questions_id:
            st += id
            st += ","
        st = st[: (len(st) - 1)]
        questions_info = self.cur.execute(
                "SELECT * FROM "+ question_type +" WHERE QUESTION_ID IN (" + st + ")").fetchall()
        return questions_info