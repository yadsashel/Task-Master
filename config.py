from pymongo import MongoClient

def get_db_connection():
    uri = "mongodb+srv://taskmaster_db:2002%40Yad@cluster0.d1s6d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, tlsAllowInvalidCertificates=True)  # Allow insecure SSL
    db = client['taskmaster_db']  # Specify your database name
    return db
