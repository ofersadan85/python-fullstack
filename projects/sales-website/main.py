from flask import Flask, redirect, url_for

from views.user import bp as user_blueprint
from views.product import bp as product_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(product_blueprint, url_prefix="/products", name="products")

# @app.route("/")
# def main_page():
#     return product_list()

# app.route("/")(product_list)

@app.route("/")
def main_page():
    return redirect(url_for("products.product_list"))


app.run(debug=True)
