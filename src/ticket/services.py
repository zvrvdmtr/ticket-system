from typing import Dict

from .models import Comment, Ticket


DEFAULT_STATUS = 'OPEN'

STATUSES = {
    'OPEN': ['ANSWERED', 'CLOSED'],
    'ANSWERED': ['AWAITING REPLY', 'CLOSED'],
    'AWAITING REPLY': ['ANSWERED'],
    'CLOSED': [],
}


def _is_transition_valid(transition_from: str, transition_to: str) -> bool:
    if transition_to in STATUSES[transition_from]:
        return True
    return False


def create_new_ticket(**kwargs) -> Dict:
    ticket = Ticket.create_ticket(**kwargs)
    if not ticket:
        return {}
    return ticket.serialize()


def get_ticket_by_id(ticket_id: str) -> Dict:
    ticket = Ticket.get_by_id(ticket_id)
    if not ticket:
        return {}
    return ticket.serialize()


def transition_ticket_status(ticket_id: str, transition_to: str) -> bool:
    ticket = Ticket.get_by_id(ticket_id)
    if not ticket:
        return False

    if not _is_transition_valid(ticket.status, transition_to):
        return False

    return ticket.update_status(transition_to)


def create_new_comment(ticket_id: str, **kwargs) -> Dict:
    ticket = Ticket.get_by_id(ticket_id)
    if not ticket:
        return {}
    kwargs['ticket_id'] = ticket.id
    comment = Comment.create_comment(**kwargs)
    return comment.serialize()
