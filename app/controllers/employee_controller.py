
from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash

from app import db

from app.models import Employee, Role, AuditLog

from app.repositories import employee_repository, skill_repository

from app.services.skill_gap_service import (
    get_employee_skill_summary
)


bp = Blueprint(
    "employees",
    __name__,
    url_prefix="/employees"
)


# =========================
# EMPLOYEE LIST
# =========================

@bp.route("/", methods=["GET"])
def get_employees():

    employees = Employee.query.all()

    return render_template(
        "employees/employee_list.html",
        employees=employees
    )


# =========================
# ADD EMPLOYEE FORM
# =========================

@bp.route("/create", methods=["GET"])
def create_employee_form():

    roles = Role.query.all()

    return render_template(
        "employees/employee_form.html",
        employee=None,
        roles=roles
    )


# =========================
# CREATE EMPLOYEE
# =========================

@bp.route("/", methods=["POST"])
def create_employee():

    # Read HTML form data
    data = request.form

    employee_code = data.get("employee_code", "").strip()
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    department = data.get("department", "").strip()
    role_id = data.get("role_id", "").strip()
    status = data.get("status", "active")

    roles = Role.query.all()

    # Validate required fields
    if not employee_code or not name or not email or not role_id:

        flash("Please fill all required fields.", "danger")

        return render_template(
            "employees/employee_form.html",
            employee=None,
            roles=roles
        ), 400

    # Validate role ID
    try:
        role_id = int(role_id)

    except ValueError:

        flash("Please select a valid role.", "danger")

        return render_template(
            "employees/employee_form.html",
            employee=None,
            roles=roles
        ), 400

    # Check role
    role = db.session.get(Role, role_id)

    if role is None:

        flash("Selected role does not exist.", "danger")

        return render_template(
            "employees/employee_form.html",
            employee=None,
            roles=roles
        ), 400

    # Check duplicate employee code
    existing_code = Employee.query.filter_by(
        employee_code=employee_code
    ).first()

    if existing_code:

        flash("Employee code already exists.", "danger")

        return render_template(
            "employees/employee_form.html",
            employee=None,
            roles=roles
        ), 400

    # Check duplicate email
    existing_email = Employee.query.filter_by(
        email=email
    ).first()

    if existing_email:

        flash("Email already exists.", "danger")

        return render_template(
            "employees/employee_form.html",
            employee=None,
            roles=roles
        ), 400

    try:

        # Create employee
        employee = Employee(

            employee_code=employee_code,

            name=name,

            email=email,

            department=department,

            role_id=role_id,

            status=status

        )

        db.session.add(employee)

        db.session.flush()

        # Create audit log
        log = AuditLog(

            action="CREATE",

            entity_type="Employee",

            entity_id=employee.id,

            details=f"Created employee {employee.name}"

        )

        db.session.add(log)

        db.session.commit()

        flash("Employee added successfully!", "success")

        return redirect(
            url_for("employees.get_employees")
        )

    except Exception as error:

        db.session.rollback()

        flash(
            f"Error creating employee: {str(error)}",
            "danger"
        )

        return render_template(
            "employees/employee_form.html",
            employee=None,
            roles=Role.query.all()
        ), 500


# =========================
# EMPLOYEE DETAILS
# =========================

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


# =========================
# EMPLOYEE SKILL GAPS
# =========================

@bp.route("/<int:employee_id>/skill-gaps", methods=["GET"])
def employee_skill_gaps(employee_id):

    result = get_employee_skill_summary(
        employee_id
    )

    if result is None:

        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify(result)
