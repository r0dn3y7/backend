# app/routes/workout_routes.py
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.models import db, Workout
from . import api

@api.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify([
        {
            "id": w.id,
            "title": w.title,
            "category": w.category,
            "duration": w.duration,
            "description": w.description
        }
        for w in workouts
    ]), 200

@api.route("/workouts", methods=["POST"])
@jwt_required()
def create_workout():
    data = request.get_json()
    new_w = Workout(
        title=data.get("title"),
        category=data.get("category"),
        duration=data.get("duration"),
        description=data.get("description")
    )
    db.session.add(new_w)
    db.session.commit()
    return jsonify({"message": "Workout created!", "workout_id": new_w.id}), 201
