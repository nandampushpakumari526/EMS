from app.models import (
    Course,
    CourseSkill
)

from app.services.skill_gap_service import (
    calculate_skill_gaps
)

from app.services.prerequisite_service import (
    check_prerequisites
)

from app.services.budget_service import (
    check_budget
)


def recommend_courses(employee_id):

    gaps = calculate_skill_gaps(
        employee_id
    )

    gap_skill_ids = []

    for gap in gaps:

        gap_skill_ids.append(
            gap["skill_id"]
        )

    courses = Course.query.all()

    recommendations = []

    for course in courses:

        mappings = CourseSkill.query.filter_by(
            course_id=course.id
        ).all()

        matched_skills = []

        for mapping in mappings:

            if mapping.skill_id in gap_skill_ids:

                matched_skills.append(
                    mapping.skill_id
                )

        if len(matched_skills) == 0:

            continue

        eligible = check_prerequisites(
            employee_id,
            course.id
        )

        affordable = check_budget(
            course.cost
        )

        recommendations.append({

            "course": course,

            "matched_skills": matched_skills,

            "eligible": eligible,

            "affordable": affordable

        })

    return recommendations