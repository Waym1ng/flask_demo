from flask import blueprints

msg_bp = blueprints.Blueprint("msg", __name__, url_prefix="/msg")
from . import views