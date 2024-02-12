import os

from infra.constants import SQL_FILE, DATABASE_NAME, TITLING, READING, FILLING
from infra.sqlite.database_connect import Database
from infra.sqlite.questions import MultipleChoiceQuestionDataBase, FillTextQuestionDataBase, TitlingQuestionDataBase, \
    FillWithArticlesQuestionDataBase
from infra.sqlite.tasks import TasksDatabase


def fill_table():
    db = Database(DATABASE_NAME, os.path.abspath(SQL_FILE))
    db.initial()
    taskDB = TasksDatabase(db.get_connection(), db.get_cursor())
    titlingDB = TitlingQuestionDataBase(db.get_connection(), db.get_cursor())
    mcqDB = MultipleChoiceQuestionDataBase(db.get_connection(), db.get_cursor())
    fill_questionDB = FillTextQuestionDataBase(db.get_connection(), db.get_cursor())
    articlesDB = FillWithArticlesQuestionDataBase(db.get_connection(), db.get_cursor())
    taskDB.insert_task(1,
                       "Read the questions (1-8) and find the answers to them in the paragraphs (A-F) of the text. Some paragraphs correspond to more than one question.",
                       '''A. Harrods department store is one of the most famous shops in London with millions of people visiting each year. In the
                                beginning, though, Harrods was just a small shop in a single room in Stepney, East London. The shop sold only tea and groceries.
                                A young tea merchant, Charles Henry Harrod opened it in 1824 when he was only 25 years old. Besides himself, Charles Henry
                                Harrod employed two assistants and a messenger boy*. In 1849 the store moved to the Knightsbridge area of London and
                                expanded. Just two years later, the Great Exhibition of 1851 brought many visitors to Knightsbridge. This was a great change
                                because, as a result, Harrods attracted more customers and enjoyed great success.
                                10#B. Harrods steadily grew, and by 1873 the name ‘Harrod’s Store’ appeared at the front of the shop. Over several years the shop
                                got bigger and started selling fruit, vegetables and furniture. By 1883 Harrods had grown to six departments across five floors,
                                with over 200 assistants. It started to offer its customers everything from medicines and perfumes to clothing and food. The
                                department store became well known for its high-quality products and excellent personalised service. This way it managed to
                                reach out to wealthy customers who were willing to spend more money for better quality.#C. Then, on the night of December 7, 1883, the store unexpectedly caught fire. The entire building burnt down to the ground. But
                                instead of closing down, the store moved across the street and an architect was hired to build a newer, grander building. Despite
                                the tragedy, all Christmas orders were fulfilled and the store’s reputation was not only saved but also improved. The store reopened
                                the following year. In 1898, Harrods installed England’s first ‘moving stairs’ that we now call an escalator. The first escalator was
                                considered a frightening experience, so nervous customers were offered brandy - an alcoholic drink - at the top floor to calm them
                                down.#D. Ever since Harrods opened, its motto* has been ‘Omnia Omnibus Ubique’. This is a Latin phrase which means ‘All things, for
                                all people, everywhere.’ The motto reflects the store’s goal to provide everything a customer could want. Today, the store has 330
                                departments and customers can get everything from expensive jewellery and furniture, to paper and pens. On an average day,
                                approximately 100,000 people come to shop at Harrods. On peak days, especially during the Christmas season, this number can
                                jump up to 300,000. Harrods still has a strict dress code which means that the doorman won’t let people in if they are wearing the
                                wrong kind of clothes like torn jeans or beach shorts.
                                11#E. Harrods sells everything you can possibly imagine. The store even used to have a pet department, which first opened in 1917.
                                Harrods’ Pet Kingdom sold all kinds of animals – from domestic to exotic pets. In fact, it was the place where, if your wallet and
                                your home were large enough, you could buy an elephant, a tiger, a lion, a panther or even a camel as a household pet. In the
                                1970s, former US president Ronald Reagan bought a baby elephant called Gartie there.#F. Today, more than 5,000 people from over 50 different countries work for this luxury department store. However, the
                                staff are not just shop assistants. Harrods has its own hairdresser’s, doctor’s, bank, fire brigade, café, restaurants and more.
                                A huge team of people clean and look after the store. At night, Harrods is lit up by 12,000 light bulbs on the outside of the
                                building and 300 bulbs have to be changed every day. Now the Harrods name means the best of British quality, service
                                and style. And if the founder of the department store, Charles Henry Harrod, walked into the store today, he would be
                                welcomed with a cup of tea – the very thing that started it all.''',
                       "", 8, TITLING, 2021, 1, "english")

    titlingDB.insert_titling_question(1, "explains how Harrods attracted rich customers?", ["B"])
    titlingDB.insert_titling_question(1, "mentions a cultural event which had a positive effect on Harrods?", ["A"])
    titlingDB.insert_titling_question(1, "states how customers should dress when going to Harrods?", ["D"])
    titlingDB.insert_titling_question(1, "gives the date when the Harrods building was totally destroyed? ", ["C"])
    titlingDB.insert_titling_question(1, "gives the number of people currently employed by Harrods?", ["F"])
    titlingDB.insert_titling_question(1, "mentions the staircase built to carry people between the floors?", ["C"])
    titlingDB.insert_titling_question(1, "could have the title: ‘How it all started’?", ["A"])
    titlingDB.insert_titling_question(1, "could have the title: ‘An extraordinary pet shop’?", ["E"])

    taskDB.insert_task(2,
                       "Read the text and the questions which follow. For each question mark the correct answer (A, B, C or D)",
                       '''This is a true story told by a British-South African environmental activist, Lewis Pugh.
                                Lewis Pugh is a British-South African environmentalist who works hard to protect the oceans of the world. One way he
                                does this is by swimming! He goes on difficult swims in different parts of the world. People from various countries read
                                about Lewis Pugh and watch him swim. Pugh swam at the North Pole to warn people that some of the Arctic Sea ice was
                                disappearing. Another time he swam in a lake on Mount Everest to warn the governments about the effect of climate change
                                in the Himalayas. This is what Lewis Pugh says:
                                ‘Ocean water covers 70% of the earth. But human behaviour is having negative effects on the oceans. Ocean water is
                                becoming dirty and polluted. Many kinds of fish and sea animals are dying off. The Ross Sea in Antarctica is different, it’s
                                completely free of pollution. It contains many different animals and fish such as the Antarctic Toothfish, the Colossal
                                Squid* and the Emperor Penguin. Many of these animals and fish cannot be found anywhere else on the planet. I want to
                                gain global support for the Ross Sea so that it becomes a Protected Area. Because of that I decided to go on five symbolic
                                swims in Antarctica. My first Antarctic swim was near Campbell Island in New Zealand. I started to swim in the freezing
                                water. But after 200 metres, a sea lion attacked me. I had to stop swimming. And my team pulled me out of the water to
                                save me. My next swim was around Cape Adare. I completed a swim of 500 metres. The swim lasted ten minutes. As the
                                water temperature was minus 1.7 degrees, I was extremely cold when I got out of the sea. I had to take a hot shower for 50
                                minutes to get warm. It was a particularly hard swim, because I had to be careful with sharp ice. Needle-sharp ice was
                                cutting my fingers. I was in extreme pain after having swum about 300 metres. I have never felt pain like that before.
                                Nevertheless, my second swim was a great success.
                                13
                                As to my third swim, I had to cancel it because the wind was too strong. Then I travelled to the Bay of Whales in the Ross
                                Sea for my fourth swim. In this swim I was very proud of myself as no one had swum so far south before, but it was very
                                frightening. This area had many dangerous killer whales. But I successfully swam 350 metres in the freezing sea. I
                                remember my crew going out to see that there were no killer whales where I was going to swim. The water was so freezing
                                that it was extremely difficult to breathe. I had to concentrate and swim as quickly as possible. Four days later I had my
                                fifth and final swim. I swam 500 metres near the lonely Peter I Island, 450 kilometres from Antarctica. As I finished, two
                                humpback whales came to the surface of the water near me. This made me joyful. And it reminded me of the reason for
                                my dangerous swims. I have finished my swims, but I have not yet reached my goal. I will now travel around the world to
                                persuade the leaders of different countries to make the Ross Sea a Protected Area.’ ''',
                       "", 8, READING, 2021, 1, "english")

    mcqDB.insert_multiple_choice_question(2, "What is the story about?",
                                          ["A.An Arctic scientist.", "B.An environmentalist.", "C.A swimming champion.",
                                           "D.A person interested in oceanology."], "B")
    mcqDB.insert_multiple_choice_question(2, "The author swam at the North Pole to warn people about",
                                          ["A. the problems on Mount Everest.",
                                           "B. the climate change in the Himalayas.",
                                           "C. the disappearance of some of the ice on the Arctic Sea.",
                                           "D. what the government does to keep oceans clean."], "C")

    mcqDB.insert_multiple_choice_question(2, "What makes the Ross Sea in Antarctica special?",
                                          ["A. It is absolutely clean.", "B. Its water is dirtiest in the world.",
                                           "C. There are very few sea animals there.",
                                           "D. The only fish found there is Toothfish."], "A")

    mcqDB.insert_multiple_choice_question(2, "Why wasn’t the author able to finish his first Antarctic swim?",
                                          ["A. The water was too cold.", "B. 200 meters was too hard to cover.",
                                           "C. His team thought he was drowning.",
                                           "D. A sea animal hit him aggressively."], "D")

    mcqDB.insert_multiple_choice_question(2, "The author considered his swim around Cape Adare especially hard because",
                                          ["A. he had to cover a long distance.", "B. he suffered from terrible pain.",
                                           "C. he had to stay in the water for a long time.",
                                           "D. no hot water could warm him after the swim."], "B")

    mcqDB.insert_multiple_choice_question(2,
                                          "The author was happy with his achievement in swimming very far south in his",
                                          ["A. second swim.", "B. third swim.", "C. fourth swim.", "D. fifth swim."],
                                          "C")

    mcqDB.insert_multiple_choice_question(2, "How did the author feel when he saw two whales very close to him?",
                                          ["A. Scared.", "B. Cheerful.", "C. Worried.", "D. Disappointed."], "B")

    mcqDB.insert_multiple_choice_question(2, "Which of the following would be the best title for the text?",
                                          ["A. Pollution-free areas", "B. How to save ocean animals",
                                           "C. Sportsmen against climate change",
                                           "D. Symbolic swims to protect the environment"], "D")

    taskDB.insert_task(3,
                       "Read the text and fill the gaps with the words given. Use each word only once. Two words are extra.",
                       '''One of the world’s most geographically isolated countries, the Republic of Maldives, also called the Maldives, is situated in the
                                north-central Indian Ocean. It …… (1) of a group of about 1,200 small …… (2) and sandy beaches. The people who live in
                                the Maldives are often …… (3) Maldivians or Maldive Islanders. Due to its geographic …… (4) near the equator, the Maldives
                                enjoys exceptionally …… (5) temperatures practically throughout the whole year. The Maldives has the smallest population in
                                Asia. More than one-quarter of Maldivians live in the city Male. The official …… (6) of the Maldives is Dhivehi, which is believed
                                to originate from the Sri Lankan language Sinhala. Although Maldivians use Dhivehi for most of their daily communications, the
                                English language is becoming more and more …… (7) as the most common second language. The official religion of the Maldives
                                is Sunni Islam, and according to the Maldivian Constitution, only Muslims may be …… (8) of the country. In the early 1980s, the
                                Maldives was one of the world's 20 …… (9) countries because of its low-income; nowadays, it is a middle-income country where
                                only tourism and fishing are the major industries. Tourist agencies bring tourists to the country and take them directly to resorts
                                and private beaches. The tourists do not …… (10) with the local population who dislike alcoholic …… (11) and immodest
                                clothing. Scientists …… (12) that because of the global warming, the sea levels may rise and the islands may disappear completely.''',
                       "called (A)#citizens(B)#communicate (C)#consists (D)#drinks (E)#guide (F)#islands (G)#landscapes (H)#language (I)#location (J)#poorest (K)#popular (L)#warm (M)#worry (N)",
                       12, FILLING, 2021, 1, "english")

    fill_questionDB.insert_fill_text_question(3, 1, "D")
    fill_questionDB.insert_fill_text_question(3, 2, "G")
    fill_questionDB.insert_fill_text_question(3, 3, "A")
    fill_questionDB.insert_fill_text_question(3, 4, "J")
    fill_questionDB.insert_fill_text_question(3, 5, "M")
    fill_questionDB.insert_fill_text_question(3, 6, "I")
    fill_questionDB.insert_fill_text_question(3, 7, "L")
    fill_questionDB.insert_fill_text_question(3, 8, "B")
    fill_questionDB.insert_fill_text_question(3, 9, "K")
    fill_questionDB.insert_fill_text_question(3, 10, "C")
    fill_questionDB.insert_fill_text_question(3, 11, "E")
    fill_questionDB.insert_fill_text_question(3, 12, "N")

    taskDB.insert_task(4,
                       "Read the text and fill the gaps with one of the following: article, preposition, conjunction or relative pronoun. Insert only ONE word. Do not copy the extra words from the text on the answer sheet.",
                       '''An invention is the discovery or creation of a new material, a new process or a new use of existing material. Inventions
                                almost always cause change. Sometimes great inventions are ideas that can change ….. (1) world. Many of the everyday
                                products which we use today were invented years ago. While some inventions were discovered accidentally, most of them
                                were the result ….. (2) hard work, continuous effort ….. (3) a great wish to try again. The invention of the radio has brought
                                distant places closer together, and the invention of the car has made it possible to travel long distances. An invention might
                                also be ….. (4) better way of doing something, ….. (5) example, a tool to make a job easier or some new farming method.
                                When looking for the examples of inventions ….. (6) changed the world, we should consider not just the item, but also the
                                progress it brought about. Many inventions, such as musical instruments ….. (7) sports equipment, have made our life more
                                comfortable and enjoyable. Although there are a lot of inventions, not every good idea leads ….. (8) immediate success.
                                The key to the success of the invention is to be in the right place ….. (9) the right time. It is believed that ….. (10) the 15th
                                century an Italian painter, Leonardo da Vinci, wrote down his idea for big iron chains ….. (11) would drive machines, …..
                                (12) unfortunately the technology to produce those chains didn’t exist then. This shows that even the greatest inventions
                                may be useless if they are ahead of their time.''',
                       "", 12, "articles", 2021, 1, "english")

    articlesDB.insert_fill_with_articles_question(4, ["the"])
    articlesDB.insert_fill_with_articles_question(4, ["of"])
    articlesDB.insert_fill_with_articles_question(4, ["and", "or"])
    articlesDB.insert_fill_with_articles_question(4, ["a"])
    articlesDB.insert_fill_with_articles_question(4, ["for"])
    articlesDB.insert_fill_with_articles_question(4, ["what", "which"])
    articlesDB.insert_fill_with_articles_question(4, ["and", "or"])
    articlesDB.insert_fill_with_articles_question(4, ["to"])
    articlesDB.insert_fill_with_articles_question(4, ["at"])
    articlesDB.insert_fill_with_articles_question(4, ["in"])
    articlesDB.insert_fill_with_articles_question(4, ["that", "which"])
    articlesDB.insert_fill_with_articles_question(4, ["but", "though"])
