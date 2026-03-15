from datetime import datetime


def create_appointment_document(data, user_id):
    return {
        "user_id": user_id,
        "city": data["city"],
        "hospital": data["hospital"],
        "department": data["department"],
        "doctor": data["doctor"],
        "appointment_date": data["appointment_date"],
        "appointment_time": data["appointment_time"],
        "status": "active",
        "created_at": datetime.utcnow()
    }