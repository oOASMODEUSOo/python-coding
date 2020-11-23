import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"

)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

result = mycursor.fetchall()

for x in result:
    print(x)