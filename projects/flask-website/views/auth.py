import json
from pathlib import Path

from flask import Blueprint, flash, redirect, render_template, request, session

bp = Blueprint("auth", __name__, url_prefix="/auth")
users_file = Path(__file__).parent.with_name("users.json")

@bp.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        with open(users_file, "r") as f:
            users = json.load(f)
        form_username = request.form["username"]
        form_password = request.form["password"]
        if form_username in users and form_password == users[form_username]["password"]:
            session["username"] = form_username
            return redirect("/")
        else:
            flash("Invalid username or password", "error")
    return render_template("login.html", session=session)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
