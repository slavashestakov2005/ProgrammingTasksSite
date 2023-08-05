from backend import app
from flask import render_template, request, redirect
from flask_cors import cross_origin
from .__help__ import get_user, send_query, send_simple_query


TEMPLATE = 'task.html'


@app.route("/task")
@cross_origin()
def task():
    task_id = request.args.get('task_id')
    lesson_id = request.args.get('lesson_id')
    course_id = request.args.get('course_id')
    args = {'task_id': task_id, 'lesson_id': lesson_id, 'course_id': course_id}
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
    solves = []
    try:
        status, ans = send_query('tasks/{}/solves'.format(task_id), current_user.refresh)
        if status == 200:
            solves = ans['solves']
    except Exception:
        pass
    return render_template(TEMPLATE, task=true_task, **args, solves=solves)


@app.route("/solve_task", methods=['POST'])
@cross_origin()
def solve_task():
    task_id = request.args.get('task_id')
    lesson_id = request.args.get('lesson_id')
    course_id = request.args.get('course_id')
    current_user = get_user(request)
    code = request.form['code']
    send_query('tasks/' + task_id, current_user.refresh, {'code': code}, 'POST')
    return redirect('task?task_id={}&lesson_id={}&course_id={}'.format(task_id, lesson_id, course_id))
