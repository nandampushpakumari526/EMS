
from datetime import date

from app import db

from app.models import EmployeeSkill, Skill, Employee


def reassess_skill(
    employee_id,
    skill_id,
    proficiency_level
):

    employee = Employee.query.get(employee_id)

    skill = Skill.query.get(skill_id)

    if employee is None:
        return {
            "success": False,
            "message": "Employee not found"
        }

    if skill is None:
        return {
            "success": False,
            "message": "Skill not found"
        }

    if not isinstance(proficiency_level, int):

        return {
            "success": False,
            "message": "Level must be an integer"
        }

    if proficiency_level < 1 or proficiency_level > 5:

        return {
            "success": False,
            "message": "Level must be between 1 and 5"
        }

    try:

        employee_skill = EmployeeSkill.query.filter_by(
            employee_id=employee_id,
            skill_id=skill_id
        ).first()

        if employee_skill is None:

            employee_skill = EmployeeSkill(

                employee_id=employee_id,

                skill_id=skill_id,

                proficiency_level=proficiency_level,

                assessed_date=date.today()

            )

            db.session.add(employee_skill)

        else:

            employee_skill.proficiency_level = proficiency_level

            employee_skill.assessed_date = date.today()

        db.session.commit()

        return {
            "success": True,
            "message": "Skill reassessment successful"
        }

    except Exception as error:

        db.session.rollback()

        return {
            "success": False,
            "message": str(error)
        }
