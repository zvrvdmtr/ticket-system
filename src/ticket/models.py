from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func

from src.app import db


class Ticket(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())
    subject = db.Column(db.String, nullable=False, unique=True)
    text = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    status = db.Column(db.String, default='OPEN', nullable=False)
    comment = db.relationship("Comment", backref='comment', lazy=True)

    @classmethod
    def create_ticket(cls, **kwargs):
        ticket = Ticket(**kwargs)
        db.session.add(ticket)
        try:
            db.session.commit()
        except IntegrityError:
            return {}
        return ticket

    @classmethod
    def get_by_id(cls, ticket_id):
        ticket = Ticket.query.get(ticket_id)
        return ticket

    def update_status(self, transition_to):
        self.status = transition_to
        db.session.commit()
        return self

    def serialize(self):
        return {
            'id': self.id,
            'created': str(self.created),
            'updated': str(self.updated),
            'subject': self.subject,
            'text': self.text,
            'email': self.email,
            'status': self.status,
            'comments': [comment.serialize() for comment in self.comment]
        }


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey(Ticket.id))
    created = db.Column(db.DateTime, default=func.now())
    email = db.Column(db.String)
    text = db.Column(db.String, nullable=False)

    @classmethod
    def create_comment(cls, **kwargs):
        comment = Comment(**kwargs)
        db.session.add(comment)
        db.session.commit()
        return comment

    def serialize(self):
        return {
            'id': self.id,
            'ticket_id': self.ticket_id,
            'created': str(self.created),
            'email': self.email,
            'text': self.text,
        }
