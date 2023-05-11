import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Len[hn2006]",
    database="many_to_many_students",
)

cursor = db.cursor()

# cursor.execute("Insert into student_classes values (1, 4),(2,3),(3,1),(4,2);")
# db.commit()
cursor.execute("select * from student_classes;")
result = cursor.fetchall()
for x in result:
    print(x)
