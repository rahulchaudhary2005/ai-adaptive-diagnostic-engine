import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["adaptive_engine"]

questions_collection = db["questions"]

with open("data/seed_questions.json") as f:
    questions = json.load(f)

questions_collection.insert_many(questions)

print("Questions inserted successfully!")