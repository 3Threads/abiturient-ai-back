DROP TABLE IF EXISTS TASKS;
DROP TABLE IF EXISTS QUESTIONS;


CREATE TABLE TASKS
(
    ID           INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_NUM     INTEGER      NOT NULL,
    TASK_TITLE   TEXT         NOT NULL,
    TASK_TEXT    TEXT,
    TASK_OPTIONS  TEXT,
    POINT        INTEGER      NOT NULL,
    TASK_TYPE    TEXT         NOT NULL,
    YEAR         INTEGER TEXT NOT NULL,
    VARIANT      INTEGER      NOT NULL,
    SUBJECT      TEXT         NOT NULL,
    QUESTIONS_ID TEXT         NOT NULL
);

CREATE TABLE MultipleChoiceQuestion
(
    QUESTION_ID       INTEGER PRIMARY KEY AUTOINCREMENT,
    QUESTION_TEXT     TEXT,
    QUESTION_OPTIONS  TEXT,
    QUESTION_ANSWER  TEXT
);


CREATE TABLE FillWithArticlesQuestion
(
    QUESTION_ID       INTEGER PRIMARY KEY AUTOINCREMENT,
    CORRECT_ANSWER  TEXT
);


CREATE TABLE TitlingQuestion
(
    QUESTION_ID       INTEGER PRIMARY KEY AUTOINCREMENT,
    PARAGRAPH TEXT,
    CORRECT_ANSWERS  TEXT
);


CREATE TABLE FillTextQuestion
(
    QUESTION_ID       INTEGER PRIMARY KEY AUTOINCREMENT,
    CORRECT_ANSWER  TEXT
);

INSERT INTO TASKS (TASK_NUM, TASK_TITLE, TASK_TEXT, POINT, TASK_TYPE, YEAR, VARIANT, SUBJECT, QUESTIONS_ID)
VALUES (1,
        'You are going to listen to five texts. For each of them answer the two questions given. Mark the correct
answer A, B or C. You have 20 seconds to look through the task. You will hear the recording twice.',
        NULL,
        10,
        'ListeningTask',
        2021,
        1,
        'English',
        '1#2#3');
INSERT INTO MultipleChoiceQuestion (QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
VALUES ('What does Sandro want to be?',
        'A doctor.#An actor.#An economist.',
        'A doctor.');
INSERT INTO MultipleChoiceQuestion (QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
VALUES ('Where does Sandro work? ',
        'In a bank.#In a theatre.#In a bookshop.',
        'In a bookshop.');
INSERT INTO MultipleChoiceQuestion (QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
VALUES ('Where does Sandro work? ',
        'In a bank.#In a theatre.#In a bookshop.',
        'In a bookshop.');

INSERT INTO TASKS (TASK_NUM, TASK_TITLE, TASK_TEXT, POINT, TASK_TYPE, YEAR, VARIANT, SUBJECT, QUESTIONS_ID)
VALUES (2,
        'Read the questions (1-8) and find the answers to them in the paragraphs (A-F) of the text. Some
paragraphs correspond to more than one question.'
        ,
        '1. explains how Harrods attracted rich customers?#
        2. mentions a cultural event which had a positive effect on Harrods?#
        3. states how customers should dress when going to Harrods?#
        4. gives the date when the Harrods building was totally destroyed?#
        5. gives the number of people currently employed by Harrods?#
        6. mentions the staircase built to carry people between the floors?',
        8,
        'TitlingTask',
        2021,
        1,
        'English',
        '1#2#3');
INSERT INTO TitlingQuestion (PARAGRAPH, CORRECT_ANSWERS) VALUES (
                                                                 'A. Harrods department store is one of the most famous shops in London with millions of people visiting each year. In the
beginning, though, Harrods was just a small shop in a single room in Stepney, East London. The shop sold only tea and groceries.
A young tea merchant, Charles Henry Harrod opened it in 1824 when he was only 25 years old. Besides himself, Charles Henry
Harrod employed two assistants and a messenger boy*. In 1849 the store moved to the Knightsbridge area of London and
expanded. Just two years later, the Great Exhibition of 1851 brought many visitors to Knightsbridge. This was a great change
because, as a result, Harrods attracted more customers and enjoyed great success.',
                                                                 '1#3#4'
                                                                );
INSERT INTO TitlingQuestion (PARAGRAPH, CORRECT_ANSWERS) VALUES (
                                                                 'B. Harrods steadily grew, and by 1873 the name ‘Harrod’s Store’ appeared at the front of the shop. Over several years the shop
got bigger and started selling fruit, vegetables and furniture. By 1883 Harrods had grown to six departments across five floors,
with over 200 assistants. It started to offer its customers everything from medicines and perfumes to clothing and food. The
department store became well known for its high-quality products and excellent personalised service. This way it managed to
reach out to wealthy customers who were willing to spend more money for better quality. ',
                                                                 '2#5'
                                                                );
INSERT INTO TitlingQuestion (PARAGRAPH, CORRECT_ANSWERS) VALUES (
                                                                 'C. Then, on the night of December 7, 1883, the store unexpectedly caught fire. The entire building burnt down to the ground. But
instead of closing down, the store moved across the street and an architect was hired to build a newer, grander building. Despite
the tragedy, all Christmas orders were fulfilled and the store’s reputation was not only saved but also improved. The store reopened
the following year. In 1898, Harrods installed England’s first ‘moving stairs’ that we now call an escalator. The first escalator was
considered a frightening experience, so nervous customers were offered brandy - an alcoholic drink - at the top floor to calm them
down.',
                                                                 '6'
                                                                )