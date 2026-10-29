
from app import db


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    description = db.Column(db.Text)

    department = db.Column(
        db.String(100)
    )

    employees = db.relationship(
        "Employee",
        back_populates="role"
    )

    skill_targets = db.relationship(
        "RoleSkillTarget",
        back_populates="role",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Role {self.name}>"
