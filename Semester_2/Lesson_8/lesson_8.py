# """
# Strings in MySql:       Integers:
# VARCHAR(10)             BOOL - 0, 1
# CHAR(2)                 BOOLEAN - True, False
# ENUM("F", "M")          INT -  integers(TINYINT, MEDIUMINT, BIGINT)        
#                         FLOAT - floats 
#                         DECIMAL(size, size_after_dot)

# Dates:
# DATE: 2023-03-14
# TIMESTAMP: 2023-03-14 19:48:00.0000
# """
# import datetime
# import mysql.connector

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Len[hn2006]",
#     database="mydatabase",
# )

# mycursor = db.cursor()


# mycursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS types_table 
#     (
#         ID INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(50),
#         surname CHAR(10),
#         gender ENUM("F", "M"),
#         balance FLOAT,
#         cash INT,
#         study_online Boolean,
#         price DECIMAL(12, 2),
#         logged_in_date TIMESTAMP,
#         created_at_date DATE
#     )
# """
# )
# now = datetime.datetime.now()

# sql = """
#     INSERT INTO types_table (name, surname, gender, balance, cash, study_online, price, logged_in_date, created_at_date)
#     VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")
# """
# values = ("John", "Walter", 1, 1000.876, 120023, 1, 124.23, 'datetime.datetime(2023, 3, 14, 12, 23, 43)', "datetime.datetime.now.date()")
# mycursor.execute(sql, values)
# db.commit()

# mycursor.execute("select * from types_table;")

# result = mycursor.fetchall()
# for x in result:
#     print(x)
