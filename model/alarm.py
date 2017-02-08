from database.database import db


class AlarmType(db.Model):
    __tablename__ = 'alarm_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description


class Alarm(db.Model):
    __tablename__ = 'alarms'
    alarm_type_id = db.Column(db.Integer, db.ForeignKey('alarm_type.id'))
    alarm_type = db.relationship('AlarmType', backref=db.backref('alarm', lazy='dynamic'))
    alarmer_id = db.Column(db.Integer, db.ForeignKey('alarmers.id'))
    alarmer = db.relationship('Alarmer', backref=db.backref('alarm', lazy='dynamic'))
    latitude = db.Column(db.Float(9,6))
    longitude = db.Column(db.Float(9,6))

    def __init__(self, alarme_type=None, alarmer=None, latitude=None, longitude=None):
        self.alarm_type = alarme_type
        self.alarmer = alarmer
        self.latitude = latitude
        self.longitude = longitude
