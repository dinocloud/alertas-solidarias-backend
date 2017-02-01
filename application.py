from flask import jsonify, request
from werkzeug.exceptions import HTTPException
from database.database import create_app
from schemas import *
from views import *
import os

application = create_app()
from model import *

userSchema = UserSchema()
alarmerSchema = AlarmerSchema()

@application.errorhandler(404)
@application.errorhandler(403)
@application.errorhandler(400)
@application.errorhandler(409)
@application.errorhandler(500)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e.description), code=code), code

@application.route('/')
def home():
    return "You shouldn't be here!!!"

api_prefix = "/api/v1/"
AlarmersView.register(application, route_prefix=api_prefix)

if __name__ == '__main__':
    with application.app_context():
        db.create_all()
        application.run(port=int(os.getenv("APP_PORT", "5000")), debug=True)

