import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# Orderby
mycurser.execute("select * from students order by age ")
result = mycurser.fetchall()

for i in result:
    print(i)
