from flask import render_template, Blueprint
from db import get_db
from models.products import Product

bp = Blueprint("products", __name__)


@bp.route("/products/create")
def product_create_form():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT category FROM products")
    data = cursor.fetchall()
    # categories = [row[0] for row in data]
    return render_template("product-create.html", categories=data)


@bp.route("/products")
def product_list():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, title, description, price, image FROM products")
    data = cursor.fetchall()  # List of tuples - tuple = row in table
    product_list = [Product(*item) for item in data]
    return render_template("product-list.html", products=product_list)


@bp.route("/products/delete/<product_id>")
def delete_product(product_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", [product_id])
    if cursor.rowcount == 1:
        db.commit()
        return ("", 200)
    if cursor.rowcount == 0:
        return ("", 404)


@bp.route("/products/<product_id>")
def product_page(product_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, title, description, price, image FROM products WHERE id = ?",
        [product_id],
    )
    data = cursor.fetchone()
    if data:
        return render_template("product.html", product=Product(*data))
    else:
        return "PRODUCT NOT FOUND"
