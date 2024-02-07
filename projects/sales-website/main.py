from flask import Flask, request, make_response
from views.users import bp as users_bp
from views.products import bp as products_bp
from views.carts import bp as carts_bp


app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)
app.register_blueprint(carts_bp)


@app.route("/")
def main_page():
    print(request.cookies)
    response = make_response("HOME PAGE")
    response.set_cookie("user_id", "7")
    return response


@app.route("/logout")
def logout():
    response = make_response("YOU LOGGED OUT")
    response.delete_cookie("user_id")
    return response


app.run(debug=True)
