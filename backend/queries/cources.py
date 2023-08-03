from backend import app
from flask import render_template, request
from flask_cors import cross_origin
from .__help__ import get_user, send_query


TEMPLATE = 'cources.html'


@app.route("/cources", methods=['GET', 'POST'])
@cross_origin()
def cources():
    current_user = get_user(request)
    print(current_user.info)
    status, ans = send_query('courses', current_user.refresh)
    print(ans)
    if status == 200:
        return render_template(TEMPLATE, cources=ans['courses'])
