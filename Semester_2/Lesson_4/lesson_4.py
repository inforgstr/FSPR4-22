import csv

row_list = [
    ["ID", "NAME", "SURNAME", "PASSPORT", "AGE", "EMAIL"],
]
# with open("Semester_2/Lesson_4/file.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     for list in row_list:
#         for i in range(len(list)):
#             if list[i] == "Mathematics":
#                 list[i] = "Programming"
#         writer.writerow(list)


name = input("Input your name: ")
surname = input("Input your surname: ")
passport = input("Input your passport: ")
age = input("Input your age: ")
email = input("Input your email: ")

with open("Semester_2/Lesson_4/file.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    loader = csv.reader(file)
    for i in loader:
        print(i)
    i = 0
    while i != 3:
        ID = i + 1
        if "@" in email and age.isdigit():
            row = [ID, name, surname, passport, age, email]
            row_list.append(row)
            break
        else:
            print("\nError\n")
            name = input("Input your name: ")
            surname = input("Input your surname: ")
            passport = input("Input your passport: ")
            age = input("Input your age: ")
            email = input("Input your email: ")
            i += 1
    writer.writerows(row_list)


