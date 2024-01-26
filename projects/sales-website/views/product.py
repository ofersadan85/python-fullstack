from flask import redirect, request, Blueprint, url_for

from models.product import Product, ProductCreate

bp = Blueprint("product", __name__, url_prefix="/product")


@bp.route("")
def product_list():
    # list_of_products = get_list_of_products()
    return f"List of all products"


@bp.route("/<product_id>")
def product_page(product_id):
    return f"Page for product {Product.get_product_by_id(product_id)}"


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
