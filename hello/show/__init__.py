from flask import blueprints

show_bp = blueprints.Blueprint("show", __name__, url_prefix="/show")
from . import views
