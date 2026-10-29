
from flask import Blueprint, jsonify, request,render_template

from app import db

from app.models import Employee, Role, AuditLog

from app.services.skill_gap_service import (
    calculate_skill_gaps,
    get_employee_skill_summary
)

from app.repositories import employee_repository,skill_repository

bp = Blueprint(
    "employees",
    __name__,
    url_prefix="/employees"
)


@bp.route("/", methods=["GET"])
def get_employees():

    employees = Employee.query.all()

    result = []

    for employee in employees:

        result.append({

            "id": employee.id,

            "employee_code": employee.employee_code,

            "name": employee.name,

            "email": employee.email,

            "department": employee.department,

            "role": employee.role.name,

            "status": employee.status

        })

    return jsonify(result)


@bp.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):

    employee = employee_repository.get_employee_by_id(
        employee_id
    )

    if employee is None:
        return "Employee not found", 404

    skills = skill_repository.get_employee_skills(
        employee_id
    )

    return render_template(
        "employees/employee_detail.html",
        employee=employee,
        skills=skills
    )

@bp.route("/", methods=["POST"])
def create_employee():

    data = request.get_json(silent=True) or {}

    required_fields = [
        "employee_code",
        "name",
        "email",
        "department",
        "role_id"
    ]

    for field in required_fields:

        if not data.get(field):

            return jsonify({
                "error": f"{field} is required"
            }), 400

    role = Role.query.get(data["role_id"])

    if role is None:

        return jsonify({
            "error": "Role not found"
        }), 404

    if Employee.query.filter_by(
        employee_code=data["employee_code"]
    ).first():

        return jsonify({
            "error": "Employee code already exists"
        }), 409

    if Employee.query.filter_by(
        email=data["email"]
    ).first():

        return jsonify({
            "error": "Email already exists"
        }), 409

    try:

        employee = Employee(

            employee_code=data["employee_code"],

            name=data["name"],

            email=data["email"],

            department=data["department"],

            role_id=role.id,

            status="active"

        )

        db.session.add(employee)

        db.session.flush()

        log = AuditLog(

            action="CREATE",

            entity_type="Employee",

            entity_id=employee.id,

            details=f"Created employee {employee.name}"

        )

        db.session.add(log)

        db.session.commit()

        return jsonify({

            "message": "Employee created successfully",

            "employee_id": employee.id

        }), 201

    except Exception as error:

        db.session.rollback()

        return jsonify({
            "error": str(error)
        }), 500


@bp.route("/<int:employee_id>/skill-gaps", methods=["GET"])
def employee_skill_gaps(employee_id):

    result = get_employee_skill_summary(employee_id)

    if result is None:

        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify(result)
