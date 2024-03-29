from dataclasses import asdict

from db import close_db, get_db, init_db
from flask import Flask, request, session
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, jwt_required

app = Flask(__name__)
app.config.from_prefixed_env()
FRONTEND_URL = app.config.get("FRONTEND_URL")
cors = CORS(app, origins=FRONTEND_URL, methods=["GET", "POST", "DELETE"])
print(FRONTEND_URL)
jwt = JWTManager(app)
app.teardown_appcontext(close_db)  # Close the database connection after each request


@app.route("/login", methods=["POST"])
def login() -> dict:
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (data["username"], data["password"]),
    )
    user = cursor.fetchone()
    if user is None:
        return {"error": "Invalid username or password"}
    else:
        access_token = create_access_token(identity=user["id"])
        return {"access_token": access_token}


@app.route("/logout", methods=["POST"])
def logout() -> dict:
    # This does absolutely nothing, it's just here to show that you don't really need to do anything special to "log out"
    # What you will need to do is to delete the access token from the client side, which will effectively log the user out
    # Alternatively, you can blacklist the token, but that's a more advanced topic
    return {"message": "Successfully logged out"}


@app.route("/users/me")
@jwt_required()
def get_me() -> dict:
    token_data = get_jwt()
    user_id = token_data["sub"]
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, username, role, email, age FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user is None:
        return {"error": "User not found"}
    else:
        return {
            "id": user["id"],
            "username": user["username"],
            "role": user["role"],
            "email": user["email"],
            "age": user["age"],
        }
