from backend import app
from flask import render_template, request
from flask_cors import cross_origin
from .__help__ import get_user, send_query


TEMPLATE = 'courses.html'


@app.route("/courses", methods=['GET', 'POST'])
@cross_origin()
def courses():
    current_user = get_user(request)
    status, ans = send_query('courses', current_user.refresh)
    if status == 200:
        return render_template(TEMPLATE, cources=ans['courses'])


@app.route("/course/<course_id>")
@cross_origin()
def course(course_id: str):
    current_user = get_user(request)
    status, ans = send_query('courses/' + course_id, current_user.refresh)
    if status == 200:
        print(ans)
    return render_template(TEMPLATE)
