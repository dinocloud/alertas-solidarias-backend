from flask import jsonify, request
from database.database import create_app, db
from utils import *
import os

from utils.settings import DBSettings

application = create_app()
from model import *

@application.route("/refreshdb")
def refresh_db():
    with application.app_context():
        db.create_all()

@application.route('/')
def home():
    return "Hello, {0}".format(DBSettings.SQLALCHEMY_DATABASE_URI)

if __name__ == '__main__':
    with application.app_context():
        db.create_all()
        db.session.commit()
        application.run(port=int(os.getenv("APP_PORT", "5000")), debug=True)

