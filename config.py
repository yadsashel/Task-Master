from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    # Use the environment variable for MongoDB URI
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise ValueError("MONGODB_URI not set in .env file")
    
    # Initialize MongoDB client with URI
    client = MongoClient(uri, tlsAllowInvalidCertificates=True)  # Allow insecure SSL
    db = client['taskmaster_db']  # Specify your database name
    return db