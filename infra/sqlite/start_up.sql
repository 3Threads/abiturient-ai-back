DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS QUESTIONS;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Subscribes;
DROP TABLE IF EXISTS MultipleChoiceQuestion;
DROP TABLE IF EXISTS FillWithArticlesQuestion;
DROP TABLE IF EXISTS TitlingQuestion;
DROP TABLE IF EXISTS FillTextQuestion;


CREATE TABLE Subscribes
(
    ID              INTEGER PRIMARY KEY AUTOINCREMENT,
    SUBSCRIBE_TYPE  TEXT    NOT NULL,
    SUBSCRIBE_PRICE FLOAT   NOT NULL,
    TRIAL_DAY       INTEGER NOT NULL
);

CREATE TABLE Users
(
    ID                   INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME             TEXT NOT NULL UNIQUE,
    EMAIL                TEXT NOT NULL UNIQUE,
    PASSWORD             TEXT NOT NULL UNIQUE,
    SUBSCRIBE_ID         INTEGER,
    START_SUBSCRIBE_DATE DATE,
    END_SUBSCRIBE_DATE   DATE

);

---------------------------------------------------------------
CREATE TABLE Exams
(
    EXAM_ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    YEAR      INTEGER NOT NULL,
    VARIANT   INTEGER NOT NULL,
    SUBJECT   TEXT    NOT NULL
);

CREATE TABLE Tasks
(
    TASK_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_NUMBER INTEGER NOT NULL,
    TASK_TITLE  TEXT    NOT NULL,
    POINT       INTEGER NOT NULL,
    TASK_TYPE   TEXT    NOT NULL,
    EXAM_ID     INTEGER NOT NULL,
    FOREIGN KEY (EXAM_ID) REFERENCES Exams (EXAM_ID)
);

CREATE TABLE ListeningTask
(
    task_id          INTEGER PRIMARY KEY,
    address_to_audio TEXT,
    text_num         INTEGER,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

CREATE TABLE MatchParagraphsTask
(
    task_id    INTEGER PRIMARY KEY,
    text_title TEXT,
    paragraphs TEXT,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

CREATE TABLE ReadingTask
(
    task_id    INTEGER PRIMARY KEY,
    text_title TEXT,
    text       TEXT,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

CREATE TABLE FillTextTask
(
    task_id    INTEGER PRIMARY KEY,
    text_title TEXT,
    text       TEXT,
    options    TEXT,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

CREATE TABLE FillTextWithoutOptionsTask
(
    task_id    INTEGER PRIMARY KEY,
    text_title TEXT,
    text       TEXT,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

CREATE TABLE ConversationTask
(
    task_id    INTEGER PRIMARY KEY,
    text_title TEXT,
    text       TEXT,
    dialogues  TEXT,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

CREATE TABLE EmailTask
(
    task_id            INTEGER PRIMARY KEY,
    text_title         TEXT,
    text               TEXT,
    asking_information TEXT,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

CREATE TABLE EssayTask
(
    task_id     INTEGER PRIMARY KEY,
    essay_title TEXT,
    FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
);

---------------------------------------------------------------

CREATE TABLE MultipleChoiceQuestion
(
    QUESTION_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID          INTEGER NOT NULL,
    QUESTION_TEXT    TEXT,
    QUESTION_OPTIONS TEXT,
    QUESTION_ANSWER  TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES Tasks (ID) ON DELETE CASCADE
);


CREATE TABLE FillWithArticlesQuestion
(
    QUESTION_ID    INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID        INTEGER NOT NULL,
    CORRECT_ANSWER TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES Tasks (ID) ON DELETE CASCADE
);


CREATE TABLE TitlingQuestion
(
    QUESTION_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID         INTEGER NOT NULL,
    TITLE           TEXT,
    CORRECT_ANSWERS TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES Tasks (ID) ON DELETE CASCADE
);


CREATE TABLE FillTextQuestion
(
    QUESTION_ID    INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID        INTEGER NOT NULL,
    CORRECT_ANSWER TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES Tasks (ID) ON DELETE CASCADE
);
