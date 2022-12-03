import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()


# insert a record
sql = "insert into students (name, sex, age) values (%s,%s, %s)"
val = ("Desye","M",26)
mycurser.execute(sql,val)

con.commit()
print(mycurser.rowcount, "record is inserted")