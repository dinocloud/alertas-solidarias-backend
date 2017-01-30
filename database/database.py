from sqlalchemy import create_engine
from utils.settings import DBSettings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    return engine

def create_app():
    application = Flask(__name__)
    application.config.from_object(DBSettings)
    init_engine(application.config['SQLALCHEMY_DATABASE_URI'])
    db = SQLAlchemy()
    db.init_app(application)
    return application


