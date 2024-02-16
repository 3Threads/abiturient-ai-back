import os
from dataclasses import dataclass

from openai import OpenAI

from infra.constants import (
    ESSAY_EVALUATION_SCHEME,
    AI_OUTPUT_EXAMPLE_ESSAY,
    EMAIL_EVALUATION_SCHEME,
    AI_OUTPUT_EXAMPLE_EMAIL,
)


@dataclass
class CheckerAI:
    email_evaluation_scheme = EMAIL_EVALUATION_SCHEME
    essay_evaluation_scheme = ESSAY_EVALUATION_SCHEME

    def __init__(self):
        self.client = OpenAI(api_key=(os.getenv("OPENAI_API_KEY")))

    def check_email(self, email, advertisement):
        prompt = (
            self.email_evaluation_scheme
            + "\n"
            + AI_OUTPUT_EXAMPLE_EMAIL
            + "This is advertisement: "
            + advertisement
            + "\n this is my email:\n"
            + email,
        )
        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": "Please output valid json",
                },
                {"role": "user", "content": prompt[0]},
            ],
            response_format={"type": "json_object"},
        )
        return response.choices[0].message.content

    def check_essay(self, essay, title):
        prompt = (
            self.essay_evaluation_scheme
            + "\n"
            + AI_OUTPUT_EXAMPLE_ESSAY
            + "This is title: "
            + title
            + "\n this is my essay:\n"
            + essay,
        )
        response = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": "Please output valid json",
                },
                {"role": "user", "content": prompt[0]},
            ],
            response_format={"type": "json_object"},
        )
        return response.choices[0].message.content
