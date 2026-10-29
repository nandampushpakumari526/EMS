
from app.services.recommendation_service import recommend_courses


def generate_learning_path(employee_id, fiscal_year=2026):

    recommendations = recommend_courses(
        employee_id,
        fiscal_year
    )

    if recommendations is None:
        return None

    eligible_courses = []

    for recommendation in recommendations:

        if recommendation["prerequisites_met"]:

            if recommendation["budget_available"]:

                eligible_courses.append(recommendation)

    # Sort by skill gap, largest first
    eligible_courses.sort(
        key=lambda item: item["gap"],
        reverse=True
    )

    total_cost = sum(
        item["cost"]
        for item in eligible_courses
    )

    total_hours = sum(
        item["duration_hours"]
        for item in eligible_courses
    )

    return {

        "employee_id": employee_id,

        "courses": eligible_courses,

        "total_courses": len(eligible_courses),

        "total_cost": total_cost,

        "total_duration_hours": total_hours

    }
