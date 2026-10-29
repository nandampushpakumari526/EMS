from app import db
from app.models import Skill, EmployeeSkill, RoleSkillTarget


def get_all_skills():
    return Skill.query.order_by(Skill.name).all()


def get_skill_by_id(skill_id):
    return db.session.get(Skill, skill_id)


def get_skill_by_name(name):
    return Skill.query.filter_by(name=name).first()


def create_skill(skill):
    db.session.add(skill)
    db.session.commit()
    return skill


def update_skill(skill):
    db.session.commit()
    return skill


def delete_skill(skill):
    db.session.delete(skill)
    db.session.commit()


def get_employee_skills(employee_id):
    return EmployeeSkill.query.filter_by(
        employee_id=employee_id
    ).all()


def get_employee_skill(employee_id, skill_id):
    return EmployeeSkill.query.filter_by(
        employee_id=employee_id,
        skill_id=skill_id
    ).first()


def get_role_skill_targets(role_id):
    return RoleSkillTarget.query.filter_by(
        role_id=role_id
    ).all()


def get_skill_targets_by_skill(skill_id):
    return RoleSkillTarget.query.filter_by(
        skill_id=skill_id
    ).all()


def create_employee_skill(employee_skill):
    db.session.add(employee_skill)
    db.session.commit()
    return employee_skill


def update_employee_skill(employee_skill):
    db.session.commit()
    return employee_skill