import os


class Config:
    UPLOAD_FOLDER = 'backend/static'
    TEMPLATES_FOLDER = 'backend/templates'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'html', 'docx'}
    SECRET_KEY = os.getenv('ALL_SECRET_KEY')
    TEMPLATES_AUTO_RELOAD = True

    HEROKU = True if os.getenv('HEROKU') else False
    HOST = 'http://iti106.pythonanywhere.com/'
