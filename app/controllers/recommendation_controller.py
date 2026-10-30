
from flask import Blueprint, jsonify, render_template

from app import db

from app.repositories import employee_repository

from app.models import (
    Employee,
    RoleSkillTarget,
    EmployeeSkill,
    Skill,
    Course,
    CourseSkill
)

from app.services.recommendation_service import (
    recommend_courses
)

from app.services.learning_path_service import (
    generate_learning_path
)

from app.services.skill_gap_service import (
    calculate_skill_gaps
)


bp = Blueprint(
    "recommendations",
    __name__,
    url_prefix="/recommendations"
)


# ==========================================
# COURSE RECOMMENDATIONS
# ==========================================

@bp.route("/<int:employee_id>", methods=["GET"])
def get_recommendations(employee_id):

    employee = employee_repository.get_employee_by_id(
        employee_id
    )

    if employee is None:
        return "Employee not found", 404

    recommendations = recommend_courses(employee_id)

    if recommendations is None:
        recommendations = []

    return render_template(
        "recommendations/course_recommendations.html",
        employee=employee,
        recommendations=recommendations
    )
# ==========================================
# LEARNING PATH
# ==========================================

@bp.route("/learning-path/<int:employee_id>", methods=["GET"])
def get_learning_path(employee_id):

    # Get employee
    employee = employee_repository.get_employee_by_id(
        employee_id
    )

    if employee is None:
        return "Employee not found", 404

    # Generate learning path
    learning_path = generate_learning_path(
        employee_id
    )

    if learning_path is None:

        learning_path = {
            "employee_id": employee_id,
            "courses": [],
            "total_courses": 0,
            "total_cost": 0,
            "total_duration_hours": 0
        }

    print("LEARNING PATH:", learning_path)

    # Display learning path template
    return render_template(
        "recommendations/learning_path.html",
        employee=employee,
        learning_path=learning_path
    )


# ==========================================
# CHECK EMPLOYEE SKILL GAPS AND COURSE DATA
# ==========================================

@bp.route("/check-data/<int:employee_id>", methods=["GET"])
def check_recommendation_data(employee_id):

    # Get employee
    employee = db.session.get(
        Employee,
        employee_id
    )

    if employee is None:

        return jsonify({
            "error": "Employee not found"
        }), 404

    # Get role skill targets
    targets = RoleSkillTarget.query.filter_by(
        role_id=employee.role_id
    ).all()

    # Get employee skills
    employee_skills = EmployeeSkill.query.filter_by(
        employee_id=employee_id
    ).all()

    # Calculate skill gaps
    gaps = calculate_skill_gaps(
        employee_id
    )

    if gaps is None:
        gaps = []

    # Get all skills
    skills = Skill.query.all()

    # Get all courses
    courses = Course.query.all()

    # Get course skill mappings
    course_skills = CourseSkill.query.all()

    # Get recommendations
    recommendations = recommend_courses(
        employee_id
    )

    if recommendations is None:
        recommendations = []

    # Return debugging data
    return jsonify({

        "employee": employee.name,

        "employee_id": employee.id,

        "role_id": employee.role_id,

        "role_skill_targets": [

            {
                "skill_id": target.skill_id,

                "skill_name": target.skill.name,

                "target_level": target.target_level
            }

            for target in targets

        ],

        "employee_skills": [

            {
                "skill_id": item.skill_id,

                "skill_name": item.skill.name,

                "current_level": item.proficiency_level
            }

            for item in employee_skills

        ],

        "calculated_gaps": gaps,

        "all_skills": [

            {
                "id": skill.id,

                "name": skill.name
            }

            for skill in skills

        ],

        "all_courses": [

            {
                "id": course.id,

                "name": course.course_name
            }

            for course in courses

        ],

        "course_skill_mappings": [

            {
                "course_id": item.course_id,

                "skill_id": item.skill_id
            }

            for item in course_skills

        ],

        "recommendations": recommendations

    })


# ==========================================
# LEARNING PATH JSON
# ==========================================

@bp.route("/learning-path-data/<int:employee_id>", methods=["GET"])
def get_learning_path_data(employee_id):

    learning_path = generate_learning_path(
        employee_id
    )

    if learning_path is None:

        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify(learning_path)
