import sqlite3
from flask import redirect, request, Blueprint, url_for, render_template

from models.product import Product, ProductCreate

bp = Blueprint("product", __name__, url_prefix="/product")


@bp.route("")
def product_list():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT id, title, description, price, image FROM products")
    data = cursor.fetchall()
    product_list = []
    for item in data:
        product = Product(
            id=item[0],
            title=item[1],
            description=item[2],
            price=item[3],
            image=item[4],
        )
        product_list.append(product)
    return render_template("product-list.html", products=product_list)


@bp.route("/<product_id>")
def product_page(product_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, title, description, price, image FROM products WHERE id = ?",
        [product_id],
    )
    data = cursor.fetchone()
    if data:
        product = Product(
            id=data[0],
            title=data[1],
            description=data[2],
            price=data[3],
            image=data[4],
        )
        return render_template("product.html", product=product)
    else:
        return "PRODUCT NOT FOUND"

@bp.route("/create", methods=["GET", "POST"])
def product_create():
    if request.method == "GET":
        return "Product create form"
    elif request.method == "POST":
        new_product = ProductCreate("new product name", 1.0, 1, "nothing")
        print(f"Creating product: {new_product}")
        return "Created product successfully"


@bp.route("/<int:product_id>", methods=["DELETE"])
def product_delete(product_id):
    return f"Deleted product successfully {product_id}"


@bp.route("/<int:product_id>", methods=["PATCH"])
def product_update(product_id):
    updated_product = request.json()
    print(f"Updated product {product_id} with data {updated_product}")
    product_page_url = url_for("product.product_page", product_id=product_id)
    return redirect(product_page_url)
