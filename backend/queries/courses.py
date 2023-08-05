from backend import app
from flask import render_template, request
from flask_cors import cross_origin
from .__help__ import get_user, send_query, send_simple_query


TEMPLATE = 'index.html'


@app.route("/")
@app.route("/courses")
@cross_origin()
def courses():
    error_login = request.args.get('error_login')
    error_reg = request.args.get('error_reg')
    current_user = get_user(request)
    if current_user.is_authenticated:
        status, ans = send_query('courses', current_user.refresh)
        if status == 200:
            return render_template(TEMPLATE, courses=ans['courses'], error_login=error_login, error_reg=error_reg)
    else:
        status, ans = send_simple_query('courses')
        if status == 200:
            return render_template(TEMPLATE, courses=ans['courses'], error_login=error_login, error_reg=error_reg)
    return render_template(TEMPLATE, courses=[], error_login=error_login, error_reg=error_reg)
