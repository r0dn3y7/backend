# seed.py
"""
Seed the database with sample workouts.
Run with: pipenv run python seed.py
"""

from app import app, db
from app.models import Workout

sample_workouts = [
    {
        "name": "Push-Up Blast",
        "category": "Upper Body",
        "description": "3 sets of 15 push-ups. Rest 60 s between sets.",
        "duration": 10,
    },
    {
        "name": "Leg Day Burner",
        "category": "Lower Body",
        "description": "4 sets of 20 body-weight squats.",
        "duration": 15,
    },
    {
        "name": "Core Crusher",
        "category": "Core",
        "description": "3 sets of 60-second plank holds.",
        "duration": 8,
    },
    {
        "name": "HIIT Cardio",
        "category": "Cardio",
        "description": "5 rounds: 30 s high knees / 30 s rest.",
        "duration": 12,
    },
    {
        "name": "Yoga Stretch",
        "category": "Flexibility",
        "description": "Sun-salutation flow for overall mobility.",
        "duration": 20,
    },
]

def seed():
    with app.app_context():
        # Drop & recreate tables (CAUTION: wipes data!)
        db.drop_all()
        db.create_all()

        workouts = [Workout(**w) for w in sample_workouts]
        db.session.bulk_save_objects(workouts)
        db.session.commit()
        print(f"Seeded {len(workouts)} workouts!")


if __name__ == "__main__":
    seed()
