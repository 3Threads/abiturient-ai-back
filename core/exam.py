from dataclasses import dataclass


@dataclass
class Exam:
    exam_id: int
    year: int
    variant: int
    subject: str
