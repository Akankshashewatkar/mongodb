from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

for doc in coll.find():
    print(doc)