import json
from dataclasses import dataclass
from typing import Protocol

from infra.openAI.checker_ai import CheckerAI


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
        # print(self.correct_answers, user_answer)
        if user_answer in self.correct_answers:
            return 1, ",".join(self.correct_answers)
        return 0, ",".join(self.correct_answers)


@dataclass
class EmailQuestion(QuestionType):
    def check_answer(self, user_answer: str) -> tuple[int, str]:
        result = """{
          "my total point": 13,
          "max total point": 16,
          "my Fluency/Task fulfilment point": 7,
          "max Fluency/Task fulfilment point": 8,
          "my grammar point": 6,
          "max grammar point": 8,
          "grammar mistakes": [
            "17-18 years old children",
            "the tend to decline",
            "length of studying course",
            "a medical university is much longer",
            "it is certain how complicated",
            "exhausting days spent on studying turn into pleasurable life",
            "it is still difficult to face to the responsibility",
            "becoming a doctor hives one responsibility"
          ],
          "corrected version of grammar mistakes": [
            "17-18-year-old children",
            "they tend to decline",
            "length of study",
            "a medical university is significantly longer",
            "it is clear how complicated",
            "exhausting days of study turn into a life of pleasure",
            "it is still difficult to face the responsibility",
            "becoming a doctor gives one a responsibility"
          ],
          "possible arguments": [
            "The extensive duration of medical studies compared to other fields.",
            "The complexity of the human body making medical studies challenging.",
            "Despite the high pay, the immense responsibility over patients' lives remains a challenge for doctors."
          ]
        }"""

        json_result = json.loads(result)
        return json_result["my total point"], result


@dataclass
class EssayQuestion(QuestionType):
    def check_answer(self, user_answer: str) -> tuple[int, str]:
        essay = """Nowadays most 17-18 years old children have to choose what to study at the university. While thinking of a future profession the tend to decline an opportunity of becoming a doctor after realizing how hard the studying will be. So, I completely agree with this issue and I will strengthen my opinion with appropriate arguments. 
    First of all, I want to emphasize that the length of studying course at a medical university is much longer than at others. In Georgia the difference is approximately 2 years. Secondly, for me it is almost impossible to imagine the difficulty of studying anatomy because it is certain how complicated a human's body is.
    However, some people may think that after becoming a doctor exhausting days spent on studying turn into pleasurable life, but although doctors have high-paid jobs, it is still difficult to face to the responsibility of patients' lives.
    To conclude, it seems obvious to me that becoming a doctor hives one responsibility which only few can have. It makes a doctor's life difficult."""
        # return 0, "Not implemented yet ;)"

        # result = CheckerAI().check_essay(
        #     user_answer,
        #     """Some people think that it’s very hard to be a doctor nowadays. Do you agree or disagree with this opinion? State your opinion and support it with reasons and examples""",
        # )
        result = """{
          "my_total_point": 13,
          "max_total_point": 16,
          "my_Fluency/Task_fulfilment_point": 7,
          "max_Fluency/Task_fulfilment_point": 8,
          "my_grammar_point": 6,
          "max_grammar_point": 8,
          "grammar_mistakes": [
            "17-18 years old children",
            "the tend to decline",
            "length of studying course",
            "a medical university is much longer",
            "it is certain how complicated",
            "exhausting days spent on studying turn into pleasurable life",
            "it is still difficult to face to the responsibility",
            "becoming a doctor hives one responsibility"
          ],
          "corrected_version_of_grammar_mistakes": [
            "17-18-year-old children",
            "they tend to decline",
            "length of study",
            "a medical university is significantly longer",
            "it is clear how complicated",
            "exhausting days of study turn into a life of pleasure",
            "it is still difficult to face the responsibility",
            "becoming a doctor gives one a responsibility"
          ],
          "possible_arguments": [
            "The extensive duration of medical studies compared to other fields.",
            "The complexity of the human body making medical studies challenging.",
            "Despite the high pay, the immense responsibility over patients' lives remains a challenge for doctors."
          ]
        }"""
        json_result = json.loads(result)
        return json_result["my_total_point"], result
