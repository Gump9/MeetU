from flask import Blueprint

course_bp = Blueprint('course',__name__,url_prefix='/course')


@course_bp.route('/list')
def course_list():
    return '课程列表'