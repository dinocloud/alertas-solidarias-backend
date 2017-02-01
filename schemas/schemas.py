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

user_schema = UserSchema()
users_schema = UserSchema(many=True, only=('id', 'username'))
alarmer_schema = AlarmerSchema()
alarmers_schema = AlarmerSchema(many=True)


