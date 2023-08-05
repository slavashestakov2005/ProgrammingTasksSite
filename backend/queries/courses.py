from backend import app
from flask import render_template, request
from flask_cors import cross_origin
from .__help__ import get_user, send_query, send_simple_query


TEMPLATE = 'index.html'


@app.route("/")
@app.route("/courses")
@cross_origin()
def courses():
    current_user = get_user(request)
    if current_user.is_authenticated:
        status, ans = send_query('courses', current_user.refresh)
        if status == 200:
            return render_template(TEMPLATE, courses=ans['courses'])
    else:
        status, ans = send_simple_query('courses')
        if status == 200:
            return render_template(TEMPLATE, courses=ans['courses'])
    return render_template(TEMPLATE, courses=[])
