import sys
import sqlite3
import random

def addContact(name,title):
    con=sqlite3.connect("contactos.db")
    cur=con.cursor()
    num = str(random.randrange(9999))
    cur.execute("INSERT INTO contact VALUES ('"+num+"','"+name+"','"+title+"')")
    con.commit()
    con.close()
    print('contact added')
    return

def listContacts():
    con=sqlite3.connect("contactos.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM contact")
    rows = cur.fetchall()
    for row in rows:
       print(row)
    con.commit()
    con.close()

def removeContact(name):
    con=sqlite3.connect("contactos.db")
    cur=con.cursor()
    cur.execute("DELETE FROM contact WHERE name=='"+name+"'")
    con.commit()
    con.close()
    return

def updateContact(num,name,title):
    con=sqlite3.connect("contactos.db")
    cur=con.cursor()
    print("UPDATE contact SET name='"+name+"', title='"+title+"' WHERE num='"+num+"'")
    cur.execute("UPDATE contact SET name='"+name+"', title='"+title+"' WHERE reg_no='"+num+"'")
    con.commit()
    con.close()

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
    if len(sys.argv)<2:
        quit()
    else:
        removeContact(sys.argv[2])
elif sys.argv[1] == 'update':
    if len(sys.argv)<4:
        quit()
    else:
        updateContact(sys.argv[2],sys.argv[3],sys.argv[4])
