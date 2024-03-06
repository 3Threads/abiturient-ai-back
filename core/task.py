from abc import ABC
from dataclasses import dataclass
from typing import Protocol

from core.question import QuestionType


@dataclass
class Task(ABC):
    task_id: int
    task_number: int
    task_title: str
    task_point: int
    task_type: str
    questions: list[QuestionType]
    exam_id: int

    def get_questions(self) -> list[QuestionType]:
        return self.questions

    def get_result_points(
            self, answers: list[str]
    ) -> tuple[int, list[tuple[int, str]]]:
        points = 0
        result = []
        for i, question in enumerate(self.questions):
            point, correct_answer = question.check_answer(answers[i])
            if point > 0:
                points += point
            result.append((point, correct_answer))
        return points, result


@dataclass
class ListeningTask(Task):
    address_to_audio: str
    text_num: int = 1


@dataclass
class MatchParagraphsTask(Task):
    text_title: str
    paragraphs: list[str]


@dataclass
class ReadingTask(Task):
    text_title: str
    text: str


@dataclass
class FillTextTask(Task):
    text_title: str
    text: str
    options: list[str]


@dataclass
class FillTextWithoutOptionsTask(Task):
    text_title: str
    text: str


@dataclass
class ConversationTask(Task):
    text_title: str
    text: str
    dialogue: list[str]


@dataclass
class EmailTask(Task):
    pass


@dataclass
class EssayTask(Task):
    pass


class TasksRepository(Protocol):

    def get_tasks(self, subject: str, year: int, variant: int) -> list[Task]:
        pass

    def get_result_points(self, request: dict) -> list[tuple[int, dict[int, str]]]:
        pass
