import csv


class Store:
    purchases = []

    def __init__(self, name, password, email, card_code, card_balance):
        self.name = name
        self.password = password
        self.email = email
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        with open("users.csv", "r") as users:
            USERS = list(csv.DictReader(users))
            
        for user in USERS:
            user["purchases"] = []

        for user in USERS:
            if email != user["email"] and password != user["password"]:
                break
            else:
                return "Wrong email or password"

        if not (name and email and password and card_balance and card_code):
            return "Empty values were given."

        if (
            isinstance(name, str)
            and "@" in email
            and len(password) >= 6
            and len(card_code) == 16
        ):
            csv.DictWriter(users, )
            USERS.append(
                {
                    "name": name,
                    "password": password,
                    "email": email,
                    "purchases": [],
                    "card": {"code": card_code, "money": card_balance},
                }
            )
            print(USERS)
            return cls(name, email, password, card_code, card_balance)

    @classmethod
    def login(cls, email, password):
        with open("users.csv", "r") as users:
            USERS = list(csv.DictReader(users))

        if not (email and password):
            return "Empty values were given."
        for user in USERS:
            if user["email"] == email and password == user["password"]:
                return cls(
                    user["name"],
                    email,
                    password,
                    user["card"]["code"],
                    user["card"]["balance"],
                )
            else:
                return "Wrong email or password"

    def purchase(self, product):
        """
        - purchase - метод для покупки товаров.
        Для покупки вам нужно узнать, какой товар хочет купить человек и есть у него достаточно денег для этого.
        Если условия верны, то человек покупает товар и с его счета снимаются деньги
        Если товара нет в списке товаров, вывести сообщение что товара нет, если не достаточно денег,
        то вывести сообщение что не достаточно средств.
        """
        with open("products.csv", "r") as products:
            PRODUCTS = list(csv.DictReader(products))[0]

        with open("users.csv", "r") as users:
            USERS = list(csv.DictReader(users))

        if product not in PRODUCTS:
            return "This product didn't find"
        for i, val in PRODUCTS.items():
            if self.card_balance - int(val) < 0:
                return "Not enough money"
            elif self.card_balance - int(val) >= 0 and i == product:
                self.card_balance -= int(val)
                print(USERS[-1])
                USERS[-1]["purchases"].append(product)
                return f"Succesfully bought this product, your balance - {self.card_balance}."


enter_method = input("Choose method: login or register: ")
if enter_method == "register":
    user_1 = Store.register(
        "behruz", "behrz@gmail.com", "234k32k3", "2345522345678964", 1000
    )
    print(user_1.purchase("wear"))
    user_2 = Store.register(
        "Name", "dsfsf@gmail.com", "234423lkjdf", "8675968577688857", 800
    )
    print(user_2.purchase("key"))
elif enter_method == "login":
    user_1 = Store.login("behruz@gmail.com", "234fjfdsd")
    print(user_1.purchase("wear"))
    print(user_1.purchase("ke"))
