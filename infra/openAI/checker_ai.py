import os
from dataclasses import dataclass

from openai import OpenAI

from infra.constants import (
    ESSAY_EVALUATION_SCHEME,
    AI_OUTPUT_EXAMPLE,
    EMAIL_EVALUATION_SCHEME,
)


@dataclass
class CheckerAI:
    ai_output_example = AI_OUTPUT_EXAMPLE
    email_evaluation_scheme = EMAIL_EVALUATION_SCHEME
    essay_evaluation_scheme = ESSAY_EVALUATION_SCHEME

    def __init__(self):
        self.client = OpenAI(api_key=(os.getenv("OPENAI_API_KEY")))

    def check_email(self, email):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-instruct",
            messages=[
                {
                    "role": "user",
                    "content": self.ai_output_example
                    + self.email_evaluation_scheme
                    + email,
                }
            ],
        )
        return response.choices[0].message.content

    def check_essay(self, essay, title):
        prompt = (
            self.essay_evaluation_scheme
            + "\n"
            + self.ai_output_example
            + "This is title: "
            + title
            + "\n this is my essay:\n"
            + essay,
        )
        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "user",
                    "content": prompt[0]
                },
            ],
            # response_format={"type": "json_object"},
        )
        return response.choices[0].message.content
