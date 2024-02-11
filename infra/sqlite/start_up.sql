DROP TABLE IF EXISTS TASKS;
DROP TABLE IF EXISTS QUESTIONS;
DROP TABLE IF EXISTS USERS;
DROP TABLE IF EXISTS SUBSCRIBE;
DROP TABLE IF EXISTS MultipleChoiceQuestion;
DROP TABLE IF EXISTS FillWithArticlesQuestion;
DROP TABLE IF EXISTS TitlingQuestion;
DROP TABLE IF EXISTS FillTextQuestion;

CREATE TABLE SUBSCRIBE
(
    ID              INTEGER PRIMARY KEY AUTOINCREMENT,
    SUBSCRIBE_TYPE  TEXT    NOT NULL,
    SUBSCRIBE_PRICE FLOAT   NOT NULL,
    TRIAL_DAY       INTEGER NOT NULL
);
CREATE TABLE USERS
(
    ID       INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT NOT NULL UNIQUE,
    EMAIL TEXT NOT NULL UNIQUE,
    PASSWORD TEXT NOT NULL UNIQUE,
    HAVE_SUBSCRIBE INTEGER NOT NULL,
    SUBSCRIBE_ID INTEGER,
    START_SUBSCRIBE_DATE DATE,
    END_SUBSCRIBE_DATE DATE,
--     FOREIGN KEY (SUBSCRIBE_ID) REFERENCES SUBSCRIBE(ID),
    CHECK ( HAVE_SUBSCRIBE = 0 OR HAVE_SUBSCRIBE = 1)

);
CREATE TABLE TASKS
(
    ID           INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_NUM     INTEGER      NOT NULL,
    TASK_TITLE   TEXT         NOT NULL,
    TASK_TEXT    TEXT,
    TASK_OPTIONS TEXT,
    POINT        INTEGER      NOT NULL,
    TASK_TYPE    TEXT         NOT NULL,
    YEAR         INTEGER TEXT NOT NULL,
    VARIANT      INTEGER      NOT NULL,
    SUBJECT      TEXT         NOT NULL
);

CREATE TABLE MultipleChoiceQuestion
(
    QUESTION_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID INTEGER NOT NULL,
    QUESTION_TEXT    TEXT,
    QUESTION_OPTIONS TEXT,
    QUESTION_ANSWER  TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES TASKS(ID) ON DELETE CASCADE
);


CREATE TABLE FillWithArticlesQuestion
(
    QUESTION_ID    INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID INTEGER NOT NULL,
    CORRECT_ANSWER TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES TASKS(ID) ON DELETE CASCADE
);


CREATE TABLE TitlingQuestion
(
    QUESTION_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID INTEGER NOT NULL,
    PARAGRAPH       TEXT,
    CORRECT_ANSWERS TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES TASKS(ID) ON DELETE CASCADE
);


CREATE TABLE FillTextQuestion
(
    QUESTION_ID    INTEGER PRIMARY KEY AUTOINCREMENT,
    TASK_ID INTEGER NOT NULL,
    CORRECT_ANSWER TEXT,
    FOREIGN KEY (TASK_ID) REFERENCES TASKS(ID) ON DELETE CASCADE
);
--
-- INSERT INTO TASKS (TASK_NUM, TASK_TITLE, TASK_TEXT, TASK_OPTIONS, POINT, TASK_TYPE, YEAR, VARIANT, SUBJECT)
-- VALUES (1,
--         'You are going to listen to five texts. For each of them answer the two questions given. Mark the correct
-- answer A, B or C. You have 20 seconds to look through the task. You will hear the recording twice.',
--         NULL,
--         NUll,
--         10,
--         'listening',
--         2021,
--         1,
--         'english');
--
-- INSERT INTO MultipleChoiceQuestion (TASK_ID , QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
-- VALUES (1, 'What does Sandro want to be?',
--         'A doctor.#An actor.#An economist.',
--         'A doctor.');
--
-- INSERT INTO MultipleChoiceQuestion (TASK_ID, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
-- VALUES (1, 'Where does Sandro work? ',
--         'In a bank.#In a theatre.#In a bookshop.',
--         'In a bookshop.');
-- INSERT INTO MultipleChoiceQuestion (TASK_ID, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
-- VALUES (1, 'Where does Sandro work? ',
--         'In a bank.#In a theatre.#In a bookshop.',
--         'In a bookshop.');
--
-- INSERT INTO TASKS (TASK_NUM, TASK_TITLE, TASK_TEXT, TASK_OPTIONS, POINT, TASK_TYPE, YEAR, VARIANT, SUBJECT)
-- VALUES (2,
--         'Read the questions (1-8) and find the answers to them in the paragraphs (A-F) of the text. Some
-- paragraphs correspond to more than one question.'
--            ,
--         '1. explains how Harrods attracted rich customers?#
--         2. mentions a cultural event which had a positive effect on Harrods?#
--         3. states how customers should dress when going to Harrods?#
--         4. gives the date when the Harrods building was totally destroyed?#
--         5. gives the number of people currently employed by Harrods?#
--         6. mentions the staircase built to carry people between the floors?',
--         NULL,
--         8,
--         'titling',
--         2021,
--         1,
--         'english');
-- INSERT INTO TitlingQuestion (TASK_ID, PARAGRAPH, CORRECT_ANSWERS)
-- VALUES (2, 'A. Harrods department store is one of the most famous shops in London with millions of people visiting each year. In the
-- beginning, though, Harrods was just a small shop in a single room in Stepney, East London. The shop sold only tea and groceries.
-- A young tea merchant, Charles Henry Harrod opened it in 1824 when he was only 25 years old. Besides himself, Charles Henry
-- Harrod employed two assistants and a messenger boy*. In 1849 the store moved to the Knightsbridge area of London and
-- expanded. Just two years later, the Great Exhibition of 1851 brought many visitors to Knightsbridge. This was a great change
-- because, as a result, Harrods attracted more customers and enjoyed great success.',
--         '1#3#4');
-- INSERT INTO TitlingQuestion (TASK_ID, PARAGRAPH, CORRECT_ANSWERS)
-- VALUES (2, 'B. Harrods steadily grew, and by 1873 the name ‘Harrod’s Store’ appeared at the front of the shop. Over several years the shop
-- got bigger and started selling fruit, vegetables and furniture. By 1883 Harrods had grown to six departments across five floors,
-- with over 200 assistants. It started to offer its customers everything from medicines and perfumes to clothing and food. The
-- department store became well known for its high-quality products and excellent personalised service. This way it managed to
-- reach out to wealthy customers who were willing to spend more money for better quality. ',
--         '2#5');
-- INSERT INTO TitlingQuestion (TASK_ID, PARAGRAPH, CORRECT_ANSWERS)
-- VALUES (2, 'C. Then, on the night of December 7, 1883, the store unexpectedly caught fire. The entire building burnt down to the ground. But
-- instead of closing down, the store moved across the street and an architect was hired to build a newer, grander building. Despite
-- the tragedy, all Christmas orders were fulfilled and the store’s reputation was not only saved but also improved. The store reopened
-- the following year. In 1898, Harrods installed England’s first ‘moving stairs’ that we now call an escalator. The first escalator was
-- considered a frightening experience, so nervous customers were offered brandy - an alcoholic drink - at the top floor to calm them
-- down.',
--         '6');
-- --
-- INSERT INTO TASKS (TASK_NUM, TASK_TITLE, TASK_TEXT, TASK_OPTIONS, POINT, TASK_TYPE, YEAR, VARIANT, SUBJECT) VALUES (
--                                                                                                                                   3,
--                                                                                                                                     'Read the text and the questions which follow. For each question mark the correct answer (A, B, C or D)',
--                                                                                                                                   'This is a true story told by a British-South African environmental activist, Lewis Pugh.
-- Lewis Pugh is a British-South African environmentalist who works hard to protect the oceans of the world. One way he
-- does this is by swimming! He goes on difficult swims in different parts of the world. People from various countries read
-- about Lewis Pugh and watch him swim. Pugh swam at the North Pole to warn people that some of the Arctic Sea ice was
-- disappearing. Another time he swam in a lake on Mount Everest to warn the governments about the effect of climate change
-- in the Himalayas. This is what Lewis Pugh says:
-- ‘Ocean water covers 70% of the earth. But human behaviour is having negative effects on the oceans. Ocean water is
-- becoming dirty and polluted. Many kinds of fish and sea animals are dying off. The Ross Sea in Antarctica is different, it’s
-- completely free of pollution. It contains many different animals and fish such as the Antarctic Toothfish, the Colossal
-- Squid* and the Emperor Penguin. Many of these animals and fish cannot be found anywhere else on the planet. I want to
-- gain global support for the Ross Sea so that it becomes a Protected Area. Because of that I decided to go on five symbolic
-- swims in Antarctica. My first Antarctic swim was near Campbell Island in New Zealand. I started to swim in the freezing
-- water. But after 200 metres, a sea lion attacked me. I had to stop swimming. And my team pulled me out of the water to
-- save me. My next swim was around Cape Adare. I completed a swim of 500 metres. The swim lasted ten minutes. As the
-- water temperature was minus 1.7 degrees, I was extremely cold when I got out of the sea. I had to take a hot shower for 50
-- minutes to get warm. It was a particularly hard swim, because I had to be careful with sharp ice. Needle-sharp ice was
-- cutting my fingers. I was in extreme pain after having swum about 300 metres. I have never felt pain like that before.
-- Nevertheless, my second swim was a great success.
-- 13
-- As to my third swim, I had to cancel it because the wind was too strong. Then I travelled to the Bay of Whales in the Ross
-- Sea for my fourth swim. In this swim I was very proud of myself as no one had swum so far south before, but it was very
-- frightening. This area had many dangerous killer whales. But I successfully swam 350 metres in the freezing sea. I
-- remember my crew going out to see that there were no killer whales where I was going to swim. The water was so freezing
-- that it was extremely difficult to breathe. I had to concentrate and swim as quickly as possible. Four days later I had my
-- fifth and final swim. I swam 500 metres near the lonely Peter I Island, 450 kilometres from Antarctica. As I finished, two
-- humpback whales came to the surface of the water near me. This made me joyful. And it reminded me of the reason for
-- my dangerous swims. I have finished my swims, but I have not yet reached my goal. I will now travel around the world to
-- persuade the leaders of different countries to make the Ross Sea a Protected Area.’ ',
--                                                                                                                                   NULL,
--                                                                                                                                   8,
--                                                                                                                                   'reading',
--                                                                                                                                   2021,
--                                                                                                                                   1,
--                                                                                                                                   'english'
--                                                                                                                                  );
-- INSERT INTO MultipleChoiceQuestion (QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
-- VALUES ('What is the story about?',
--         'A.An Arctic scientist.#B.An environmentalist.# C.A swimming champion.# D.A person interested in oceanology.',
--         'B');
-- INSERT INTO MultipleChoiceQuestion (QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
-- VALUES ('The author swam at the North Pole to warn people about',
--         'A.the problems on Mount Everest. #B.the climate change in the Himalayas.# C.the disappearance of some of the ice on the Arctic Sea. #D.what the government does to keep oceans clean.',
--         'D');
-- INSERT INTO MultipleChoiceQuestion (QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_ANSWER)
-- VALUES ('What makes the Ross Sea in Antarctica special?',
--         'A.It is absolutely clean. #B.Its water is dirtiest in the world.# C.There are very few sea animals there. #D.The only fish found there is Toothfish',
--         'C');