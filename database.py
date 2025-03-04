 
from pymongo import MongoClient# Update with your MongoDB URI
MONGO_URI = "mongodb://localhost:27017" 
DB_NAME = "battery_monitoring"
COLLECTION_NAME = "predictions"
 # Update if needed


client = MongoClient(MONGO_URI)
database = client[DB_NAME]
collection = database[COLLECTION_NAME]