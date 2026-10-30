
from app import db


class EmployeeSkill(db.Model):

    __tablename__ = "employee_skills"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.id"),
        nullable=False
    )

    proficiency_level = db.Column(
        db.Integer,
        nullable=False
    )

    assessed_date = db.Column(
        db.Date
    )

    employee = db.relationship(
        "Employee",
        back_populates="skills"
    )

    skill = db.relationship(
        "Skill",
        back_populates="employee_skills"
    )

    __table_args__ = (

        db.UniqueConstraint(
            "employee_id",
            "skill_id",
            name="unique_employee_skill"
        ),

        db.CheckConstraint(
            "proficiency_level BETWEEN 1 AND 5",
            name="valid_proficiency"
        ),

    )

    def __repr__(self):

        return (
            f"<EmployeeSkill "
            f"employee_id={self.employee_id} "
            f"skill_id={self.skill_id}>"
        )
