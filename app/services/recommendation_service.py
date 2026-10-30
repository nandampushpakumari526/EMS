
from app import db

from app.models import Employee, Course, CourseSkill

from app.services.skill_gap_service import (
    calculate_skill_gaps
)

from app.services.prerequisite_service import (
    check_prerequisites
)

from app.services.budget_service import (
    check_budget
)


def recommend_courses(employee_id, fiscal_year=2026):

    # Step 1: Get employee
    employee = db.session.get(
        Employee,
        employee_id
    )

    if employee is None:
        return None

    print("EMPLOYEE:", employee.name)

    # Step 2: Calculate skill gaps
    gaps = calculate_skill_gaps(employee.id)

    print("SKILL GAPS:", gaps)

    if not gaps:
        print("No skill gaps found")
        return []

    recommendations = []

    # Step 3: Find courses for each skill gap
    for gap in gaps:

        skill_id = gap["skill_id"]

        gap_level = gap["gap"]

        print("SEARCHING SKILL:", gap["skill_name"])

        course_skills = CourseSkill.query.filter_by(
            skill_id=skill_id
        ).all()

        print("MATCHING COURSE SKILLS:", course_skills)

        # Step 4: Get matching courses
        for course_skill in course_skills:

            course = db.session.get(
                Course,
                course_skill.course_id
            )

            if course is None:
                continue

            print("MATCHING COURSE:", course.course_name)

            # Step 5: Check prerequisites
            prerequisite_result = check_prerequisites(
                employee.id,
                course.id
            )

            prerequisites_met = (
                prerequisite_result["eligible"]
            )

            missing_prerequisites = (
                prerequisite_result["missing_prerequisites"]
            )

            # Step 6: Check budget
            budget_available = check_budget(
                employee.id,
                course.cost,
                fiscal_year
            )

            # Step 7: Create recommendation
            recommendation = {

                "employee_id": employee.id,

                "course_id": course.id,

                "course_name": course.course_name,

                "skill_id": skill_id,

                "skill_name": gap["skill_name"],

                "current_level": gap["current_level"],

                "required_level": gap["required_level"],

                "gap": gap_level,

                "cost": course.cost,

                "duration_hours": course.duration_hours,

                "prerequisites_met": prerequisites_met,

                "missing_prerequisites": missing_prerequisites,

                "budget_available": budget_available,

                "budget_message": (
                    "Budget available"
                    if budget_available
                    else "Budget not available"
                )

            }

            recommendations.append(recommendation)

    # Step 8: Remove duplicate courses
    unique_recommendations = {}

    for recommendation in recommendations:

        course_id = recommendation["course_id"]

        if course_id not in unique_recommendations:

            unique_recommendations[course_id] = (
                recommendation
            )

        else:

            existing = unique_recommendations[course_id]

            if recommendation["gap"] > existing["gap"]:

                unique_recommendations[course_id] = (
                    recommendation
                )

    # Step 9: Return recommendations
    final_recommendations = list(
        unique_recommendations.values()
    )

    print("FINAL RECOMMENDATIONS:", final_recommendations)

    return final_recommendations


def recommend_courses_for_employee(
    employee_id,
    fiscal_year=2026
):

    return recommend_courses(
        employee_id,
        fiscal_year
    )
