from flask import Blueprint

public = Blueprint('public', __name__, template_folder='templatesPublic')

from . import routes