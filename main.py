import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


from backend import app
from backend.help import start_debug
from backend.config import Config


start_debug()
# init_mail_messages()
if __name__ == '__main__' and not Config.HEROKU:
    app.run(host='0.0.0.0', port=8080)
