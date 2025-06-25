# app/routes/user_routes.py
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from . import api

@api.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify(
        id=user.id,
        email=user.email,
        joined=user.created_at.strftime("%Y-%m-%d")
    ), 200
