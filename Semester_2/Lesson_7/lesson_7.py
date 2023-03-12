import json
import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Len[hn2006]",
    database="mydatabase",
)

mycursor = mydb.cursor()

# mycursor.execute("Drop table students;")
student = """
        CREATE TABLE IF NOT EXISTS students 
        (
            ID INT auto_increment primary key,
            name VARCHAR(50), 
            surname VARCHAR(50), 
            Gender Bool, 
            Study_online Bool, 
            class varchar(50), adress varchar(150), 
            phone_number varchar(15)
        )
    """
mycursor.execute(student)
# mycursor.execute("""
#     ALTER TABLE students
#     ADD column id int
#     auto_increment primary key
# """)


sql = """
    INSERT INTO students (name, surname, Gender, Study_online, class, adress, phone_number)
    VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")
"""

with open("data.json") as f:
    reader = json.load(f)


r = [1, 9, 0, 7]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

val = [
    (
        f"{random.choice(reader['people'])['name']}",
        f"{random.choice(reader['people'])['surname']}",
        random.choice((0, 1)),
        random.choice((0, 1)),
        f"{random.choice(['django', 'javascript', 'java', 'flutter', 'python'])} - {random.choice([x for x in range(1, 31)])}",
        "Hper st.", 
        f"+9989{random.choice(r)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}") 
        for x in range(1000)
]


mycursor.executemany(sql, val)


mydb.commit()

mycursor.execute("select * from students;")
result = mycursor.fetchall()
for x in result:
    print(x)


# mycursor.execute("select * from students;")
# result = mycursor.fetchall()
# for x in result:
#     print(x)
