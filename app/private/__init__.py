from flask import Blueprint

private = Blueprint('private', __name__, template_folder='templatesPrivate')

from . import routes