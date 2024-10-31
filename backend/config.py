import os
from pymongo import MongoClient

def get_db_connection():
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client['taskmaster_db']
    return db
