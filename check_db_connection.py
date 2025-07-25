import pymysql

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    pass
finally:
    connection.close()