from pathlib import Path
import sqlite3
from flask import g


CURRENT_FILE = Path(__file__)
DB_PATH = CURRENT_FILE.parent / "data.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
