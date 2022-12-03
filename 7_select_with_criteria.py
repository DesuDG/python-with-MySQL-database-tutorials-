import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# Select with criteria
# mycurser.execute("select * from students where sex='M'")
mycurser.execute("select * from students where name like '%m%'")
result = mycurser.fetchall()

for i in result:
    print(i)