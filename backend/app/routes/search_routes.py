from flask import Blueprint, request
from app.services.search_service import search_hospitals
from app.utils.response import success_response

search_bp = Blueprint("search", __name__)


@search_bp.route("", methods=["GET"])
def search():
    keyword = request.args.get("q", "")
    results = search_hospitals(keyword)
    return success_response("Arama tamamlandı", results)