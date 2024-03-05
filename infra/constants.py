DATABASE_NAME = "../infra/sqlite/main.db"
SQL_FILE = "../infra/sqlite/start_up.sql"
SQL_FILE_TEST = "../infra/sqlite/start_up.sql"

TOKEN_HEX_BYTES_NUM = 32

STARTING_BITCOIN_AMOUNT = 1
WALLETS_LIMIT = 3
MINIMUM_AMOUNT_OF_BITCOIN = 0.00000001

FAKE_RATE = 100.0

ADMIN_API_KEY = "b42b6a94c86a51f016e0ee11d140de6824b81d2cadcea443370d0c49ce251789"

LISTENING = "listening"
MATCHING = "matching"
READING = "reading"
TITLING = "titling"
FILLING = "filling"
ARTICLES = "articles"
EMAIL = "email"
ESSAY = "essay"

DELIMITER = "#"

AI_OUTPUT_EXAMPLE_ESSAY = """Follow this example for the output:
{
  "my_total_point": int,
  "max_total_point": int,
  "my_Fluency/Task_fulfilment_point": int,
  "max_Fluency/Task_fulfilment_point": int,
  "my_grammar_point": int,
  "max_grammar_point": int,
  "grammar_mistakes": list[str],
  "corrected_version_of_grammar_mistakes": list[str],
  "possible_arguments": list[str],
}
"""

AI_OUTPUT_EXAMPLE_EMAIL = """Follow this example for the output:
{
  "my_total_point": int,
  "max_total_point": int,
  "grammar_mistakes": list[str],
  "corrected_version_of_grammar_mistakes": list[str],
}
"""
EMAIL_EVALUATION_SCHEME = """I'll be submitting emails to you and you'll be grading them. I'll tell you the grading system and what format you'll be doing it in. Email should be write about advertisement.

Total Score: 6 points, Language Proficiency: B1
6 points: Excellent writing. Clear opinion, used various grammar structures, abundant vocabulary. 
there are no mistakes or minimal ones.
5 points: Good writing. Clear opinion, task addressed fully, minimal mistakes, but answered only on 2 questions.
4 points: Average writing. Opinion is understandable but lack of grammar structures, there are few mistakes which do not bother understanding main idea. There are only answered 2 questions or answered all of them but with lack of logic.
3 points: Low than average writing. Used basic grammar structures and there are vocabulary mistakes; Or writing is average level but answers only 2 questions out of 3.
2 points: Weak understanding of language. Vocabulary is simple. Answered only on 1 question or there are not more than 3 lines of writing. Idea of the text is not understandable.
1 points: Very weak understanding of language. Only written 1-2 short sentences or there are mistakes in every sentence. Idea of the text is not understandable.
0 points: Writing doesn't answer the exercise or writing was left empty.

The entire email is evaluated with 6 points. The advertisement given below is taken from an online newspaper. Read the advertisement and write an
email to the editor of the newspaper asking for more information about the details which are indicated. The
beginning is given on the answer sheet.
"""

ESSAY_EVALUATION_SCHEME = """I'll be submitting essays to you and you'll be grading them. I'll tell you the grading system and what format you'll be doing it in.

Fluency/Task fulfilment Evaluation system:
8-7 points:
- the writing is very good. It is perfect Responds to the task.
- The meaning is clear and understandable conveyed. Supported by examples and with personal opinions.
- Moving from one sentence to another is logical.
6-5 points:
- the writing is good, answers the task, however in some cases redundant or, on the contrary, insufficient information is provided.
- The idea is mostly good conveyed. It shows personal opinion and/or An example is given.
- Moving from one sentence to another is mostly logical, but in some instances, the reader may lose focus
4-3 points: 
- The writing is of average quality. The opinion is generally understandable, but in some cases, it lacks depth. 
- Information is generally provided, but explanations are lacking. 
- Transitions between paragraphs are not well-connected logically. 
- Personal opinion is not clear, Or: The writing consists of 61-109 words, or: The writing only partially addresses the task. 
2-1 points:
- The writing is (very) concise. Information is generally relevant and to the point. 
- Understanding the opinion, in most cases, is difficult, Or: The writing is 60 words or fewer /written with few transitions, Or: Some general ideas, which are not directly related to a specific theme, are often repeated.
0 points:
- The paragraph is either empty or contains only one sentence or is solely a repetition of the assignment instructions, Or: The writing does not address the task.

Evaluation of the grammar part:
8-7 points:
- The number of grammatical errors is limited to 2. 
- Difficult expressions and constructions are used. 
- The vocabulary is rich. Errors in spelling and punctuation are negligible.
6-5 points:
- There may be 3-6 grammatical errors, not counting incorrect syntactic structures, but these do not hinder the understanding of the main idea. 
- The vocabulary is appropriate. 
- Errors in spelling and punctuation do not significantly impede understanding.
4-3 points:
- There may be 7-11 grammatical errors, with predominantly simple or incorrect syntactic structures. 
- The vocabulary is fairly basic and limited. 
- Errors in spelling and punctuation have a systematic pattern that sometimes hinders understanding.
2-1 points:
- There are more than 11 grammatical errors. 
- The sentences are structurally incorrect. 
- The vocabulary is very simple and inappropriate. 
- A good understanding of spelling and punctuation rules is lacking.
0 points:
- Several sentences are constructed in a way that makes it difficult to extract the main idea. 
- Errors are present in every sentence.

The entire essay is evaluated with 16 points, 8 points in Fluency/Task fulfilment and 8 points in grammar, according to the evaluation system that I have written for you, you will write a separate score for Fluency/Task fulfilment and a separate score for grammar.
"""
