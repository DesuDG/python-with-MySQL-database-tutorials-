import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycurseor=con.cursor()
# show existing database

# craete a databse
# # mycurseor.execute("create database student")
# mycurseor.execute("show databases")
# for i in mycurseor:
#     print(i)