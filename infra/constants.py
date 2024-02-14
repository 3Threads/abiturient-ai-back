DATABASE_NAME = "../infra/sqlite/main.db"
SQL_FILE = "../infra/sqlite/start_up.sql"
SQL_FILE_TEST = "../infra/sqlite/start_up.sql"

TOKEN_HEX_BYTES_NUM = 32

STARTING_BITCOIN_AMOUNT = 1
WALLETS_LIMIT = 3
MINIMUM_AMOUNT_OF_BITCOIN = 0.00000001

FAKE_RATE = 100.0

ADMIN_API_KEY = "b42b6a94c86a51f016e0ee11d140de6824b81d2cadcea443370d0c49ce251789"

READING = "reading"
TITLING = "titling"
FILLING = "filling"
ARTICLES = "articles"
EMAIL = "email"
ESSAY = "essay"


AI_OUTPUT_EXAMPLE = """Follow this example for the output:
{
  "my total point": int,
  "max total point": int,
  "my Fluency/Task fulfilment point": int,
  "max Fluency/Task fulfilment point": int,
  "my grammar point": int,
  "max grammar point": int,
  "suggestions": str
}
"""
EMAIL_EVALUATION_SCHEME = """Email Evaluation Scheme: 

Total Score: 8 points, Language Proficiency: B1

6 points: Excellent writing. Clear opinion, used various grammar structures, abundant vocabulary. 
there are no mistakes or minimal ones.
5 points: Good writing. Clear opinion, task addressed fully, minimal mistakes, but answered only on 2 questions.
4 points: Average writing. Opinion is understandable but lack of grammar structures, there are few mistakes which do not bother understanding main idea. There are only answered 2 questions or answered all of them but with lack of logic.
3 points: Low than average writing. Used basic grammar structures and there are vocabulary mistakes; Or writing is average level but answers only 2 questions out of 3.
2 points: Weak understanding of language. Vocabulary is simple. Answered only on 1 question or there are not more than 3 lines of writing. Idea of the text is not understandable.
1 points: Very weak understanding of language. Only written 1-2 short sentences or there are mistakes in every sentence. Idea of the text is not understandable.
0 points: Writing doesn't answer the exercise or writing was left empty."""

ESSAY_EVALUATION_SCHEME = """I'll be submitting essays to you and you'll be grading them. I'll tell you the grading system and what format you'll be doing it in.

Fluency/Task fulfilment Evaluation system:
8-7 points - the writing is very good. It is perfect
Responds to the task.
- The meaning is clear and understandable
conveyed. Supported by examples and
with personal opinions.
- Moving from one sentence to another
It is logical.
6-5 points - the writing is good, answers the task, however
in some cases redundant or, on the contrary,
Insufficient information is provided.
- The idea is mostly good
conveyed. It shows personal opinion and/or
An example is given.
- Moving from one sentence to another
It is mostly logical, although some
In case of straining the reader's attention
It suits.
4-3 points - the writing is of an average level. The idea is basically
It's understandable, but in some cases it makes sense
is in trouble The information is general, provisions
is repeated. Sentences to each other logically
poorly connected. Personal opinion
It is not clearly visible.
  Or: the writing is 61-109 words, respectively
The number of errors is less.
  Or: the text only partially answers
task.
2-1 points - the writing is (very) weak. information
It is general and scarce. Understanding the meaning, mostly
In this case, it is impossible.
Or: The writing is 60 words or less
A few suggestions.
Or: Provisions of a general kind which
Not related to a specific topic, often
is repeated.
0 points - the sheet is blank or written
Only one sentence or
The assignment instructions have been downloaded.
Or: the writing does not answer the task.

Evaluation of the grammar part:
8-7 points - the number of grammatical errors is 3
does not exceed It is difficult to use
Prepositions and constructions.
- - Vocabulary is rich.
- Accepted in spelling and punctuation
Errors are minor.
6-5 points - 4-7 grammatical errors are allowed,
Incorrect syntactic structures
Including, but it does not prevent
to understand the main idea.
  - Vocabulary of task and request
It is compatible.
  - in spelling and punctuation
The mistakes made are mainly by hand
does not prevent the understanding of the thought.

4-3 points - 8-11 grammatical errors are allowed.
Too simple and/or is used
Incorrect syntactic structures.
  - Vocabulary is quite simple and
is limited.
  - in spelling and punctuation
The errors made are of a systematic nature
has, which, in some cases, prevents
to understand the meaning.

2-1 points - more than 11 grammars are allowed
error. sentences structurally
is faulty.
- Vocabulary is very simple and irrelevant.
- Reveals spelling and punctuation
Poor knowledge of the rules.

0 points - several sentences are written,
from which it is impossible to draw an opinion.
An error is made in every sentence.

The entire essay is evaluated with 16 points, 8 points in thought and 8 points in grammar, according to the evaluation system that I have written for you, you will write a separate score for Fluency/Task fulfilment and a separate score for grammar.
"""
