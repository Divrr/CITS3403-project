from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# from app.test_data import initialise_test_database
# initialise_test_database() # Comment this out to stop resetting your database

from app import routes, models