from pymongo import MongoClient

def get_db_connection():
    # Be sure to URL-encode any special characters in the username/password
    client = MongoClient("mongodb+srv://taskmaster_db:2002%40Yad@cluster0.d1s6d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 
    db = client['taskmaster_db']  # Use square brackets to access the database
    return db