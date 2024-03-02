import json
from dataclasses import dataclass, field
from typing import Protocol

from infra.openAI.checker_ai import CheckerAI


class QuestionType(Protocol):
    def check_answer(self, user_answer: str) -> tuple[int, str]:
        pass


@dataclass
class MultipleChoiceQuestion(QuestionType):
    options: list[str]
    correct_option: str
    question: str = field(default_factory=str)

    def check_answer(self, user_answer: str) -> tuple[int, str]:
        if user_answer == self.correct_option:
            return 1, self.correct_option
        return 0, self.correct_option


@dataclass
class OpenQuestion(QuestionType):
    question: str
    correct_answer: str

    def check_answer(self, user_answer: str) -> tuple[int, str]:
        if user_answer == self.correct_answer:
            return 1, self.correct_answer
        return 0, self.correct_answer


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
        #         email = """Dear Sir/Madam,
        # I read your advertisement in the online newspaper. I got interested in it. But there is not enough information about some details in the advertisement. So, I am writing to enquire about some points. First of all, I would like to know where the workshop will take place exactly, so please inform me about it. Then, I would be grateful if you could tell me by whom the workshop will be conducted. And last, can you also tell me when the workshop will start exactly. I look forward to your reply.
        # Thank you in advance."""
        #
        #         result = """{
        #   "my_total_point": 5,
        #   "max_total_point": 6,
        #   "grammar_mistakes": [
        #     "I got interested in it.",
        #     "So, I am writing to enquire about some points.",
        #     "Then, I would be grateful if you could tell me by whom the workshop will be conducted.",
        #     "And last, can you also tell me when the workshop will start exactly."
        #   ],
        #   "corrected_version_of_grammar_mistakes": [
        #     "I became interested in it.",
        #     "Thus, I am writing to inquire about certain details.",
        #     "Additionally, I would appreciate it if you could inform me who will be conducting the workshop.",
        #     "Lastly, could you also tell me exactly when the workshop will start?"
        #   ]
        # }"""

        result = CheckerAI().check_email(
            user_answer,
            """Do you want to learn how to be confident and express yourself
                        clearly? Then read this advert carefully.
                        Arts Centre invites you to join ‘Professional development Workshop’.
                        The workshop will take place <b>in the centre of Rome¹</b>. Attendance is
                        free. <b>An American psychologist²</b> will conduct the workshop. It is held
                        on June 5. The workshop will start <b>in the afternoon³</b>. All the
                        participants will receive a Certificate of Attendance. For more
                        information, please contact us at: artscen@gmail.com
                        <br>1.Where exactly?
                        <br>2.Who?
                        <br>3.When exactly?""",
        )
        print(result)
        json_result = json.loads(result)
        return json_result["my_total_point"], result


@dataclass
class EssayQuestion(QuestionType):
    def check_answer(self, user_answer: str) -> tuple[int, str]:
        #         essay = """Nowadays most 17-18 years old children have to choose what to study at the university. While thinking of a future profession they tend to decline an opportunity of becoming a doctor after realizing how hard the studying will be. So, I completely agree with this issue and I will strengthen my opinion with appropriate arguments.
        #     First of all, I want to emphasize that the length of studying course at a medical university is much longer than at others. In Georgia the difference is approximately 2 years. Secondly, for me it is almost impossible to imagine the difficulty of studying anatomy because it is certain how complicated a human's body is.
        #     However, some people may think that after becoming a doctor exhausting days spent on studying turn into pleasurable life, but although doctors have high-paid jobs, it is still difficult to face to the responsibility of patients' lives.
        #     To conclude, it seems obvious to me that becoming a doctor gives one responsibility which only few can have. It makes a doctor's life difficult."""
        #
        #         result = """{
        #   "my_total_point": 14,
        #   "max_total_point": 16,
        #   "my_Fluency/Task_fulfilment_point": 7,
        #   "max_Fluency/Task_fulfilment_point": 8,
        #   "my_grammar_point": 7,
        #   "max_grammar_point": 8,
        #   "grammar_mistakes": [
        #     "Nowadays most 17-18 years old children",
        #     "the length of studying course",
        #     "In Georgia the difference",
        #     "it is certain how complicated a human's body is.",
        #     "exhausting days spent on studying turn into pleasurable life"
        #   ],
        #   "corrected_version_of_grammar_mistakes": [
        #     "Nowadays, most 17-18-year-old",
        #     "the length of the course of study",
        #     "In Georgia, the difference",
        #     "it is certain that the human body is complicated.",
        #     "exhausting days spent studying turn into a pleasurable life"
        #   ],
        #   "possible_arguments": [
        #     "The extensive length and difficulty of medical education",
        #     "The complexity of human anatomy and medical subjects",
        #     "The high responsibility and stress that comes with being a doctor",
        #     "Comparative analysis with other professions concerning study duration and responsibility levels"
        #   ]
        # }"""

        result = CheckerAI().check_essay(
            user_answer,
            """Some people think that it’s very hard to be a doctor nowadays. Do you agree or disagree with this opinion? State your opinion and support it with reasons and examples""",
        )
        print(result)
        json_result = json.loads(result)
        return json_result["my_total_point"], result
