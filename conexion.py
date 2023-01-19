import mysql.connector

def connec():
    conec = mysql.connector.connect(user='root', password='', host='localhost', database='erick_xavier',port='3306')
    return conec


'''cursor.execute("SHOW TABLES")

for base in cursor:
    print(base)

conec.close()'''

