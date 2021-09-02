from marshmallow import EXCLUDE, Schema, fields


class TicketSchema(Schema):
    subject = fields.String(required=True)
    text = fields.String(required=True)
    email = fields.String()

    class Meta:
        unknown = EXCLUDE


class CommentSchema(Schema):
    text = fields.String(required=True)
    email = fields.String()

    class Meta:
        unknown = EXCLUDE
