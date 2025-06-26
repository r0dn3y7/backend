"""
SQLAlchemy models for My Home Workout backend.
"""

from datetime import datetime
from . import db

# ────────────────────────────────────────────────────────────────────────────────
# Association table: a user can complete many workouts,
#                    and a workout can be completed by many users
# ────────────────────────────────────────────────────────────────────────────────
class UserWorkout(db.Model):
    __tablename__ = "user_workouts"

    id         = db.Column(db.Integer, primary_key=True)
    status     = db.Column(db.String(20), default="started")  # started | completed
    timestamp  = db.Column(db.DateTime, default=datetime.utcnow)

    # foreign keys
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)

    # relationships (back-populate)
    user    = db.relationship("User", back_populates="user_workouts")
    workout = db.relationship("Workout", back_populates="user_workouts")

    def __repr__(self):
        return f"<UserWorkout user={self.user_id} workout={self.workout_id} status={self.status}>"


# ────────────────────────────────────────────────────────────────────────────────
# User model (for future authentication)
# ────────────────────────────────────────────────────────────────────────────────
class User(db.Model):
    __tablename__ = "users"

    id         = db.Column(db.Integer, primary_key=True)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(256), nullable=False)  # hashed w/ bcrypt
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    user_workouts = db.relationship(
        "UserWorkout",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email}>"


# ────────────────────────────────────────────────────────────────────────────────
# Workout model (matches seed.py expectations)
# ────────────────────────────────────────────────────────────────────────────────
class Workout(db.Model):
    __tablename__ = "workouts"

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)        # <-- changed field to name
    category    = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    duration    = db.Column(db.Integer)   # in minutes
    completed   = db.Column(db.Boolean, default=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    user_workouts = db.relationship(
        "UserWorkout",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Workout {self.name}>"
