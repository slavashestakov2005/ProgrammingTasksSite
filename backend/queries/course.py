from backend import app
from flask import render_template, request
from flask_cors import cross_origin
from .__help__ import get_user, send_query, send_simple_query


TEMPLATE = 'course.html'


@app.route("/course")
@cross_origin()
def course():
    course_id = request.args.get('course_id')
    current_user = get_user(request)
    if current_user.is_authenticated:
        status, ans = send_query('courses/' + course_id, current_user.refresh)
        if status == 200:
            print(ans)
            return render_template(TEMPLATE, course=ans)
    else:
        status, ans = send_simple_query('courses/' + course_id)
        if status == 200:
            print(ans)
            return render_template(TEMPLATE, course=ans)
    return render_template(TEMPLATE)
