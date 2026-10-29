
from app.models import Employee, EmployeeSkill, RoleSkillTarget


def calculate_skill_gaps(employee_id):

    employee = Employee.query.get(employee_id)

    if employee is None:
        return None

    role_targets = RoleSkillTarget.query.filter_by(
        role_id=employee.role_id
    ).all()

    employee_skills = EmployeeSkill.query.filter_by(
        employee_id=employee_id
    ).all()

    current_skills = {
        item.skill_id: item.proficiency_level
        for item in employee_skills
    }

    gaps = []

    for target in role_targets:

        current_level = current_skills.get(
            target.skill_id,
            0
        )

        required_level = target.target_level

        gap = required_level - current_level

        if gap > 0:

            gaps.append({
                "skill_id": target.skill_id,
                "skill_name": target.skill.name,
                "current_level": current_level,
                "required_level": required_level,
                "gap": gap
            })

    return gaps


def get_employee_skill_summary(employee_id):

    employee = Employee.query.get(employee_id)

    if employee is None:
        return None

    gaps = calculate_skill_gaps(employee_id)

    return {
        "employee_id": employee.id,
        "employee_name": employee.name,
        "role": employee.role.name,
        "skill_gaps": gaps,
        "total_gaps": len(gaps)
    }
