import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# insert multiple record
sql = "insert into students (name, sex, age) values (%s,%s, %s)"
val = [
    ("Nahom","M",26),
    ("Mesi","F",20),
    ("Abebe","M",26),
    ("Eman","f",22),
    ("Kedir","M",27)

]
mycurser.executemany(sql,val)

con.commit()
print(mycurser.rowcount, "record is inserted")