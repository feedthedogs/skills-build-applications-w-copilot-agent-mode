from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Directly insert users into MongoDB
        print("Inserting users into MongoDB...")
        db.users.insert_many([
            {"_id": str(ObjectId()), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": str(ObjectId()), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": str(ObjectId()), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": str(ObjectId()), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": str(ObjectId()), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ])

        # Directly insert teams into MongoDB
        print("Inserting teams into MongoDB...")
        db.teams.insert_many([
            {"_id": str(ObjectId()), "name": "Blue Team", "members": []},
            {"_id": str(ObjectId()), "name": "Gold Team", "members": []},
        ])

        # Directly insert activities into MongoDB
        print("Inserting activities into MongoDB...")
        db.activity.insert_many([
            {"_id": str(ObjectId()), "user": "thundergod", "activity_type": "Cycling", "duration": "1:00:00"},
            {"_id": str(ObjectId()), "user": "metalgeek", "activity_type": "Crossfit", "duration": "2:00:00"},
            {"_id": str(ObjectId()), "user": "zerocool", "activity_type": "Running", "duration": "1:30:00"},
            {"_id": str(ObjectId()), "user": "crashoverride", "activity_type": "Strength", "duration": "0:30:00"},
            {"_id": str(ObjectId()), "user": "sleeptoken", "activity_type": "Swimming", "duration": "1:15:00"},
        ])

        # Directly insert leaderboard entries into MongoDB
        print("Inserting leaderboard entries into MongoDB...")
        db.leaderboard.insert_many([
            {"_id": str(ObjectId()), "user": "thundergod", "score": 100},
            {"_id": str(ObjectId()), "user": "metalgeek", "score": 90},
            {"_id": str(ObjectId()), "user": "zerocool", "score": 95},
            {"_id": str(ObjectId()), "user": "crashoverride", "score": 85},
            {"_id": str(ObjectId()), "user": "sleeptoken", "score": 80},
        ])

        # Directly insert workouts into MongoDB
        print("Inserting workouts into MongoDB...")
        db.workouts.insert_many([
            {"_id": str(ObjectId()), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": str(ObjectId()), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": str(ObjectId()), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": str(ObjectId()), "name": "Strength Training", "description": "Training for strength"},
            {"_id": str(ObjectId()), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
