from .atm_class import ATM
import time
import csv


atm = ATM(1000000)
counter = 0
i = 0
ID = []
with open("Semester_2/Lesson_3/file.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != "ID":
            ID.append(int(row[0]))
    file.close()
print(
    f"""
    ***********************************************
    |              Information:                   |
    |                                             |                    
    |     ACCOUNT USERNAME: {atm.name.upper()}\t\t\t\t  |                      
    |                                             |                          
    |     ACCOUNT BALANCE: {atm.balance}\t              |                    
    |                                             |                    
    |                                             |                      
    |  MENU OF COMMANDS:                          |                    
    |    1. EXIT FROM ATM                         |                    
    |    2. LOG IN OR SIGN UP                     |           
    |    3. NEXT STEP:                            |                    
    |           1) Check account balance          |                    
    |           2) Withdraw                       |                    
    |           3) Deposit                        |                    
    |           4) Exchange                       |                  
    |           5) Log out.                       |                     
    |                                             |                    
    ***********************************************
"""
)

request = input("\nLog in or Sign up?\nENTER 1 TO QUIT\n\n")

# Registration or Log in
x = 0
while x != 1:
    if request == "1":
        break
    while True:
        if request.lower() == "log in":
            btn = input("\nEnter 1 to exit from ATM, or just skip it to log in!.\n")
            if btn == "1":
                x += 1
                break

            login = input("Input your email: ")
            password = input("Input your password: ")

        elif request.lower() == "sign up":
            i = 0
            btn = input("\nEnter 1 to exit from ATM, or just skip it to sign up!.\n")
            if btn == "1":
                break
            login = input("Input your email: ")
            password = input("Create a new password: ")
            EMAIL = []
            PASSWORD = []
            while i <= 5:
                with open("Semester_2/Lesson_3/file.csv", "r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[1] != "EMAIL" and row[2] != "PASSWORD":
                            EMAIL.append(row[1])
                            PASSWORD.append(row[2])
                    if (
                        login.isascii()
                        and "@" in login
                        and len(password) >= 8
                        and password not in PASSWORD
                        and login not in EMAIL
                    ):
                        lst = [ID[-1] + 1, login, password]
                        print("\nYou have successfully registered!")
                        with open(
                            "Semester_2/Lesson_3/file.csv", "a", newline=""
                        ) as file:
                            writer = csv.writer(file)
                            writer.writerow(lst)
                            file.close()
                        break
                    elif login in EMAIL and password in PASSWORD:
                        print("\nThis email has been already taken, please try again!")
                        i += 1
                    elif login not in EMAIL or password not in PASSWORD:
                        print("\nWrong email or password!\n")
                        login = input("Input your email: ")
                        password = input("Create a new password: ")
                        i += 1
        # Menu actions
        while counter < 3:
            time.sleep(2)
            info = {}
            with open("Semester_2/Lesson_3/file.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] != "EMAIL" and row[1] == login and row[2] == password:
                        info[login] = password
            if login in info and info[login] == password:
                command = input(
                    f"\n\nWhat would you want to do?\n\n{'_'*36}"
                    f"\n1 - Check balance\t3 - Deposit\n2 - Withdraw\t"
                    f"\t4 - Exchange\n\t5 - Transfer\n\t6 - Log out\n{'_'*36}\n\n"
                )
                if command == "1":
                    print(atm.Balance())

                elif command == "2":
                    print(atm.get_cash())

                elif command == "3":
                    print(atm.deposit())

                elif command == "4":
                    atm.cur_exchange()
                elif command == "5":
                    print(atm.transfer())
                elif command == "6":
                    break
                else:
                    print("Please, choose one of them!")

            elif login not in info and password not in info.values():
                print("\nWrong email or password!\n")
                login = input("\nLogging in, input your email: ")
                password = input("\nInput your password: ")
                counter += 1
        request = input("\nLog in or Sign up?\nENTER 1 TO QUIT\n\n")
        break
    if counter == 3:
        counter = 0
        print("You were blocked!")
        request = input("\nLog in or Sign up?\nENTER 1 TO QUIT\n\n")

