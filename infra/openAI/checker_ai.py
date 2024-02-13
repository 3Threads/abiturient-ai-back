import os
from dataclasses import dataclass

from openai import OpenAI


@dataclass
class CheckerAI:
    email_initial = "hello, "
    essay_initial = "This essay is"

    def __init__(self):
        self.client = OpenAI(api_key=(os.getenv("OPENAI_API_KEY")))

    def check_email(self, email):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.email_initial + email}],
        )
        return response.choices[0].message.content

    def check_essay(self, essay):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.essay_initial + essay}],
        )
        return response.choices[0].message.content
