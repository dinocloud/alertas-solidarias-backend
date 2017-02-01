from database.database import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = pwd_context.encrypt(password)


class Alarmer(db.Model):
    __tablename__ = 'alarmers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('alarmer', lazy='dynamic'))
    isOrg = db.Column(db.Boolean, unique=False, default=False)
    phone = db.Column(db.String(30))

    def __init__(self, name=None, last_name=None, email=None, user=None, isOrg=None, phone=None):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.user = user
        self.isOrg = isOrg
        self.phone = phone








