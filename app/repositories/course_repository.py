
from flask import Blueprint, render_template
from app import db

from app.repositories import course_repository
from app.models import Course
from app.models import CourseSkill
from app.models import Prerequisite


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


def get_active_courses():

    courses = Course.query.filter_by(
        status="active"
    ).order_by(
        Course.id
    ).all()

    return courses

def get_course_by_id(course_id):

    course = db.session.get(
        Course,
        course_id
    )

    return course


# ==================================
# GET COURSE SKILLS
# ==================================

def get_course_skills(course_id):

    course_skills = CourseSkill.query.filter_by(
        course_id=course_id
    ).all()

    return course_skills


# ==================================
# GET COURSE PREREQUISITES
# ==================================

def get_course_prerequisites(course_id):

    prerequisites = Prerequisite.query.filter_by(
        course_id=course_id
    ).all()

    return prerequisites

def get_all_courses():
    return Course.query.order_by(Course.id).all()


def get_active_courses():
    return Course.query.filter_by(status="active").order_by(Course.id).all()


def get_course_by_id(course_id):
    return db.session.get(Course, course_id)
