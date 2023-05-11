import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Len[hn2006]",
    database="mydatabase",
)

cursor = db.cursor()


table_users = """
    CREATE TABLE IF NOT EXISTS users (
        userID INT AUTO_INCREMENT PRIMARY KEY,
        NAME VARCHAR(100),
        SURNAME VARCHAR(150)
    )
"""

table_products = """
    CREATE TABLE IF NOT EXISTS products (
        productID INT AUTO_INCREMENT PRIMARY KEY,
        NAME VARCHAR(150),
        favorite INT
        constraint FK_UserFavorite FOREIGN KEY (favorite) 
        REFERENCES users(ID)
    )
"""

# cursor.execute(table_users)
# db.commit()
# cursor.execute(table_products)
# db.commit()


# user_insert = """
#     insert into users (name, surname)
#     values (%s, %s)
# """

# user_values = [
#     ("John", "Walter"),
#     ("Nick", "Walter"),
#     ("Emma", "Smith"),
#     ("Bob", "Tylon"),
# ]
# cursor.executemany(user_insert, user_values)
# db.commit()

# product_insert = """
# #     insert into products (name, favorite) values (%s, %s)
# # """

# product_values = [
#     ("Chocolate", 5),
#     ("Milk", 8),
#     ("Twix", 5),
#     ("Water", 6),
# ]
# cursor.executemany(product_insert, product_values)
# db.commit()

cursor.execute("select * from users;")
result = cursor.fetchall()
for x in result:
    print(x)



# result_data = {"user_data": [], "product_data": []}

# cursor.execute("select * from users;")
# result = cursor.fetchall()
# for x in result:
#     result_data["user_data"].append(x[1:])

# cursor.execute("select * from products;")
# result = cursor.fetchall()
# for x in result:
#     result_data["product_data"].append(x[1:])

# print(result_data)
# import json
# with open("file.json", "a") as file:
#     json.dump(result_data, file, indent=4)
