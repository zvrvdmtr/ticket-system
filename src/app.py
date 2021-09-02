import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


DATABASE_URI = 'postgresql://postgres:postgres@postgres:5432/postgres'


db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
    app = Flask('Ticket')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI", default=DATABASE_URI)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from src.ticket import ticket
    app.register_blueprint(ticket)
    db.init_app(app)
    migrate.init_app(app, db)
    return app
