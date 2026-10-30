
from app import db

from app.models import (
    Employee,
    EmployeeSkill,
    RoleSkillTarget
)


def calculate_skill_gaps(employee_id):

    # Get employee
    employee = db.session.get(
        Employee,
        employee_id
    )

    if employee is None:
        print("Employee not found:", employee_id)
        return []

    print("Employee:", employee.name)
    print("Role ID:", employee.role_id)

    # Get required skills for employee role
    role_targets = RoleSkillTarget.query.filter_by(
        role_id=employee.role_id
    ).all()

    print("Role targets:", len(role_targets))

    # Get employee current skills
    employee_skills = EmployeeSkill.query.filter_by(
        employee_id=employee.id
    ).all()

    print("Employee skills:", len(employee_skills))

    # Store current skill levels
    current_skills = {}

    for item in employee_skills:

        current_skills[item.skill_id] = (
            item.proficiency_level
        )

    gaps = []

    # Calculate skill gaps
    for target in role_targets:

        current_level = current_skills.get(
            target.skill_id,
            0
        )

        required_level = target.target_level

        gap = required_level - current_level

        print(
            "Skill:",
            target.skill.name,
            "Current:",
            current_level,
            "Required:",
            required_level,
            "Gap:",
            gap
        )

        if gap > 0:

            gaps.append({

                "skill_id": target.skill_id,

                "skill_name": target.skill.name,

                "current_level": current_level,

                "required_level": required_level,

                "gap": gap

            })

    print("FINAL SKILL GAPS:", gaps)

    return gaps


def get_employee_skill_summary(employee_id):

    employee = db.session.get(
        Employee,
        employee_id
    )

    if employee is None:
        return None

    gaps = calculate_skill_gaps(
        employee_id
    )

    return {

        "employee_id": employee.id,

        "employee_name": employee.name,

        "role": employee.role.name,

        "skill_gaps": gaps,

        "total_gaps": len(gaps)

    }
