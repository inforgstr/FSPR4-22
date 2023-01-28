class Atm:
    def __init__(self, balance):
        self.balance = balance
        self.name = input("Input your user name: ")

    def Balance(self):
        return f"\nYour balance: {self.balance:.2f}"

    def get_cash(self):
        amount = float(input("\nInput withdraw: "))
        total = amount / 100 + amount
        if self.balance >= total:
            self.balance -= total
            return f"\nSuccessfully!\nYour money: {amount}\nYour account balance: {self.balance}\n\n"
        else:
            return "Not available! Please, try again."

    def deposit(self):
        amount = float(input("\nInput deposit sum: "))
        self.balance += amount
        return f"\nCurrent account balance: {self.balance:.2f}\n\n"

    def cur_exchange(self):
        while True:
            type = input(
                f"Input type of exchanging sum:\n{'_'*36}\n1. SUM - > USD\t\t"
                f"2. USD - > SUM\n3. SUM - > EURO\t\t4. EURO - > SUM\n5. SUM -> POUND\t\t6. POUND - > SUM\n{'_'*36}\n\t7. Back\n{'_'*36}\n"
            )
            if type == "7":
                break
            amount = float(input(f"Input amount of exchanging sum:\n{'_'*36}\n"))
            if amount <= self.balance:
                mod = amount / 100 + amount
                self.balance -= mod
                total = [
                    amount / 11337,
                    amount / 0.000088,
                    amount / 12311,
                    amount / 0.000081,
                    amount / 14042,
                    amount / 0.000071,
                ]
                if type == "1":
                    print(f"Total: {total[0]:.2f} ($) has been exchanged!")
                elif type == "2":
                    print(f"Total: {total[1]:.2f} (sums) has been exchanged!")
                elif type == "3":
                    print(f"Total: {total[2]:.2f} (€) has been exchanged!")
                elif type == "4":
                    print(f"Total: {total[3]:.2f} (sums) has been exchanged!")
                elif type == "5":
                    print(f"Total: {total[4]:.2f} (pounds) has been exchanged!")
                elif type == "6":
                    print(f"Total: {total[5]:.2f} (sums) has been exchanged!")
                    
            elif amount > self.balance:
                print(f"\nNot available, try again!\n")
    
    def transfer(self):
        card = input("Input name of the card: ")
        amount = float(input("Input amount of transfer: "))
        total = amount + amount/100
        if card == "10000" and total <= self.balance:
            self.balance -= total
            return f"\nSuccessfull! Your account balance: {self.balance}"
                
                


import time

USERS = {
    "email@gmail.com": "root",
}


atm = Atm(10000)
counter = 0
i = 0

print(
    f"""
    ***********************************************
    |              Information:                   |
    |                                             |                    
    |     ACCOUNT USERNAME: {atm.name.upper()}\t\t  |                      
    |                                             |                          
    |     ACCOUNT BALANCE: {atm.balance}\t          |                    
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

request = input("\nLIMIT: 3min\nLog in or Sign up?\n\n")

# Registration or Log in
x = 0
while True:
    time.sleep(1)
    if request.lower() == "log in":
        btn = input("\nEnter 1 to exit from ATM, or just skip it to log in!.\n")
        if btn == "1":
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
        while i <= 5:
            time.sleep(1)
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
    # Menu actions
    while counter < 3:
        time.sleep(2)
        if login in USERS and password == USERS[login]:
            command = input(
                f"\n\nWhat would you want to do?\n\n{'_'*36}"
                f"\n1 - Check balance\t3 - Deposit\n2 - Withdraw\t"
                f"\t4 - Exchange\n\t5 - Transfer\n6 - exit from ATM\n{'_'*36}\n\n"
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

        else:
            print("\nWrong email or password!\n")
            login = input("\nLogging in, input your email: ")
            password = input("\nInput your password: ")
            counter += 1

    if counter == 3:
        counter = 0
        print("You were blocked!")
        request = input("\nLog in or Sign up?:\n")
