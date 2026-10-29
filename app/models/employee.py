from app import db


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    employee_code = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    department = db.Column(db.String(100))

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="active",
        nullable=False
    )

    role = db.relationship(
        "Role",
        back_populates="employees"
    )

    skills = db.relationship(
        "EmployeeSkill",
        back_populates="employee",
        cascade="all, delete-orphan"
    )

    enrollments = db.relationship(
        "Enrollment",
        back_populates="employee"
    )

    def __repr__(self):
        return f"<Employee {self.name}>"
