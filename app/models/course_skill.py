
from app import db


class CourseSkill(db.Model):
    __tablename__ = "course_skills"

    id = db.Column(db.Integer, primary_key=True)

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    skill_id = db.Column(
        db.Integer,
        db.ForeignKey("skills.id"),
        nullable=False
    )

    target_level = db.Column(
        db.Integer,
        nullable=False,
        default=3
    )

    course = db.relationship(
        "Course",
        back_populates="course_skills"
    )

    skill = db.relationship(
        "Skill",
        back_populates="course_skills"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "course_id",
            "skill_id"
        ),
        db.CheckConstraint(
            "target_level BETWEEN 1 AND 5"
        ),
    )
