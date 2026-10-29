
from app import db


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(db.Text)

    duration_hours = db.Column(
        db.Integer,
        nullable=False
    )

    cost = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    difficulty_level = db.Column(
        db.String(30),
        nullable=False
    )

    provider = db.Column(db.String(100))

    status = db.Column(
        db.String(20),
        default="active"
    )

    course_skills = db.relationship(
        "CourseSkill",
        back_populates="course",
        cascade="all, delete-orphan"
    )

    enrollments = db.relationship(
        "Enrollment",
        back_populates="course"
    )

    __table_args__ = (
        db.CheckConstraint(
            "duration_hours > 0",
            name="valid_course_duration"
        ),
        db.CheckConstraint(
            "cost >= 0",
            name="valid_course_cost"
        ),
    )

    def __repr__(self):
        return f"<Course {self.title}>"
