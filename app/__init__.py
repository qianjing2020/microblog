from flask import Flask
from configenv import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)  # create flask app

login = LoginManager(app) # create login extension 
login.login_view = 'login'

app.config.from_object(Config)

db = SQLAlchemy(app) # crate db object

migrate = Migrate(app, db) # create migrate engine


from app import routes, models