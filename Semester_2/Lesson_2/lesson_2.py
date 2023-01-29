import random
import csv


leaders = {}

print(
    """
    ************WELCOME-TO*************
    ************CASINO-GAME************
    |         DOCUMENTATION           |
    | 1.THE MINIMUM AGE MUST BE 18    |
    | 2 USERNAME MUST BE NON-IDENTICAL|
    ***********************************
"""
)

req = input(f"\t  MENU:\n\t1 - START THE GAME\n\t2 - LEADERS\n\t3 - QUIT\n\n")

while True:
    if req == "3":
        break
    if req == "2":
        i = 0
        while i != 1:
            with open("Semester_2/Lesson_2/file.csv", "r") as file:
                reader = csv.reader(file)
                print("\n\tLEADERS\n\t||||||||||")
                for row in reader:
                    if row[7] != "POINTS" and row[1] != "USERS":
                        leaders[row[1]] = row[7]
                new_dict = dict(
                    sorted(leaders.items(), key=lambda x: int(x[1]), reverse=True)
                )
                for user, a in new_dict.items():
                    print(f"\t{user} -- {a}")
                file.close()
            q = input("\t||||||||||\n\nB - BACK.\n")
            if q == "B":
                i += 1
                req = input(
                    f"\tMENU:\n\t1 - START THE GAME\n\t2 - LEADERS\n\t3 - QUIT\n\n"
                )
    if req == "1":
        USERS = []
        ID = []
        with open("Semester_2/Lesson_2/file.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] != "PLAYERS":
                    USERS.append(row[1])
                if row[0] != "ID":
                    ID.append(row[0])
        g = 0
        while g != 1:
            command = input("\nSKIP TO START OR ENTER B TO MOVE BACK\nGOOD LUCK!\n")
            if command == "B":
                req = input(
                    f"\tMENU:\n\t1 - START THE GAME\n\t2 - LEADERS\n\t3 - QUIT\n\n"
                )
                break
            i = 0
            user = input("Input your name: ")
            age = input("Input your age: ")
            if (
                age.isdigit()
                and (user.lower() not in USERS and user.upper() not in USERS)
                and user.isalnum()
                and int(age) >= 18
            ):
                counter = 0
                win = 1000000
                points = 0
                wins = 0
                loses = 0
                while i != 1:
                    x = random.randint(0, 100)
                    print("Guess the number!\n\n")
                    s = -1

                    while s != x:
                        a = int(input())
                        if a < x:
                            print("Your number is less than random number!")
                            counter += 1
                            points -= 10
                        elif a > x:
                            print("Your number is greater than random number!")
                            counter += 1
                            points -= 10
                        elif a == x:
                            s = a
                            points += 100
                            wins += 1
                            break
                        if counter > 10:
                            print("You lose, lot of attempts!")
                            loses += 1
                            points = 0
                            break
                    break
                if counter <= 10:
                    if counter == 0:
                        points += 500
                        print(win)
                    elif counter == 1:
                        win -= 999650
                        points += 300
                        print(win)
                    elif counter == 2:
                        win -= 999700
                        points += 200
                        print(win)
                    else:
                        win = 300
                        for i in range(counter - 3):
                            win -= 100
                    if win > 0:
                        print(
                            f"\n\nYour number is correct! The random number was {s}\nYour attempts: {counter}\n\t\tYou won {win}"
                        )

                    else:
                        print(
                            f"\n\nYour number is correct! The random number was {s}\nYour attempts: {counter}\n\t\tYour duty is {abs(win)}"
                        )

                ID = int(ID[-1]) + 1
                info = [
                    f"{ID}",
                    user,
                    f"{age}",
                    f"{wins}",
                    f"{win}",
                    f"{loses}",
                    f"{counter}",
                    f"{points}",
                ]
                with open("Semester_2/Lesson_2/file.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(info)
            elif user.lower() in USERS or user.upper() in USERS:
                print("\nYour username must be non-identical!\n")
                g += 1
                req = input(
                    f"\tMENU:\n\t1 - START THE GAME\n\t2 - LEADERS\n\t3 - QUIT\n\n"
                )
            elif not (int(age) >= 18):
                print("\nYour age must be at least 18!\n")
                g += 1
                req = input(
                    f"\tMENU:\n\t1 - START THE GAME\n\t2 - LEADERS\n\t3 - QUIT\n\n"
                )
            else:
                print("\nWRONG CREDENTIALS!\n")
                g += 1
                req = input(
                    f"\tMENU:\n\t1 - START THE GAME\n\t2 - LEADERS\n\t3 - QUIT\n\n"
                )
