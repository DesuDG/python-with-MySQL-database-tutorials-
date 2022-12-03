import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# update record
sql = "update students set age = 28 where name =%s"
na =('Desye',)
mycurser.execute(sql, na)
con.commit()
print(mycurser.rowcount, "record is updated")
