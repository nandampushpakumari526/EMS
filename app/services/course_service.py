
from app.models import Course, CourseSkill


def get_all_courses():

    return Course.query.filter_by(
        status="active"
    ).all()


def get_course_by_id(course_id):

    return Course.query.get(course_id)


def search_courses(skill_id):

    return (
        Course.query
        .join(CourseSkill)
        .filter(
            CourseSkill.skill_id == skill_id,
            Course.status == "active"
        )
        .all()
    )


def get_course_details(course_id):

    course = get_course_by_id(course_id)

    if course is None:
        return None

    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "duration_hours": course.duration_hours,
        "cost": course.cost,
        "difficulty_level": course.difficulty_level,
        "provider": course.provider
    }
