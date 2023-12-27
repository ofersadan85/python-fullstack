import sqlite3
from flask import Blueprint, flash, redirect, render_template, request, session, current_app
from db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()
        form_username = request.form["username"]
        form_password = request.form["password"]
        try:
            with current_app.open_resource("sql/users_insert.sql", "r") as f:
                sql = f.read()
            cursor.execute(sql, [form_username, form_password])
        except sqlite3.IntegrityError:
            flash("The username you selected already exists", "error")
            return render_template("register.html")
        else:
            db.commit()
            return redirect("/")
    return render_template("register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()
        form_username = request.form["username"]
        form_password = request.form["password"]
        with current_app.open_resource("sql/users_select_username.sql", "r") as f:
            sql = f.read()
        cursor.execute(sql, [form_username])
        db_user = cursor.fetchone()  # (username, password)
        if db_user[0] == form_username and db_user[1] == form_password:
            session["username"] = form_username
            return redirect("/")
        else:
            flash("Invalid username or password", "error")
    return render_template("login.html", session=session)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
