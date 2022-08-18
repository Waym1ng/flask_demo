from flask import blueprints

home_bp = blueprints.Blueprint("home", __name__)
from . import views
from . import login