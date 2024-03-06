from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.exam import Exam


@dataclass
class ExamsDatabase:
    con: Connection
    cur: Cursor

    def create_new_exam(self, subject: str, year: int, variant: int) -> None:
        self.cur.execute(
            "INSERT INTO Exams(YEAR, VARIANT, SUBJECT) VALUES (?, ?, ?)",
            (year, variant, subject),
        )
        self.con.commit()

    def get_exam_id(self, subject: str, year: int, variant: int) -> int:
        return self.cur.execute(
            "SELECT EXAM_ID FROM Exams WHERE SUBJECT = ? AND YEAR = ? AND VARIANT = ?",
            (subject, year, variant),
        ).fetchone()[0]

    def get_exam(self, exam_id: int) -> Exam:
        exam_tuple = self.cur.execute(
            "SELECT * FROM Exams WHERE EXAM_ID = ?", (exam_id,)
        ).fetchone()
        return Exam(*exam_tuple)

    def get_exams(self) -> list[Exam]:
        exams_tuple = self.cur.execute(
            "SELECT * FROM Exams"
        ).fetchall()
        exams = []
        for exam in exams_tuple:
            exams.append(Exam(*exam))
        return exams

    def get_exams_by_subject(self, subject: str) -> list[Exam]:
        exams_tuple = self.cur.execute(
            "SELECT * FROM Exams WHERE SUBJECT = ?", (subject,)
        ).fetchall()
        exams = []
        for exam in exams_tuple:
            exams.append(Exam(*exam))
        return exams
