
from app.models import Budget


def check_budget(department, fiscal_year, course_cost):

    budget = Budget.query.filter_by(
        department=department,
        fiscal_year=fiscal_year
    ).first()

    if budget is None:

        return {
            "eligible": False,
            "message": "Department budget not found",
            "remaining_amount": 0
        }

    remaining = (
        budget.total_amount - budget.spent_amount
    )

    if course_cost <= remaining:

        return {
            "eligible": True,
            "message": "Budget available",
            "remaining_amount": remaining
        }

    return {
        "eligible": False,
        "message": "Insufficient budget",
        "remaining_amount": remaining
    }
