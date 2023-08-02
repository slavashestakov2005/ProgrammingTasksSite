from backend import app
from flask import render_template
from flask_cors import cross_origin

TEMPLATE = 'cource.html'


@app.route("/cource", methods=['GET', 'POST'])
@cross_origin()
def cource():
    data = [("gggggggg", "ссылка"), ("как не приручить python'а", "ссылка")]
    return render_template(TEMPLATE, cources=data)
