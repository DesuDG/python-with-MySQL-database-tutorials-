import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurseor=con.cursor()
# craete a table
# mycurseor.execute("create table students (name varchar(30), sex text(10), age int)")
# mycurseor.execute("show tables")
# for x in mycurseor:
#     print(x)
#     delete a table
# mycurseor.execute("drop table students")

# Alter table and costraints primary key auto increment
mycurseor.execute("alter table students add column id int auto_increment primary key")