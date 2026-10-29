
from app import db


class Budget(db.Model):
    __tablename__ = "budgets"

    id = db.Column(db.Integer, primary_key=True)

    department = db.Column(
        db.String(100),
        nullable=False
    )

    fiscal_year = db.Column(
        db.Integer,
        nullable=False
    )

    total_amount = db.Column(
        db.Float,
        nullable=False
    )

    spent_amount = db.Column(
        db.Float,
        default=0,
        nullable=False
    )

    enrollments = db.relationship(
        "Enrollment",
        back_populates="budget"
    )

    @property
    def remaining_amount(self):
        return self.total_amount - self.spent_amount

    __table_args__ = (
        db.CheckConstraint(
            "total_amount >= 0"
        ),
        db.CheckConstraint(
            "spent_amount >= 0"
        ),
        db.CheckConstraint(
            "spent_amount <= total_amount"
        ),
    )
