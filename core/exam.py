from dataclasses import dataclass


@dataclass
class Exam:
    exam_id: int
    subject: str
    year: int
    variant: int
