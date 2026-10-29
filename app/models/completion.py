
from app import db
from datetime import datetime


class Completion(db.Model):
    __tablename__ = "completions"

    id = db.Column(db.Integer, primary_key=True)

    enrollment_id = db.Column(
        db.Integer,
        db.ForeignKey("enrollments.id"),
        unique=True,
        nullable=False
    )

    completion_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    score = db.Column(
        db.Float,
        nullable=True
    )

    status = db.Column(
        db.String(30),
        default="completed",
        nullable=False
    )

    enrollment = db.relationship(
        "Enrollment",
        back_populates="completion"
    )

    __table_args__ = (
        db.CheckConstraint(
            "score IS NULL OR score BETWEEN 0 AND 100"
        ),
    )
