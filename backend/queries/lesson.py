from backend import app
from flask import render_template, request
from flask_cors import cross_origin
from .__help__ import get_user, send_query, send_simple_query


TEMPLATE = 'lesson.html'


@app.route("/lesson")
@cross_origin()
def lesson():
    lesson_id = request.args.get('lesson_id')
    course_id = request.args.get('course_id')
    current_user = get_user(request)
    if current_user.is_authenticated:
        status, ans = send_query('lessons/' + lesson_id, current_user.refresh)
        if status == 200:
            print(ans)
            return render_template(TEMPLATE, lesson=ans, course_id=course_id)
    else:
        status, ans = send_simple_query('courses/' + lesson_id)
        if status == 200:
            return render_template(TEMPLATE, lesson=ans, course_id=course_id)
    return render_template(TEMPLATE, course_id=course_id)
