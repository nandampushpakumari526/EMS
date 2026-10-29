
from app import db
from datetime import datetime


class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    budget_id = db.Column(
        db.Integer,
        db.ForeignKey("budgets.id"),
        nullable=True
    )

    enrollment_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(30),
        default="enrolled",
        nullable=False
    )

    employee = db.relationship(
        "Employee",
        back_populates="enrollments"
    )

    course = db.relationship(
        "Course",
        back_populates="enrollments"
    )

    budget = db.relationship(
        "Budget",
        back_populates="enrollments"
    )

    completion = db.relationship(
        "Completion",
        back_populates="enrollment",
        uselist=False
    )
