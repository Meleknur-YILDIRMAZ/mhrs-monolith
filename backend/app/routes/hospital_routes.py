from flask import Blueprint
from app.extensions import db
from app.utils.response import success_response

hospital_bp = Blueprint("hospital", __name__)


@hospital_bp.route("", methods=["GET"])
def get_hospitals():
    hospitals = list(db.hospitals.find({}, {"_id": 0}))
    return success_response("Hastaneler listelendi", hospitals)