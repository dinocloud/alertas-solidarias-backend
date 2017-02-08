from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str()
    enabled = fields.Bool()

class AlarmerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    user = fields.Nested(UserSchema)
    isOrg = fields.Boolean()
    phone = fields.Str()

class AlarmTypeSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()

class AlarmSchema(Schema):
    id = fields.Int()
    description = fields.Int()
    alarm_type = fields.Nested(AlarmTypeSchema)
    alarmer = fields.Nested(AlarmerSchema)
    latitude = fields.Float()
    longitude = fields.Float()

user_schema = UserSchema()
users_schema = UserSchema(many=True, only=('id', 'username'))
alarmer_schema = AlarmerSchema()
alarmers_schema = AlarmerSchema(many=True)
alarm_type_schema = AlarmTypeSchema()
alarm_types_schema = AlarmTypeSchema(many=True)
alarm_schema = AlarmSchema()
alarms_schema = AlarmSchema(many=True)


