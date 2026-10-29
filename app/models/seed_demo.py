
from datetime import date

from app import db

from app.models.role import Role
from app.models.employee import Employee
from app.models.skill import Skill
from app.models.employee_skill import EmployeeSkill
from app.models.course import Course
from app.models.course_skill import CourseSkill
from app.models.prerequisite import Prerequisite
from app.models.budget import Budget

from app.models.role_skill_target import RoleSkillTarget
def seed_demo():

    print("Starting demo data seeding...")

    # ==========================================
    # 1. ROLES
    # ==========================================

    roles_data = [
        {
            "name": "Python Developer",
            "description": "Develops Python applications",
            "department": "IT"
        },
        {
            "name": "Data Analyst",
            "description": "Analyzes business data",
            "department": "Analytics"
        },
        {
            "name": "AI Engineer",
            "description": "Develops AI and machine learning applications",
            "department": "AI"
        },
        {
            "name": "Full Stack Developer",
            "description": "Develops frontend and backend applications",
            "department": "IT"
        }
    ]

    for data in roles_data:

        role = Role.query.filter_by(
            name=data["name"]
        ).first()

        if role is None:

            role = Role(
                name=data["name"],
                description=data["description"],
                department=data["department"]
            )

            db.session.add(role)

    db.session.flush()

    print("Roles created successfully")


    # ==========================================
    # 2. SKILLS
    # ==========================================

    skills_data = [
        {
            "name": "Python",
            "description": "Python programming language",
            "category": "Programming"
        },
        {
            "name": "SQL",
            "description": "Database querying",
            "category": "Database"
        },
        {
            "name": "HTML",
            "description": "Web page structure",
            "category": "Frontend"
        },
        {
            "name": "CSS",
            "description": "Web page styling",
            "category": "Frontend"
        },
        {
            "name": "JavaScript",
            "description": "Frontend programming",
            "category": "Frontend"
        },
        {
            "name": "Flask",
            "description": "Python web framework",
            "category": "Backend"
        },
        {
            "name": "Machine Learning",
            "description": "Machine learning algorithms",
            "category": "AI"
        },
        {
            "name": "Pandas",
            "description": "Data analysis library",
            "category": "Data Science"
        },
        {
            "name": "NumPy",
            "description": "Numerical computing library",
            "category": "Data Science"
        },
        {
            "name": "Git",
            "description": "Version control",
            "category": "Tools"
        }
    ]

    for data in skills_data:

        skill = Skill.query.filter_by(
            name=data["name"]
        ).first()

        if skill is None:

            skill = Skill(
                name=data["name"],
                description=data["description"],
                category=data["category"]
            )

            db.session.add(skill)

    db.session.flush()

    print("Skills created successfully")


    # ==========================================
    # 3. EMPLOYEES
    # ==========================================

    python_role = Role.query.filter_by(
        name="Python Developer"
    ).first()

    analyst_role = Role.query.filter_by(
        name="Data Analyst"
    ).first()

    ai_role = Role.query.filter_by(
        name="AI Engineer"
    ).first()

    fullstack_role = Role.query.filter_by(
        name="Full Stack Developer"
    ).first()


    employees_data = [
        {
            "employee_code": "EMP001",
            "name": "Rahul Sharma",
            "email": "rahul@example.com",
            "department": "IT",
            "role": python_role
        },
        {
            "employee_code": "EMP002",
            "name": "Priya Reddy",
            "email": "priya@example.com",
            "department": "Analytics",
            "role": analyst_role
        },
        {
            "employee_code": "EMP003",
            "name": "Arjun Kumar",
            "email": "arjun@example.com",
            "department": "AI",
            "role": ai_role
        },
        {
            "employee_code": "EMP004",
            "name": "Sneha Patel",
            "email": "sneha@example.com",
            "department": "IT",
            "role": fullstack_role
        }
    ]

    for data in employees_data:

        employee = Employee.query.filter_by(
            employee_code=data["employee_code"]
        ).first()

        if employee is None:

            employee = Employee(
                employee_code=data["employee_code"],
                name=data["name"],
                email=data["email"],
                department=data["department"],
                role_id=data["role"].id,
                status="active"
            )

            db.session.add(employee)

    db.session.flush()

    print("Employees created successfully")


    # ==========================================
    # 4. EMPLOYEE SKILLS
    # ==========================================

    employee_skills_data = [

        ("EMP001", "Python", 4),
        ("EMP001", "SQL", 3),
        ("EMP001", "Flask", 2),
        ("EMP001", "Git", 3),

        ("EMP002", "SQL", 4),
        ("EMP002", "Python", 2),
        ("EMP002", "Pandas", 3),
        ("EMP002", "NumPy", 2),

        ("EMP003", "Python", 3),
        ("EMP003", "Machine Learning", 2),
        ("EMP003", "NumPy", 3),
        ("EMP003", "Pandas", 2),

        ("EMP004", "HTML", 4),
        ("EMP004", "CSS", 3),
        ("EMP004", "JavaScript", 2),
        ("EMP004", "Python", 2),
        ("EMP004", "Flask", 2)
    ]

    for employee_code, skill_name, level in employee_skills_data:

        employee = Employee.query.filter_by(
            employee_code=employee_code
        ).first()

        skill = Skill.query.filter_by(
            name=skill_name
        ).first()

        existing = EmployeeSkill.query.filter_by(
            employee_id=employee.id,
            skill_id=skill.id
        ).first()

        if existing is None:

            employee_skill = EmployeeSkill(
                employee_id=employee.id,
                skill_id=skill.id,
                proficiency_level=level,
                assessed_date=date.today()
            )

            db.session.add(employee_skill)

    db.session.flush()

    print("Employee skills created successfully")


    # ==========================================
    # 5. COURSES
    # ==========================================

    courses_data = [
        {
            "title": "Python Basics",
            "description": "Learn Python fundamentals",
            "duration_hours": 20,
            "cost": 2000,
            "difficulty_level": "Beginner",
            "provider": "Codegnan"
        },
        {
            "title": "Advanced Python",
            "description": "Learn advanced Python programming",
            "duration_hours": 30,
            "cost": 3500,
            "difficulty_level": "Intermediate",
            "provider": "Codegnan"
        },
        {
            "title": "SQL Fundamentals",
            "description": "Learn SQL queries and databases",
            "duration_hours": 15,
            "cost": 1500,
            "difficulty_level": "Beginner",
            "provider": "Online Academy"
        },
        {
            "title": "Flask Web Development",
            "description": "Build web applications using Flask",
            "duration_hours": 25,
            "cost": 3000,
            "difficulty_level": "Intermediate",
            "provider": "Codegnan"
        },
        {
            "title": "Machine Learning Basics",
            "description": "Learn machine learning algorithms",
            "duration_hours": 40,
            "cost": 5000,
            "difficulty_level": "Intermediate",
            "provider": "AI Academy"
        },
        {
            "title": "Data Analysis with Pandas",
            "description": "Learn data analysis using Pandas",
            "duration_hours": 20,
            "cost": 2500,
            "difficulty_level": "Beginner",
            "provider": "Data Academy"
        },
        {
            "title": "Frontend Development",
            "description": "Learn HTML CSS and JavaScript",
            "duration_hours": 35,
            "cost": 4000,
            "difficulty_level": "Beginner",
            "provider": "Web Academy"
        },
        {
            "title": "Git and GitHub",
            "description": "Learn version control",
            "duration_hours": 10,
            "cost": 1000,
            "difficulty_level": "Beginner",
            "provider": "Online Academy"
        }
    ]

    for data in courses_data:

        course = Course.query.filter_by(
            title=data["title"]
        ).first()

        if course is None:

            course = Course(
                title=data["title"],
                description=data["description"],
                duration_hours=data["duration_hours"],
                cost=data["cost"],
                difficulty_level=data["difficulty_level"],
                provider=data["provider"],
                status="active"
            )

            db.session.add(course)

    db.session.flush()

    print("Courses created successfully")


    # ==========================================
    # 6. COURSE SKILLS
    # ==========================================

    course_skills_data = [

        ("Python Basics", "Python", 3),

        ("Advanced Python", "Python", 5),

        ("SQL Fundamentals", "SQL", 4),

        ("Flask Web Development", "Python", 4),
        ("Flask Web Development", "Flask", 4),

        ("Machine Learning Basics", "Python", 4),
        ("Machine Learning Basics", "Machine Learning", 4),
        ("Machine Learning Basics", "NumPy", 3),
        ("Machine Learning Basics", "Pandas", 3),

        ("Data Analysis with Pandas", "Python", 3),
        ("Data Analysis with Pandas", "Pandas", 4),
        ("Data Analysis with Pandas", "NumPy", 3),

        ("Frontend Development", "HTML", 4),
        ("Frontend Development", "CSS", 4),
        ("Frontend Development", "JavaScript", 4),

        ("Git and GitHub", "Git", 4)
    ]

    for course_title, skill_name, target_level in course_skills_data:

        course = Course.query.filter_by(
            title=course_title
        ).first()

        skill = Skill.query.filter_by(
            name=skill_name
        ).first()

        existing = CourseSkill.query.filter_by(
            course_id=course.id,
            skill_id=skill.id
        ).first()

        if existing is None:

            course_skill = CourseSkill(
                course_id=course.id,
                skill_id=skill.id,
                target_level=target_level
            )

            db.session.add(course_skill)

    db.session.flush()

    print("Course skills created successfully")

    # ==========================================
    # 7. PREREQUISITES
    # ==========================================

    prerequisites_data = [

        ("Advanced Python", "Python Basics"),

        ("Flask Web Development", "Python Basics"),

        ("Machine Learning Basics", "Python Basics"),

        ("Machine Learning Basics", "Data Analysis with Pandas")
    ]

    for course_title, prerequisite_title in prerequisites_data:

        course = Course.query.filter_by(
            title=course_title
        ).first()

        prerequisite_course = Course.query.filter_by(
            title=prerequisite_title
        ).first()

        existing = Prerequisite.query.filter_by(
            course_id=course.id,
            prerequisite_course_id=prerequisite_course.id
        ).first()

        if existing is None:

            prerequisite = Prerequisite(
                course_id=course.id,
                prerequisite_course_id=prerequisite_course.id
            )

            db.session.add(prerequisite)

    db.session.flush()

    print("Prerequisites created successfully")


    # ==========================================
    # 8. BUDGETS
    # ==========================================

    budgets_data = [

        {
            "department": "IT",
            "fiscal_year": 2026,
            "total_amount": 50000,
            "spent_amount": 0
        },

        {
            "department": "Analytics",
            "fiscal_year": 2026,
            "total_amount": 40000,
            "spent_amount": 0
        },

        {
            "department": "AI",
            "fiscal_year": 2026,
            "total_amount": 60000,
            "spent_amount": 0
        }
    ]

    for data in budgets_data:

        budget = Budget.query.filter_by(
            department=data["department"],
            fiscal_year=data["fiscal_year"]
        ).first()

        if budget is None:

            budget = Budget(
                department=data["department"],
                fiscal_year=data["fiscal_year"],
                total_amount=data["total_amount"],
                spent_amount=data["spent_amount"]
            )

            db.session.add(budget)

    # ==========================================
    # 9. COMMIT
    # ==========================================

    try:

        db.session.commit()

        print("Demo data seeded successfully!")

    except Exception as error:

        db.session.rollback()

        print("Error while seeding demo data:", error)

        raise

    # ==========================================
    # ROLE SKILL TARGETS
    # ==========================================

    role_skill_targets_data = [

        ("Python Developer", "Python", 5),
        ("Python Developer", "SQL", 4),
        ("Python Developer", "Flask", 4),
        ("Python Developer", "Git", 3),

        ("Data Analyst", "SQL", 5),
        ("Data Analyst", "Python", 4),
        ("Data Analyst", "Pandas", 5),
        ("Data Analyst", "NumPy", 4),

        ("AI Engineer", "Python", 5),
        ("AI Engineer", "Machine Learning", 5),
        ("AI Engineer", "NumPy", 4),
        ("AI Engineer", "Pandas", 4),

        ("Full Stack Developer", "HTML", 5),
        ("Full Stack Developer", "CSS", 5),
        ("Full Stack Developer", "JavaScript", 4),
        ("Full Stack Developer", "Python", 3),
        ("Full Stack Developer", "Flask", 4)
    ]

    for role_name, skill_name, target_level in role_skill_targets_data:

        role = Role.query.filter_by(
            name=role_name
        ).first()

        skill = Skill.query.filter_by(
            name=skill_name
        ).first()

        existing = RoleSkillTarget.query.filter_by(
            role_id=role.id,
            skill_id=skill.id
        ).first()

        if existing is None:

            target = RoleSkillTarget(
                role_id=role.id,
                skill_id=skill.id,
                target_level=target_level
            )

            db.session.add(target)

    db.session.flush()

    print("Role skill targets created successfully")
