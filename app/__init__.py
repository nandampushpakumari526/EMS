
# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# from app.config import Config

# db = SQLAlchemy()


# def create_app():

#     app = Flask(__name__)

#     app.config.from_object(Config)

#     db.init_app(app)

#     # Home page route
#     @app.route("/")
#     def home():
#         return render_template("dashboard.html")

#     # Import controllers
#     from app.controllers.employee_controller import bp as employee_bp
#     from app.controllers.skill_controller import bp as skill_bp
#     from app.controllers.course_controller import bp as course_bp
#     from app.controllers.recommendation_controller import bp as recommendation_bp
#     from app.controllers.enrollment_controller import bp as enrollment_bp
#     from app.controllers.report_controller import bp as report_bp

#     # Register blueprints
#     app.register_blueprint(employee_bp)
#     app.register_blueprint(skill_bp)
#     app.register_blueprint(course_bp)
#     app.register_blueprint(recommendation_bp)
#     app.register_blueprint(enrollment_bp)
#     app.register_blueprint(report_bp)

#     # Database initialization
#     with app.app_context():

#         from app import models
#         from app.models import seed_demo

#         db.create_all()

#         seed_demo()

#     return app

from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy

from app.config import Config



db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
     # Home page route
    @app.route("/")
    def home():
        return render_template("dashboard.html")


    # Import Controllers

    from app.controllers.ui_controller import ui_bp

    from app.controllers.employee_controller import bp as employee_bp

    from app.controllers.skill_controller import bp as skill_bp

    from app.controllers.course_controller import bp as course_bp

    from app.controllers.recommendation_controller import bp as recommendation_bp

    from app.controllers.enrollment_controller import bp as enrollment_bp

    from app.controllers.report_controller import bp as report_bp


    # Register Blueprints

    app.register_blueprint(ui_bp)

    app.register_blueprint(employee_bp)

    app.register_blueprint(skill_bp)

    app.register_blueprint(course_bp)

    app.register_blueprint(recommendation_bp)

    app.register_blueprint(enrollment_bp)

    app.register_blueprint(report_bp)


    # Database Initialization

    with app.app_context():

        from app import models

        from app.models import seed_demo

        db.create_all()

        seed_demo()


    return app
