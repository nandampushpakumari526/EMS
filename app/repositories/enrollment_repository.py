from app import db
from app.models import Enrollment, Completion, Budget


def get_all_enrollments():
    return Enrollment.query.order_by(
        Enrollment.enrollment_date.desc()
    ).all()


def get_enrollment_by_id(enrollment_id):
    return db.session.get(Enrollment, enrollment_id)


def get_employee_enrollments(employee_id):
    return Enrollment.query.filter_by(
        employee_id=employee_id
    ).order_by(
        Enrollment.enrollment_date.desc()
    ).all()


def get_course_enrollments(course_id):
    return Enrollment.query.filter_by(
        course_id=course_id
    ).all()


def get_employee_course_enrollment(employee_id, course_id):
    return Enrollment.query.filter_by(
        employee_id=employee_id,
        course_id=course_id
    ).first()


def create_enrollment(enrollment):
    db.session.add(enrollment)
    db.session.commit()
    return enrollment


def update_enrollment(enrollment):
    db.session.commit()
    return enrollment


def delete_enrollment(enrollment):
    db.session.delete(enrollment)
    db.session.commit()


def get_completed_enrollments(employee_id):
    return (
        Enrollment.query
        .join(Completion)
        .filter(
            Enrollment.employee_id == employee_id,
            Completion.status == "completed"
        )
        .all()
    )


def get_completion_by_enrollment(enrollment_id):
    return Completion.query.filter_by(
        enrollment_id=enrollment_id
    ).first()


def create_completion(completion):
    db.session.add(completion)
    db.session.commit()
    return completion


def get_budget_by_id(budget_id):
    return db.session.get(Budget, budget_id)


def get_department_budget(department, fiscal_year):
    return Budget.query.filter_by(
        department=department,
        fiscal_year=fiscal_year
    ).first()


def get_all_budgets():
    return Budget.query.order_by(
        Budget.department,
        Budget.fiscal_year
    ).all()