
from flask import Blueprint, render_template

from app.repositories import employee_repository

from app.services.recommendation_service import (
    recommend_courses
)


bp = Blueprint(
    "recommendations",
    __name__,
    url_prefix="/recommendations"
)


# --------------------------------
# Employee Recommendations
# --------------------------------

@bp.route("/<int:employee_id>")
def get_recommendations(employee_id):

    employee = employee_repository.get_employee_by_id(
        employee_id
    )

    if employee is None:
        return "Employee not found", 404

    recommendations = recommend_courses(
        employee_id
    )

    if recommendations is None:
        recommendations = []

    return render_template(
        "recommendations/recommendation_list.html",
        employee=employee,
        recommendations=recommendations
    )
