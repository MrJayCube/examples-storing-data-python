import sys
import redis
import random

redis = redis.Redis(
    host = 'localhost',
    port = '6379'
    )

def addContact(name,surname):
    if(name != ''):
        num = random.randrange(9999)
        dict = {name + " " + surname: num}
        redis.zadd("contactos", dict)
        print('contact added')
    return

def listContacts():
    contacts = redis.zrange("contactos", 0, -1)
    print(contacts)
    return

def removeContact(name,surname):
    redis.zrem('contactos', name + " " + surname)
    return

def updateContact(name,surname, newName, newSurname):
    redis.zrem('contactos', surname + " " + title)
    num = random.randrange(9999)
    dict = {newName + " " + newSurname: num}
    redis.zadd("contactos", dict)
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
    if len(sys.argv)<6:
        quit()
    else:
        updateContact(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
