
from flask import Blueprint, render_template

from app.services.course_service import (
    get_all_courses,
    get_course_details
)

bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/courses"
)


@bp.route("/")
def get_courses():

    courses = get_all_courses()

    return render_template(
        "courses/course_list.html",
        courses=courses
    )


@bp.route("/<int:course_id>")
def get_course(course_id):

    course = get_course_details(course_id)

    if course is None:
        return "Course not found", 404

    return render_template(
        "courses/course_detail.html",
        course=course
    )
