
from flask import Blueprint, render_template

from app.repositories import (
    employee_repository,
    course_repository,
    enrollment_repository
)


bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports"
)


# --------------------------------
# Reports Dashboard
# --------------------------------

@bp.route("/")
def dashboard():

    employees = employee_repository.get_all_employees()

    courses = course_repository.get_all_courses()

    enrollments = (
        enrollment_repository.get_all_enrollments()
    )

    budgets = enrollment_repository.get_all_budgets()

    return render_template(
        "reports/dashboard.html",
        employees=employees,
        courses=courses,
        enrollments=enrollments,
        budgets=budgets
    )
