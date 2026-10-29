
from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.repositories import employee_repository
from app.repositories import skill_repository
from app.repositories import course_repository
from app.repositories import enrollment_repository

from app.models import Employee, EmployeeSkill, Enrollment


ui_bp = Blueprint("ui", __name__)


# -------------------------
# Dashboard
# -------------------------

@ui_bp.route("/")
def dashboard():

    employees = employee_repository.get_all_employees()

    skills = skill_repository.get_all_skills()

    courses = course_repository.get_active_courses()

    enrollments = enrollment_repository.get_all_enrollments()

    budgets = enrollment_repository.get_all_budgets()

    return render_template(
        "dashboard.html",
        employees=employees,
        skills=skills,
        courses=courses,
        enrollments=enrollments,
        budgets=budgets
    )


# -------------------------
# Employees
# -------------------------

@ui_bp.route("/employees/")
def employee_list():
    employees = employee_repository.get_all_employees()

    return render_template(
        "employees/employee_list.html",
        employees=employees
    )


@ui_bp.route("/employees/<int:employee_id>")
def employee_detail(employee_id):
    employee = employee_repository.get_employee_by_id(employee_id)

    if employee is None:
        return "Employee not found", 404

    skills = skill_repository.get_employee_skills(employee_id)

    return render_template(
        "employees/employee_detail.html",
        employee=employee,
        skills=skills
    )


@ui_bp.route("/employees/create", methods=["GET", "POST"])
def employee_create():

    if request.method == "POST":

        employee_code = request.form.get("employee_code")
        name = request.form.get("name")
        email = request.form.get("email")
        department = request.form.get("department")
        role_id = request.form.get("role_id")

        if not all([employee_code, name, email, department, role_id]):
            flash("Please fill all required fields.", "danger")
            return redirect(url_for("ui.employee_create"))

        if employee_repository.get_employee_by_code(employee_code):
            flash("Employee code already exists.", "danger")
            return redirect(url_for("ui.employee_create"))

        if employee_repository.get_employee_by_email(email):
            flash("Email already exists.", "danger")
            return redirect(url_for("ui.employee_create"))

        employee = Employee(
            employee_code=employee_code,
            name=name,
            email=email,
            department=department,
            role_id=int(role_id),
            status="active"
        )

        employee_repository.create_employee(employee)

        flash("Employee created successfully.", "success")

        return redirect(url_for("ui.employee_list"))

    from app.models import Role

    roles = Role.query.order_by(Role.name).all()

    return render_template(
        "employees/employee_form.html",
        roles=roles
    )


# -------------------------
# Skills
# -------------------------

@ui_bp.route("/skills/")
def skill_list():
    skills = skill_repository.get_all_skills()

    return render_template(
        "skills/skill_list.html",
        skills=skills
    )


# -------------------------
# Courses
# -------------------------

@ui_bp.route("/courses/")
def course_list():
    courses = course_repository.get_active_courses()

    return render_template(
        "courses/course_list.html",
        courses=courses
    )


@ui_bp.route("/courses/<int:course_id>")
def course_detail(course_id):
    course = course_repository.get_course_by_id(course_id)

    if course is None:
        return "Course not found", 404

    skills = course_repository.get_course_skills(course_id)

    prerequisites = course_repository.get_course_prerequisites(
        course_id
    )

    return render_template(
        "courses/course_detail.html",
        course=course,
        skills=skills,
        prerequisites=prerequisites
    )


# -------------------------
# Recommendations
# -------------------------

@ui_bp.route("/recommendations/<int:employee_id>")
def recommendation_list(employee_id):

    from app.services.recommendation_service import (
        recommend_courses_for_employee
    )

    recommendations = recommend_courses_for_employee(employee_id)

    employee = employee_repository.get_employee_by_id(employee_id)

    if employee is None:
        return "Employee not found", 404

    return render_template(
        "recommendations/recommendation_list.html",
        employee=employee,
        recommendations=recommendations
    )


# -------------------------
# Learning Path
# -------------------------

@ui_bp.route("/learning-path/<int:employee_id>")
def learning_path(employee_id):

    from app.services.recommendation_service import (
        recommend_courses_for_employee
    )

    from app.services.learning_path_service import (
        build_learning_path
    )

    employee = employee_repository.get_employee_by_id(employee_id)

    if employee is None:
        return "Employee not found", 404

    recommendations = recommend_courses_for_employee(employee_id)

    learning_path = build_learning_path(recommendations)

    return render_template(
        "recommendations/learning_path.html",
        employee=employee,
        learning_path=learning_path
    )


# -------------------------
# Enrollments
# -------------------------

@ui_bp.route("/enrollments/")
def enrollment_list():

    enrollments = enrollment_repository.get_all_enrollments()

    return render_template(
        "enrollments/enrollment_list.html",
        enrollments=enrollments
    )


# -------------------------
# Reports
# -------------------------

@ui_bp.route("/reports/dashboard")
def report_dashboard():

    employees = employee_repository.get_all_employees()

    courses = course_repository.get_all_courses()

    enrollments = enrollment_repository.get_all_enrollments()

    budgets = enrollment_repository.get_all_budgets()

    return render_template(
        "reports/dashboard.html",
        employees=employees,
        courses=courses,
        enrollments=enrollments,
        budgets=budgets
    )
