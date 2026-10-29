
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from app.repositories import enrollment_repository

from app.services.enrollment_service import enroll_employee


bp = Blueprint(
    "enrollments",
    __name__,
    url_prefix="/enrollments"
)


# --------------------------------
# Enrollment List
# --------------------------------

@bp.route("/")
def get_enrollments():

    enrollments = (
        enrollment_repository.get_all_enrollments()
    )

    return render_template(
        "enrollments/enrollment_list.html",
        enrollments=enrollments
    )


# --------------------------------
# Enroll Employee
# --------------------------------

@bp.route(
    "/enroll/<int:employee_id>/<int:course_id>",
    methods=["POST"]
)
def enroll(employee_id, course_id):

    result = enroll_employee(
        employee_id,
        course_id
    )

    if result["success"]:

        flash(
            result["message"],
            "success"
        )

    else:

        flash(
            result["message"],
            "danger"
        )

    return redirect(
        url_for(
            "recommendations.get_recommendations",
            employee_id=employee_id
        )
    )
