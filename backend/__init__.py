from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from .config import Config


app = Flask(__name__)
CORS(app)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)


from . import queries
from . import database
from . import help
