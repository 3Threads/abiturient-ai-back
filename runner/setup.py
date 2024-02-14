import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

from infra.constants import DATABASE_NAME, SQL_FILE
from infra.fastapi.login import sign_api
from infra.fastapi.subsribes import subscribe_api
from infra.fastapi.tasks import tasks_api
from infra.in_memory.tasks import TasksInMemory
from infra.in_memory.users import UsersInMemory
from infra.openAI.checker_ai import CheckerAI
from infra.sqlite.database_connect import Database
from infra.sqlite.subscribes import SubscribesDataBase
from infra.sqlite.tasks import TasksDatabase
from infra.sqlite.users import UsersDatabase


def init_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace "*" with your frontend domain(s)
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
    app.include_router(tasks_api)
    app.include_router(sign_api)
    app.include_router(subscribe_api)

    print(
        CheckerAI().check_essay(
            """Nowadays most 17-18 years old children have to choose what to study at the university. While thinking of a future profession the tend to decline an opportunity of becoming a doctor after realizing how hard the studying will be. So, I completely agree with this issue and I will strengthen my opinion with appropriate arguments. 
First of all, I want to emphasize that the length of studying course at a medical university is much longer than at others. In Georgia the difference is approximately 2 years. Secondly, for me it is almost impossible to imagine the difficulty of studying anatomy because it is certain how complicated a human's body is.
However, some people may think that after becoming a doctor exhausting days spent on studying turn into pleasurable life, but although doctors have high-paid jobs, it is still difficult to face to the responsibility of patients' lives.
To conclude, it seems obvious to me that becoming a doctor hives one responsibility which only few can have. It makes a doctor's life difficult.""",
            """Some people think that it’s very hard to be a doctor nowadays. Do you agree or disagree with this opinion? State your opinion and support it with reasons and examples""",
        )
    )

    if os.getenv("WALLET_REPOSITORY_KIND", "memory") == "sqlite":
        db = Database(DATABASE_NAME, os.path.abspath(SQL_FILE))
        # db.initial()    # Uncomment this if you want to create initial db
        app.state.tasks = TasksDatabase(db.con, db.cur)
        app.state.subscribes = SubscribesDataBase(db.con, db.cur)
        app.state.users = UsersDatabase(db.con, db.cur, app.state.subscribes)

    else:
        app.state.tasks = TasksInMemory()
        app.state.users = UsersInMemory()

    return app
