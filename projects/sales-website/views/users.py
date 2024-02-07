from flask import request, render_template, Blueprint
from db import get_db
from models.users import User, UserCreate
bp = Blueprint("users", __name__)


@bp.route("/users/create", methods=["GET", "POST"])
def user_create_form():
    if request.method == "POST":
        print("Creating new user in DB")
        db = get_db()
        cursor = db.cursor()
        # new_user = UserCreate(
        #     request.form["username"],
        #     request.form["password"],
        #     request.form["email"],
        # )
        UserCreate(**request.form).create(cursor)
        db.commit()
        return "USER CREATED"
    return render_template("user-create.html")


@bp.route("/users/<user_id>")
def user_page(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, username, email FROM users WHERE id = ?",
        [user_id],
    )
    data = cursor.fetchone()
    if data:
        # user = User(*data)
        # user = User(data[0], data[1], data[2])
        return render_template("user-page.html", user=User(*data))
    else:
        return "USER NOT FOUND"


@bp.route("/users")
def user_list():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, username, email FROM users")
    data = cursor.fetchall()  # List of tuples - tuple = row in table
    # users_list = []
    # for item in data:
    #     user = User(*item)
    #     # user = User(item[0], item[1], item[2])
    #     users_list.append(user)
    users_list = [User(*item) for item in data]
    return render_template("user-list.html", users=users_list)
