from flask import Blueprint

kmvertical = Blueprint('kmvertical', __name__, template_folder='templatesKmVertical')

from . import routes