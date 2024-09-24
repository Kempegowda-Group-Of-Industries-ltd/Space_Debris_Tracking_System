# mongo_db.py
from pymongo import MongoClient
import os

# Connect to MongoDB
def get_db():
    client = MongoClient('mongodb://localhost:27017/')  # Adjust this if using a different MongoDB URI
    db = client['spacedebris']
    return db

# Load debris data from MongoDB
def load_debris_data():
    db = get_db()
    collection = db['debris']
    return list(collection.find({}))

# Insert initial debris data if the collection is empty
def insert_initial_data():
    db = get_db()
    collection = db['debris']
    
    if collection.count_documents({}) == 0:
        debris_data = [
            { "name": "Debris A", "size": 10, "mass": 500, "currentOrbit": "LEO", "trajectoryData": {}, "lastUpdated": "2024-01-01" },
            { "name": "Debris B", "size": 5, "mass": 300, "currentOrbit": "MEO", "trajectoryData": {}, "lastUpdated": "2024-01-01" }
        ]
        collection.insert_many(debris_data)
