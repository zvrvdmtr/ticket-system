from flask import request
from marshmallow import ValidationError

from . import ticket
from .schemas import CommentSchema, TicketSchema
from .services import (
    create_new_comment,
    create_new_ticket,
    get_ticket_by_id,
    transition_ticket_status,
)


@ticket.route('/ping')
def ping():
    return 'Pong'


@ticket.route('/ticket', methods=['POST'])
def create_ticket():
    try:
        result = TicketSchema().loads(request.data.decode())
    except ValidationError:
        return 'Invalid query body.', 400

    new_ticket = create_new_ticket(**result)
    if not new_ticket:
        return 'Invalid data.', 422

    return new_ticket, 201


@ticket.route('/ticket/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = get_ticket_by_id(ticket_id)
    if not ticket:
        return 'Not Found', 404

    return ticket, 200


@ticket.route('/ticket/<int:ticket_id>/status', methods=['PATCH'])
def change_status(ticket_id):
    body = request.get_json()
    if not isinstance(body, dict):
        return 'Invalid query body.', 400

    status = body.get("status")
    if not status:
        return 'Invalid query body.', 400

    if not transition_ticket_status(ticket_id, status):
        return f"Can't change status to '{status}'", 400

    return "", 204


@ticket.route('/ticket/<int:ticket_id>/comment', methods=['POST'])
def comment(ticket_id):
    try:
        result = CommentSchema().loads(request.data.decode())
    except ValidationError:
        return 'Invalid query body.', 400

    new_commentary = create_new_comment(ticket_id, **result)

    if not new_commentary:
        return 'Not Found', 404

    return new_commentary, 201
