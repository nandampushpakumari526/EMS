
from app import db


class RoleSkillTarget(db.Model):

    __tablename__ = "role_skill_targets"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
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

    role = db.relationship(
        "Role",
        back_populates="skill_targets"
    )

    skill = db.relationship(
        "Skill"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "role_id",
            "skill_id",
            name="unique_role_skill"
        ),
        db.CheckConstraint(
            "target_level BETWEEN 1 AND 5",
            name="valid_target_level"
        ),
    )

    def __repr__(self):
        return f"<RoleSkillTarget {self.role_id}-{self.skill_id}>"
