from flask import Flask
from views.users import bp as users_bp
from views.products import bp as products_bp


app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)


@app.route("/")
def main_page():
    return "HOME PAGE"


app.run(debug=True)
