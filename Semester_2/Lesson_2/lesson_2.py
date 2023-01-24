import random
import csv

x = random.randint(0, 100)

s = -1
counter = 0
win = 1000000


while s != x and counter != 10:
    a = int(input())
    if a < x:
        print("Your number is less than random number!")
        counter += 1

    elif a > x:
        print("Your number is greater than random number!")
        counter += 1
    elif a == x:
        s = a
    else:
        print("You lose lot of attempts!")

if counter <= 10:
    if counter == 1:
        win -= 999650
        print(win)
    elif counter == 2:
        win -= 999700
        print(win)
    else:
        win = 300
        for i in range(counter - 3):
            win -= 100
    if win > 0:
        result = [
            f"\n\nYour number is correct! The random number was {s}\nYour attempts: {counter}\n\t\tYou win {win}"
        ]
        print("".join(result))
    else:
        result = [
            f"\n\nYour number is correct! The random number was {s}\nYour attempts: {counter}\n\t\tYour duty is {abs(win)}"
        ]
        print("".join(result))

with open("Semester_2/Lesson_2/file.csv", "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(result)