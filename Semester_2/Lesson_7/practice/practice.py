import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Len[hn2006]",
    database="mydatabase",
)

mycursor = db.cursor()


mycursor.execute(
    "CREATE TABLE IF NOT EXISTS users (ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(150), SURNAME VARCHAR(150))"
)
data = """
    INSERT INTO users (NAME, SURNAME)
    VALUES ("%s", "%s")
"""
name = input("Input your name: ").strip()
surname = input("Input your surname: ").strip()
if name and surname:
    mycursor.execute("select * from users;")
    result1 = mycursor.fetchall()

    names = (x[1] for x in result1)
    surnames = (x[2] for x in result1)

    if repr(name) not in names:
        sql = (name, surname)
        mycursor.execute(data, sql)
        db.commit()

        # mycursor.execute("alter table products ADD column Is_fresh bool default(True)")

        mycursor.execute("select * from users;")
        result = mycursor.fetchall()

        for x in result:
            print(x)
    else:
        print("Try other name or surname!")
else:
    print("Did not match. Try again!")
