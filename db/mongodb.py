from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["ai_maintenance"]
bookings_collection = db["service_bookings"]
