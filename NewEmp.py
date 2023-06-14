from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]
dic = {}

try:
    id = input('Enter Employee id : ')
    dic['_id'] = id
    nm = input('Enter Employee Name : ')
    dic['Name'] = nm
    dep = input('Enter the Department of Employee : ')
    dic['Department'] = dep
    po = input('Enter the Post of Employee : ')
    dic['Post'] = po
    ct = input('Enter the City of Employee : ')
    dic['City'] = ct
    sal = float(input('Enter Salary of Employee : '))
    dic['Salary'] = sal
    mob = input('Enter Mobile Number : ')
    dic['Mobile'] = mob
    em = input('Enter E-Mail id : ')
    dic['E-Mail'] = em

    coll.insert_one(dic)
    print('Employee is added')

except:
    print('Wrong input')