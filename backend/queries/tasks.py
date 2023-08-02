from backend import app
from flask import render_template, request
from flask_cors import cross_origin

TEMPLATE = 'tasks.html'


@app.route("/tasks", methods=['GET', 'POST'])
@cross_origin()
def task():
    lesson_id = request.args.get('lesson_id')
    data = [("задание не приручать python'a", "ссылка"), ("задание приручить python'а", "ссылка")]
    date = [("задание не приручать python'a", "ссылка"), ("задание приручить python'а", "ссылка")]
    return render_template(TEMPLATE, tasks=data, hrefs=date)


TEMPLATE_v2 = 'tasks_v2.html'


@app.route("/tasks_v2", methods=['GET', 'POST'])
@cross_origin()
def tasks_v2():
    tasks = [['Hello World', '31.07.2023'], ['A + B', '01.08.2023']]
    return render_template(TEMPLATE_v2, tasks=tasks)

