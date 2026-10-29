
from flask import Blueprint, render_template

from app.repositories import skill_repository


bp = Blueprint(
    "skills",
    __name__,
    url_prefix="/skills"
)


# --------------------------------
# Skill List
# --------------------------------

@bp.route("/")
def get_skills():

    skills = skill_repository.get_all_skills()

    return render_template(
        "skills/skill_list.html",
        skills=skills
    )


# --------------------------------
# Skill Details
# --------------------------------

@bp.route("/<int:skill_id>")
def get_skill(skill_id):

    skill = skill_repository.get_skill_by_id(
        skill_id
    )

    if skill is None:
        return "Skill not found", 404

    return render_template(
        "skills/skill_detail.html",
        skill=skill
    )
