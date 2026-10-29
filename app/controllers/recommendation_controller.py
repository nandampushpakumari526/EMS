
from flask import Blueprint, jsonify

from app.services.recommendation_service import recommend_courses

from app.services.learning_path_service import generate_learning_path


bp = Blueprint(
    "recommendations",
    __name__,
    url_prefix="/recommendations"
)


@bp.route("/<int:employee_id>", methods=["GET"])
def get_recommendations(employee_id):

    recommendations = recommend_courses(employee_id)

    if recommendations is None:

        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify(recommendations)


@bp.route("/learning-path/<int:employee_id>", methods=["GET"])
def get_learning_path(employee_id):

    learning_path = generate_learning_path(employee_id)

    if learning_path is None:

        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify(learning_path)
