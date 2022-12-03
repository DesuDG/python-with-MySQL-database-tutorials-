import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="university"
)
mycurser=con.cursor()
# inner join
# sql = "select department.dep_name as dept, course.course_name as course from department inner join course on department.course_code = course.id"

# left join
# sql = "select department.dep_name as dept, course.course_name as course from department left join course on department.course_code = course.id"



# right join
sql = "select department.dep_name as dept, course.course_name as course from department right join course on department.course_code = course.id"




mycurser.execute(sql)
result = mycurser.fetchall()

for x in result:
    print(x)