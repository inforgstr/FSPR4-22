class ATM:
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
                counter = 1
                for i in range(len(total)):
                    if type == f"{counter}":
                        print(f"\nTotal: {total[i]:.2f} has been exchanged!\n\n")
                    counter += 1

            elif amount > self.balance:
                print(f"\nNot available, try again!\n")

    def transfer(self):
        card = input("Input name of the card: ")
        amount = float(input("Input amount of transfer: "))
        total = amount + amount / 100
        if len(card) >= 10 and total <= self.balance:
            self.balance -= total
            return f"\nSuccessfull! Your account balance: {self.balance:.2f}"
        else:
            return "\nWrong credentials!\nPlease, try again!\n"