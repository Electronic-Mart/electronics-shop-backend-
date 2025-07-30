from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)
    phone = fields.Str()
    role = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
