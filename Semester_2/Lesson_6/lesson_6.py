# colors = ["Red", "Black", "White"]
# def writeToFile(title):
#     with open(title+".txt", "w") as file:
#         file.write(title)
# for color in colors:
#     writeToFile(color)

# try:
#     file = open("text.txt", "w")
#     print(file.read())
# except:
#     print("Exception!")


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Len[hn2006]",
    database="mydatabase",
)


mycursor = mydb.cursor()


for x in mycursor:
    print(x)
