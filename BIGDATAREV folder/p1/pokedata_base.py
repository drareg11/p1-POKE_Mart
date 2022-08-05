import mysql.connector

cnx = mysql.connector.connect(
    user="root", 
    password="Amityville27*", 
    host="127.0.0.1", 
    database="Project_1"
    )

my_cursor = cnx.cursor()
my_cursor.close()
cnx.close()