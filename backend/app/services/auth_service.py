from app.extensions import get_db
from app.models.user_model import create_user_document, verify_password
from app.utils.validators import is_valid_email, is_valid_password, is_valid_tc


def register_user(data):
    db = get_db()

    if db is None:
        return False, "Veritabanı bağlantısı kurulamadı"

    required_fields = ["first_name", "last_name", "tc_no", "phone", "email", "password"]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return False, f"{field} alanı zorunludur"

    if not is_valid_tc(data["tc_no"]):
        return False, "Geçerli bir TC kimlik numarası giriniz"

    if not is_valid_email(data["email"]):
        return False, "Geçerli bir e-posta giriniz"

    if not is_valid_password(data["password"]):
        return False, "Şifre en az 6 karakter olmalıdır"

    existing_user = db.users.find_one({
        "$or": [
            {"email": data["email"]},
            {"tc_no": data["tc_no"]}
        ]
    })

    if existing_user:
        return False, "Bu e-posta veya TC ile kayıtlı kullanıcı zaten var"

    user_doc = create_user_document(data)
    result = db.users.insert_one(user_doc)
    return True, str(result.inserted_id)


def login_user(email, password):
    db = get_db()

    if db is None:
        return False, "Veritabanı bağlantısı kurulamadı"

    user = db.users.find_one({"email": email})
    if not user:
        return False, "Kullanıcı bulunamadı"

    if not verify_password(user["password"], password):
        return False, "Şifre hatalı"

    return True, user