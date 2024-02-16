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

    if os.getenv("WALLET_REPOSITORY_KIND", "memory") == "sqlite":
        db = Database(DATABASE_NAME, os.path.abspath(SQL_FILE))
        db.initial()    # Uncomment this if you want to create initial db
        app.state.tasks = TasksDatabase(db.con, db.cur)
        app.state.subscribes = SubscribesDataBase(db.con, db.cur)
        app.state.users = UsersDatabase(db.con, db.cur, app.state.subscribes)

    else:
        app.state.tasks = TasksInMemory()
        app.state.users = UsersInMemory()

    return app
