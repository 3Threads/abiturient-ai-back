import sqlite3
from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from infra.constants import SQL_FILE_TEST


@dataclass
class Database:
    database_name: str
    sql_file: str = SQL_FILE_TEST

    def __post_init__(self) -> None:
        self.con = sqlite3.connect(self.database_name, check_same_thread=False)
        self.con.execute("PRAGMA foreign_keys = 1")
        self.cur = self.con.cursor()

    def initial(self) -> None:
        with open(self.sql_file, "r") as sql_file:
            sql = sql_file.read()
        self.cur.executescript(sql)
        self.con.commit()
        # self.fill_table()

    def close_database(self) -> None:
        self.con.close()

    def get_connection(self) -> Connection:
        return self.con

    def get_cursor(self) -> Cursor:
        return self.cur

    # def fill_table(self) -> None:
    #     subscriptionDB = SubscribesDataBase(self.con, self.cur)
    #     subscriptionDB.add_subscribe("Free", 0.0, 365)
    #     subscriptionDB.add_subscribe("PremiumMonthly", 10, 30)
    #     subscriptionDB.add_subscribe("PremiumAnnually", 90, 365)
    #     subscriptionDB.add_subscribe("UltimateMonthly", 30, 30)
    #     subscriptionDB.add_subscribe("UltimateAnnually", 280, 365)
    #
    #     taskDB = TasksDatabase(self.con, self.cur)
    #     titlingDB = TitlingQuestionDataBase(self.con, self.cur)
    #     mcqDB = MultipleChoiceQuestionDataBase(self.con, self.cur)
    #     fill_questionDB = FillTextQuestionDataBase(self.con, self.cur)
    #     articlesDB = FillWithArticlesQuestionDataBase(self.con, self.cur)
    #
    #     taskDB.insert_task(
    #         1,
    #         "Read the questions (1-8) and find the answers to them in the paragraphs (A-F) of the text. Some paragraphs correspond to more than one question.",
    #         """A. Leonardo da Vinci, born in 1452 in the heart of Italy, was a polymath whose areas of interest included invention, painting, sculpting, architecture, science, music, mathematics, engineering, literature, anatomy, geology, astronomy, botany, writing, history, and cartography. He has been variously called the father of palaeontology, ichnology, and architecture, and is widely considered one of the greatest painters of all time. Despite his many contributions in other areas, Leonardo is best known for his masterpieces: The Mona Lisa and The Last Supper, which are among the most influential works in the history of art.
    #     10
    #     # B. Leonardo’s early life was spent in the Vinci region of Italy where he received an informal education that included Latin, geometry, and mathematics. However, it was his apprenticeship under the artist Verrocchio in Florence that truly ignited his career in the arts. This period was crucial for Leonardo, as he was exposed to both the technical and creative aspects of being an artist. Additionally, his curiosity in the sciences began to shape his approach to art, leading him to study the human body, animals, and nature in great detail.
    #     11
    #     # C. Perhaps one of the most fascinating aspects of Leonardo’s work was his meticulous research and detailed journals. He filled thousands of pages with sketches, scientific diagrams, and his observations on topics ranging from the anatomy of humans and animals to the characteristics of light and shadow in painting. His studies in anatomy, in particular, were so advanced that they foreshadowed the discoveries of later scientists and medical practitioners.
    #     12
    #     # D. Despite the reverence we hold for Leonardo today, his contemporaries often saw him as a figure of contradiction and controversy. Known for his erratic work habits, he left many projects unfinished and was constantly juggling multiple endeavors. This aspect of his personality led to a somewhat tumultuous relationship with his patrons. Moreover, his pursuits in scientific research were often met with skepticism, as they challenged the prevailing norms and beliefs of the time.
    #     13
    #     # E. One of the lesser-known facets of Leonardo’s legacy is his contribution to engineering and inventions. He conceptualized flying machines, a type of armored vehicle, concentrated solar power, an adding machine, and the double hull. Albeit most of these were not constructed during his lifetime, they are considered remarkably ahead of their time. His inventions showcased his belief in the potential for human ingenuity to overcome the limitations of nature.
    #     14
    #     # F. In his later years, Leonardo left Italy to work in France upon the invitation of King Francis I. It was in France that Leonardo spent the last years of his life, continuing his work in art and science until his death in 1519. He was buried in the Chapel of Saint-Hubert in the castle of Amboise. Today, his legacy lives on, not only in his art and scientific contributions but also in the countless stories and legends that surround his life and personality.",
    #     """,
    #         "",
    #         8,
    #         TITLING,
    #         2021,
    #         1,
    #         "english",
    #     )
    #
    #     titlingDB.insert_titling_question(1, "highlights Leonardo's contributions outside of painting?", ["C"])
    #     titlingDB.insert_titling_question(1, "details Leonardo's formative years and education?", ["B"])
    #     titlingDB.insert_titling_question(1, "describes the relationship with his contemporaries and patrons?", ["D"])
    #     titlingDB.insert_titling_question(1, "mentions where Leonardo spent his final years?", ["F"])
    #     titlingDB.insert_titling_question(1, "could have the title: ‘The Genius of Invention’?", ["E"])
    #     titlingDB.insert_titling_question(1, "outlines the subjects Leonardo da Vinci studied?", ["C"])
    #     titlingDB.insert_titling_question(1, "could have the title: ‘Early Life of a Polymath’?", ["B"])
    #     titlingDB.insert_titling_question(1, "presents Leonardo's most famous artworks?", ["A"])
    #
    #     taskDB.insert_task(
    #         2,
    #         "Read the text and the questions which follow. For each question mark the correct answer (A, B, C or D)",
    #         """The narrative revolves around Maria Silva, a Brazilian wildlife conservationist who is devoted to protecting the Amazon rainforest. Maria Silva is not
    # just any conservationist; she has spent her life in the Amazon, working tirelessly to save its diverse ecosystems. She does this by monitoring wildlife,
    # collaborating with local communities, and raising global awareness. Maria undertook a remarkable journey on foot across various parts of the Amazon to
    # document and expose the impacts of deforestation. Here is what Maria Silva says: ‘The Amazon rainforest, often described as the planet's lungs, plays a
    # crucial role in regulating the Earth's climate. However, it's under threat. Illegal logging, mining, and widespread agriculture are leading to unprecedented
    # deforestation. During my journey, I encountered species that are on the brink of extinction and areas that were once lush with life now barren. I captured
    # these changes in my documentary to show the world what's at stake. I believe in a future where the Amazon is recognized globally for its ecological worth and
    # protected as such. After my treacherous travels, which included evading dangerous wildlife and navigating through nearly impassable terrain, I made it my
    # mission to bring this issue to the forefront of international environmental discussions. The journey was fraught with challenges; at one point, I was lost for
    # three days with no contact with my team, relying solely on natural navigation skills to find my way back. Yet, these experiences have only strengthened my
    # resolve. It's time the world acknowledges and acts to save the Amazon, our natural treasure.’""",
    #         "",
    #         8,
    #         READING,
    #         2021,
    #         1,
    #         "english",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "What is Maria Silva known for?",
    #         [
    #             "A. Being an expert navigator.",
    #             "B. Her documentary filmmaking.",
    #             "C. Her dedication to the Amazon rainforest.",
    #             "D. Her work in illegal mining.",
    #         ],
    #         "C",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "What primary issue does the Amazon face according to Maria?",
    #         [
    #             "A. Overpopulation.",
    #             "B. Deforestation.",
    #             "C. Water pollution.",
    #             "D. Industrialization.",
    #         ],
    #         "B",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "Why is the Amazon often called the planet's lungs?",
    #         [
    #             "A. It's the source of much of the world's oxygen.",
    #             "B. It has a vast number of animal species.",
    #             "C. It's the largest rainforest on Earth.",
    #             "D. It absorbs a significant amount of carbon dioxide.",
    #         ],
    #         "A",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "What challenge did Maria face during her journey?",
    #         [
    #             "A. She was injured by wildlife.",
    #             "B. She got lost for several days.",
    #             "C. She ran out of supplies.",
    #             "D. Her filming equipment was stolen.",
    #         ],
    #         "B",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "Maria’s ultimate goal is to",
    #         [
    #             "A. Become a renowned explorer.",
    #             "B. Turn the Amazon into a tourist destination.",
    #             "C. Have the Amazon recognized for its environmental importance.",
    #             "D. Publish a series of books on her adventures.",
    #         ],
    #         "C",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "Maria’s journey was mainly characterized by",
    #         [
    #             "A. Excitement and discovery.",
    #             "B. Constant fear and trepidation.",
    #             "C. Challenges and determination.",
    #             "D. Solitude and contemplation.",
    #         ],
    #         "C",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "How did Maria react to being lost?",
    #         [
    #             "A. She waited for rescue.",
    #             "B. She used her skills to navigate back.",
    #             "C. She built a signal fire.",
    #             "D. She contacted her team with a satellite phone.",
    #         ],
    #         "B",
    #     )
    #
    #     mcqDB.insert_multiple_choice_question(
    #         2,
    #         "What would be the most fitting title for the text?",
    #         [
    #             "A. The Dangers of the Amazon",
    #             "B. The Amazon’s Hidden Beauty",
    #             "C. A Journey to Save the Amazon",
    #             "D. Adventures of an Amazon Explorer",
    #         ],
    #         "C",
    #     )
    #
    #     taskDB.insert_task(
    #         3,
    #         "Read the text and complete the sentences with the correct form of the verbs in brackets. Use each verb only once. Two verbs are extra.",
    #         '''Switzerland is widely recognized for its impressive mountains, clock-making traditions, and mouth-watering chocolates. Nestled in the heart of Europe, this country …… (1) (maintain) its neutrality for centuries. Many international organizations …… (2) (find) their home in Geneva, including the United Nations and the Red Cross. The Swiss …… (3) (possess) a strong sense of national identity, despite having four official languages: German, French, Italian, and Romansh. Tourism …… (4) (flourish) year-round; in winter, the Alpine ski resorts …… (5) (attract) sports enthusiasts from all over the globe, while in summer, its pristine lakes …… (6) (offer) refreshing escapes. Remarkably, Switzerland …… (7) (be) home to some of the world’s most innovative companies, especially in the pharmaceutical and financial sectors. The country’s education system …… (8) (recognize) as one of the best, enabling Swiss students to …… (9) (excel) in various fields. Although Switzerland …… (10) (vote) regularly on issues through referendums, the Swiss often …… (11) (pride) themselves on their direct democracy system. Environmental protection …… (12) (remain) a priority for the Swiss, with numerous initiatives to conserve natural beauty and wildlife.''',
    #         "attract #be #excel #find #flourish #maintain #offer #possess #pride #recognize #remain #vote #restore #shape ",
    #         12,
    #         FILLING,
    #         2021,
    #         1,
    #         "english",
    #     )
    #
    #     fill_questionDB.insert_fill_text_question(3, 1, "F")
    #     fill_questionDB.insert_fill_text_question(3, 2, "D")
    #     fill_questionDB.insert_fill_text_question(3, 3, "H")
    #     fill_questionDB.insert_fill_text_question(3, 4, "E")
    #     fill_questionDB.insert_fill_text_question(3, 5, "A")
    #     fill_questionDB.insert_fill_text_question(3, 6, "G")
    #     fill_questionDB.insert_fill_text_question(3, 7, "B")
    #     fill_questionDB.insert_fill_text_question(3, 8, "J")
    #     fill_questionDB.insert_fill_text_question(3, 9, "C")
    #     fill_questionDB.insert_fill_text_question(3, 10, "L")
    #     fill_questionDB.insert_fill_text_question(3, 11, "I")
    #     fill_questionDB.insert_fill_text_question(3, 12, "K")
    #
    #     taskDB.insert_task(
    #         4,
    #         "Read the text and fill the gaps with one of the following: article, preposition, conjunction or relative pronoun. Insert only ONE word. Do not copy the extra words from the text on the answer sheet.",
    #         """An invention is the discovery or creation of a new material, a new process or a new use of existing material. Inventions
    #                                 almost always cause change. Sometimes great inventions are ideas that can change ….. (1) world. Many of the everyday
    #                                 products which we use today were invented years ago. While some inventions were discovered accidentally, most of them
    #                                 were the result ….. (2) hard work, continuous effort ….. (3) a great wish to try again. The invention of the radio has brought
    #                                 distant places closer together, and the invention of the car has made it possible to travel long distances. An invention might
    #                                 also be ….. (4) better way of doing something, ….. (5) example, a tool to make a job easier or some new farming method.
    #                                 When looking for the examples of inventions ….. (6) changed the world, we should consider not just the item, but also the
    #                                 progress it brought about. Many inventions, such as musical instruments ….. (7) sports equipment, have made our life more
    #                                 comfortable and enjoyable. Although there are a lot of inventions, not every good idea leads ….. (8) immediate success.
    #                                 The key to the success of the invention is to be in the right place ….. (9) the right time. It is believed that ….. (10) the 15th
    #                                 century an Italian painter, Leonardo da Vinci, wrote down his idea for big iron chains ….. (11) would drive machines, …..
    #                                 (12) unfortunately the technology to produce those chains didn’t exist then. This shows that even the greatest inventions
    #                                 may be useless if they are ahead of their time.""",
    #         "",
    #         12,
    #         ARTICLES,
    #         2021,
    #         1,
    #         "english",
    #     )
    #
    #     articlesDB.insert_fill_with_articles_question(4, ["the"])
    #     articlesDB.insert_fill_with_articles_question(4, ["of"])
    #     articlesDB.insert_fill_with_articles_question(4, ["and", "or"])
    #     articlesDB.insert_fill_with_articles_question(4, ["a"])
    #     articlesDB.insert_fill_with_articles_question(4, ["for"])
    #     articlesDB.insert_fill_with_articles_question(4, ["what", "which"])
    #     articlesDB.insert_fill_with_articles_question(4, ["and", "or"])
    #     articlesDB.insert_fill_with_articles_question(4, ["to"])
    #     articlesDB.insert_fill_with_articles_question(4, ["at"])
    #     articlesDB.insert_fill_with_articles_question(4, ["in"])
    #     articlesDB.insert_fill_with_articles_question(4, ["that", "which"])
    #     articlesDB.insert_fill_with_articles_question(4, ["but", "though"])
    #
    #     taskDB.insert_task(
    #         5,
    #         '''The advertisement given below is taken from an online newspaper. Read the advertisement and write an
    #                     email to the editor of the newspaper asking for more information about the details which are indicated. The
    #                     beginning is given on the answer sheet. Do not write your or anybody else’s name or surname in the letter.''',
    #         f'''Do you want to learn how to be confident and express yourself
    #                     clearly? Then read this advert carefully.
    #                     Arts Centre invites you to join ‘Professional development Workshop’.
    #                     The workshop will take place <b>in the centre of Rome¹</b>. Attendance is
    #                     free. <b>An American psychologist²</b> will conduct the workshop. It is held
    #                     on June 5. The workshop will start <b>in the afternoon³</b>. All the
    #                     participants will receive a Certificate of Attendance. For more
    #                     information, please contact us at: artscen@gmail.com
    #                     <br>1.Where exactly?
    #                     <br>2.Who?
    #                     <br>3.When exactly?''',
    #         "",
    #         6,
    #         EMAIL,
    #         2021,
    #         1,
    #         "english",
    #     )
    #
    #     taskDB.insert_task(6, "Read the essay task and write between 120-150 words.",
    #                        '''Some people think that it’s very hard to be a doctor nowadays. Do you agree or disagree with this opinion? State your opinion and support it with reasons and examples.''',
    #                        "", 16, ESSAY, 2021, 1, "english")
