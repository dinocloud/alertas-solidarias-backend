from flask_classy import FlaskView
from flask import jsonify, request
from werkzeug.exceptions import Conflict, NotFound
from schemas import *
from model import *
from utils.validators import *

class AlarmersView(FlaskView):
    route_base = '/alarmers/'
    alarmer_schema = AlarmerSchema()
    model_instance = "Alarmer"

    def index(self):
        alarmers = Alarmer.query.order_by(Alarmer.last_name.desc())
        data = alarmer_schema.dump(alarmers, many=True).data
        return jsonify(data)

    def get(self, id):
        try:
            alarmer = Alarmer.query.get_or_404(int(id))
        except NotFound:
            raise NotFound("Alarmer not found")
            # return jsonify({"message": "Alarmer not found"}), 404
        data = alarmer_schema.dump(alarmer).data
        return jsonify(data)

    def post(self):
        data = request.json
        data, errors = alarmer_schema.load(data)
        if errors:
            return jsonify(errors), 422
        username = data['user']['username'], data['user']['password']
        user = User.query.filter_by(username=username).first()
        if user is None:
            # Create user
            user = User(
                username=username,
                password=password
            )
        else:
            raise Conflict("Username already exists in database")
        alarmer = Alarmer(
            last_name=data['last_name'],
            name=data['name'],
            email=validate_param("email", data['email'], [(TYPE_VALIDATOR, unicode), (REGEX_VALIDATOR, EMAIL_REGEX)], True),
            user=user,
            isOrg=data['isOrg'],
            phone=data['phone']
        )
        db.session.add(user)
        db.session.add(alarmer)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return jsonify(self.alarmer_schema.dump(alarmer).data), 201

    def put(self, id):
        try:
            alarmer = Alarmer.query.get_or_404(int(id))
        except NotFound:
            raise NotFound("Alarmer not found")
        json_data = request.json
        if not json_data:
            return jsonify({"message": "No data provided in the request"}), 400
        alarmer.name = validate_param("name", json_data['name'], [(TYPE_VALIDATOR, unicode)], True)
        alarmer.last_name = validate_param("last_name", json_data['last_name'], [(TYPE_VALIDATOR, unicode)], True)
        alarmer.email = validate_param(
            "email",
            json_data['email'],
            [(TYPE_VALIDATOR, unicode), (REGEX_VALIDATOR, EMAIL_REGEX)]
        )
        alarmer.phone = validate_param("phone", json_data['phone'], [(TYPE_VALIDATOR, unicode)])
        db.session.merge(alarmer)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return jsonify({"message":"Alarmer updated", "alarmer": alarmer_schema.dump(alarmer).data}), 200

