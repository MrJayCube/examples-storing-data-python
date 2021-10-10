import sys
import json


def printHelp():
    print('''
    Usage:

    > pythom contacts.py <cmd>

    Avalible commands:

        - create <path>: creates new database
        - put <path> <key> <value>: write a new key=value pair
        - get <path> <key>: return the value asssociated to the key
        - list <path>: list all the pairs key=value

         
    ''')

def create(path): #python3 store.py create midb.log
 
    print(f'create {path}')
    f = open(path,"w")
    f.close()


def put(path,key,value):
    print(f'put{key}{value}')
    f = open(path,"at")
    line=json.dumps([key,value]) + "\n"  
    f.write(line)
    f.close()

def get (path,key):
    print(f'get{key}')
    f = open(path,"rt")
    value=None
    line= f.readline()
    while line:
        pair=json.loads(line)
        if pair[0] ==key: value = pair[1]
        line=f.readline()

    if value:print(f'Value found:{value} ')
    else: print(f'Value not found ')
    f.close()

    
def listAll (path):
    f = open(path,"rt")
    value=None
    key=None
    line= f.readline()
    while line:
        pair=json.loads(line)
        key = pair[1]
        value = pair[1]
        line=f.readline()

    if value:print(f'Value found Key: {key} Value: {value} ')
    else: print(f'Value not found ')
    f.close()

if len(sys.argv) < 2:
    printHelp()
    quit()
elif sys.argv[1] == 'create':
    if len(sys.argv) < 3:
        printHelp()
        quit()
    else:
        create(sys.argv[2])
elif sys.argv[1] == 'put':
    if len(sys.argv) < 5:
        printHelp()
        quit()
    else:
        put(sys.argv[2],sys.argv[3],sys.argv[4])
elif sys.argv[1] == 'list':
    if len(sys.argv) < 2:
        printHelp()
        quit()
    else:
        listAll(sys.argv[2])
elif sys.argv[1] == 'get':
    if len(sys.argv) < 4:
        printHelp()
        quit()
    else:
        get(sys.argv[2],sys.argv[3])

else:
    printHelp()
    quit()