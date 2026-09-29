import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="SQLite Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


DB_NAME = "tasks.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.on_event("startup")
def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
            """
        )
        conn.commit()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


@app.get("/tasks")
def get_tasks():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM tasks").fetchall()
    return [dict(row) for row in rows]


# TODO: Add POST, GET by id, PUT/PATCH, and DELETE endpoints here
