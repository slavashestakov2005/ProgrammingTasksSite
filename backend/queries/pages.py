from flask import render_template
from flask_cors import cross_origin
from jinja2 import TemplateNotFound
from backend import app
from ..help.errors import not_found_error


@app.route("/")
@cross_origin()
def main_page():
    return render_template('login.html')


@app.route('/<path:path>')
@cross_origin()
def static_file(path):
    try:
        return render_template(path)
    except TemplateNotFound:
        pass
    try:
        return app.send_static_file(path)
    except Exception:
        return not_found_error()
