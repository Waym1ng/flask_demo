from flask import blueprints

user_bp = blueprints.Blueprint("user", __name__, url_prefix="/user")
from . import views