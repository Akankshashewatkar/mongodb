from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

id = input('Enter Employee id : ')
if coll.find_one({'_id' : id}):
    try:
        sl = float(input('Enter new salary of Employee : '))
        coll.update_one({'_id' : id}, {'$set': {'Salary': sl}})
        print('Salary of Employee is changed')
        print(coll.find_one({'_id' : id}))
    except:
        print('Wrong input')

else:
    print('Employee not found')