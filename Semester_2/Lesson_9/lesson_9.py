import mysql.connector

# from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Len[hn2006]",
    database="mydatabase",
)

cursor = db.cursor()

table_1 = """
    CREATE TABLE IF NOT EXISTS users (
    id int auto_increment primary key,
    name varchar(50),
    fav int
    )
"""
# sql_1 = """
#     insert into users (name, fav) Values (%s, %s)
# """
# value_1 = [
#     ("asd", 3),
#     ("qwe", 1),
#     ("zxc", 2),
#     ("vbnm", None),
# ]
# cursor.executemany(sql_1, value_1)
# db.commit()


# cursor.execute(table_1)
# table_2 = """
#     CREATE TABLE IF NOT EXISTS products (
#     id int auto_increment primary key,
#     name varchar(50)
#     )
# """

# sql_2 = """
#     insert into products (name) Values (%s)
# """
# value_2 = [
#     tuple("a"),
#     tuple("b"),
#     tuple("c"),
#     tuple("d")
# ]
# cursor.executemany(sql_2, value_2)
# db.commit()

# cursor.execute(table_2)


"""
INNER JOIN
LEFT JOIN
RIGHT JOIN
"""

# sql = """
#     SELECT users.name, products.name FROM users LEFT JOIN products ON products.id=users.fav;
# """

# cursor.execute(sql)




result = cursor.fetchall()
for x in result:
    print(x)


db.close()
