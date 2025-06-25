# app/routes/__init__.py
from flask import Blueprint

api = Blueprint("api", __name__)

# Import *after* blueprint so each file can use `from . import api`
from . import auth_routes
from . import user_routes
from . import workout_routes
