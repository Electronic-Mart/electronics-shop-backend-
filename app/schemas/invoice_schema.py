from marshmallow import Schema, fields

class InvoiceSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(dump_only=True)
    invoice_number = fields.Str()
    issued_date = fields.DateTime()
    amount = fields.Float()
