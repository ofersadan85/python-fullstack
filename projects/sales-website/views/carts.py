from flask import Blueprint
from db import get_db
import json

bp = Blueprint("carts", __name__)

@bp.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    cart_id = 6
    user_id = 5
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT products FROM carts WHERE id = ? AND user_id = ?", [cart_id, user_id])
    old_value = cursor.fetchone()  # ('5',)
    old_value_dict = json.loads(old_value[0])  # 5

    if product_id in old_value_dict:
        old_value_dict[product_id] = old_value_dict[product_id] + 1
    else:
        old_value_dict[product_id] = 1
    new_value = json.dumps(old_value_dict)
    params = [new_value, cart_id, user_id]

    query = """
UPDATE carts set products = ?
WHERE id = ?
AND user_id = ?
"""
    cursor.execute(query, params)
    db.commit()
    return ""
