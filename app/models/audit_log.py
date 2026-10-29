
from app import db
from datetime import datetime


class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=True
    )

    action = db.Column(
        db.String(100),
        nullable=False
    )

    entity_type = db.Column(
        db.String(100),
        nullable=False
    )

    entity_id = db.Column(
        db.Integer,
        nullable=True
    )

    details = db.Column(db.Text)

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    employee = db.relationship("Employee")
