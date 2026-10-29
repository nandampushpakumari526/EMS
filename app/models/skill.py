
from app import db


class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    description = db.Column(db.Text)

    category = db.Column(db.String(100))

    employee_skills = db.relationship(
        "EmployeeSkill",
        back_populates="skill"
    )

    course_skills = db.relationship(
        "CourseSkill",
        back_populates="skill"
    )

    def __repr__(self):
        return f"<Skill {self.name}>"
