from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

id = input('Enter Employee id : ')

if coll.find_one({'_id' : id}):
    ct = input('Enter new City of Employee : ')
    dp = input('Enter new Department of Employee : ')
    dic = {}
    dic['City'] = ct
    dic['Department'] = dp
    
    coll.update_one({'_id' : id}, {'$set' : dic})
    print('Salary of Employee is changed')
    print(coll.find_one({'_id' : id}))

else:
    print('Employee not found')