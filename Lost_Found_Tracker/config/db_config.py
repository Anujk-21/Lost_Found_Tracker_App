import os
from pymongo import MongoClient

def get_database():
    mongo_uri = os.getenv("MONGODB_URI")
    client = MongoClient(mongo_uri)
    return client["lost_found_db"]
