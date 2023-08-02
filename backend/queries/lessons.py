from backend import app
from flask import render_template, request
from flask_cors import cross_origin

TEMPLATE = 'lesson.html'


@app.route("/lesson", methods=['GET', 'POST'])
@cross_origin()
def lesson():
    cource_id = request.args.get('cource_id')
    data = [("урок не приручать python'a", "ссылка"), ("урок приручить python'а", "ссылка")]
    discr = 'курс по питhony'
    return render_template(TEMPLATE, lessons=data, discription=discr)
