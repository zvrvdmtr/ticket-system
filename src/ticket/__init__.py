from flask import Blueprint


ticket = Blueprint('api', __name__, url_prefix='/api/v1')

from . import handlers  # noqa
