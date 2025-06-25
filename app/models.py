# app/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id         = db.Column(db.Integer, primary_key=True)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(256), nullable=False)   # bcrypt hash
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    user_workouts = db.relationship(
        "UserWorkout",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email}>"

class Workout(db.Model):
    __tablename__ = "workouts"

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(120), nullable=False)
    category    = db.Column(db.String(50), nullable=False)
    duration    = db.Column(db.String(50))
    description = db.Column(db.Text)

    user_workouts = db.relationship(
        "UserWorkout",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Workout {self.title}>"

class UserWorkout(db.Model):
    """
    Many-to-many join table with an extra `status` field.
    """
    __tablename__ = "user_workouts"

    id         = db.Column(db.Integer, primary_key=True)
    status     = db.Column(db.String(20), default="started")  # or 'completed'
    timestamp  = db.Column(db.DateTime, default=datetime.utcnow)

    # FKs
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)

    # backrefs
    user    = db.relationship("User", back_populates="user_workouts")
    workout = db.relationship("Workout", back_populates="user_workouts")

    def __repr__(self):
        return f"<UserWorkout user={self.user_id} workout={self.workout_id}>"
