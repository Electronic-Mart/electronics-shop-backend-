from marshmallow import Schema, fields

class OrderItemSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(dump_only=True)
    product = fields.Nested('ProductSchema', dump_only=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    total = fields.Float(dump_only=True)
    address = fields.Str(required=True)
    billing_info = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    items = fields.List(fields.Nested(OrderItemSchema))
