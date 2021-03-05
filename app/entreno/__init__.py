from flask import Blueprint

entreno = Blueprint('entreno', __name__, template_folder='templatesEntreno')

from . import routes