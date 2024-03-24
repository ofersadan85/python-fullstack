from pathlib import Path
from flask import g
import sqlite3

CURRENT_DIR = Path(__file__).parent
DB_PATH = CURRENT_DIR / "data.db"


def get_db() -> sqlite3.Connection:
    """Connect to the SQLite database, and return the connection object"""
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(_e=None) -> None:
    """Close the connection to the SQLite database"""
    db = g.pop("db", None)
    if db is not None:
        db.close()
