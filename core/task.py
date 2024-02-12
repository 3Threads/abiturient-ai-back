from abc import ABC
from dataclasses import dataclass
from typing import Protocol

from core.question import QuestionType


@dataclass
class TaskType(ABC):
    questions: list[QuestionType]

    def get_questions(self) -> list[QuestionType]:
        return self.questions

    def get_result_points(self, answers: list[str]) -> tuple[int, dict[int, str]]:
        points = 0
        result = {}
        for i, question in enumerate(self.questions):
            point, correct_answer = question.check_answer(answers[i])
            if point == 1:
                points += 1
            result[i] = correct_answer
        return points, result


@dataclass
class ListeningTask(TaskType):
    pass


@dataclass
class TitlingTask(TaskType):
    paragraphs: list[str]


@dataclass
class ReadAndWriteTask(TaskType):
    text: str


@dataclass
class FillTextTask(TaskType):
    text: str
    options: list[str]


@dataclass
class FillWithArticlesTask(TaskType):
    text: str


@dataclass
class EmailTask(TaskType):
    img_link: str


@dataclass
class EssayTask(TaskType):
    title: str


@dataclass
class Task:
    task_number: int
    task_title: str
    point: int
    task_type: str
    task: TaskType


class TasksRepository(Protocol):

    def get_tasks(self, subject: str, year: int, variant: int) -> list[Task]:
        pass

    def get_result_points(self, request: dict) -> list[tuple[int, dict[int, str]]]:
        pass
