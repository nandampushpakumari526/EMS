from app.services.skill_gap_service import calculate_skill_gaps
from app.services.prerequisite_service import check_prerequisites
from app.services.budget_service import check_budget
from app.models import Course, CourseSkill


def recommend_courses(employee_id, fiscal_year=2026):

    # Step 1: Get employee skill gaps
    gaps = calculate_skill_gaps(employee_id)

    if not gaps:
        return []

    recommendations = []

    # Step 2: Check courses for each skill gap
    for gap in gaps:

        skill_id = gap["skill_id"]
        gap_level = gap["gap"]

        # Step 3: Find courses that teach this skill
        course_skills = CourseSkill.query.filter_by(
            skill_id=skill_id
        ).all()

        for course_skill in course_skills:

            course = Course.query.get(
                course_skill.course_id
            )

            if course is None:
                continue

            # Step 4: Check prerequisites
            prerequisites_met = check_prerequisites(
                employee_id,
                course.id
            )

            # Step 5: Check budget
            budget_available = check_budget(
                employee_id,
                course.cost,
                fiscal_year
            )

            # Step 6: Prepare recommendation
            recommendation = {
                "employee_id": employee_id,
                "course_id": course.id,
                "course_name": course.course_name,
                "skill_id": skill_id,
                "skill_name": gap.get("skill_name"),
                "gap": gap_level,
                "cost": course.cost,
                "duration_hours": course.duration_hours,
                "prerequisites_met": prerequisites_met,
                "budget_available": budget_available
            }

            recommendations.append(
                recommendation
            )

    # Step 7: Remove duplicate courses
    unique_recommendations = {}

    for recommendation in recommendations:

        course_id = recommendation["course_id"]

        if course_id not in unique_recommendations:

            unique_recommendations[course_id] = recommendation

    return list(
        unique_recommendations.values()
    )


# Compatibility function
def recommend_courses_for_employee(
    employee_id,
    fiscal_year=2026
):

    return recommend_courses(
        employee_id,
        fiscal_year
    )