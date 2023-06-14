from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

try:
    sl = float(input('Enter the Salary : '))
    for doc in coll.find({'Salary' : {'$gt' : sl}}):
        print(doc)

except:
    print('Wrong input')