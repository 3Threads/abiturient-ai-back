from dataclasses import dataclass
from typing import Protocol

from core.question import QuestionType


class TaskType(Protocol):
    def get_questions(self) -> list[QuestionType]:
        pass

    def get_question(self) -> QuestionType:
        pass


@dataclass
class ListeningTask(TaskType):
    questions: list[QuestionType]

    def get_questions(self):
        return self.questions


@dataclass
class TitlingTask(TaskType):
    question: QuestionType

    def get_question(self):
        return self.question


@dataclass
class ReadAndWriteTask(TaskType):
    text: str
    questions: list[QuestionType]

    def get_questions(self):
        return self.questions


@dataclass
class FillTextTask(TaskType):
    question: QuestionType

    def get_questions(self):
        return self.question


@dataclass
class FillWithArticlesTask(TaskType):
    question: QuestionType

    def get_questions(self):
        return self.question


@dataclass
class EmailTask(TaskType):
    question: QuestionType

    def get_questions(self):
        return self.question


@dataclass
class EssayTask(TaskType):
    question: QuestionType

    def get_questions(self):
        return self.question


@dataclass
class Task:
    task_number: int
    task_title: str
    point: int
    task_type: str
    task: TaskType


class TasksRepository(Protocol):

    def get_tasks(self, year: int, variant: int, subject: str) -> list[Task]:
        pass
