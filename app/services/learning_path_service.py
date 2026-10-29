
from app.services.recommendation_service import recommend_courses


def generate_learning_path(
    employee_id,
    fiscal_year=2026
):

    # Step 1: Get recommendations
    recommendations = recommend_courses(
        employee_id,
        fiscal_year
    )

    if recommendations is None:
        return None

    # Step 2: Keep eligible courses
    eligible_courses = []

    for recommendation in recommendations:

        if recommendation["prerequisites_met"]:

            if recommendation["budget_available"]:

                eligible_courses.append(
                    recommendation
                )

    # Step 3: Sort by skill gap
    eligible_courses.sort(
        key=lambda item: item["gap"],
        reverse=True
    )

    # Step 4: Calculate total cost
    total_cost = sum(
        item["cost"]
        for item in eligible_courses
    )

    # Step 5: Calculate total duration
    total_hours = sum(
        item["duration_hours"]
        for item in eligible_courses
    )

    # Step 6: Return learning path
    return {
        "employee_id": employee_id,
        "courses": eligible_courses,
        "total_courses": len(eligible_courses),
        "total_cost": total_cost,
        "total_duration_hours": total_hours
    }


# Compatibility function
def build_learning_path(
    employee_id,
    fiscal_year=2026
):

    return generate_learning_path(
        employee_id,
        fiscal_year
    )
