import os
from dataclasses import dataclass

from openai import OpenAI

from infra.constants import ESSAY_PRE_TEXT, AI_PRE_TEXT


@dataclass
class CheckerAI:
    ai_pre_text = AI_PRE_TEXT
    email_initial = "hello, "
    essay_initial = ESSAY_PRE_TEXT

    def __init__(self):
        self.client = OpenAI(api_key=(os.getenv("OPENAI_API_KEY")))

    def check_email(self, email):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.ai_pre_text + self.email_initial + email,
                }
            ],
        )
        return response.choices[0].message.content

    def check_essay(self, essay, title):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": self.ai_pre_text
                    + self.essay_initial
                    + "This is title: "
                    + title
                    + "\n this is my essay:\n"
                    + essay,
                }
            ],
        )
        return response.choices[0].message.content
