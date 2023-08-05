from backend import app
from flask import render_template, request
from flask_cors import cross_origin
from .__help__ import get_user, send_query, send_simple_query


TEMPLATE = 'task.html'


@app.route("/task")
@cross_origin()
def task():
    task_id = request.args.get('task_id')
    lesson_id = request.args.get('lesson_id')
    course_id = request.args.get('course_id')
    current_user = get_user(request)
    true_task = {}
    if current_user.is_authenticated:
        status, ans = send_query('lessons/' + lesson_id, current_user.refresh)
        if status == 200:
            for task in ans['tasks']:
                if task['id'] == task_id:
                    true_task = task
    else:
        status, ans = send_query('lessons/' + lesson_id, current_user.refresh)
        if status == 200:
            for task in ans['tasks']:
                if task['id'] == task_id:
                    true_task = task
    print(true_task)
    return render_template(TEMPLATE, task=true_task)
