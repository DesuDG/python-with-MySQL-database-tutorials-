import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# Select all records
mycurser.execute("select * from students")
# select a specfic column
#mycurser.execute("select id, name from students")

# select only first row

# result = mycurser.fetchall()
result=mycurser.fetchone()

for i in result:
    print(i)