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
from core.task import Task, TitlingTask, ListeningTask, ReadAndWriteTask, FillTextTask


@dataclass
class TasksDatabase:
    con: Connection
    cur: Cursor

    def get_tasks(self, year: int, variant: int, subject: str) -> list[Task]:
        tasks_info = self.cur.execute(
            "SELECT * FROM TASKS " "WHERE SUBJECT = ? AND VARIANT = ? AND YEAR = ?",
            [subject, variant, year],
        ).fetchall()
        tasks = []
        for (
            id,
            task_num,
            task_title,
            task_text,
            point,
            task_type,
            year,
            variant,
            subject,
            questions_id,
        ) in tasks_info:
            st = ""
            list_of_questions_id = str(questions_id).split("#")
            for id in list_of_questions_id:
                st += id
                st += ","
            st = st[: (len(st) - 1)]
            print(st)
            questions_info = self.cur.execute(
                "SELECT * FROM QUESTIONS WHERE QUESTION_ID IN (" + st + ")"
            ).fetchall()

            print(questions_info)
            questions = []
            for question_info in questions_info:
                questions.append(self.get_question(question_info))
            match task_type:
                case "TitlingTask":
                    task_type = TitlingTask(questions[0])
                case "ReadAndWriteTask":
                    task_type = ReadAndWriteTask(task_text, questions)
                case "FillTextTask":
                    task_type = FillTextTask(questions[0])
                case "FillWithArticlesTask":
                    task_type = FillTextTask(questions[0])
                case "EmailTask":
                    task_type = FillTextTask(questions[0])
                case "EssayTask":
                    task_type = FillTextTask(questions[0])
                case "ListeningTask":
                    task_type = ListeningTask(questions)
            task = Task(task_num, task_title, point, task_type, task_type)
            tasks.append(task)
        return tasks

    def get_question(self, question_info) -> QuestionType:
        (
            question_id,
            question_type,
            question_img_link,
            question_text,
            question_options,
            questions_answers,
        ) = question_info
        match question_type:
            case "MultipleChoiceQuestion":
                options = question_options.split("#")
                return MultipleChoiceQuestion(question_text, options, questions_answers)
            case "TitlingQuestion":
                paragraphs = question_text.split("#")
                titles = question_options.split("#")
                answers = questions_answers.split("###")
                correct_answers: dict[int : list[str]] = {}
                for an in answers:
                    paragraph_index, answers = an.splite("##")
                    correct_answers[int(paragraph_index)] = list(answers.splite("#"))
                return TitlingQuestion(titles, paragraphs, correct_answers)
            case "FillTextQuestion":
                options = question_options.split("#")
                answers = questions_answers.split("#")
                return FillTextQuestion(question_text, options, answers)
            case "FillWithArticlesQuestion":
                answers = questions_answers.split("##")
                correct_answers = []
                for answ in answers:
                    correct_answers.append(answers(answ.split("#")))
                return FillWithArticlesQuestion(question_text, correct_answers)
            case "EmailQuestion":
                return EmailQuestion(question_img_link)
            case "EssayQuestion":
                return EssayQuestion(question_text)
