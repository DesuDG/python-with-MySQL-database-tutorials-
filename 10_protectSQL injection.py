import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurser=con.cursor()
# deleting records
# mycurser.execute("delete from students where age=22")
sql = "delete from students where id = %s"
# %s place holder
idno = (6,)

mycurser.execute(sql,idno)
con.commit()

print(mycurser.rowcount, "record deleted")