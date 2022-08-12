from flask import blueprints

show_bp = blueprints.Blueprint("show", __name__)
from . import views