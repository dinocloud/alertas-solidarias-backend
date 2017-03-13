from flask_classy import FlaskView
from flask import jsonify, request
from werkzeug.exceptions import Conflict, NotFound
from schemas import *
from model import *
from utils.validators import *


class UsersView(FlaskView):
    route_base = '/users/'
    user_schema = UserSchema()
    model_instance = "User"

    def index(self):
        alarmers = Alarmer.query.order_by(Alarmer.last_name.desc())
        data = alarmer_schema.dump(alarmers, many=True).data
        return jsonify(data)

    def get(self, username):
        try:
            user = User.query.filter(User.username == str(username))
        except NotFound:
            raise NotFound("User not found")
        data = user_schema.dump(user).data
        return jsonify(data)


