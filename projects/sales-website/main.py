from flask import Flask, request, make_response, render_template, redirect
from db import get_db
from views.users import bp as users_bp
from views.products import bp as products_bp
from views.carts import bp as carts_bp


app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)
app.register_blueprint(carts_bp)


@app.route("/")
def main_page():
    if "username" in request.args:
        username = request.args["username"]
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", [username])
        user_id = cursor.fetchone()  # (7,)  # None
        if user_id is not None:  # if user_id:
            user_id = user_id[0]  # 7
            response = redirect("/products")
            response.set_cookie("user_id", str(user_id))
            return response
        else:
            return render_template("login.html", error_messages="Username does not exist")

    if "user_id" in request.cookies:
        return redirect("/products")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    response = redirect("/")
    response.delete_cookie("user_id")
    return response


app.run(debug=True)
