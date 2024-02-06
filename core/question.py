from dataclasses import dataclass
from typing import Protocol


class QuestionType(Protocol):
    pass


@dataclass
class MultipleChoiceQuestion(QuestionType):
    question: str
    options: list[str]
    correct_option: str


@dataclass
class TitlingQuestion(QuestionType):
    titles: list[str]
    paragraphs: list[str]
    correct_titles: dict[int, list[str]]


@dataclass
class FillTextQuestion(QuestionType):
    text: str
    options: list[str]
    correct_answers: list[str]


@dataclass
class FillWithArticlesQuestion(QuestionType):
    text: str
    correct_answers: list[list[str]]


@dataclass
class EmailQuestion(QuestionType):
    img_link: str


@dataclass
class EssayQuestion(QuestionType):
    title: str
