
from datetime import datetime

from app import db

from app.models import (
    Employee,
    Course,
    Enrollment,
    Budget
)

from app.services.prerequisite_service import check_prerequisites


def enroll_employee(employee_id, course_id, fiscal_year=2026):

    employee = Employee.query.get(employee_id)

    course = Course.query.get(course_id)

    if employee is None:
        return {
            "success": False,
            "message": "Employee not found"
        }

    if course is None:
        return {
            "success": False,
            "message": "Course not found"
        }

    if course.status != "active":
        return {
            "success": False,
            "message": "Course is inactive"
        }

    existing = Enrollment.query.filter_by(
        employee_id=employee_id,
        course_id=course_id
    ).first()

    if existing:

        return {
            "success": False,
            "message": "Employee already enrolled"
        }

    prerequisite_result = check_prerequisites(
        employee_id,
        course_id
    )

    if not prerequisite_result["eligible"]:

        return {
            "success": False,
            "message": "Prerequisites not completed",
            "missing_prerequisites":
                prerequisite_result["missing_prerequisites"]
        }

    budget = Budget.query.filter_by(
        department=employee.department,
        fiscal_year=fiscal_year
    ).first()

    if budget is None:

        return {
            "success": False,
            "message": "Budget not found"
        }

    remaining = budget.total_amount - budget.spent_amount

    if course.cost > remaining:

        return {
            "success": False,
            "message": "Insufficient budget"
        }

    try:

        enrollment = Enrollment(

            employee_id=employee_id,

            course_id=course_id,

            budget_id=budget.id,

            enrollment_date=datetime.utcnow(),

            status="enrolled"

        )

        db.session.add(enrollment)

        budget.spent_amount += course.cost

        db.session.commit()

        return {

            "success": True,

            "message": "Enrollment successful",

            "enrollment_id": enrollment.id

        }

    except Exception as error:

        db.session.rollback()

        return {
            "success": False,
            "message": str(error)
        }
