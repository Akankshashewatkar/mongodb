from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll1 = db["Workers"]
coll2 = db["Exworkers"]

id = input('Enter Employee id : ')
dic = coll1.find_one({'_id' : id})

if dic:
    coll2.insert_one(dic)
    coll1.delete_one({'_id' : id})
    print('Employee is removed from Workers collection')

else:
    print('Employee not found')