
from app.services.recommendation_service import recommend_courses


def generate_learning_path(
    employee_id,
    fiscal_year=2026
):

    # Step 1: Get course recommendations
    recommendations = recommend_courses(
        employee_id,
        fiscal_year
    )

    print("EMPLOYEE ID:", employee_id)

    print("ALL RECOMMENDATIONS:", recommendations)

    # Step 2: Handle missing recommendations
    if recommendations is None:
        return None

    # Step 3: Keep eligible courses
    eligible_courses = []

    for recommendation in recommendations:

        prerequisites_met = recommendation.get(
            "prerequisites_met",
            False
        )

        budget_available = recommendation.get(
            "budget_available",
            False
        )

        print(
            "COURSE:",
            recommendation.get("course_name")
        )

        print(
            "PREREQUISITES:",
            prerequisites_met
        )

        print(
            "BUDGET:",
            budget_available
        )

        if prerequisites_met and budget_available:

            eligible_courses.append(
                recommendation
            )

    print("ELIGIBLE COURSES:", eligible_courses)

    # Step 4: Sort by skill gap
    eligible_courses.sort(
        key=lambda item: item.get("gap", 0),
        reverse=True
    )

    # Step 5: Calculate total cost
    total_cost = sum(
        item.get("cost", 0)
        for item in eligible_courses
    )

    # Step 6: Calculate total duration
    total_hours = sum(
        item.get("duration_hours", 0)
        for item in eligible_courses
    )

    # Step 7: Return learning path
    return {

        "employee_id": employee_id,

        "fiscal_year": fiscal_year,

        "courses": eligible_courses,

        "total_courses": len(
            eligible_courses
        ),

        "total_cost": total_cost,

        "total_duration_hours": total_hours

    }


def build_learning_path(
    employee_id,
    fiscal_year=2026
):

    return generate_learning_path(
        employee_id,
        fiscal_year
    )
