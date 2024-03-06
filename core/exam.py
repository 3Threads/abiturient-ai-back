from dataclasses import dataclass
from typing import Protocol


@dataclass
class Exam:
    exam_id: int
    year: int
    variant: int
    subject: str


class ExamsRepository(Protocol):

    def create_new_exam(self, subject: str, year: int, variant: int) -> None:
        pass

    def get_exam_id(self, subject: str, year: int, variant: int) -> int:
        pass

    def get_exam(self, exam_id: int) -> Exam:
        pass

    def get_exams(self) -> list[Exam]:
        pass

    def get_exams_by_subject(self, subject: str) -> list[Exam]:
        pass
