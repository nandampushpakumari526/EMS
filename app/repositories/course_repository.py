
from flask import Blueprint, render_template

from app.repositories import course_repository


bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/courses"
)


# --------------------------------
# Course List
# --------------------------------

@bp.route("/")
def get_courses():

    courses = course_repository.get_active_courses()

    return render_template(
        "courses/course_list.html",
        courses=courses
    )


# --------------------------------
# Course Details
# --------------------------------

@bp.route("/<int:course_id>")
def get_course(course_id):

    course = course_repository.get_course_by_id(
        course_id
    )

    if course is None:
        return "Course not found", 404

    course_skills = course_repository.get_course_skills(
        course_id
    )

    prerequisites = (
        course_repository.get_course_prerequisites(
            course_id
        )
    )

    return render_template(
        "courses/course_detail.html",
        course=course,
        course_skills=course_skills,
        prerequisites=prerequisites
    )
