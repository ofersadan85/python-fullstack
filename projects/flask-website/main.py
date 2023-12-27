from flask import Flask, render_template, request, redirect, session
from views import auth
from db import close_db

app = Flask(__name__)
app.register_blueprint(auth.bp)
app.secret_key = "super duper top secret key"
app.teardown_appcontext(close_db)

@app.route("/")
@app.route("/home")
def index():
    if request.path == "/home":
        return redirect("/")
    return render_template("index.html", session=session)


@app.route("/about")
def about():
    return render_template("about.html", session=session)

app.run(debug=True)
