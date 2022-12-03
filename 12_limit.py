import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# select the first 3 records
# mycurser.execute("select * from students limit 3")

mycurser.execute("select * from students limit 2 offset 2")
result = mycurser.fetchall()

for i in result:
    print(i)