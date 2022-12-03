import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# deleting records
mycurser.execute("delete from students where age=22")
con.commit()

print(mycurser.rowcount, "record deleted")

# mycurser.execute("select * from students")
# result=mycurser.fetchall()
# for i in result:
#     print(i)