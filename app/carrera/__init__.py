from flask import Blueprint

carrera = Blueprint('carrera', __name__, template_folder='templatesCarrera')

from . import routes