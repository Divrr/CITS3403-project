from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def create_app(config):
    flaskApp = Flask(__name__)
    flaskApp.config.from_object(config)

    from app.blueprints import main
    flaskApp.register_blueprint(main)
    db.init_app(flaskApp)
    login.init_app(flaskApp)

    return flaskApp

login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'

csrf = CSRFProtect()
csrf.init_app(app)

from app.test_data import initialise_test_database
initialise_test_database()  # this is temporary!

from app import routes, models