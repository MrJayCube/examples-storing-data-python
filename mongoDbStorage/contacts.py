import sys
import pymongo
import random
from bson import ObjectId

DB_SET = "contacts"
myCol = "my_collection"


try:
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
except: 
    print("It was not possible to stablish a connection")
mydB = myClient["firstDbase"]
table = mydB["contacts"]

def addContact(name,surname):
    if(name != ''):
        contact = {"nombre": name, "apellido": surname}
        test = table.insert_one(contact)
        print(test.inserted_id)
    return

def listContacts():
    cursor = table.find({})
    for document in cursor:
          print(document)
    return

def removeContact(name,surname):
    for itm in table.remove({"nombre": name, "apellido": surname}):
        oid_str = str(itm['_id'])
        test = table.find_one_and_delete(
            {"_id" : ObjectId(oid_str)}
        )
    return

def updateContact(name, newName, newSurname):
    for itm in table.find({"nombre": name}):
        oid_str = str(itm['_id'])
        test = table.find_one_and_update(
            {"_id" : ObjectId(oid_str)},
            {"$set":
            {"nombre": newName, "apellido": newSurname}
            },upsert=True
        )
        print(test)
    return

if len(sys.argv)<1:
    help()
    quit()
elif sys.argv[1] =='add':
    print('añadir')
    if len(sys.argv)<4:
        help()
        quit()
    else:
        addContact(sys.argv[2],sys.argv[3])  
elif sys.argv[1] == 'list':
    print('listar')
    listContacts()

elif sys.argv[1] == 'remove':
    if len(sys.argv)<3:
        quit()
    else:
        removeContact(sys.argv[2],sys.argv[3])
elif sys.argv[1] == 'update':
    if len(sys.argv)<5:
        quit()
    else:
        updateContact(sys.argv[2],sys.argv[3],sys.argv[4])
