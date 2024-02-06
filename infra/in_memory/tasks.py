from dataclasses import dataclass

from core.question import (
    MultipleChoiceQuestion,
    TitlingQuestion,
    EmailQuestion,
    EssayQuestion,
    FillTextQuestion,
    FillWithArticlesQuestion,
)
from core.task import (
    Task,
    ListeningTask,
    ReadAndWriteTask,
    TitlingTask,
    EmailTask,
    EssayTask,
    FillWithArticlesTask,
    FillTextTask,
)


@dataclass
class TasksInMemory:

    def get_tasks(self, year: int, variant: int) -> list[Task]:
        tasks = []
        multiple_choice_question = MultipleChoiceQuestion(
            "What does Sandro want to be?",
            ["A. A doctor", "B. An actor", "C. An economist"],
            "B",
        )

        task = Task(
            1,
            "You are going to listen to five texts. For each of them answer the two questions given. Mark the correct answer A, B or C. You have 20 seconds to look through the task. You will hear the recording twice. ",
            10,
            "listeningMultiText",
            ListeningTask(
                [
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                    multiple_choice_question,
                ],
            ),
        )
        tasks.append(task)

        task = Task(
            2,
            "You are going to listen to one text with eight questions. Mark the correct answer A, B or C. You now have 30 seconds to look through the task. You will then hear the recording twice.",
            8,
            "listening",
            ListeningTask(
                [[multiple_choice_question] * 8],
            ),
        )
        tasks.append(task)

        titling_question = TitlingQuestion(
            [
                "1. explains how Harrods attracted rich customers?",
                "2. mentions a cultural event which had a positive effect on Harrods? ",
                "3. states how customers should dress when going to Harrods?",
                "4. gives the date when the Harrods building was totally destroyed?",
                "5. gives the number of people currently employed by Harrods? ",
                "6. mentions the staircase built to carry people between the floors?",
                "7. could have the title: ‘How it all started’?",
                "8. could have the title: ‘An extraordinary pet shop’? ",
            ],
            [
                "1. The first paragraph",
                "2. The second paragraph",
                "3. The third paragraph",
                "4. The fourth paragraph",
                "5. The fifth paragraph",
                "6. The sixth paragraph",
            ],
            {
                1: ["A", "B"],
                2: ["C", "D"],
                3: ["E"],
                4: ["F"],
                5: ["A", "B"],
                6: ["C", "D"],
                7: ["E"],
                8: ["F"],
            },
        )

        task = Task(
            3,
            "Read the questions (1-8) and find the answers to them in the paragraphs (A-F) of the text. Some paragraphs correspond to more than one question",
            8,
            "titling",
            TitlingTask(titling_question),
        )
        tasks.append(task)

        task = Task(
            4,
            "Read the text and the questions which follow. For each question mark the correct answer (A, B, C or D).",
            8,
            "readAndWrite",
            ReadAndWriteTask("The text", [multiple_choice_question] * 8),
        )
        tasks.append(task)

        task = Task(
            5,
            "Read the text and fill the gaps with the words given. Use each word only once. Two words are extra.",
            12,
            "fillText",
            FillTextTask(
                FillTextQuestion(
                    "One of the world’s most geographically isolated countries, the Republic of Maldives, also called the Maldives, is situated in the north-central Indian Ocean. It …… (1) of",
                    ["called", "citizens"],
                    ["citizens"],
                )
            ),
        )
        tasks.append(task)

        task = Task(
            6,
            "Read the text and fill the gaps with one of the following: article, preposition, conjunction or relative pronoun. Insert only ONE word. Do not copy the extra words from the text on the answer sheet.",
            12,
            "fillWithArticles",
            FillWithArticlesTask(
                FillWithArticlesQuestion(
                    "An invention is the discovery or creation of a new material, a new process or a new use of existing material. Inventions almost always cause change. Sometimes great inventions are ideas that can change ….. (1) world. Many of the every",
                    [["the", "a"]],
                ),
            ),
        )
        tasks.append(task)

        task = Task(
            7,
            "The advertisement given below is taken from an online newspaper. Read the advertisement and write an email to the editor of the newspaper asking for more information about the details which are indicated. The beginning is given on the answer sheet. Do not write your or anybody else’s name or surname in the letter.",
            6,
            "email",
            EmailTask(EmailQuestion(f"../images/{year}-var{variant}.png")),
        )
        tasks.append(task)

        task = Task(
            8,
            "Read the essay task and write between 120-150 words.",
            16,
            "essay",
            EssayTask(
                EssayQuestion(
                    "Some people think that it’s very hard to be a doctor nowadays. Do you agree or disagree with this opinion? State your opinion and support it with reasons and examples."
                )
            ),
        )
        tasks.append(task)

        return tasks
