from app import db
from app.models import Employee


def get_all_employees():
    return Employee.query.order_by(Employee.id).all()


def get_employee_by_id(employee_id):
    return db.session.get(Employee, employee_id)


def get_employee_by_code(employee_code):
    return Employee.query.filter_by(
        employee_code=employee_code
    ).first()


def get_employee_by_email(email):
    return Employee.query.filter_by(
        email=email
    ).first()


def create_employee(employee):
    db.session.add(employee)
    db.session.commit()
    return employee


def update_employee(employee):
    db.session.commit()
    return employee


def delete_employee(employee):
    db.session.delete(employee)
    db.session.commit()


def get_employees_by_department(department):
    return Employee.query.filter_by(
        department=department
    ).all()


def get_employees_by_role(role_id):
    return Employee.query.filter_by(
        role_id=role_id
    ).all()


def get_active_employees():
    return Employee.query.filter_by(
        status="active"
    ).all()