import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DB_PATH = CURRENT_DIR / "data.db"
SCHEMA_PATH = CURRENT_DIR / "schema.sql"
db = sqlite3.connect(DB_PATH)
cursor = db.cursor()
db_schema = SCHEMA_PATH.read_text()
cursor.execute(db_schema)
db.commit()
db.close()
