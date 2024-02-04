from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/users/create", methods=["GET", "POST"])
def user_create_form():
    if request.method == "POST":
        print("Creating new user in DB")
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        new_user = [
            request.form["username"],
            request.form["password"],
            request.form["email"]
        ]
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", new_user)
        db.commit()
        return "USER CREATED"
    return render_template("user-create.html")


@app.route("/products/create")
def product_create_form():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT category FROM products")
    data = cursor.fetchall()
    # categories = [row[0] for row in data]
    return render_template("product-create.html", categories=data)


@app.route("/products")
def product_list():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT id, title, description, price, image FROM products")
    data = cursor.fetchall()  # List of tuples - tuple = row in table
    product_list = []
    for item in data:
        product = {
            "id": item[0],
            "title": item[1],
            "description": item[2],
            "price": item[3],
            "image": item[4],
        }
        product_list.append(product)
    return render_template("product-list.html", products=product_list)


@app.route("/products/delete/<product_id>")
def delete_product(product_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", [product_id])
    if cursor.rowcount == 1:
        db.commit()
        return ("", 200)
    if cursor.rowcount == 0:
        return ("", 404)


@app.route("/products/<product_id>")
def product_page(product_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, title, description, price, image FROM products WHERE id = ?",
        [product_id],
    )
    data = cursor.fetchone()
    if data:
        product = {
            "id": data[0],
            "title": data[1],
            "description": data[2],
            "price": data[3],
            "image": data[4],
        }
        return render_template("product.html", product=product)
    else:
        return "PRODUCT NOT FOUND"


@app.route("/users/<user_id>")
def user_page(user_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT username, email FROM users WHERE id = ?",
        [user_id],
    )
    data = cursor.fetchone()
    if data:
        user = {
            "username": data[0],
            "email": data[1],
        }
        return render_template("user-page.html", user=user)
    else:
        return "USER NOT FOUND"


@app.route("/users")
def user_list():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT id, username, email FROM users")
    data = cursor.fetchall()  # List of tuples - tuple = row in table
    users_list = []
    for item in data:
        user = {
            "id": item[0],
            "username": item[1],
            "email": item[2],
        }
        users_list.append(user)
    return render_template("user-list.html", users=users_list)


@app.route("/")
def main_page():
    return "HOME PAGE"


app.run(debug=True)
