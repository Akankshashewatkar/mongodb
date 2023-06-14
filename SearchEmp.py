from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

id = input('Enter Employee id : ')
if coll.find_one({'_id' : id}):
    print(coll.find_one({'_id' : id}))

else:
    print('Employee not found')