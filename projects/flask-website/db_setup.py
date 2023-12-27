import sqlite3
from pathlib import Path

sql_folder = Path(__file__).parent / "sql"
db_file_path = Path(__file__).with_name("data.db")
sql_setup = (sql_folder / "setup_db.sql").read_text()

db = sqlite3.connect(db_file_path)
cursor = db.cursor()
cursor.executescript(sql_setup)
db.commit()
