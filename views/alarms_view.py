from flask_classy import FlaskView
from flask import jsonify, request
from werkzeug.exceptions import Conflict, NotFound
from schemas import *
from model import *
from utils.validators import *

class AlarmTypeView(FlaskView):
    route_base = '/alarmType/'
    alarm_type_schema = AlarmTypeSchema()

    def index(self):
        alarm_types = AlarmType.query()
        data = alarm_type_schema.dump(alarm_types, many=True).data
        return jsonify(data)

    def get(self, id):
        try:
            alarm_type = AlarmType.query.get_or_404(int(id))
        except NotFound:
            raise NotFound("Alarm type not found")
        return jsonify(alarm_type_schema.dump(alarm_type).data)

    def post:
        return None

    def put:
        return None

class AlarmView(FlaskView):
    route_base = '/alarm/'
    alarm_schema = AlarmSchema()

    def index(self):
        alarms = Alarm.query()
        data = alarm_schema.dump(alarms, many=True).data
        return jsonify(data)

    def get(self, id):
        try:
            alarm = Alarm.query.get_or_404(int(id))
        except NotFound:
            raise NotFound("Alarm not found")
        data = alarm_schema.dump(alarm).data
        return jsonify(data)

    def post(self):
        data = request.json
        data, errors = alarm_schema.load(data)
        if errors:
            return jsonify(errors), 422
        alarm = Alarm(
            latitude=data['latitude'],
            longitude=data['longitude'],
            alarmer=Alarmer.query.get(int(data['alarmer']['id'])),
            alarm_type=AlarmType.query.get(int(data['alarm_type']['id']))
        )
        db.session.add(alarm)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return jsonify(self.alarm_schema.dump(alarm).data), 201

    def put(self, id):
        try:
            alarm = Alarm.query.get_or_404(int(id))
        except NotFound:
            raise NotFound("Alarm not found")
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

