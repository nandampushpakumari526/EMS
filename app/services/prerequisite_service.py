
from app.models import Prerequisite, Completion, Enrollment


def check_prerequisites(employee_id, course_id):

    prerequisites = Prerequisite.query.filter_by(
        course_id=course_id
    ).all()

    missing = []

    for prerequisite in prerequisites:

        completed = (
            Completion.query
            .join(Enrollment)
            .filter(
                Enrollment.employee_id == employee_id,
                Enrollment.course_id ==
                prerequisite.prerequisite_course_id,
                Completion.status == "completed"
            )
            .first()
        )

        if completed is None:

            missing.append({
                "course_id": prerequisite.prerequisite_course_id,
                "course_name": prerequisite.prerequisite_course.title
            })

    return {
        "eligible": len(missing) == 0,
        "missing_prerequisites": missing
    }
