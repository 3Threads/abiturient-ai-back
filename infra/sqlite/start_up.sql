DROP TABLE IF EXISTS TASKS;
DROP TABLE IF EXISTS QUESTIONS;


CREATE TABLE TASKS
(
    ID           INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_NUM     INTEGER      NOT NULL,
    TASK_TITLE   TEXT         NOT NULL,
    TASK_TEXT    TEXT         NOT NULL,
    POINT        INTEGER      NOT NULL,
    TASK_TYPE    TEXT         NOT NULL,
    YEAR         INTEGER TEXT NOT NULL,
    VARIANT      INTEGER      NOT NULL,
    SUBJECT      TEXT         NOT NULL,
    QUESTIONS_ID TEXT         NOT NULL
);

CREATE TABLE QUESTIONS
(
    QUESTION_ID       INTEGER PRIMARY KEY AUTOINCREMENT,
    QUESTION_TYPE     TEXT NOT NULL,
    QUESTION_IMG_LINK TEXT,
    QUESTION_TEXT     TEXT,
    QUESTION_OPTIONS  TEXT,
    QUESTION_ANSWERS  TEXT
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
        'english',
        '1#2#3');
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION_IMG_LINK, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWERS)
VALUES ('MultipleChoiceQuestion',
        NULL,
        'What does Sandro want to be?',
        'A doctor.#An actor.#An economist.',
        'A doctor.');
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION_IMG_LINK, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWERS)
VALUES ('MultipleChoiceQuestion',
        NULL,
        'Where does Sandro work? ',
        'In a bank.#In a theatre.#In a bookshop.',
        'In a bookshop.');
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION_IMG_LINK, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWERS)
VALUES ('MultipleChoiceQuestion',
        NULL,
        'Where does Sandro work? ',
        'In a bank.#In a theatre.#In a bookshop.',
        'In a bookshop.');
INSERT INTO QUESTIONS (QUESTION_TYPE, QUESTION_IMG_LINK, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWERS)
VALUES ('MultipleChoiceQuestion',
        NULL,
        'Agatha Christie is called the ‘Queen of Crime’ because sh',
        'used to work as a detective.#is the author of popular books on crime.#is the most translated author of the books on crime',
        'is the author of popular books on crime.');