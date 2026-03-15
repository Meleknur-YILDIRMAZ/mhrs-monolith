from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.appointment_service import create_appointment, list_user_appointments, cancel_appointment
from app.utils.response import success_response, error_response

appointment_bp = Blueprint("appointments", __name__)


@appointment_bp.route("", methods=["POST"])
@jwt_required()
def create_new_appointment():
    data = request.get_json()
    user_id = get_jwt_identity()

    ok, result = create_appointment(data, user_id)
    if not ok:
        return error_response(result, 400)

    return success_response("Randevu başarıyla oluşturuldu", {"appointment_id": result}, 201)


@appointment_bp.route("", methods=["GET"])
@jwt_required()
def get_my_appointments():
    user_id = get_jwt_identity()
    appointments = list_user_appointments(user_id)
    return success_response("Randevular listelendi", appointments)


@appointment_bp.route("/<appointment_id>", methods=["DELETE"])
@jwt_required()
def delete_appointment(appointment_id):
    user_id = get_jwt_identity()
    ok = cancel_appointment(appointment_id, user_id)

    if not ok:
        return error_response("Randevu iptal edilemedi", 400)

    return success_response("Randevu iptal edildi")