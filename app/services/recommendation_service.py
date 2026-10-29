
from app.models import Course, CourseSkill

from app.services.skill_gap_service import calculate_skill_gaps
from app.services.prerequisite_service import check_prerequisites
from app.services.budget_service import check_budget


def recommend_courses(employee_id, fiscal_year=2026):

    from app.models import Employee

    employee = Employee.query.get(employee_id)

    if employee is None:
        return None

    gaps = calculate_skill_gaps(employee_id)

    recommendations = []

    for gap in gaps:

        courses = (
            Course.query
            .join(CourseSkill)
            .filter(
                CourseSkill.skill_id == gap["skill_id"],
                Course.status == "active"
            )
            .all()
        )

        for course in courses:

            course_skill = CourseSkill.query.filter_by(
                course_id=course.id,
                skill_id=gap["skill_id"]
            ).first()

            if course_skill is None:
                continue

            if course_skill.target_level < gap["required_level"]:
                continue

            prerequisite_result = check_prerequisites(
                employee_id,
                course.id
            )

            budget_result = check_budget(
                employee.department,
                fiscal_year,
                course.cost
            )

            recommendations.append({

                "course_id": course.id,
                "course_title": course.title,
                "skill_id": gap["skill_id"],
                "skill_name": gap["skill_name"],
                "current_level": gap["current_level"],
                "required_level": gap["required_level"],
                "gap": gap["gap"],
                "cost": course.cost,
                "duration_hours": course.duration_hours,
                "prerequisites_met": prerequisite_result["eligible"],
                "missing_prerequisites":
                    prerequisite_result["missing_prerequisites"],
                "budget_available": budget_result["eligible"],
                "budget_message": budget_result["message"]

            })

    # Remove duplicate course recommendations
    unique_recommendations = {}

    for recommendation in recommendations:

        course_id = recommendation["course_id"]

        if course_id not in unique_recommendations:

            unique_recommendations[course_id] = recommendation

    return list(unique_recommendations.values())
