from pymongo.mongo_client import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["ChatSystemDB"]

try:
    client.admin.command('ping')
    print("Pinged your deploymeny. You successfully connected to MongoDB!")
except Exception as e:
    print(e)