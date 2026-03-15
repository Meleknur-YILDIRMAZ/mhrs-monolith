from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from app.services.auth_service import register_user, login_user
from app.utils.response import success_response, error_response

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    ok, result = register_user(data)

    if not ok:
        return error_response(result, 400)

    return success_response("Kullanıcı başarıyla oluşturuldu", {"user_id": result}, 201)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    ok, result = login_user(email, password)
    if not ok:
        return error_response(result, 401)

    user = result
    token = create_access_token(identity=str(user["_id"]))

    return success_response("Giriş başarılı", {
        "token": token,
        "user": {
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "email": user["email"],
            "tc_no": user["tc_no"]
        }
    })