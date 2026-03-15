from werkzeug.security import generate_password_hash, check_password_hash


def create_user_document(data):
    return {
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "tc_no": data["tc_no"],
        "phone": data["phone"],
        "email": data["email"],
        "password": generate_password_hash(data["password"]),
        "role": "patient"
    }


def verify_password(hashed_password, raw_password):
    return check_password_hash(hashed_password, raw_password)