from dataclasses import asdict

from dotenv import load_dotenv
from flask import Flask, Response, request
from models import NewUser, PublicUser, User
from db import get_db, close_db


def add_cors_headers(response: Response) -> Response:
    """Add CORS headers to the response"""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


load_dotenv()  # Load environment variables from a .env file
app = Flask(__name__)
app.after_request(add_cors_headers)  # Add CORS headers to all responses
app.teardown_appcontext(close_db)  # Close the database connection after each request


@app.route("/users")
def get_users() -> list[PublicUser]:
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, username, email, age FROM users")
    users = [PublicUser(*row) for row in cursor.fetchall()]
    return users


@app.route("/users", methods=["POST"])
def create_user() -> dict:
    # TODO: Add validation, error handling (what if the user already exists? what if the request is missing fields? etc.)
    new_user = NewUser(**request.get_json())
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (username, password, email, age) VALUES (?, ?, ?, ?)",
        (new_user.username, new_user.password, new_user.email, new_user.age),
    )
    db.commit()
    cursor.execute("SELECT id FROM users WHERE username = ?", (new_user.username,))
    # TODO: This is a bad way to return the new user's data, it will be better not to query the database again.
    data = cursor.fetchone()
    user_id = data["id"]
    public_user = PublicUser(user_id, new_user.username, new_user.email, new_user.age)
    return asdict(public_user)


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int) -> str:
    # TODO: Add error handling (what if the user doesn't exist? etc.)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    return ""


app.run()
