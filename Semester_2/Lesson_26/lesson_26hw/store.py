"""

"""


import csv


# get list of exact file
def get_csv(file_path: str, delimiter: str) -> list[dict]:
    with open(file_path, "r") as reader:
        return list(csv.DictReader(reader, delimiter=delimiter))


# update for column by index to set new value
def update_csv_file(
    path: str, index: int, column: str, new_value, action, fieldnames, count=1
) -> None:
    with open(path, "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        data = list(reader)

    if action == "int+":
        data[index][column] = int(data[index][column]) + (int(new_value) * count)
    elif action == "int-":
        data[index][column] = int(data[index][column]) - (int(new_value) * count)

    elif action == "str" and data[index][column]:
        data[index][column] += "," + ",".join([new_value] * count)
    else:
        data[index][column] += ",".join([new_value] * count)

    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(data)


class Store:
    def __init__(self, name, password, email, card_code, card_balance):
        self.name = name
        self.password = password
        self.email = email
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        USERS = get_csv("users.csv", ";")

        for user in USERS:
            if email != user["email"] and user["password"] != password:
                continue
            else:
                return cls(name, password, email, card_code, card_balance)

        if not (name and email and password and card_balance and card_code):
            return "Empty values were given."

        if (
            isinstance(name, str)
            and "@" in email
            and len(password) >= 6
            and len(card_code) == 16
        ):
            with open("users.csv", "a", newline="") as user_write:
                user_id = int(USERS[-1]["id"]) + 1

                user_writer = csv.DictWriter(
                    user_write,
                    fieldnames=[
                        "id",
                        "name",
                        "password",
                        "email",
                        "purchases",
                        "card_code",
                        "card_balance",
                    ],
                    delimiter=";",
                )
                user_writer.writerow(
                    {
                        "id": user_id,
                        "name": name,
                        "password": password,
                        "email": email,
                        "purchases": "",
                        "card_code": card_code,
                        "card_balance": card_balance,
                    }
                )
            return cls(name, password, email, card_code, card_balance)

    @classmethod
    def login(cls, email, password):
        USERS = get_csv("users.csv", ";")

        if not (email and password):
            return "Empty values were given."
        for user in USERS:
            if user["email"] == email and password == user["password"]:
                return cls(
                    user["name"],
                    password,
                    email,
                    user["card_code"],
                    int(user["card_balance"]),
                )
            else:
                return "Wrong email or password"

    def purchase(self, product, count):
        """
        - purchase - метод для покупки товаров.
        Для покупки вам нужно узнать, какой товар хочет купить человек и есть у него достаточно денег для этого.
        Если условия верны, то человек покупает товар и с его счета снимаются деньги
        Если товара нет в списке товаров, вывести сообщение что товара нет, если не достаточно денег,
        то вывести сообщение что не достаточно средств.
        """
        if self.card_balance <= 0:
            return "Not enought balance!"

        PRODUCTS = get_csv("products.csv", ";")
        USERS = get_csv("users.csv", ";")

        for index, user in enumerate(USERS):
            if user["email"] == self.email and user["password"] == self.password:
                for i, pr in enumerate(PRODUCTS):
                    product_name = pr.get("product_name")
                    product_price = int(pr.get("price")) * count
                    balance = int(user.get("card_balance"))
                    self.card_balance = balance

                    if (
                        product_name == product
                        and self.card_balance - product_price >= 0
                        and count != 0
                        and count <= int(pr["count"])
                    ):
                        self.card_balance -= product_price
                        # substracting user balance in csv file
                        update_csv_file(
                            "users.csv",
                            index,
                            "card_balance",
                            product_price,
                            action="int-",
                            fieldnames=[
                                "id",
                                "name",
                                "password",
                                "email",
                                "purchases",
                                "card_code",
                                "card_balance",
                            ],
                        )
                        # adding product to user csv purchases and class's purchase list
                        update_csv_file(
                            "users.csv",
                            index,
                            "purchases",
                            product,
                            action="str",
                            fieldnames=[
                                "id",
                                "name",
                                "password",
                                "email",
                                "purchases",
                                "card_code",
                                "card_balance",
                            ],
                            count=count,
                        )
                        set_user_purchases = get_csv("users.csv", delimiter=";")[index][
                            "purchases"
                        ].split(",")
                        self.purchases = set_user_purchases
                        # substracting product quantity for every purchase
                        update_csv_file(
                            "products.csv",
                            i,
                            "count",
                            count,
                            action="int-",
                            fieldnames=[
                                "id",
                                "product_name",
                                "count",
                                "price",
                                "color",
                            ],
                        )
                        all_purchases = "\n\t".join(self.purchases)
                        return f"\n\nSuccessfull! Balance: {self.card_balance}\n{user['name']} purchases:\n\t{all_purchases}"
        return "Not available! Check your balance or the product you has submit."
