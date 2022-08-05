import mysql.connector
import pymysql


cnx = pymysql.connect.connector(user="root", password="Amityville27*", host="127.0.0.1", database="220711_w2")

#     #CURSOR-  points to various tables allowing to insert into our database and query our databses

cursor = cnx.cursor()

query = "SELECT * FROM employees_3nf"

cursor.execute(query)

for record in cursor:
        print(record)

cursor.close()
cnx.close()