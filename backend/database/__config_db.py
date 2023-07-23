import os
from ..config import Config


class ConfigDB:
    DB = os.getenv('DATABASE_URL') if Config.HEROKU else 'backend/database.db'
