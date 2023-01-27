class Atm:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def Balance(self):
        return f"\nYour balance: {self.balance:.2f}"

    def get_cash(self):
        amount = float(input("\nInput withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            return f"\nSuccessfully!\nYour money: {amount}\nYour account balance: {self.balance}\n\n"
        else:
            return "Not available! Please, try again."

    def deposit(self):
        amount = float(input("\nInput deposit sum: "))
        self.balance += amount
        return f"\nCurrent account balance: {self.balance:.2f}\n\n"

    def cur_exchange(self):
        type = input(
            f"Input type of exchanging sum:\n{'_'*36}\n1. SUM - > USD\t\t"
            f"2. USD - > SUM\n3. SUM - > EURO\t\t4. EURO - > SUM\n5. SUM -> POUND\t\t6. POUND - > SUM\n{'_'*36}\n\t7. Back\n{'_'*36}\n"
        )
        amount = float(input(f"Input amount of exchanging sum:\n{'_'*36}\n"))
        if amount <= self.balance:
            self.balance -= amount
            if type == "1":
                return f"Total: {amount/11337:.2f} ($) has been exchanged!"
            elif type == "2":
                return f"Total: {amount/0.000088:.2f} (sums) has been exchanged!"
            elif type == "3":
                return f"Total: {amount/12311:.2f} (€) has been exchanged!"
            elif type == "4":
                return f"Total: {amount/0.000081:.2f} (sums) has been exchanged!"
            elif type == "5":
                return f"Total: {amount/14042:.2f} (pounds) has been exchanged!"
            elif type == "6":
                return f"Total: {amount/0.000071:.2f} (sums) has been exchanged!"
        elif amount > self.balance:
            return f"Not available, try again!"


import timeit

USERS = {
    "email@gmail.com": "root",
}


atm = Atm("BYC", 10000)
counter = 0
i = 0

print(
    f"""
    ******************************************************
    |              Information:                          |
    |                                                    |                    
    |     Username: {atm.name.upper()}                                  |                      
    |                                                    |                          
    |     BALANCE: {atm.balance}                                 |                    
    |                                                    |                    
    |                                                    |                      
    |  MENU OF COMMANDS:                                 |                    
    |    1. EXIT FROM ATM                                |                    
    |    2. NEXT STEP:                                   |                    
    |           1) Check account balance                 |                    
    |           2) Withdraw                              |                    
    |           3) Deposit                               |                    
    |           4) Exchange                              |                  
    |           5) Log out.                              |                     
    |                                                    |                    
    ******************************************************
"""
)
start_time = timeit.default_timer()
request = input("\nLIMIT: 3min\nLog in or Sign up?\n")


# Registration or Log in
x = 0
while True:
    if request.lower() == "log in":
        btn = input("\nEnter 1 to exit from ATM, or just skip it to log in!.\n")
        if btn == "1":
            break
        login = input("Input your email: ")
        password = input("Input your password: ")
        if timeit.default_timer() - start_time > 100:
            print(f"\nTime is up, your limit was 3 min.\n")
            break

    elif request.lower() == "sign up":
        i = 0
        btn = input("\nEnter 1 to exit from ATM, or just skip it to sign up!.\n")
        if btn == "1":
            break
        login = input("Input your email: ")
        password = input("Create a new password: ")
        while i <= 5:
            if timeit.default_timer() - start_time > 100:
                print(f"\nTime is up, your limit was 3 min.\n")
                break
            if (
                login.isascii()
                and "@" in login
                and len(password) >= 8
                and login not in USERS
            ):
                USERS[login] = password
                print(f"\nYou have been successfully registered!")
                break
            elif login in USERS and password in USERS.values():
                print("\nThis email has been already taken, please try again!")
                i += 1
            else:
                print("\nWrong email or password!\n")
                login = input("Input your email: ")
                password = input("Create a new password: ")
                i += 1
    if timeit.default_timer() - start_time > 100:
        print(f"\nTime is up, your limit was 3 min.\n")
        break
    # Menu actions
    while counter < 3:

        if login in USERS and password == USERS[login]:
            command = input(
                f"\n\nWhat would you want to do?\n\n{'_'*36}"
                f"\n1 - Check balance\t3 - Deposit\n2 - Withdraw\t"
                f"\t4 - Exchange\n\n5 - exit from ATM\n{'_'*36}\n\n"
            )
            if command == "1":
                print(atm.Balance())

            elif command == "2":
                print(atm.get_cash())

            elif command == "3":
                print(atm.deposit())

            elif command == "4":
                print(atm.cur_exchange())
            elif command == "5":
                break
            else:
                print("Please, choose one of them!")

        else:
            print("\nWrong email or password!\n")
            login = input("\nLogging in, input your email: ")
            password = input("\nInput your password: ")
            counter += 1

    if counter == 3:
        counter = 0
        print("You were blocked!")
        request = input("\nLog in or Sign up?:\n")
    if timeit.default_timer() - start_time > 100:
        print(f"\nTime is up, your limit was 3 min.\n")
        break
