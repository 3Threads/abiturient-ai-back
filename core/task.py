from dataclasses import dataclass
from typing import Protocol

from core.question import QuestionType
from abc import ABC, abstractmethod


@dataclass
class TaskType(ABC):
    questions: list[QuestionType]

    def get_questions(self) -> list[QuestionType]:
        return self.questions

    def get_result_points(self, answers: list[str]) -> tuple[int, dict[int, str]]:
        points = 0
        result = {}
        for i, answer in enumerate(answers):
            point, correct_answer = self.questions[i].check_answer(answer)
            if point == 1:
                points += 1
            else:
                result[i] = correct_answer
        return points, result


@dataclass
class ListeningTask(TaskType):
    pass


@dataclass
class TitlingTask(TaskType):
    titles: list[str]


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

    def get_tasks(self, year: int, variant: int) -> list[Task]:
        pass

    def get_result_points(self, request: dict) -> list[(int, int)]:
        pass
