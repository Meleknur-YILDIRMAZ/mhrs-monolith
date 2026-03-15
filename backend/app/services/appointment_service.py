from bson import ObjectId
from app.extensions import get_db
from app.models.appointment_model import create_appointment_document
from app.mq.producer import publish_appointment_event


def create_appointment(data, user_id):
    db = get_db()

    if db is None:
        return False, "Veritabanı bağlantısı kurulamadı"

    required_fields = [
        "city", "hospital", "department", "doctor",
        "appointment_date", "appointment_time"
    ]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return False, f"{field} alanı zorunludur"

    existing = db.appointments.find_one({
        "doctor": data["doctor"],
        "appointment_date": data["appointment_date"],
        "appointment_time": data["appointment_time"],
        "status": "active"
    })

    if existing:
        return False, "Bu doktor için bu saat dolu"

    doc = create_appointment_document(data, user_id)
    result = db.appointments.insert_one(doc)

    try:
        publish_appointment_event({
            "event": "appointment_created",
            "appointment_id": str(result.inserted_id),
            "user_id": user_id,
            "doctor": data["doctor"],
            "date": data["appointment_date"],
            "time": data["appointment_time"]
        })
    except Exception:
        pass

    return True, str(result.inserted_id)


def list_user_appointments(user_id):
    db = get_db()

    if db is None:
        return []

    appointments = list(db.appointments.find({"user_id": user_id, "status": "active"}))
    for item in appointments:
        item["_id"] = str(item["_id"])
    return appointments


def cancel_appointment(appointment_id, user_id):
    db = get_db()

    if db is None:
        return False

    result = db.appointments.update_one(
        {"_id": ObjectId(appointment_id), "user_id": user_id},
        {"$set": {"status": "cancelled"}}
    )
    return result.modified_count > 0