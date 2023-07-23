import os


class ConfigMail:
    EMAIL = ''
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = EMAIL
    MAIL_PASSWORD = os.getenv('HELP_MAIL_PASS')
    ADMINS = [EMAIL]
    TITLE = 'Ошибка на сайте задач по программированию'
