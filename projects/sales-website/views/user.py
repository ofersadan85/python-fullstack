from flask import request, Blueprint

bp = Blueprint("user", __name__)


@bp.route("/user")
def user_list():
    return "List of all users"


@bp.route("/user/<user_id>")  # methods=["GET"]  # https://mystore.com/user/3
def user_page(user_id):
    return f"Page for user {user_id}"


@bp.route("/user/create", methods=["GET", "POST"])
def user_create():
    if request.method == "GET":
        return "User create form"
    elif request.method == "POST":
        return "Created user successfully"


@bp.route("/user/<int:user_id>", methods=["DELETE"])
def user_delete(user_id):
    return f"Deleted user successfully {user_id}"


@bp.route("/user/<int:user_id>", methods=["PATCH"])
def user_update(user_id):
    updated_user = request.json()
    return f"Updated user {user_id} with data {updated_user}"
