import re


USERS = [
    {
        "name": "Behruz",
        "password": "234fjfdsd",
        "email": "behruz@gmail.com",
        "purchases": [],
        "card": {"code": "3647583465734283", "balance": 1000},
    },
    {
        "name": "Bob",
        "password": "bob345345@",
        "email": "bob@bob.com",
        "purchases": [],
        "card": {"code": "4567485767574876", "balance": 20},
    },
]
PRODUCTS = [
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "color": "black",
    },
    {
        "product_name": "bag",
        "count": 20,
        "price": 200,
        "color": "gray",
    },
]


class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.password = password
        self.email = email
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        for user in USERS:
            if email == user["email"] and user["password"] == password:
                return "User with this email or password is already in exists."

        if not (name and email and password and card_balance and card_code):
            return "Empty values were given."

        if (
            isinstance(name, str)
            and re.match(r"^[A-Z]\w+$", name)
            and re.match(r"^[\w.]+@[\w.]+$", email)
            and re.match(r"^[\w@#$]{6,16}$", password)
            and re.match(r"^\d{16}$", card_code)
            and re.match(r"^\d+$", str(card_balance))
        ):
            USERS.append(
                {
                    "name": name,
                    "password": password,
                    "email": email,
                    "purchases": [],
                    "card": {"code": card_code, "money": int(card_balance)},
                }
            )
            return cls(name, email, password, card_code, card_balance)

        return "Wrong credentials."

    @classmethod
    def login(cls, email, password):
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

        return "Wrong email or password"

    def purchase(self, product, amount=1):
        card_balance = int(self.card_balance)
        try:
            amount = int(amount)
        except ValueError as error:
            return error

        if card_balance <= 0:
            return "Not enough money."

        product_dict = {commodity["product_name"]: commodity for commodity in PRODUCTS}

        if product not in product_dict:
            return "Not available."

        commodity = product_dict[product]
        price = int(commodity["price"])
        total_cost = price * amount

        if card_balance < total_cost:
            return "Not enough money."

        self.card_balance -= total_cost
        product_list = [product] * amount
        self.purchases += product_list

        user_exists = False

        for id, user in enumerate(USERS):
            if user["email"] == self.email and user["password"] == self.password:
                user_exists = True
                USERS[id]["purchases"] += product_list

        if not user_exists:
            return "User not found."

        commodity["count"] -= amount
        return "Success."

    def user_exists(self):
        for user in USERS:
            if self.email == user["email"] and self.password == user["password"]:
                return True
        return False
