from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

dp = input('Enter Employee department : ')

for doc in coll.find({'Department' : dp}):
    print(doc)