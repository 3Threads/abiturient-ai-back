from dataclasses import dataclass
from typing import Protocol


class QuestionType(Protocol):
    def check_answer(self, user_answer: str) -> tuple[int, str]:
        pass


@dataclass
class MultipleChoiceQuestion(QuestionType):
    question: str
    options: list[str]
    correct_option: str

    def check_answer(self, user_answer: str) -> tuple[int, str]:
        if user_answer == self.correct_option:
            return 1, self.correct_option
        return 0, self.correct_option


@dataclass
class TitlingQuestion(QuestionType):
    title: str
    correct_titles: str

    def check_answer(self, user_answer: str) -> tuple[int, str]:
        if user_answer == self.correct_titles:
            return 1, self.correct_titles
        return 0, self.correct_titles


@dataclass
class FillTextQuestion(QuestionType):
    correct_answer: str

    def check_answer(self, user_answer: str) -> tuple[int, str]:
        if user_answer == self.correct_answer:
            return 1, self.correct_answer
        return 0, self.correct_answer


@dataclass
class FillWithArticlesQuestion(QuestionType):
    correct_answers: list[str]

    def check_answer(self, user_answer: str) -> tuple[int, str]:
        print(self.correct_answers, user_answer)
        if user_answer in self.correct_answers:
            return 1, ",".join(self.correct_answers)
        return 0, ",".join(self.correct_answers)


@dataclass
class EmailQuestion(QuestionType):
    def check_answer(self, user_answer: str) -> tuple[int, str]:
        return 0, "Not implemented yet ;)"


@dataclass
class EssayQuestion(QuestionType):
    def check_answer(self, user_answer: str) -> tuple[int, str]:
        return 0, "Not implemented yet ;)"
